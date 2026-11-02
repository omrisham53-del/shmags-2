"""
M4 conversion drills: replay his own blown winning positions against a live
local Stockfish, from his own side, repeatedly. See
projects/chess/learning-system-plan.md M4.

Gated on M0's verdict and cleared by it: the clock analysis found plenty of
clock left on reaching the endgame (~381s in wins, ~327s in losses), so the
slow-dissolve failure mode is a technique problem, not a pacing one. That is
what makes replaying the positions the right intervention.

Terminal rather than browser because it needs a live engine on every move.

## How the four hard training rules apply here

Rule 2 ("never state that a win exists") is in direct tension with the very
idea of a conversion drill, since "convert this" announces the win by
construction. Resolved the same way M3 resolved it, by mixing rather than by
weakening the rule: control positions that are NOT winning are dealt into the
same session (roughly level positions from his own games), and the evaluation
is never shown while he is playing. He therefore cannot assume a position is
winning just because it came up in a conversion drill, which is the whole
point. A session of nothing but genuine +300 positions would train exactly
the "a win is here, go find it" reflex these rules exist to prevent.

Rule 1 (commit before explain) is why no eval, no best move and no cp_loss
appear until the attempt is over.

Rule 4 (harder than the game, not easier) is why the opponent defaults to
1400 Elo rather than his opponents' real ~1200: enough to punish sloppiness,
while nowhere near full strength. A full-strength Stockfish would make many
genuinely won positions unwinnable in practice and teach nothing.

The clock is a stopwatch with a soft target, never a cutoff, following the
2026-10-21 decision that replaced the drill board's forced clock. Time is
measured and reported; it never ends an attempt out from under him.

Usage:
    python scripts/chess/convert.py                 # a 5-position session
    python scripts/chess/convert.py --count 3 --attempts 1
    python scripts/chess/convert.py --opp-elo 1600  # harder opponent
    python scripts/chess/convert.py --list          # show the pool, play nothing
"""

import argparse
import random
import sys
import time
from pathlib import Path

import chess
import chess.engine
import chess.pgn

sys.path.insert(0, str(Path(__file__).parent))

import store
from detect import _game_trajectory, find_cliffs, find_decay_episodes
from engine import MATE_SCORE, STOCKFISH_PATH, fen_before_ply, pov

# Cliff-sourced positions must start at or above this my-perspective eval to
# count as a real conversion task. Matches the "conversion rate from +300 or
# better" metric in the plan's Measurement table, so drill results and the
# metric agree.
CONVERT_MIN_EVAL = 300

# Decay-sourced positions use the decay detector's OWN peak threshold (150)
# instead. Imposing CONVERT_MIN_EVAL on top of it meant the decay source could
# never yield anything at all: measured 2026-11-02 across 63 analyzed games,
# every one of the 4 clean decay episodes in the whole archive peaks between
# 157 and 289cp, so a 300 floor silently emptied the source. A position that
# satisfies the detector's definition of a decay episode is a decay episode.
DECAY_MIN_EVAL = 150

# Cap per game. Collapses cluster: one game contributed 7 cliff positions at
# plies 85/87/91/93/..., which are near-identical snapshots of a single
# collapse and would make a session feel repetitive while teaching one thing.
MAX_POSITIONS_PER_GAME = 2

# Control positions: absolute eval at or below this is "level, nothing to convert".
CONTROL_MAX_ABS_EVAL = 60

# Roughly one control position for every two real conversion positions.
CONTROL_SHARE = 0.34

MIN_PLY = 20          # skip openings; a conversion task needs a real middlegame
DEFAULT_OPP_ELO = 1400
ANALYSIS_DEPTH = 16   # below engine.py's 18 to stay responsive in a live loop
OPP_MOVE_TIME = 0.30  # seconds per engine reply
MAX_MY_MOVES = 14     # attempts end here if nothing has resolved
TARGET_SECONDS_PER_MOVE = 20.0  # soft target, reported not enforced

VERDICT_HELD_TOLERANCE = 75    # eval may drift this much and still count as held
VERDICT_LOST_EVAL = -200       # at or below this, the position is genuinely gone
VERDICT_CONVERTED_EVAL = 1000  # at or above this, won by any reasonable standard


