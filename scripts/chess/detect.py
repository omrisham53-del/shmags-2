"""
Two detectors over the engine evaluations M1 produces, joined against M0's
clock data. See projects/chess/learning-system-plan.md M1.

- Cliff detector: single-move evaluation collapses. The known-good one.
- Decay detector: sustained winning evaluation eroding across many moves
  with no single large swing. Nothing has caught this before -- it's the
  only thing that can see failure mode 2 ("slow failure to capitalize on a
  lead over many moves, with no single identifiable blunder").

Carried forward from the retired bi-weekly routine: long engine-best streaks
are frequently hollow (king shuffles in lost endgames, opening-book moves,
trivial promotions) and must not be scored as skill. is_hollow_streak() is
the reusable filter for that, for whenever M3/M6 build highlight selection.

Usage:
    python scripts/chess/detect.py                 # full report to stdout
    python scripts/chess/detect.py --write          # also write the markdown report
"""

import argparse
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402
from engine import pov  # noqa: E402

CLIFF_THRESHOLD = 200       # cp_loss on a single move to count as a cliff
DECAY_PEAK_THRESHOLD = 150  # my-perspective eval needed to start a decay watch
DECAY_TROUGH_THRESHOLD = 0  # my-perspective eval that counts as "lead gone"
DECAY_MIN_SPAN_PLIES = 10   # minimum peak-to-trough distance to count as decay, not a cliff
FAST_MOVE_SECONDS = 10      # time_spent below this counts as "played fast"
DECISIVE_EVAL = 600         # |eval| above this = already decided, streak likely hollow
BOOK_PLY_CUTOFF = 10        # plies at or below this are probably still book


def is_hollow_streak(evals_in_streak: list, start_ply: int) -> bool:
    """evals_in_streak: list of my-perspective eval_cp values across the streak.
    True if the streak is likely book moves or a shuffle in an already-decided
    position, not a real skill demonstration."""
    if start_ply <= BOOK_PLY_CUTOFF:
        return True
    if evals_in_streak and all(abs(e) >= DECISIVE_EVAL for e in evals_in_streak):
        return True
    return False


def _game_trajectory(conn, game_row):
    """Per-ply list for one game: ply, color, my_perspective_eval, cp_loss
    (only set on my own moves, else None), clock_seconds, time_spent, phase."""
    evals = {r["ply"]: r for r in conn.execute(
        "SELECT * FROM evaluations WHERE game_id = ? ORDER BY ply", (game_row["id"],)
    ).fetchall()}
    moves = {r["ply"]: r for r in store.get_moves(conn, game_row["id"])}

    traj = []
    for ply in sorted(evals.keys()):
        e = evals[ply]
        m = moves.get(ply)
        my_eval = pov(e["eval_cp"], game_row["my_color"]) if not e["is_mate"] else (
            100000 if pov(e["eval_cp"], game_row["my_color"]) > 0 else -100000
        )
        is_mine = (m is not None and m["color"] == game_row["my_color"])
        # Defensive cap: games analyzed before the 2026-10-21 engine.py fix can carry
        # mate-score-artifact cp_loss values (observed: 99986 on a single move). Clip
        # anything absurd rather than let it through as a deceptive magnitude.
        raw_cp_loss = e["cp_loss"] if is_mine else None
        cp_loss = min(raw_cp_loss, 2000) if raw_cp_loss is not None else None
        traj.append({
            "ply": ply,
            "color": m["color"] if m else None,
            "move_san": m["move_san"] if m else None,
            "my_eval": my_eval,
            "cp_loss": cp_loss,
            "best_move_san": e["best_move_san"],
            "clock_seconds": m["clock_seconds"] if m else None,
            "time_spent": m["time_spent"] if m else None,
            "phase": m["phase"] if m else None,
            "is_mine": is_mine,
        })
    return traj


