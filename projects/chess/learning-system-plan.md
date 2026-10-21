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

### M1: Engine layer and the two detectors

- `scripts/chess/engine.py` -- Stockfish wrapper (`C:\Users\User\OneDrive\Documents\stockfish\stockfish-windows-x86-64-avx2.exe`), full-game analysis at depth 18, evaluations cached in the store so no position is ever analyzed twice.
- `scripts/chess/detect.py` -- two detectors:
  - **Cliff detector.** Single-move evaluation collapses. The known-good one; existing tracker output is full of its findings.
  - **Decay detector.** Sustained winning evaluation eroding across many moves with no single large swing. This does not exist anywhere yet and is the only thing that can see failure mode 2.
- **Carry forward from the retiring bi-weekly routine:** long engine-best streaks are frequently hollow (king shuffles inside lost endgames, opening-book moves, trivial pawn promotions) and must not be scored as skill. This was learned across six real batches and is the one piece of that routine worth keeping.
- Join against M0's clock data to answer the direct question: do his blunders come from fast moves?

**Deliverable:** per-game annotated analysis, plus a recurring-pattern report that says what he keeps getting wrong rather than which game tells the best story.

### M2: `/chess-review` slash command

The daily driver. One command at the end of a session.

- Fetches new games, runs M0 and M1 over them.
- **Claude writes the natural-language explanations.** This is the division of labour that makes the system work: Stockfish supplies the number, the model supplies the reason the move loses. That translation is the thing Omri actually asked for.
- Reads his self-review note and sets his guess beside the engine's answer.
- Appends to a study log and updates the tracker.

### M3: Drill generator and HTML board

The showable piece. Portfolio value is an explicit requirement, so it gets a real design pass rather than a debug UI.

- `scripts/chess/drills.py` -- builds a drill set as JSON from three sources, shuffled together:
  1. **His own blunder positions,** taken one move *before* the mistake, served back days later with no indication they are his.
  2. **Null positions** from his own games where the right answer is quiet.
  3. **Public puzzle volume** from the openly-licensed Lichess puzzle CSV, rating-matched to his level. Downloaded as a data file; no account and no platform use, since he has neither and dislikes the site.
- **The mixing is the mechanism, not a convenience.** Every puzzle in a public database is by construction solvable, which would violate rule 2 on its own. Interleaving them with his own null positions means he can never assume a win exists, because sometimes there isn't one.
- Self-contained HTML board, two-phase by design: the drill set is baked offline, so the page needs no live engine. It works offline, on bad wifi, from any device, and publishes as a shareable Artifact.
- Enforces commit-before-explain and the clock in the UI itself.

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
