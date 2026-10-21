"""
Batch driver for M1: works through games lacking evaluations, newest first,
checkpointing after every single game so it's safe to interrupt and resume
at any point -- just re-run it. See projects/chess/learning-system-plan.md M1.

Usage:
    python scripts/chess/analyze_batch.py                      # all unanalyzed 2026+ rapid games
    python scripts/chess/analyze_batch.py --since 2020-01-01    # extend to full history
    python scripts/chess/analyze_batch.py --max-minutes 540     # stop cleanly after N minutes
    python scripts/chess/analyze_batch.py --limit 20            # stop after N games
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402
import engine as engine_mod  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", default="2026-01-01",
                         help="Only analyze games with end_date >= this (default: 2026-01-01, the relevant era)")
    parser.add_argument("--max-minutes", type=float, default=None)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    conn = store.init_db()
    pending = store.games_needing_evaluation(conn, since_date=args.since)
    total_pending = len(pending)
    print(f"[{time.strftime('%H:%M:%S')}] {total_pending} games pending analysis (since {args.since}).",
          flush=True)

    if args.limit:
        pending = pending[:args.limit]

    start = time.time()
    done = 0
    total_plies = 0

    with engine_mod.Engine() as eng:
        for g in pending:
            if args.max_minutes and (time.time() - start) / 60 >= args.max_minutes:
                print(f"[{time.strftime('%H:%M:%S')}] Hit --max-minutes budget, stopping cleanly.",
                      flush=True)
                break
            t0 = time.time()
            try:
                n_plies = engine_mod.analyze_and_store(eng, conn, g)
            except Exception as e:
                print(f"[{time.strftime('%H:%M:%S')}] ERROR on {g['url']}: {e} -- skipping", flush=True)
                continue
            dt = time.time() - t0
            done += 1
            total_plies += n_plies
            remaining = total_pending - done
            print(f"[{time.strftime('%H:%M:%S')}] {done}/{len(pending)} done "
                  f"(game id {g['id']}, {n_plies} plies, {dt:.1f}s) -- {remaining} still pending overall",
                  flush=True)

    elapsed = time.time() - start
    print(f"[{time.strftime('%H:%M:%S')}] Session done: {done} games analyzed, "
          f"{total_plies} positions, {elapsed/60:.1f} min elapsed.", flush=True)
    still_pending = store.games_needing_evaluation(conn, since_date=args.since)
    print(f"[{time.strftime('%H:%M:%S')}] {len(still_pending)} games still pending -- re-run to continue.",
          flush=True)


if __name__ == "__main__":
    main()
