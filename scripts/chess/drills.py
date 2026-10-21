"""
M3 drill generator: builds a drill set as JSON from three sources, shuffled
together. See projects/chess/learning-system-plan.md M3.

The mixing is the mechanism, not a convenience (rule 2 and 3 of the four
hard training rules): every Lichess puzzle is by construction solvable,
which would itself be a hint. Interleaving them with his own null positions
-- where the right answer is just not losing -- means he can never assume a
win exists just because a drill showed up.

Known v1 limitation: null-position and puzzle drills accept only the
engine's single top move as correct, even though by definition a null
position often has several equally fine moves. Flagged honestly rather than
building MultiPV tolerance now -- a real v1 scoping decision, not an
oversight.

Sampling is seeded (not re-randomized on every run) so a given drill set's
hand-written explanations (see explain_drills.py) stay valid across
rebuilds. Pass --seed to deliberately get a fresh set.

Explanation-writing rule, learned the hard way (2026-10-21): for
own_blunder drills, NEVER phrase the historical mistake as "X, what you
played" -- that reads as live feedback on the current drill attempt, which
the explanation has no way to know (it's baked in at build time, long
before anyone clicks anything). The drill mechanics already give live,
accurate feedback ("Right"/"Not quite", the actual move the user made).
The explanation text is baked-in color about the REAL GAME this position
came from, which may have nothing to do with whatever the user does in
any given drill session. Always frame it explicitly as "in the real game,
X was played" -- never as present-tense feedback on "you".

Usage:
    python scripts/chess/drills.py --write    # writes projects/chess/drill-set.json
"""

import argparse
import csv
import json
import random
import sys
from pathlib import Path

import chess
import chess.engine

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402
from engine import fen_before_ply, Engine  # noqa: E402
from detect import _game_trajectory, find_cliffs, CLIFF_THRESHOLD  # noqa: E402

PUZZLES_PATH = Path(__file__).parent / "puzzles_filtered.csv"
NULL_CP_LOSS_MAX = 20     # my move's cp_loss had to be this small to count as "fine"
NULL_EVAL_BAND = 250      # |my-perspective eval| had to be under this -- not already decided
ACCEPT_CP_TOLERANCE = 30  # own_blunder/own_null: moves within this many cp of the best are
                           # also accepted as correct, not just the single top move. Fixes a
                           # real v1 gap (flagged below, then actually hit in practice 2026-10-21):
                           # a null drill telling someone "Not quite" when their move scored
                           # within 20cp of the stored answer undermines the whole category's
                           # point, which is that several moves are genuinely fine here. Lichess
                           # puzzles stay single-answer on purpose -- a puzzle's solution being
                           # unique is what makes it a puzzle, not a quiet position.
MIN_PLY = 10              # below this, a position is probably still book -- not a real decision
                           # point. A "null" drill is supposed to be a quiet moment mid-game, not
                           # move 1 of some game, which trivially satisfies cp_loss/eval filters
                           # without representing anything to actually navigate. Same cutoff
                           # concept as detect.py's BOOK_PLY_CUTOFF.


def _acceptable_moves_uci(eng: Engine, fen: str, primary_uci: str,
                           cp_tolerance: int = ACCEPT_CP_TOLERANCE) -> list:
    """All moves within cp_tolerance of the best move's eval, from the mover's perspective.
    primary_uci is always included even if the multipv scan doesn't surface it for some reason
    (defensive -- the stored 'correct' answer must never stop being accepted)."""
    board = chess.Board(fen)
    color = board.turn
    info = eng.engine.analyse(board, chess.engine.Limit(depth=16), multipv=6)
    accepted = []
    best_eval = None
    for line in info:
        score = line["score"].pov(color).score(mate_score=100000)
        if score is None:
            continue
        if best_eval is None:
            best_eval = score
        if best_eval - score <= cp_tolerance:
            accepted.append(line["pv"][0].uci())
    if primary_uci not in accepted:
        accepted.append(primary_uci)
    return accepted


def _best_move_uci(fen: str, best_move_san: str):
    if not best_move_san:
        return None
    try:
        board = chess.Board(fen)
        move = board.parse_san(best_move_san)
        return move.uci()
    except ValueError:
        return None


def own_blunder_drills(conn, limit: int, rng: random.Random) -> list:
    """His own blunder positions, one move before the mistake."""
    games = [g for g in store.get_games(conn, "rapid", "600")
             if conn.execute("SELECT 1 FROM evaluations WHERE game_id=? LIMIT 1", (g["id"],)).fetchone()]
    candidates = []
    for g in games:
        traj = _game_trajectory(conn, g)
        for c in find_cliffs(traj):
            if c["ply"] < MIN_PLY:
                continue
            fen = fen_before_ply(g["pgn"], c["ply"])
            if not fen:
                continue
            uci = _best_move_uci(fen, c["best_move_san"])
            if not uci:
                continue
            candidates.append({
                "source": "own_blunder",
                "fen": fen,
                "correct_move_uci": uci,
                "correct_move_san": c["best_move_san"],
                "source_game_id": g["id"],
                "ply": c["ply"],
                "explanation": None,
            })
    rng.shuffle(candidates)
    return candidates[:limit]


