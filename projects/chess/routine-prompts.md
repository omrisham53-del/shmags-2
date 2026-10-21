# Chess Cloud Routine Prompts (mirrored)

Both chess cloud routines previously existed only in the claude.ai routines UI, with no trace in this repo -- meaning their logic couldn't be audited, diffed, or recovered if lost. Mirrored here 2026-10-21 to unblock the M6 consolidation in `learning-system-plan.md`. Manage both at https://claude.ai/code/routines.

**Keep this file in sync with the live routine whenever either is edited.** It is documentation of the live state, not a spec Claude Code runs from directly.

---

## Routine A: Chess tracker auto-update

- **ID:** `trig_01BaX2JcLCMbWYVAHh792kSd`
- **Schedule:** every 3 days, `0 6 */3 * *` (06:00 UTC)
- **Status:** active, fixed 2026-10-21 (see decision log) -- games-played counting added, Part 3 metadata flagger removed
- **Allowed tools:** Bash, Read, Edit, Glob
- **Source:** this repo (github.com/omrisham53-del/shmags-2)

### Current live prompt (as of 2026-10-21 fix)

```
This is a low-stakes, fully automatic hobby-tracking update. Do not ask any questions, do not wait for input.

## Part 1: Rating + games-played update

1. Fetch https://api.chess.com/pub/player/shamgi/stats via curl (public chess.com API, no auth needed).
2. From the response, extract: chess_rapid.last.rating, chess_blitz.last.rating, and tactics.highest.rating (use whichever field is present; if missing, note unavailable rather than failing).
3. Read projects/chess/tracker.md in this repo. Look at the most recent row in the 'Rating Log' table, including its date.
4. Fetch https://api.chess.com/pub/player/shamgi/games/archives, then fetch the JSON archive(s) covering the period from that last logged date (inclusive) through today (the current month's archive, plus the previous month's if the window spans a month boundary).
5. From those archives, count how many games have time_class == 'rapid' and how many have time_class == 'blitz', with end_time strictly after the last logged row's date (UTC midnight) through now.
6. Always append a new row to the Rating Log table with today's date (UTC, YYYY-MM-DD), the three ratings, the rapid games count, the blitz games count, and a short note on what changed (e.g. 'Rapid +15, Tactics unchanged' or, when ratings are flat, '0 rapid games played since last row -- no play, not just no rating change'). Append this row EVERY run, even when ratings are unchanged and games-played is 0 -- a flat rating with a visible '0 games' value is the signal this column exists to catch; a flat rating with no row at all hides it again.

## Part 2: Improvers Club monthly cycle flag

7. Check the 'Improvers Club Submissions' table. If the current UTC month has no row yet (last logged row is from a prior month), append a row noting the new month's submission cycle is open, status 'Cycle open, no submission yet'. Do not fabricate a submission.

## Part 3: Commit

8. Commit projects/chess/tracker.md with a short message (e.g. 'Chess tracker: rating + games-played update (auto)') and push.
9. Keep your final output to a few short lines summarizing what you did.
```

### Retired from this routine (2026-10-21)

The old Part 3 ("Recent game review for Annotated Game of the Month candidates") used to flag games into "Flagged Game Opportunities (auto)" by metadata heuristics (upset win, checkmate finish, short decisive game). Retired because at ~1200 rating nearly every decisive game ends in checkmate -- it flagged almost everything in the table (~100 rows, nearly all "Decisive finish (checkmate)") and discriminated nearly nothing. See `learning-system-plan.md` M6 and M1 (the decay/cliff detectors are the real replacement, once built).

### Prior version (as mirrored, pre-fix, created 2026-07-10)

<details>
<summary>Original 4-part prompt (rating update conditional on change + metadata flagger), superseded 2026-10-21</summary>

