"""
One-time sync of Lichess's openly-licensed puzzle database (CC0), filtered
to a rating band around Omri's own level. Downloaded as a data file, no
account, no platform use -- he has neither and dislikes the site. See
projects/chess/learning-system-plan.md M3.

Rating band defaults to his rapid rating (1193) +/- 200: the point of these
puzzles isn't raw tactical difficulty (his Tactics 1871 already shows vision
isn't the bottleneck) -- it's volume at roughly the difficulty he actually
plays at, mixed with his own null positions so he can't assume a puzzle
always has a win. Full DB is ~307MB compressed / several GB of rows;
streamed and filtered without ever materializing the whole thing on disk.

Usage:
    python scripts/chess/sync_puzzles.py                      # band 993-1393
    python scripts/chess/sync_puzzles.py --min 1000 --max 1400
"""

import argparse
import csv
import io
import subprocess
import sys
from pathlib import Path

import zstandard

URL = "https://database.lichess.org/lichess_db_puzzle.csv.zst"
RAW_PATH = Path(__file__).parent / "lichess_db_puzzle.csv.zst"
OUT_PATH = Path(__file__).parent / "puzzles_filtered.csv"


def download_if_missing():
    if RAW_PATH.exists():
        print(f"Using cached {RAW_PATH} ({RAW_PATH.stat().st_size / 1e6:.0f} MB).")
        return
    print(f"Downloading {URL} ...")
    # Shells out to curl rather than urllib: Python's bundled CA store has a stale
    # Let's Encrypt intermediate in this environment (confirmed via openssl -- the
    # leaf cert itself is valid), while curl validates against Windows's own
    # live-updated trust store. Real validation either way, just not stale.
    subprocess.run(["curl", "-sS", "-o", str(RAW_PATH), URL], check=True)
    print(f"Downloaded {RAW_PATH.stat().st_size / 1e6:.0f} MB.")


def filter_and_write(rating_min: int, rating_max: int, pool_size: int):
    """Reservoir-samples (Algorithm R) down to pool_size while streaming --
    1.6M+ rows match a typical rating band, far more than any realistic
    working pool needs, so this avoids ever materializing the full match set."""
    import random
    random.seed(42)  # reproducible pool across re-runs, not security-sensitive

    dctx = zstandard.ZstdDecompressor()
    reservoir = []
    matched = 0
    seen = 0
    with open(RAW_PATH, "rb") as compressed:
        with dctx.stream_reader(compressed) as reader:
            text_stream = io.TextIOWrapper(reader, encoding="utf-8")
            r = csv.reader(text_stream)
            header = next(r)
            idx = {name: i for i, name in enumerate(header)}
            for row in r:
                seen += 1
                try:
                    rating = int(row[idx["Rating"]])
                except (ValueError, IndexError):
                    continue
                if rating_min <= rating <= rating_max:
                    record = [row[idx["PuzzleId"]], row[idx["FEN"]], row[idx["Moves"]],
                              rating, row[idx["Themes"]]]
                    matched += 1
                    if len(reservoir) < pool_size:
                        reservoir.append(record)
                    else:
                        j = random.randint(0, matched - 1)
                        if j < pool_size:
                            reservoir[j] = record
                if seen % 500000 == 0:
                    print(f"  scanned {seen:,}, matched {matched:,}, reservoir full: {len(reservoir) >= pool_size}")

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["PuzzleId", "FEN", "Moves", "Rating", "Themes"])
        writer.writerows(reservoir)

    print(f"Done: {matched:,} puzzles matched [{rating_min}, {rating_max}] out of {seen:,} scanned; "
          f"reservoir-sampled down to {len(reservoir):,}.")
    print(f"Written to {OUT_PATH} ({OUT_PATH.stat().st_size / 1e3:.0f} KB)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min", type=int, default=993)
    parser.add_argument("--max", type=int, default=1393)
    parser.add_argument("--pool-size", type=int, default=3000)
    parser.add_argument("--keep-raw", action="store_true", help="Keep the downloaded .zst (default: delete after filtering)")
    args = parser.parse_args()

    download_if_missing()
    filter_and_write(args.min, args.max, args.pool_size)
    if not args.keep_raw and RAW_PATH.exists():
        RAW_PATH.unlink()
        print("Removed cached raw download (re-run will re-fetch if needed).")


if __name__ == "__main__":
    main()
