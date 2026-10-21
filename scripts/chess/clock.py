"""
Parse chess.com's [%clk ] PGN annotations into per-move time spent, bucket by
game phase, and report on real clock-usage patterns. See
projects/chess/learning-system-plan.md M0.

The hypothesis this exists to test: if Omri burns most of his clock in the
opening/early middlegame and reaches endgames with little time left, failure
mode 2 (slow failure to capitalize on a lead) is a time-allocation problem,
not an endgame-knowledge problem -- which would reshape or remove M4.

Usage:
    python scripts/chess/clock.py              # parse unparsed games, then report
    python scripts/chess/clock.py --report-only  # skip parsing, just report
"""

import argparse
import io
import re
import statistics
import sys
from pathlib import Path

import chess
import chess.pgn

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402

CLK_RE = re.compile(r"\[%clk (\d+):(\d+):(\d+(?:\.\d+)?)\]")
STARTING_CLOCK = 600.0  # seconds, 10+0


def parse_clock(comment: str):
    m = CLK_RE.search(comment or "")
    if not m:
        return None
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def phase_for_ply(ply: int, total_plies: int) -> str:
    """First/last 20 plies are opening/endgame; middle is middlegame. Short
    games (<=40 plies) split into equal thirds instead so very short decisive
    games still get a meaningful endgame bucket."""
    if total_plies <= 40:
        third = max(1, total_plies // 3)
        if ply <= third:
            return "opening"
        if ply <= 2 * third:
            return "middlegame"
        return "endgame"
    if ply <= 20:
        return "opening"
    if ply > total_plies - 20:
        return "endgame"
    return "middlegame"


def parse_game_clock(pgn_text: str):
    """Returns a list of per-ply dicts: ply, color, move_san, clock_seconds, time_spent, phase."""
    game = chess.pgn.read_game(io.StringIO(pgn_text))
    if game is None:
        return []

    board = game.board()
    node = game
    ply = 0
    clocks = {"white": STARTING_CLOCK, "black": STARTING_CLOCK}
    raw_moves = []

    while node.variations:
        next_node = node.variations[0]
        move = next_node.move
        san = board.san(move)
        board.push(move)
        ply += 1
        color = "white" if ply % 2 == 1 else "black"
        clk = parse_clock(next_node.comment)
        time_spent = None
        if clk is not None:
            time_spent = round(clocks[color] - clk, 1)
            clocks[color] = clk
        raw_moves.append({"ply": ply, "color": color, "move_san": san, "clock_seconds": clk,
                           "time_spent": time_spent})
        node = next_node

    total_plies = ply
    for m in raw_moves:
        m["phase"] = phase_for_ply(m["ply"], total_plies)
    return raw_moves


def parse_pending(conn):
    pending = store.games_needing_clock_parse(conn)
    parsed = 0
    skipped_no_clock = 0
    for g in pending:
        moves = parse_game_clock(g["pgn"])
        if not moves or all(m["clock_seconds"] is None for m in moves):
            # No clock data in this PGN at all -- mark parsed so we don't retry forever,
            # but it contributes nothing to the report.
            conn.execute("UPDATE games SET clock_parsed = 1 WHERE id = ?", (g["id"],))
            conn.commit()
            skipped_no_clock += 1
            continue
        store.replace_moves(conn, g["id"], moves)
        parsed += 1
    return parsed, skipped_no_clock


def build_report(conn) -> str:
    games = store.get_games(conn, time_class="rapid", time_control="600")
    games = [g for g in games if g["clock_parsed"]]

    lines = []
    lines.append(f"Games with clock data parsed: {len(games)}\n")

    # --- Aggregate time spent by phase, for MY moves only ---
    phase_totals = {"opening": [], "middlegame": [], "endgame": []}
    endgame_entry_clock = {"win": [], "loss": [], "draw": []}
    low_time_endgame_games = 0
    games_with_endgame = 0

    for g in games:
        my_moves = store.get_moves(conn, g["id"], color=g["my_color"])
        my_moves = [m for m in my_moves if m["time_spent"] is not None]
        if not my_moves:
            continue

        by_phase = {"opening": [], "middlegame": [], "endgame": []}
        for m in my_moves:
            by_phase.setdefault(m["phase"], []).append(m["time_spent"])
        for phase, vals in by_phase.items():
            if vals:
                phase_totals[phase].append(sum(vals))

        endgame_moves = [m for m in my_moves if m["phase"] == "endgame"]
        if endgame_moves:
            games_with_endgame += 1
            first_endgame_clock = endgame_moves[0]["clock_seconds"]
            if first_endgame_clock is not None:
                endgame_entry_clock[g["my_result"]].append(first_endgame_clock)
                if first_endgame_clock < 60:
                    low_time_endgame_games += 1

    lines.append("## Time spent by phase (my moves, seconds per game, averaged)\n")
    for phase in ("opening", "middlegame", "endgame"):
        vals = phase_totals[phase]
        if vals:
            lines.append(f"- {phase}: avg {statistics.mean(vals):.0f}s/game "
                         f"(median {statistics.median(vals):.0f}s), n={len(vals)} games")
    lines.append("")

    lines.append("## Clock remaining when entering the endgame phase, by game result\n")
    for result in ("win", "loss", "draw"):
        vals = endgame_entry_clock[result]
        if vals:
            lines.append(f"- {result}: avg {statistics.mean(vals):.0f}s remaining "
                         f"(median {statistics.median(vals):.0f}s), n={len(vals)} games")
    lines.append("")

    pct_low = (low_time_endgame_games / games_with_endgame * 100) if games_with_endgame else 0
    lines.append(f"Games reaching the endgame phase with under 60s on the clock: "
                 f"{low_time_endgame_games}/{games_with_endgame} ({pct_low:.0f}%)\n")

    # --- Clock remaining at fixed move milestones, my moves only ---
    lines.append("## Clock remaining at move milestones (my moves)\n")
    for milestone in (10, 20, 30, 40):
        vals = []
        for g in games:
            my_moves = store.get_moves(conn, g["id"], color=g["my_color"])
            target_ply = milestone * 2 - (1 if g["my_color"] == "white" else 0)
            for m in my_moves:
                if m["ply"] == target_ply and m["clock_seconds"] is not None:
                    vals.append(m["clock_seconds"])
                    break
        if vals:
            lines.append(f"- move {milestone}: avg {statistics.mean(vals):.0f}s remaining "
                         f"(median {statistics.median(vals):.0f}s), n={len(vals)} games "
                         f"reached move {milestone}")
    lines.append("")

    # --- Verdict ---
    lines.append("## Verdict on the M0 hypothesis\n")
    win_vals = endgame_entry_clock["win"]
    loss_vals = endgame_entry_clock["loss"]
    if win_vals and loss_vals:
        win_avg = statistics.mean(win_vals)
        loss_avg = statistics.mean(loss_vals)
        lines.append(
            f"Average clock remaining entering the endgame: **{win_avg:.0f}s in games eventually "
            f"won** vs **{loss_avg:.0f}s in games eventually lost** (n={len(win_vals)} wins, "
            f"{len(loss_vals)} losses with a detected endgame phase)."
        )
        if win_avg < 90:
            lines.append(
                "\nThis is clock-data-only evidence (no engine join yet -- that's M1), but it "
                "points toward the time-allocation hypothesis: even in games eventually won, "
                "the endgame phase is commonly entered with well under two minutes on the clock. "
                f"{pct_low:.0f}% of games with a detected endgame phase enter it under 60 seconds "
                "remaining. If this holds up once M1 joins real evaluations (confirming these are "
                "genuinely winning positions, not just games that happened to end in a win), "
                "failure mode 2 looks more like pacing than missing endgame technique -- M4 should "
                "be reshaped toward clock discipline, not just more endgame study."
            )
        else:
            lines.append(
                "\nClock doesn't look obviously starved entering the endgame on this cut of the "
                "data. Worth re-checking once M1's real evaluations are available -- a low-stakes "
                "clock total can still coexist with a technical conversion problem."
            )
    else:
        lines.append("Not enough games with a detected endgame phase and clock data to call this yet.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()

    conn = store.init_db()
    if not args.report_only:
        parsed, skipped = parse_pending(conn)
        print(f"Parsed clock data for {parsed} games ({skipped} had no clock annotations).\n")

    print(build_report(conn))


if __name__ == "__main__":
    main()