```
This is a low-stakes, fully automatic hobby-tracking update. Do not ask any questions, do not wait for input.

## Part 1: Rating update

1. Fetch https://api.chess.com/pub/player/shamgi/stats via curl (public chess.com API, no auth needed).
2. From the response, extract: chess_rapid.last.rating, chess_blitz.last.rating, and tactics.highest.rating (use whichever field is present; if missing, note unavailable rather than failing).
3. Read projects/chess/tracker.md in this repo. Look at the most recent row in the 'Rating Log' table.
4. If any of the three ratings differ from that last logged row, append a new row to the Rating Log table with today's date (UTC, YYYY-MM-DD) and the new ratings, with a short note on what changed (e.g. 'Rapid +15, Tactics unchanged').
5. If nothing changed, do not add a row.

## Part 2: Improvers Club monthly cycle flag

6. Check the 'Improvers Club Submissions' table. If the current UTC month has no row yet (last logged row is from a prior month), append a row noting the new month's submission cycle is open, status 'Cycle open, no submission yet'. Do not fabricate a submission.

## Part 3: Recent game review for Annotated Game of the Month candidates

7. Fetch https://api.chess.com/pub/player/shamgi/games/archives to get the list of monthly archive URLs. Fetch the JSON for the current UTC month's archive, and the previous month's archive too (in case the 3-day window spans a month boundary).
8. From those archives, filter to games whose end_time falls within the last 3 days (UTC) from now.
9. For each game in that window, apply these heuristic flags (metadata only, no engine needed):
   - Upset win: Omri won and the opponent's rating is at least 100 points higher than his own rating at the time.
   - Decisive finish: game ended by checkmate (either side) rather than resignation/timeout/draw.
   - Notably short decisive game: fewer than 20 total moves and a clear win/loss (possible brilliancy or blunder worth a look).
   Only flag games matching at least one of these -- most games in a 3-day window will match none, and that's fine, don't force it.
10. Read projects/chess/tracker.md's 'Flagged Game Opportunities (auto)' table (columns: Date, Opponent (rating), Result, Why flagged, Link, Status). For each newly-flagged game not already listed there (match on date + opponent), append a row with Status set to 'Flagged, pending analysis'. The game's URL is in the archive JSON's 'url' field per game.
11. If there's nothing to flag, don't add anything.

## Part 4: Commit

12. If you changed projects/chess/tracker.md in any part above, commit with a short message (e.g. 'Chess tracker: update ratings + flag N game(s) (auto)') and push. If nothing changed anywhere, do not commit.
13. Keep your final output to a few short lines summarizing what you did (or that nothing changed).
```

</details>

---

## Routine B: Chess bi-weekly Stockfish analysis

- **ID:** `trig_01JFSQUYQf78TzhRxQmxuHoQ`
- **Schedule:** 1st and 16th of each month, `0 7 1,16 * *` (07:00 UTC)
- **Status:** retired 2026-10-21 (disabled, not deleted -- see decision log)
- **Allowed tools:** Bash, Read, Edit, Glob
- **Source:** this repo (github.com/omrisham53-del/shmags-2)

### Prompt at time of retirement (created 2026-07-10, never edited)