# --------------------------------------------------------------------------
# Position sourcing
# --------------------------------------------------------------------------

def _first_own_move_at_or_after(traj, ply):
    """The first of his own moves at or after `ply`, so he is the one to move."""
    for row in traj:
        if row["ply"] >= ply and row["is_mine"]:
            return row["ply"]
    return None


def collect_positions(conn, time_class="rapid", time_control="600"):
    """Build the candidate pool: decay peaks, cliffs from winning positions,
    and level control positions, all from his own analyzed games."""
    conversion, control = [], []

    games = [
        g for g in store.get_games(conn, time_class=time_class, time_control=time_control)
        if g["my_color"]
    ]

    for g in games:
        traj = _game_trajectory(conn, g)
        if len(traj) < MIN_PLY + 2:
            continue

        per_game = 0

        # 1. Decay-episode peaks: he was winning and let it slide over many moves.
        #    Rare in practice (see DECAY_MIN_EVAL), but they are the purest form
        #    of the failure mode, so they get first claim on the per-game budget.
        for ep in find_decay_episodes(traj):
            if per_game >= MAX_POSITIONS_PER_GAME:
                break
            if ep["peak_eval"] < DECAY_MIN_EVAL or abs(ep["peak_eval"]) >= MATE_SCORE:
                continue
            ply = _first_own_move_at_or_after(traj, ep["peak_ply"])
            if ply is None or ply < MIN_PLY:
                continue
            fen = fen_before_ply(g["pgn"], ply)
            if fen:
                conversion.append({
                    "fen": fen, "game_id": g["id"], "source": "decay_peak",
                    "ply": ply, "hint_eval": ep["peak_eval"],
                    "url": g["url"], "end_date": g["end_date"],
                    "my_result": g["my_result"],
                })
                per_game += 1

        # 2. Cliffs that happened while winning: the position just before the
        #    collapse is a conversion task he demonstrably failed once already.
        for c in find_cliffs(traj):
            if per_game >= MAX_POSITIONS_PER_GAME:
                break
            prior = [r for r in traj if r["ply"] == c["ply"] - 1]
            start_eval = prior[0]["my_eval"] if prior else None
            if start_eval is None or start_eval < CONVERT_MIN_EVAL:
                continue
            if abs(start_eval) >= MATE_SCORE or c["ply"] < MIN_PLY:
                continue
            fen = fen_before_ply(g["pgn"], c["ply"])
            if fen:
                conversion.append({
                    "fen": fen, "game_id": g["id"], "source": "cliff_peak",
                    "ply": c["ply"], "hint_eval": start_eval,
                    "url": g["url"], "end_date": g["end_date"],
                    "my_result": g["my_result"],
                })
                per_game += 1

        # 3. Control positions: level, nothing to convert, no win to find.
        #    These are what keep rule 2 intact across a session.
        for row in traj:
            if not row["is_mine"] or row["ply"] < MIN_PLY:
                continue
            if abs(row["my_eval"]) <= CONTROL_MAX_ABS_EVAL:
                fen = fen_before_ply(g["pgn"], row["ply"])
                if fen:
                    control.append({
                        "fen": fen, "game_id": g["id"], "source": "control_level",
                        "ply": row["ply"], "hint_eval": row["my_eval"],
                        "url": g["url"], "end_date": g["end_date"],
                        "my_result": g["my_result"],
                    })
                break  # at most one control position per game, to spread them out

    return conversion, control


def select_session(conversion, control, count, seed):
    """Mix conversion and control positions into one shuffled session.

    Independent RNGs per source, following the 2026-10-21 fix: a shared global
    random state meant changing one source's filtering silently reshuffled the
    others.
    """
    n_control = round(count * CONTROL_SHARE) if control else 0
    # Control positions exist to stop him assuming a win is present; they must
    # never crowd out the conversion positions that are the point of the drill.
    # Without this clamp, --count 1 produced a session with zero conversion
    # positions at all, since round(1 * 0.34) rounded up to the only slot.
    if conversion and n_control >= count:
        n_control = count - 1
    n_convert = max(0, count - n_control)

    rc = random.Random(seed)
    rk = random.Random(seed + 1)
    rs = random.Random(seed + 2)

    conv_pool = list(conversion)
    ctrl_pool = list(control)
    rc.shuffle(conv_pool)
    rk.shuffle(ctrl_pool)

    chosen = conv_pool[:n_convert] + ctrl_pool[:n_control]
    rs.shuffle(chosen)
    return chosen


