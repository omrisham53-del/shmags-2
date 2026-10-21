# Chess Learning System: Build Plan

**Created:** 2026-10-19
**Goal it serves:** 1600 rapid (10+0) on chess.com. Currently 1193.
**Discovery session:** `brainstorms/2026-10-19_chess-learning-routine.md` (full reasoning behind every choice here)

---

## What this is

A set of tools that turn Omri's own games into targeted training, replacing a paid chess.com membership with local Stockfish plus custom software. Secondary goal, stated explicitly: the build itself should grow his Claude Code skills and produce something presentable.

**The diagnosis it is built around.** Two failure modes, one root cause:

1. **One-move collapses** from winning positions. Visible in six batches of existing engine data.
2. **Slow failure to capitalize** on a lead over many moves, with no single identifiable blunder.

Underneath both, in Omri's words: *"thinking about my opponent's possible move under the time pressure."* A process gap, not a knowledge gap. Tactics 1871 against Rapid 1193 is not evidence that he needs more pattern recognition; it is evidence that puzzles announce a win exists and real games do not.

"Improve my endgames" is not a third item. It is the same problem as failure mode 2.

---

## Four rules every training surface must obey

These exist because Omri raised the risk himself: training with hints and explanations could degrade the unaided board-reading he needs mid-game. They are constraints, not preferences.

1. **Commit before explain.** Position shown cold, move committed, explanation only after. Feedback after a commitment teaches; commentary before it is a crutch.
2. **Never state that a win exists.** Do not reveal whether a position is winning, equal, or lost.
3. **Include null positions** where the correct answer is a quiet consolidating move, or just not losing. This is the single highest-leverage design choice in the build, because it is the thing that attacks the tactics-to-rapid transfer gap directly.
4. **Clock the drills,** calibrated to his real measured per-move time. Training should be harder than the game, not easier.

Applied to game review as well: **he writes his own guess at what went wrong before seeing any engine output.** The recorded gap between his guess and the engine's answer is his board-reading skill, measured over time.

---

## The session routine

4 sessions per week, about 12 rapid games per week. That volume is the fuel supply for everything below; the diagnostic needs roughly three weeks of it to find real patterns.

| Block | Time | What |
|---|---|---|
| Play | ~40 min | 2-3 rapid games, 10+0, chess.com |
| Self-review | 5 min | His guess at what went wrong, before any engine output |
| Engine pass | automatic | Pipeline runs on the games just played |
| Drill | 15 min | Positions from previous sessions, cold and clocked |
| Book | 20 min | Rozman *How to Win at Chess: Intermediate*, one concept, logged in his own words |

---

## Milestones

Sequenced so the cheapest thing that could invalidate later work runs first.

### M0: Foundation and clock analyzer -- DONE 2026-10-21

**Why first:** it is cheap, it shares all its plumbing with everything downstream, and it can redirect a whole workstream before that workstream is built.

- `scripts/chess/fetch.py` -- pull games from the chess.com public API, filter to rapid 10+0, store raw PGNs. Public endpoint, no auth, no membership. Idempotent, re-runnable. Pulled the full archive: 1,506 rapid 10+0 games, 2020-2026.
- `scripts/chess/store.py` -- local SQLite store (`scripts/chess/chess.db`, gitignored): games, moves, evaluations, annotations, drill history. Everything else reads and writes through this. Evaluations/annotations/drills tables created now (empty) for M1/M2/M3.
- `scripts/chess/clock.py` -- parses the `[%clk ]` annotations already present in chess.com PGNs, derives per-move time spent, buckets by game phase (opening/middlegame/endgame, with a short-game fallback to even thirds).

**The hypothesis M0 exists to test:** if Omri burns most of his clock in the opening and early middlegame and reaches won endgames with a minute left, then failure mode 2 is a **time-allocation problem, not an endgame-knowledge problem**, and the fix is pacing rather than technique study.

**Verdict: hypothesis does NOT hold.** Full report at `clock-analysis-report.md`. Entering the endgame phase he averages ~381s (6.4 min) remaining in games he eventually wins, ~327s even in games he loses -- only 4-5% of games see him under 60s by that point. True across the full 2020-2026 archive and when restricted to 2026 alone (ruling out old habits diluting a real recent pattern). **M4 proceeds as originally scoped, not reshaped** -- failure mode 2 looks like a genuine conversion/technique gap, not a clock-management one. Caveat flagged in the report: this doesn't yet confirm these are genuinely winning positions at endgame entry, since that needs M1's real evaluations -- worth a finer-grained re-check (clock at the exact moment an advantage starts eroding) once M1 exists.

### M1: Engine layer and the two detectors -- CODE DONE 2026-10-21, BATCH ANALYSIS RUNNING

