"""
Pull games from the chess.com public API (no auth, no membership) and store
them locally. See projects/chess/learning-system-plan.md M0.

Usage:
    python scripts/chess/fetch.py              # fetch all archive months
    python scripts/chess/fetch.py --since 2026-07   # only months >= this one
"""

import argparse
import sys
import time
import urllib.request
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import store  # noqa: E402

USERNAME = "shamgi"
API_BASE = f"https://api.chess.com/pub/player/{USERNAME}"
HEADERS = {"User-Agent": "Mozilla/5.0 (chess learning system; personal use)"}


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def list_archives() -> list:
    return fetch_json(f"{API_BASE}/games/archives")["archives"]


def result_word(raw_result: str) -> str:
    """Map chess.com's per-player result string to win/loss/draw."""
    if raw_result == "win":
        return "win"
    if raw_result in ("agreed", "repetition", "stalemate", "insufficient",
                       "50move", "timevsinsufficient"):
        return "draw"
    return "loss"


def extract_game(raw: dict) -> dict | None:
    white = raw.get("white", {})
    black = raw.get("black", {})
    white_user = white.get("username", "").lower()
    black_user = black.get("username", "").lower()

    if white_user == USERNAME:
        my_color, opp = "white", black
        my_raw_result = white.get("result")
    elif black_user == USERNAME:
        my_color, opp = "black", white
        my_raw_result = black.get("result")
    else:
        return None  # shouldn't happen on our own archive, but skip defensively

    me = white if my_color == "white" else black
    pgn = raw.get("pgn", "")
    termination = ""
    for line in pgn.splitlines():
        if line.startswith("[Termination "):
            termination = line.split('"')[1]
            break

    ply_count = pgn.count(". ") if pgn else None  # rough, refined properly in clock.py

    return {
        "url": raw.get("url"),
        "pgn": pgn,
        "white": white.get("username"),
        "black": black.get("username"),
        "white_elo": white.get("rating"),
        "black_elo": black.get("rating"),
        "my_color": my_color,
        "my_rating": me.get("rating"),
        "opp_rating": opp.get("rating"),
        "result": None,  # not provided at this granularity by the API; PGN has it if ever needed
        "my_result": result_word(my_raw_result),
        "termination": termination,
        "time_class": raw.get("time_class"),
        "time_control": raw.get("time_control"),
        "end_date": time.strftime("%Y-%m-%d", time.gmtime(raw.get("end_time", 0))),
        "end_time": time.strftime("%H:%M:%S", time.gmtime(raw.get("end_time", 0))),
        "ply_count": ply_count,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", default=None, help="Only fetch archive months >= YYYY-MM")
    parser.add_argument("--rapid-only", action="store_true", default=True,
                         help="Only store rapid 10+0 games (default: on)")
    args = parser.parse_args()

    conn = store.init_db()
    archives = list_archives()
    if args.since:
        since_key = args.since.replace("-", "/")
        archives = [a for a in archives if a.rsplit("/", 2)[-2] + "/" + a.rsplit("/", 1)[-1] >= since_key]

    total_seen = 0
    total_new = 0
    by_class = {}

    for archive_url in archives:
        data = fetch_json(archive_url)
        for raw in data.get("games", []):
            total_seen += 1
            tc = raw.get("time_class")
            by_class[tc] = by_class.get(tc, 0) + 1
            if args.rapid_only and not (tc == "rapid" and raw.get("time_control") == "600"):
                continue
            game = extract_game(raw)
            if game is None or not game["url"]:
                continue
            before = conn.execute(
                "SELECT 1 FROM games WHERE url = ?", (game["url"],)
            ).fetchone()
            store.insert_game(conn, game)
            if not before:
                total_new += 1

    print(f"Scanned {len(archives)} archive months, {total_seen} total games ({dict(by_class)}).")
    print(f"Stored {total_new} new rapid 10+0 games.")
    n = conn.execute(
        "SELECT COUNT(*) AS n FROM games WHERE time_class='rapid' AND time_control='600'"
    ).fetchone()["n"]
    print(f"DB now holds {n} rapid 10+0 games total.")


if __name__ == "__main__":
    main()