# --------------------------------------------------------------------------
# Board rendering
# --------------------------------------------------------------------------

def render(board, my_color_is_white):
    """Plain-letter board, uppercase White and lowercase black.

    Deliberately not unicode chess glyphs: the Windows console codepage
    mangles them, and CLAUDE.md already bans box-drawing characters for the
    same reason.
    """
    ranks = range(7, -1, -1) if my_color_is_white else range(8)
    files = range(8) if my_color_is_white else range(7, -1, -1)
    lines = []
    for r in ranks:
        cells = []
        for f in files:
            piece = board.piece_at(chess.square(f, r))
            cells.append(piece.symbol() if piece else ".")
        lines.append("{}  {}".format(r + 1, " ".join(cells)))
    lines.append("   " + " ".join(chess.FILE_NAMES[f] for f in files))
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Engine helpers
# --------------------------------------------------------------------------

class Analyser:
    """Full-strength engine, used only for scoring. Never shown mid-attempt."""

    def __init__(self, depth=ANALYSIS_DEPTH):
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        self.depth = depth

    def score(self, board, my_color):
        if board.is_game_over():
            outcome = board.outcome()
            if outcome and outcome.winner is None:
                return 0
            if outcome:
                won = (outcome.winner == chess.WHITE) == (my_color == "white")
                return MATE_SCORE if won else -MATE_SCORE
        info = self.engine.analyse(board, chess.engine.Limit(depth=self.depth))
        return pov(info["score"].white().score(mate_score=MATE_SCORE), my_color)

    def best_move_san(self, board):
        if board.is_game_over():
            return None
        info = self.engine.analyse(board, chess.engine.Limit(depth=self.depth))
        pv = info.get("pv")
        return board.san(pv[0]) if pv else None

    def close(self):
        self.engine.quit()


class Opponent:
    """Deliberately weakened engine, so conversion stays a real task."""

    def __init__(self, elo=DEFAULT_OPP_ELO):
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        self.elo = elo
        try:
            self.engine.configure({"UCI_LimitStrength": True, "UCI_Elo": elo})
        except Exception:
            # A full-strength opponent is wrong for this drill, so say so
            # rather than quietly play one.
            print("  (note: could not limit engine strength to {}, playing full strength)".format(elo))

    def reply(self, board):
        return self.engine.play(board, chess.engine.Limit(time=OPP_MOVE_TIME)).move

    def close(self):
        self.engine.quit()


# --------------------------------------------------------------------------
# One attempt
# --------------------------------------------------------------------------

def parse_move(board, text):
    text = text.strip()
    for parser in (board.parse_san, board.parse_uci):
        try:
            return parser(text)
        except Exception:
            continue
    return None


def verdict_for(start_eval, final_eval, board, my_color):
    if board.is_checkmate():
        mated_side = board.turn  # the side to move has been mated
        i_was_mated = (mated_side == chess.WHITE) == (my_color == "white")
        return "lost" if i_was_mated else "converted"
    if final_eval >= VERDICT_CONVERTED_EVAL > start_eval:
        return "converted"
    if final_eval >= VERDICT_CONVERTED_EVAL:
        return "held"
    if final_eval >= start_eval - VERDICT_HELD_TOLERANCE:
        return "held"
    if final_eval > VERDICT_LOST_EVAL:
        return "slipped"
    return "lost"