- `scripts/chess/engine.py` -- Stockfish wrapper (`C:\Users\User\OneDrive\Documents\stockfish\stockfish-windows-x86-64-avx2.exe`), full-game analysis at depth 18, evaluations cached in the store (`scripts/chess/chess.db`) so no position is ever analyzed twice. One eval per ply, White-POV centipawns; cp_loss and is_best_move computed against the engine's top choice from the position before each move.
- `scripts/chess/analyze_batch.py` -- resumable driver, newest-first, checkpoints to the DB after every single game so it's safe to interrupt and resume anytime. **Rescoped 2026-10-21, same day:** first launched against the full 670-game 2026 set assuming ~0.9s/position (one fast opening-only benchmark), but real per-game pace varied 4x on the first two games (63s vs 400s) -- true cost looked more like 20-30+ hours of continuous 3-thread CPU, not the estimated 12. Stopped and relaunched with `--limit 60` (the most recent 60 games) instead: the original six-batch diagnosis that found both failure modes was built from about that many games total, so a fresh ~60-game sample is enough to validate the decay detector and produce a real report, without tying up the machine for a day plus for marginal gain. Full-archive backfill (`--since 2020-01-01`, no `--limit`) stays available as optional, opportunistic future work -- mainly useful for M5's pattern matcher later, not blocking anything now.
- `scripts/chess/detect.py` -- two detectors, runnable against whatever's analyzed so far (prints coverage N/670):
  - **Cliff detector.** Single-move cp_loss >= 200 on my own moves. The known-good one; existing tracker output is full of its findings.
  - **Decay detector.** My-perspective eval peaking >= 150cp then eroding to <= 0cp over >= 10 plies with no single qualifying cliff inside. This does not exist anywhere else and is the only thing that can see failure mode 2.
  - `is_hollow_streak()` -- carried forward from the retired bi-weekly routine: long engine-best streaks are frequently hollow (book moves, king shuffles in decided positions) and must not be scored as skill. Reusable filter for whenever M3/M6 build highlight selection.
  - Clock join built in: every cliff and every decay-window move carries its `time_spent`, directly answering "do blunders come from fast moves?" (report section: "Direct answer").

**Deliverable:** `python scripts/chess/detect.py --write` → `projects/chess/engine-analysis-report.md`, a recurring-pattern report (not "best game of the batch") that refreshes as coverage grows. Re-run once the background batch has made real progress -- with 1 game in, the pipeline is confirmed working end to end but has nothing statistically meaningful to say yet.

### M2: `/chess-review` slash command -- DONE 2026-10-21

The daily driver. One command at the end of a session.

