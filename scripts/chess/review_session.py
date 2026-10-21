"""
M2 support script for the /chess-review slash command. Finds games played
since the last review, makes sure they have clock + engine data, runs the
cliff/decay detectors on just those games, and prints structured findings
for Claude to narrate. See projects/chess/learning-system-plan.md M2.

This script does NOT write natural-language explanations -- that's the
division of labour the plan calls for: Stockfish supplies the number, the
model supplies the reason the move loses.

Usage:
    python scripts/chess/review_session.py            # fetch + analyze + report unreviewed games
    python scripts/chess/review_session.py --mark-reviewed 1489,1490   # call after narrating
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402
import engine as engine_mod  # noqa: E402
from clock import parse_game_clock  # noqa: E402
from detect import find_cliffs, find_decay_episodes, _game_trajectory  # noqa: E402


def ensure_clock_and_eval(conn, game_row):
    if not game_row["clock_parsed"]:
        moves = parse_game_clock(game_row["pgn"])
        if moves and any(m["clock_seconds"] is not None for m in moves):
            store.replace_moves(conn, game_row["id"], moves)
        else:
            conn.execute("UPDATE games SET clock_parsed = 1 WHERE id = ?", (game_row["id"],))
            conn.commit()

    has_eval = conn.execute(
        "SELECT 1 FROM evaluations WHERE game_id = ? LIMIT 1", (game_row["id"],)
    ).fetchone()
    if not has_eval:
        with engine_mod.Engine() as eng:
            # re-fetch the row so clock_parsed reflects what we just did
            fresh = conn.execute("SELECT * FROM games WHERE id = ?", (game_row["id"],)).fetchone()
            engine_mod.analyze_and_store(eng, conn, fresh)


def review_pending(conn) -> list:
    pending = store.games_needing_review(conn)
    results = []
    for g in pending:
        ensure_clock_and_eval(conn, g)
        fresh = conn.execute("SELECT * FROM games WHERE id = ?", (g["id"],)).fetchone()
        traj = _game_trajectory(conn, fresh)
        cliffs = find_cliffs(traj)
        decays = find_decay_episodes(traj)
        results.append({
            "game_id": fresh["id"],
            "url": fresh["url"],
            "end_date": fresh["end_date"],
            "my_color": fresh["my_color"],
            "my_result": fresh["my_result"],
            "opp_rating": fresh["opp_rating"],
            "my_rating": fresh["my_rating"],
            "termination": fresh["termination"],
            "ply_count": len(traj),
            "cliffs": [
                {"ply": c["ply"], "move_san": c["move_san"], "best_move_san": c["best_move_san"],
                 "cp_loss": c["cp_loss"], "time_spent": c["time_spent"], "phase": c["phase"]}
                for c in cliffs
            ],
            "decays": [
                {"peak_ply": d["peak_ply"], "peak_eval": d["peak_eval"],
                 "trough_ply": d["trough_ply"], "trough_eval": d["trough_eval"],
                 "span_plies": d["span_plies"],
                 "my_moves_in_window": [
                     {"ply": m["ply"], "move_san": m["move_san"], "cp_loss": m["cp_loss"],
                      "time_spent": m["time_spent"]}
                     for m in d["my_moves_in_window"]
                 ]}
                for d in decays
            ],
        })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mark-reviewed", default=None,
                         help="Comma-separated game ids to mark reviewed (call after narrating)")
    args = parser.parse_args()

    conn = store.init_db()

    if args.mark_reviewed:
        ids = [int(x) for x in args.mark_reviewed.split(",") if x.strip()]
        store.mark_reviewed(conn, ids)
        print(f"Marked {len(ids)} game(s) as reviewed: {ids}")
        return

    results = review_pending(conn)
    if not results:
        print(json.dumps({"status": "no_new_games", "results": []}))
        return
    print(json.dumps({"status": "ok", "results": results}, indent=2))


if __name__ == "__main__":
    main()
