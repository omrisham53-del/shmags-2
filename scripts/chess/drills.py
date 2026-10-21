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

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402
from engine import fen_before_ply  # noqa: E402
from detect import _game_trajectory, find_cliffs, CLIFF_THRESHOLD  # noqa: E402

PUZZLES_PATH = Path(__file__).parent / "puzzles_filtered.csv"
NULL_CP_LOSS_MAX = 20     # my move's cp_loss had to be this small to count as "fine"
NULL_EVAL_BAND = 250      # |my-perspective eval| had to be under this -- not already decided


def _best_move_uci(fen: str, best_move_san: str):
    if not best_move_san:
        return None
    try:
        board = chess.Board(fen)
        move = board.parse_san(best_move_san)
        return move.uci()
    except ValueError:
        return None


def own_blunder_drills(conn, limit: int) -> list:
    """His own blunder positions, one move before the mistake."""
    games = [g for g in store.get_games(conn, "rapid", "600")
             if conn.execute("SELECT 1 FROM evaluations WHERE game_id=? LIMIT 1", (g["id"],)).fetchone()]
    candidates = []
    for g in games:
        traj = _game_trajectory(conn, g)
        for c in find_cliffs(traj):
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
            })
    random.shuffle(candidates)
    return candidates[:limit]


def own_null_drills(conn, limit: int) -> list:
    """Quiet positions from his own games -- the right answer is just not losing."""
    games = [g for g in store.get_games(conn, "rapid", "600")
             if conn.execute("SELECT 1 FROM evaluations WHERE game_id=? LIMIT 1", (g["id"],)).fetchone()]
    candidates = []
    for g in games:
        traj = _game_trajectory(conn, g)
        for row in traj:
            if not row["is_mine"] or row["cp_loss"] is None:
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
            })
    random.shuffle(candidates)
    return candidates[:limit]


def lichess_puzzle_drills(limit: int) -> list:
    if not PUZZLES_PATH.exists():
        print(f"WARNING: {PUZZLES_PATH} not found -- run sync_puzzles.py first. Skipping this source.")
        return []
    with open(PUZZLES_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    random.shuffle(rows)

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
        })
    return candidates


def build_drill_set(conn, n_blunder=20, n_null=20, n_puzzle=20) -> list:
    drills = (
        own_blunder_drills(conn, n_blunder)
        + own_null_drills(conn, n_null)
        + lichess_puzzle_drills(n_puzzle)
    )
    random.shuffle(drills)
    for i, d in enumerate(drills):
        d["id"] = i
    return drills


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-blunder", type=int, default=20)
    parser.add_argument("--n-null", type=int, default=20)
    parser.add_argument("--n-puzzle", type=int, default=20)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    conn = store.init_db()
    drills = build_drill_set(conn, args.n_blunder, args.n_null, args.n_puzzle)

    by_source = {}
    for d in drills:
        by_source[d["source"]] = by_source.get(d["source"], 0) + 1
    print(f"Built {len(drills)} drills: {by_source}")

    if args.write:
        out = Path(__file__).parent.parent.parent / "projects" / "chess" / "drill-set.json"
        out.write_text(json.dumps(drills, indent=2), encoding="utf-8")
        print(f"Written to {out}")


if __name__ == "__main__":
    main()