- `scripts/chess/review_session.py` -- finds games played since the last review (new `games.reviewed_at` column; all 1,506 pre-existing games bulk-marked reviewed on rollout so this starts clean, not with a backlog), ensures each has clock + engine data (running inline if the M1 batch hasn't reached it yet), runs the cliff/decay detectors, and prints structured findings as JSON -- no prose, that's Claude's job.
- `.claude/commands/chess-review.md` -- the command itself. Asks for his self-review guess BEFORE showing any engine output (rule 1), **Claude writes the natural-language explanations** (Stockfish supplies the number, the model supplies the reason the move loses -- the division of labour that makes the system work and the thing Omri actually asked for), states the guess-vs-engine gap plainly, appends a dated entry to the new `study-log.md`, then marks the games reviewed.
- **Bug caught building this, fixed before it could compound:** a cliff's cp_loss showed 99986 -- a mate-score arithmetic artifact (eval_white_prev to eval_white_after differenced straight through a mate-score conversion), the exact failure class the retired routine's "hollow streak" lesson warned about, just manifesting differently. Fixed at the source in `engine.py` (cap eval magnitudes to +/-1000 before diffing, going forward) and at read-time in `detect.py` (clip anything already stored above 2000, for the games M1's batch had already analyzed before the fix landed).

### M3: Drill generator and HTML board -- DONE 2026-10-21, local build verified

The showable piece. Portfolio value is an explicit requirement, so it got a real design pass and a real browser test (Playwright, installed for this), not just a static-file check.

- `scripts/chess/sync_puzzles.py` -- downloads Lichess's CC0 puzzle DB (one-time, ~307MB compressed), reservoir-samples down to a 3,000-puzzle working pool in Omri's rating band (993-1393, centered on his rapid rating -- the puzzles aren't meant to test raw tactical difficulty, since Tactics 1871 already shows that's not the bottleneck). **Hit a real SSL issue downloading:** Python's bundled CA store had a stale Let's Encrypt intermediate in this environment (confirmed via `openssl` that the leaf cert itself was valid), while curl/schannel validated fine against Windows's live-updated trust store -- fixed by shelling out to curl for this one download rather than disabling verification.
- `scripts/chess/drills.py` -- builds a drill set as JSON from three sources, shuffled together: his own blunder positions (one move *before* the mistake, from M1's cliffs), his own null positions (quiet moments where cp_loss was low and the position wasn't already decided), and the Lichess puzzle pool. **The mixing is the mechanism, not a convenience** -- every puzzle is by construction solvable, which would violate rule 2 on its own; interleaving with his own null positions means he can never assume a win exists. **Known v1 limitation, flagged honestly rather than hidden:** null/puzzle drills accept only the engine's single top move as correct, even though a null position by definition often has several equally fine moves -- real MultiPV tolerance is a future improvement, not built now.
- `scripts/chess/build_board.py` -- bakes the drill set into one self-contained HTML file (`projects/chess/drill-board.html`): no live engine, no external libraries or CDN, works offline. Chess pieces rendered via Unicode glyphs on a hand-built 8x8 grid (no chessboard.js dependency). Enforces commit-before-explain structurally (no engine data reaches the page until a move is clicked or skipped) and a clock calibrated to his real measured per-move time from M0 (8s -- tighter than his 8-14s/move average, per rule 4: harder than the game, not easier). Theme-aware (light/dark), orients the board to whoever's actually on move.
- **Real bug caught in browser testing, not just a lint pass:** the board didn't visually update after a move was committed -- feedback said "Right -- b6b7" but the piece stayed on b6. Fixed with a minimal move-applier (`applyMove`) handling captures, promotion, castling, and en passant, so the resulting position actually reflects what should have happened. Verified via Playwright: real click-driven moves, skip path, and the full-session summary screen, in both light and dark color schemes.

### M4: Conversion drills (terminal)

**Gated on M0's verdict.** Only worth building if the clock analysis says conversion failure is a technique problem rather than a pacing one.

Replays his own blown winning positions against live local Stockfish, from his side, repeatedly. Needs a live engine, hence terminal rather than browser, hence lower frequency.

### M5: Book loop and position-pattern matcher

- Concept log: one entry per studied chapter, in his own words. Read the book in order, since Rozman built a sequenced curriculum and skipping around breaks dependencies.
- `scripts/chess/patterns.py` -- back-searches the whole archive for positions matching a concept's structural conditions, then shows what he actually did. "Here are 7 of your games where both kings castled opposite; in 5 you never started a pawn storm."
- Chapter first, then the games. The concept provides the lens he re-reads his own play through.

### M6: Routine consolidation -- DONE 2026-10-21

- **Mirrored both routine prompts into the repo first** (`routine-prompts.md`), via direct `RemoteTrigger` API access rather than the claude.ai UI -- unblocked in one step rather than needing a separate manual-transcription session.
- **Fixed Routine A (`trig_01BaX2JcLCMbWYVAHh792kSd`):** now always appends a Rating Log row every 3-day run (not only when ratings change), with a **games-played-per-format column**. Backfilled retroactively against the real chess.com archive for Jul-Oct 2026, which confirmed the hypothesis exactly: **zero rapid games played in every single window from Sept 4 through Oct 19** -- 8 straight rows, ~6.5 weeks, that "Rapid unchanged" never made visible on its own.
- **Retired the metadata flagger** (was Part 3 of Routine A). ~100 flagged rows, almost all "decisive finish (checkmate)", because at 1200 nearly every game ends in mate -- it flagged nearly everything so it discriminated nearly nothing.
- **Retired Routine B (`trig_01JFSQUYQf78TzhRxQmxuHoQ`)**, disabled not deleted. Its input (the flagger) is gone, and it's superseded by M1's local pipeline once built. The one lesson worth carrying forward -- long engine-best streaks are frequently hollow and must not be scored as skill -- is preserved in `routine-prompts.md` and the tracker's retired tables.
- Improvers Club candidate selection becomes a query against the local store once M1/M2 exist, rather than its own scheduled routine -- still pending on M1/M2, not yet built.

---

## Measurement

The rating is a lagging indicator. 1193 to 1600 is realistically a 6 to 12 month climb, so judging the system on rating in December would wrongly declare it broken.

**What should move by December:**

| Metric | Source | Direction |
|---|---|---|
| Blunders per rapid game | M1 cliff detector | down |
| Advantage-decay episodes per game | M1 decay detector | down |
| Conversion rate from +300 or better | M1 + store | up |
| Gap between his self-review guess and the engine | M2 | down |
| Repeat-blunder rate on drilled positions | M3 drill history | down |
| Clock remaining on reaching a winning endgame | M0 | up |
| Rapid games played per week | fixed Routine A | at or above 12 |

Rating follows those. If they improve and rating does not, something is wrong with the model of the problem, and that is worth knowing.

---

## Out of scope for v1

- **Openings.** Caro-Kann as Black, London and d4 setups as White. Left out deliberately: most points between 1200 and 1600 are lost in the middlegame. An acknowledged gap, not a resolved question.
- **Human coach in the loop.** The occasional NM Dane Mattson online lessons stay as they are; the system does not prepare material for them.
- **Blitz.** Not the goal format. Blitz games get stored but not analyzed or drilled.