def find_cliffs(traj: list) -> list:
    """Single-move collapses on my own moves."""
    cliffs = []
    for row in traj:
        if row["is_mine"] and row["cp_loss"] is not None and row["cp_loss"] >= CLIFF_THRESHOLD:
            cliffs.append(row)
    return cliffs


def find_decay_episodes(traj: list) -> list:
    """Sustained erosion of a lead across many moves, no single qualifying cliff inside."""
    episodes = []
    i = 0
    n = len(traj)
    while i < n:
        if traj[i]["my_eval"] >= DECAY_PEAK_THRESHOLD:
            peak_idx = i
            peak_eval = traj[i]["my_eval"]
            # extend the peak forward while eval keeps climbing or holding near the peak
            j = i + 1
            while j < n and traj[j]["my_eval"] >= peak_eval - 30:
                if traj[j]["my_eval"] > peak_eval:
                    peak_idx, peak_eval = j, traj[j]["my_eval"]
                j += 1
            # now look for the trough: does it decline to/below threshold without a cliff?
            k = peak_idx + 1
            had_cliff = False
            lowest = peak_eval
            trough_idx = None
            while k < n:
                if traj[k]["is_mine"] and traj[k]["cp_loss"] is not None and traj[k]["cp_loss"] >= CLIFF_THRESHOLD:
                    had_cliff = True
                    break
                lowest = min(lowest, traj[k]["my_eval"])
                if traj[k]["my_eval"] <= DECAY_TROUGH_THRESHOLD:
                    trough_idx = k
                    break
                k += 1
            if trough_idx is not None and not had_cliff:
                span = traj[trough_idx]["ply"] - traj[peak_idx]["ply"]
                if span >= DECAY_MIN_SPAN_PLIES:
                    window = traj[peak_idx:trough_idx + 1]
                    episodes.append({
                        "peak_ply": traj[peak_idx]["ply"],
                        "peak_eval": peak_eval,
                        "trough_ply": traj[trough_idx]["ply"],
                        "trough_eval": traj[trough_idx]["my_eval"],
                        "span_plies": span,
                        "my_moves_in_window": [w for w in window if w["is_mine"]],
                    })
                    i = trough_idx + 1
                    continue
            i = peak_idx + 1
        else:
            i += 1
    return episodes