def own_null_drills(conn, limit: int, rng: random.Random) -> list:
    """Quiet positions from his own games -- the right answer is just not losing."""
    games = [g for g in store.get_games(conn, "rapid", "600")
             if conn.execute("SELECT 1 FROM evaluations WHERE game_id=? LIMIT 1", (g["id"],)).fetchone()]
    candidates = []
    for g in games:
        traj = _game_trajectory(conn, g)
        for row in traj:
            if not row["is_mine"] or row["cp_loss"] is None:
                continue
            if row["ply"] < MIN_PLY:
                continue
            if row["cp_loss"] > NULL_CP_LOSS_MAX:
                continue
            if abs(row["my_eval"]) > NULL_EVAL_BAND:
                continue
            fen = fen_before_ply(g["pgn"], row["ply"])
            if not fen:
                continue
            uci = _best_move_uci(fen, row["best_move_san"])
            if not uci:
                continue
            candidates.append({
                "source": "own_null",
                "fen": fen,
                "correct_move_uci": uci,
                "correct_move_san": row["best_move_san"],
                "source_game_id": g["id"],
                "ply": row["ply"],
                "explanation": None,
            })
    rng.shuffle(candidates)
    return candidates[:limit]


def lichess_puzzle_drills(limit: int, rng: random.Random) -> list:
    if not PUZZLES_PATH.exists():
        print(f"WARNING: {PUZZLES_PATH} not found -- run sync_puzzles.py first. Skipping this source.")
        return []
    with open(PUZZLES_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    rng.shuffle(rows)

    candidates = []
    for row in rows:
        if len(candidates) >= limit:
            break
        moves = row["Moves"].split()
        if len(moves) < 2:
            continue
        try:
            board = chess.Board(row["FEN"])
            board.push_uci(moves[0])  # the setup move that reaches the real puzzle position
        except (ValueError, IndexError):
            continue
        candidates.append({
            "source": "lichess_puzzle",
            "fen": board.fen(),
            "correct_move_uci": moves[1],
            "correct_move_san": None,  # filled in client-side from the FEN if wanted
            "puzzle_id": row["PuzzleId"],
            "rating": row["Rating"],
            "themes": row["Themes"],
            "explanation": None,
        })
    return candidates


def build_drill_set(conn, n_blunder=8, n_null=7, n_puzzle=5, seed=7) -> list:
    # Independent RNGs per source, not one shared global sequence -- otherwise a filter
    # change in one source (different number of rng.shuffle() calls consumed) silently
    # reshuffles the OTHER sources too, orphaning every hand-written explanation at once.
    # Learned this the hard way: a one-line fix to own_null's ply floor changed all 20 drills.
    drills = (
        own_blunder_drills(conn, n_blunder, random.Random(seed))
        + own_null_drills(conn, n_null, random.Random(seed + 1000))
        + lichess_puzzle_drills(n_puzzle, random.Random(seed + 2000))
    )
    random.Random(seed + 3000).shuffle(drills)
    for i, d in enumerate(drills):
        d["id"] = i

    # Acceptable-move tolerance: computed only for the final 20 (not the whole candidate
    # pool) to keep engine calls bounded -- one multipv query per drill, not per candidate.
    with Engine() as eng:
        for d in drills:
            if d["source"] in ("own_blunder", "own_null"):
                d["acceptable_moves_uci"] = _acceptable_moves_uci(eng, d["fen"], d["correct_move_uci"])
            else:
                d["acceptable_moves_uci"] = [d["correct_move_uci"]]

    return drills


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-blunder", type=int, default=8)
    parser.add_argument("--n-null", type=int, default=7)
    parser.add_argument("--n-puzzle", type=int, default=5)
    parser.add_argument("--seed", type=int, default=7,
                         help="Fixed by default so hand-written explanations survive a rebuild; "
                              "pass a different value for a genuinely fresh set.")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    conn = store.init_db()
    drills = build_drill_set(conn, args.n_blunder, args.n_null, args.n_puzzle, args.seed)

    by_source = {}
    for d in drills:
        by_source[d["source"]] = by_source.get(d["source"], 0) + 1
    print(f"Built {len(drills)} drills: {by_source}")

    if args.write:
        out = Path(__file__).parent.parent.parent / "projects" / "chess" / "drill-set.json"
        # Carry over hand-written explanations from the existing file, keyed by
        # (fen, correct_move_uci) -- not by id, since id is just array position and
        # shifts on every rebuild. Explanations are a manual, out-of-band patch step
        # (see decisions/log.md 2026-10-21); without this merge, every `--write` run
        # silently resets all of them to null, which has already happened twice in one
        # session. This makes that a non-issue going forward: same content -> keeps its
        # explanation automatically, only genuinely new drills need a fresh one.
        carried = 0
        if out.exists():
            old = json.loads(out.read_text(encoding="utf-8"))
            old_explanations = {
                (d["fen"], d["correct_move_uci"]): d.get("explanation")
                for d in old if d.get("explanation")
            }
            for d in drills:
                key = (d["fen"], d["correct_move_uci"])
                if key in old_explanations:
                    d["explanation"] = old_explanations[key]
                    carried += 1
        out.write_text(json.dumps(drills, indent=2), encoding="utf-8")
        missing = sum(1 for d in drills if not d.get("explanation"))
        print(f"Written to {out} ({carried} explanations carried over, {missing} still need one)")


if __name__ == "__main__":
    main()