def run_attempt(pos, attempt_index, analyser, opponent, my_color, max_moves):
    """Play one attempt. Returns a result dict, or None if he quit the session."""
    board = chess.Board(pos["fen"])
    mine_is_white = (my_color == "white")
    start_eval = analyser.score(board, my_color)

    print("\n  You are {}. Your move.".format(my_color))
    print("  Target is about {:.0f}s per move. The clock counts up and never cuts you off.".format(
        TARGET_SECONDS_PER_MOVE))
    print("  Commands: 'resign' gives up this attempt, 'quit' ends the session.\n")
    print(render(board, mine_is_white))

    my_moves = 0
    worst_san, worst_loss = None, -1
    eval_before = start_eval
    total_seconds = 0.0
    resigned = False

    while my_moves < max_moves and not board.is_game_over():
        t0 = time.monotonic()
        try:
            raw = input("\n  your move > ").strip()
        except EOFError:
            # stdin closed (piped input exhausted, or Ctrl+Z). End the session
            # cleanly rather than dying with a traceback and losing the summary
            # for attempts that already finished.
            print("\n  (input closed)")
            return None
        elapsed = time.monotonic() - t0
        if not raw:
            continue
        low = raw.lower()
        if low == "quit":
            return None
        if low == "resign":
            resigned = True
            break
        move = parse_move(board, raw)
        if move is None or move not in board.legal_moves:
            print("  Not a legal move here. Try again (SAN like Rxe4, or UCI like e2e4).")
            continue

        san = board.san(move)
        total_seconds += elapsed
        board.push(move)
        my_moves += 1

        eval_after = analyser.score(board, my_color)
        loss = max(0, eval_before - eval_after)
        if loss > worst_loss:
            worst_loss, worst_san = loss, san

        if board.is_game_over():
            break

        reply = opponent.reply(board)
        reply_san = board.san(reply)
        board.push(reply)
        print("\n  You played {} ({:.0f}s). Opponent replied {}.".format(san, elapsed, reply_san))
        print(render(board, mine_is_white))

        if board.is_game_over():
            break
        eval_before = analyser.score(board, my_color)

    final_eval = analyser.score(board, my_color)
    if resigned and my_moves == 0:
        # Declining to play a position is not the same as losing it. Scoring
        # this as "lost" would quietly poison the conversion-rate metric with
        # positions he never actually attempted.
        verdict = "skipped"
        final_eval = start_eval
    elif resigned:
        verdict = "lost"
    else:
        verdict = verdict_for(start_eval, final_eval, board, my_color)

    return {
        "fen": pos["fen"],
        "source_game_id": pos["game_id"],
        "source": pos["source"],
        "start_eval": start_eval,
        "final_eval": final_eval,
        "verdict": verdict,
        "my_moves": my_moves,
        "worst_move_san": worst_san,
        "worst_move_cp_loss": worst_loss if worst_loss >= 0 else None,
        "opp_elo": opponent.elo,
        "seconds_per_move": (total_seconds / my_moves) if my_moves else None,
        "attempt_index": attempt_index,
        "resigned": resigned,
        "board": board,
    }


def _fmt_cp(cp):
    if abs(cp) >= MATE_SCORE:
        return "mate" if cp > 0 else "mated"
    return "{:+d}cp".format(cp)


def reveal(res, pos, analyser):
    """Everything withheld during play, shown only now (rule 1)."""
    print("\n  " + "-" * 60)
    start, final = res["start_eval"], res["final_eval"]

    if abs(start) <= CONTROL_MAX_ABS_EVAL:
        print("  This one was level to begin with: {}. There was no win to find.".format(_fmt_cp(start)))
    else:
        print("  Starting position: {} in your favour.".format(_fmt_cp(start)))

    if res["verdict"] != "skipped":
        print("  Where it ended:    {} after {} of your moves.".format(
            _fmt_cp(final), res["my_moves"]))

    labels = {
        "converted": "Converted. That is the whole skill.",
        "held": "Held. You did not let it slip.",
        "slipped": "Slipped. The advantage leaked away without one obvious blunder.",
        "lost": "Lost. The position got away from you.",
        "skipped": "Skipped before playing a move. Not scored.",
    }
    print("  Verdict: {}".format(labels[res["verdict"]]))

    wl = res["worst_move_cp_loss"]
    if res["worst_move_san"] and wl is not None and wl >= 100:
        print("  Costliest move: {}, giving up {}cp.".format(res["worst_move_san"], wl))
    elif wl is not None and wl < 100:
        print("  No single move cost much. Nothing to single out.")

    if res["seconds_per_move"]:
        sp = res["seconds_per_move"]
        comp = "within" if sp <= TARGET_SECONDS_PER_MOVE else "over"
        print("  Pace: {:.0f}s per move, {} your {:.0f}s target.".format(
            sp, comp, TARGET_SECONDS_PER_MOVE))

    if not res["board"].is_game_over():
        bm = analyser.best_move_san(res["board"])
        if bm:
            print("  From where you stopped, the engine would play {}.".format(bm))

    origin = {
        "decay_peak": "a game where you had this edge and lost it slowly",
        "cliff_peak": "a game where this edge vanished on one move",
        "control_level": "a level moment from one of your games",
    }[pos["source"]]
    print("  Source: {}, {} ({}).".format(origin, pos["end_date"], pos["my_result"]))
    print("  {}".format(pos["url"]))
    print("  " + "-" * 60)


