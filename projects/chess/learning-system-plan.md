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

### M0: Foundation and clock analyzer

**Why first:** it is cheap, it shares all its plumbing with everything downstream, and it can redirect a whole workstream before that workstream is built.

- `scripts/chess/fetch.py` -- pull games from the chess.com public API, filter to rapid 10+0, store raw PGNs. Public endpoint, no auth, no membership. Already proven to work from the existing routines.
- `scripts/chess/store.py` -- local SQLite store: games, moves, evaluations, annotations, drill history. Everything else reads and writes through this.
- `scripts/chess/clock.py` -- parse the `[%clk ]` annotations already present in chess.com PGNs, derive per-move time spent, bucket by game phase.

**The hypothesis M0 exists to test:** if Omri burns most of his clock in the opening and early middlegame and reaches won endgames with a minute left, then failure mode 2 is a **time-allocation problem, not an endgame-knowledge problem**, and the fix is pacing rather than technique study. This is checkable retroactively against his entire existing archive, before any training is built. If it comes back true, M4 changes shape or disappears.

**Deliverable:** a report on his real clock patterns, and a verdict on that hypothesis.

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

### M6: Routine consolidation

- **Keep Routine A (`trig_01BaX2JcLCMbWYVAHh792kSd`), fixed:** split its two jobs apart, and **add a games-played-per-format column** to the Rating Log. Eight rows since Sept 13 read "Rapid unchanged" and hid a five-week rapid blackout, because a flat rating looks identical to inactivity. This column would have surfaced the laptop-access problem in mid-September.
- **Retire the metadata flagger.** About 100 flagged rows, almost all "decisive finish (checkmate)", because at 1200 nearly every game ends in mate. It flags nearly everything so it discriminates nearly nothing.
- **Retire Routine B (`trig_01JFSQUYQf78TzhRxQmxuHoQ`).** Superseded by the local pipeline on depth, on not reinstalling Stockfish into a fresh sandbox every run, and on having a coaching objective instead of a storytelling one.
- **Blocked:** both routine prompts live only in the claude.ai routines UI and exist nowhere in this repo, so their logic cannot be audited or recovered. Mirror them into the repo first. Omri is handling that in a separate session, so **Routine B must not be retired until that lands.**
- Improvers Club candidate selection becomes a query against the local store rather than its own scheduled routine.

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