def build_report(conn, since_date="2026-01-01") -> str:
    all_rapid = [g for g in store.get_games(conn, "rapid", "600") if g["end_date"] >= since_date]
    analyzed = [g for g in all_rapid if conn.execute(
        "SELECT 1 FROM evaluations WHERE game_id = ? LIMIT 1", (g["id"],)
    ).fetchone()]

    lines = []
    lines.append(f"Coverage: {len(analyzed)}/{len(all_rapid)} rapid 10+0 games analyzed "
                 f"(since {since_date}). Re-run as more finish analyzing.\n")

    all_cliffs = []
    all_decays = []
    for g in analyzed:
        traj = _game_trajectory(conn, g)
        for c in find_cliffs(traj):
            c["game"] = g
            all_cliffs.append(c)
        for d in find_decay_episodes(traj):
            d["game"] = g
            all_decays.append(d)

    lines.append(f"## Cliffs (single-move collapses >= {CLIFF_THRESHOLD}cp)\n")
    lines.append(f"Total: {len(all_cliffs)} across {len(analyzed)} games "
                 f"({len(all_cliffs)/max(1,len(analyzed)):.2f} per game).\n")
    fast_cliffs = [c for c in all_cliffs if c["time_spent"] is not None and c["time_spent"] < FAST_MOVE_SECONDS]
    pct_fast = (len(fast_cliffs) / len(all_cliffs) * 100) if all_cliffs else None
    if all_cliffs:
        lines.append(f"Played in under {FAST_MOVE_SECONDS}s: {len(fast_cliffs)}/{len(all_cliffs)} ({pct_fast:.0f}%).")
        by_phase = {}
        for c in all_cliffs:
            by_phase[c["phase"]] = by_phase.get(c["phase"], 0) + 1
        lines.append(f"By phase: {dict(sorted(by_phase.items(), key=lambda x: -x[1]))}")
    lines.append("")

    top_cliffs = sorted(all_cliffs, key=lambda c: -c["cp_loss"])[:10]
    if top_cliffs:
        lines.append("### Worst 10 cliffs\n")
        for c in top_cliffs:
            lines.append(f"- {c['game']['url']} ply {c['ply']} ({c['move_san']}): "
                         f"-{c['cp_loss']}cp, {c['time_spent']}s spent, phase={c['phase']}")
        lines.append("")

    lines.append(f"## Decay episodes (lead >= {DECAY_PEAK_THRESHOLD}cp eroding to <= "
                 f"{DECAY_TROUGH_THRESHOLD}cp over >= {DECAY_MIN_SPAN_PLIES} plies, no single cliff)\n")
    lines.append(f"Total: {len(all_decays)} across {len(analyzed)} games "
                 f"({len(all_decays)/max(1,len(analyzed)):.2f} per game).\n")
    pct_decay_fast = None
    total_decay_moves = 0
    if all_decays:
        spans = [d["span_plies"] for d in all_decays]
        lines.append(f"Average span: {statistics.mean(spans):.0f} plies (median {statistics.median(spans):.0f}).")
        fast_decay_moves = sum(
            1 for d in all_decays for m in d["my_moves_in_window"]
            if m["time_spent"] is not None and m["time_spent"] < FAST_MOVE_SECONDS
        )
        total_decay_moves = sum(len(d["my_moves_in_window"]) for d in all_decays)
        if total_decay_moves:
            pct_decay_fast = fast_decay_moves / total_decay_moves * 100
            lines.append(f"My moves inside decay windows played under {FAST_MOVE_SECONDS}s: "
                         f"{fast_decay_moves}/{total_decay_moves} ({pct_decay_fast:.0f}%).")
    lines.append("")

    top_decays = sorted(all_decays, key=lambda d: -(d["peak_eval"] - d["trough_eval"]))[:10]
    if top_decays:
        lines.append("### Worst 10 decay episodes (biggest eval swing lost)\n")
        for d in top_decays:
            lines.append(f"- {d['game']['url']} plies {d['peak_ply']}-{d['trough_ply']} "
                         f"(+{d['peak_eval']} -> {d['trough_eval']}, {d['span_plies']} plies, "
                         f"{len(d['my_moves_in_window'])} of my moves in window)")
        lines.append("")

    lines.append("## Direct answer: do blunders come from fast moves?\n")
    if all_cliffs:
        avg_cliff_time = statistics.mean([c["time_spent"] for c in all_cliffs if c["time_spent"] is not None])
        lines.append(f"Average time spent on a cliff move: {avg_cliff_time:.1f}s "
                     f"({pct_fast:.0f}% under {FAST_MOVE_SECONDS}s).")
    else:
        lines.append("No cliffs found yet to check.")
    if total_decay_moves:
        lines.append(f"Average time spent on moves inside a decay window: see per-move breakdown above "
                     f"({pct_decay_fast:.0f}% under {FAST_MOVE_SECONDS}s) -- this is the comparison that "
                     "matters, since decay moves are individually unremarkable but collectively bleed the lead.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", default="2026-01-01")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    conn = store.init_db()
    report = build_report(conn, since_date=args.since)
    print(report)

    if args.write:
        out = Path(__file__).parent.parent.parent / "projects" / "chess" / "engine-analysis-report.md"
        out.write_text(
            "# M1 Engine Analysis: Cliffs, Decay, and the Clock Join\n\n"
            f"**Last refreshed:** see coverage line below.\n\n{report}\n",
            encoding="utf-8",
        )
        print(f"\nWritten to {out}")


if __name__ == "__main__":
    main()