def save(conn, res):
    conn.execute(
        """INSERT INTO conversion_attempts
           (fen, source_game_id, source, start_eval, final_eval, verdict, my_moves,
            worst_move_san, worst_move_cp_loss, opp_elo, seconds_per_move, attempt_index)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
        (res["fen"], res["source_game_id"], res["source"], res["start_eval"],
         res["final_eval"], res["verdict"], res["my_moves"], res["worst_move_san"],
         res["worst_move_cp_loss"], res["opp_elo"], res["seconds_per_move"],
         res["attempt_index"]),
    )
    conn.commit()


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="M4 conversion drills against live Stockfish")
    ap.add_argument("--count", type=int, default=5, help="positions this session")
    ap.add_argument("--attempts", type=int, default=2, help="tries per position")
    ap.add_argument("--opp-elo", type=int, default=DEFAULT_OPP_ELO)
    ap.add_argument("--moves", type=int, default=MAX_MY_MOVES,
                    help="max of your moves per attempt")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--list", action="store_true", help="show the pool and exit")
    args = ap.parse_args()

    conn = store.init_db()
    conversion, control = collect_positions(conn)

    print("Pool: {} conversion positions, {} control positions.".format(
        len(conversion), len(control)))
    if not conversion and not control:
        print("Nothing to drill yet. Run analyze_batch.py so games have evaluations.")
        return

    if args.list:
        for p in (conversion + control)[:40]:
            print("  {:14s} ply {:3d}  {}  {}".format(
                p["source"], p["ply"], p["end_date"], p["url"]))
        return

    session = select_session(conversion, control, args.count, args.seed)
    if not session:
        print("Could not assemble a session from the pool.")
        return

    analyser = Analyser()
    opponent = Opponent(args.opp_elo)
    results = []

    try:
        for idx, pos in enumerate(session, 1):
            row = conn.execute("SELECT my_color FROM games WHERE id = ?",
                               (pos["game_id"],)).fetchone()
            my_color = row["my_color"]
            for attempt in range(1, args.attempts + 1):
                label = "Position {}/{}".format(idx, len(session))
                if args.attempts > 1:
                    label += ", attempt {}/{}".format(attempt, args.attempts)
                print("\n{}\n{}\n{}".format("=" * 64, label, "=" * 64))
                res = run_attempt(pos, attempt, analyser, opponent, my_color, args.moves)
                if res is None:
                    print("\nSession ended early.")
                    raise KeyboardInterrupt
                reveal(res, pos, analyser)
                save(conn, res)
                results.append(res)
    except KeyboardInterrupt:
        pass
    finally:
        analyser.close()
        opponent.close()

    if results:
        print("\n{}\nSession summary\n{}".format("=" * 64, "=" * 64))
        counts = {}
        for r in results:
            counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
        for v in ("converted", "held", "slipped", "lost", "skipped"):
            if counts.get(v):
                print("  {}: {}".format(v, counts[v]))
        real = [r for r in results
                if abs(r["start_eval"]) > CONTROL_MAX_ABS_EVAL
                and r["verdict"] != "skipped"]
        if real:
            good = sum(1 for r in real if r["verdict"] in ("converted", "held"))
            print("\n  Conversion rate on real winning positions: {}/{}".format(good, len(real)))
        print("  Logged {} attempts to conversion_attempts.".format(len(results)))


if __name__ == "__main__":
    main()
