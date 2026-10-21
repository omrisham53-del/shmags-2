# scripts/

Standalone scripts that run from the command line (no MCP / no Claude needed).

## job-tracker.py - Job opportunity tracker automation

Moved here 2026-07-24 from `.claude/skills/` (skills are .md trigger files; this is the actual automation code). Job search is paused for the Sept-Dec trip -- dormant until active search resumes. See `job_tracker_skill.md` memory for the framework this supports.

## chess/ - Local chess learning system (fetch, store, clock analysis)

Built 2026-10-21 for `projects/chess/learning-system-plan.md` M0. Replaces paid chess.com membership + the retired cloud routines with local Stockfish and a SQLite store.

```bash
python scripts/chess/fetch.py          # pull new games from chess.com's public API, filter to rapid 10+0
python scripts/chess/clock.py          # parse [%clk] annotations, bucket by phase, print the clock-pattern report
python scripts/chess/analyze_batch.py  # Stockfish depth-18 analysis, resumable, newest-first (slow: ~1s/position)
python scripts/chess/detect.py --write # cliff + decay detectors over whatever's analyzed so far
python scripts/chess/review_session.py # M2 support: finds games played since the last /chess-review, analyzes if needed, prints findings as JSON
python scripts/chess/sync_puzzles.py   # one-time: Lichess CC0 puzzle DB -> rating-matched local pool
python scripts/chess/drills.py --write # M3: builds drill-set.json from own blunders + own null positions + puzzle pool
python scripts/chess/build_board.py    # bakes drill-set.json into the self-contained drill-board.html
```

Day-to-day use is the `/chess-review` slash command (`.claude/commands/chess-review.md`), not these scripts directly -- run it at the end of a chess session.

- `store.py` -- SQLite store at `scripts/chess/chess.db` (gitignored, rebuildable from chess.com's API + local Stockfish). Schema covers games/moves/evaluations/`reviewed_at` now, plus an annotations/drills tables for M3.
- `fetch.py` -- idempotent, safe to re-run; only inserts games not already stored.
- `clock.py` -- parses unparsed games then reports. `--report-only` skips parsing.
- `engine.py` -- Stockfish wrapper (depth 18, 3 threads), one eval per ply, never re-analyzes a cached position. Eval magnitudes capped to +/-1000 before computing cp_loss, so a move crossing into/out of a forced mate doesn't produce a deceptive ~100000 "centipawn loss" (a real bug caught building M2).
- `analyze_batch.py` -- checkpoints after every game, so it's always safe to kill and re-run. Meant to run for a while unattended (`nohup python scripts/chess/analyze_batch.py --limit N > scripts/chess/analysis_log.txt 2>&1 &` on this machine) -- heavy on CPU (3 engine threads) for as long as it runs. Use `--limit` -- real per-game pace varies 4x+, so size the batch deliberately rather than assuming a quick benchmark holds.
- `detect.py` -- cliff detector (single-move collapses) + decay detector (slow-bleed losses, joined against clock data to check if blunders come from fast moves).
- `review_session.py` -- M2's engine: games with `reviewed_at IS NULL`, oldest first. Outputs JSON only, no prose -- the slash command does the explaining.
- `sync_puzzles.py` -- one-time Lichess CC0 puzzle DB sync (~307MB compressed download, reservoir-sampled to a 3,000-puzzle local pool, ~380KB). Downloads via curl rather than Python's urllib -- the bundled CA store had a stale intermediate for Lichess's cert chain in this environment (confirmed the leaf cert was fine via openssl; curl/schannel validates against Windows's own live trust store instead).
- `drills.py` -- M3 data layer: own-blunder + own-null + puzzle-pool drills, shuffled together, written to `projects/chess/drill-set.json`.
- `build_board.py` -- M3 presentation layer: bakes the drill set into `projects/chess/drill-board.html`, a single offline-capable file with no external dependencies.

Full writeups: `projects/chess/clock-analysis-report.md` (M0), `projects/chess/engine-analysis-report.md` (M1, refresh with `detect.py --write` as analysis coverage grows), `projects/chess/study-log.md` (M2, one dated entry per `/chess-review` run), `projects/chess/drill-board.html` (M3, the drill board itself -- just open it in a browser).

## sync_jobs.py - Bidirectional sync with the "Job Applications" Notion DB

One-time setup:

1. Create a Notion internal integration at https://www.notion.so/profile/integrations
   - Type: Internal
   - Capabilities: Read content, Update content, Insert content
2. Open the **Job Search** page in Notion. Click the `...` menu in the top right -> **Connections** -> search for your new integration and add it. This gives the integration access to the page and its child database.
3. Copy the integration's "Internal Integration Secret".
4. Create a `.env` file in the repo root (already gitignored):

   ```
   NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. Install dependencies:

   ```
   pip install requests python-dotenv
   ```

Daily use:

```bash
# After /job-tracker adds new rows to tracker.md
python scripts/sync_jobs.py push

# After marking statuses in Notion
python scripts/sync_jobs.py pull

# See drift between the two sides without writing
python scripts/sync_jobs.py status
```

Notes:

- Dedup key is the **Link** column. Rows without a link are skipped on push.
- Push only updates a Notion row if at least one field changed.
- Pull regenerates `tracker.md` from scratch, sorted by Date Found (newest first), grouped by status priority. The file's surrounding prose (legend, etc.) is preserved by the template in `write_tracker()`.
- Database ID and data-source ID are hardcoded in the script. If the DB is recreated, update `DATABASE_ID` at the top.