```
This is a low-stakes, fully automatic hobby-analysis routine. Do not ask any questions, do not wait for input.

## Part 0: Set up analysis tools in this sandbox

1. Try to install Stockfish: `sudo apt-get update -qq && sudo apt-get install -y stockfish` (or `apt-get` without sudo if already root). Then `pip install --quiet python-chess`. If installation fails for any reason (no package manager access, no internet to package repos, etc.), fall back to a metadata-only comparison in Part 2 below (pick the batch's best candidate using the same heuristics as the flagging routine: upset win margin, checkmate finish, shortness of decisive game) and clearly note in the tracker and your final output that this run used metadata-only comparison, not engine analysis.

## Part 1: Gather pending games

2. Read projects/chess/tracker.md. In the 'Flagged Game Opportunities (auto)' table, find all rows with Status = 'Flagged, pending analysis'.
3. If there are none, skip to Part 4 (nothing to do this run, but still check Part 4's monthly comparison in case a prior batch this month is waiting on this one -- unlikely if there's nothing pending, but check anyway).

## Part 2: Analyze each pending game

4. For each pending game, determine its year/month from its Date column, then fetch https://api.chess.com/pub/player/shamgi/games/{year}/{month} (zero-padded month, e.g. 07) to get that month's game archive, and find the matching game by its URL (from the Link column). Extract its 'pgn' field.
5. If Stockfish is available: analyze the game with python-chess (`chess.engine.SimpleEngine.popen_uci("stockfish")`), depth 18, walking through Omri's moves (he may be either White or Black -- determine from the PGN headers) and classifying each by centipawn loss vs the engine's top choice. Compute per game: total centipawn loss for Omri's moves, count of moves matching the engine's best move, longest consecutive streak of engine-best moves, and the single biggest evaluation swing in the game (a blunder or brilliancy).
6. Pick the single most compelling candidate from this batch: favor a long streak of consecutive engine-best moves converting a difficult position, a dramatic evaluation swing, or an otherwise clean decisive win with a real story -- not just the lowest average centipawn loss. This is the 'batch pick' for this run.
7. Update the 'Flagged Game Opportunities (auto)' table: change Status to 'Analyzed' for every game you just processed.
8. Append one row to the 'Bi-Weekly Stockfish Analysis (auto)' table: Date Run (today, UTC), Games Analyzed (count), Batch Pick (opponent + date + link), Engine Reasoning (1-2 sentences on why this game, referencing the specific engine-verified moments -- e.g. move numbers with a best-move streak, or the size of a blunder/brilliancy swing).

## Part 3: (only if nothing was pending in Part 1)

If Part 1 found no pending games, don't add a row to 'Bi-Weekly Stockfish Analysis (auto)' for this run -- there's no batch to log.

## Part 4: Monthly comparison

9. Count how many rows in 'Bi-Weekly Stockfish Analysis (auto)' have a Date Run within the current UTC calendar month (including any row you just added in Part 2).
10. If that count is 2 or more for this month, take this run's batch pick and the OTHER batch-pick row from earlier this same month, compare them (favor the more engine-verified, more dramatic, more clearly-tellable story), and append one row to 'Monthly Submission Candidate (auto)': Month (e.g. 'July 2026'), Recommended Game (opponent + date + link), Reasoning (why it beats the other batch's pick, referencing both), Status 'Recommended -- Omri to write hook + annotate + submit'. Do not write the actual annotation, hook, or submission text yourself -- that part is Omri's work, this is just picking which game.
11. If the count is less than 2, skip this step entirely -- there's nothing to compare yet.

## Part 5: Commit

12. If you changed projects/chess/tracker.md anywhere above, commit with a short message (e.g. 'Chess tracker: bi-weekly Stockfish analysis (auto)') and push. If nothing changed, do not commit.
13. Keep your final output to a few short lines: how many games were analyzed, the batch pick if any, and whether a monthly recommendation was made.
```

**Why retired rather than kept running:** its own data source (the metadata flagger in Routine A) is retired in the same change, so it would run bi-weekly with nothing to process. More fundamentally, per `learning-system-plan.md` M6, it's superseded by the local pipeline (M1's cliff/decay detectors) on depth, on not reinstalling Stockfish into a fresh cloud sandbox every run, and on having a coaching objective (what does Omri keep getting wrong) instead of a storytelling one (what's the best club-submission narrative). One piece of its judgment carries forward and must not be lost when M1 is built: **long engine-best streaks are frequently hollow** (king shuffles in lost endgames, opening-book moves, trivial promotions) and must not be scored as skill -- learned the hard way across six real batches (see the Bi-Weekly Stockfish Analysis table above for the specific games that taught this).

**Improvers Club candidate selection** becomes a query against the local store once M1/M2 exist, rather than its own scheduled routine.
