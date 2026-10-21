# Chess

**Description:** Personal chess improvement hobby. Not a career/work priority -- something Omri enjoys in his free time.

**Status:** Active
**Account:** [shamgi](https://www.chess.com/member/shamgi) on chess.com (joined Dec 2020, returned seriously ~early 2026)

---

## The Goal

**1600 rapid (10+0) on chess.com.** Set 2026-10-19 as the explicit long-term target. Everything else in this project -- study routine, engine analysis, puzzles, the Levy Rozman book -- is in service of that number. Current gap: **+407 points** from 1193. Realistically a 6-12 month climb, so it's a 2027 target; by December the things that should move are blunder rate and conversion rate, not the rating.

**The system being built to get there:** `learning-system-plan.md` (sequenced build plan, 7 milestones). Discovery session behind it: `brainstorms/2026-10-19_chess-learning-routine.md`.

---

## Current Ratings

| Format | Rating | Notes |
|---|---|---|
| Rapid | 1193 | As of 2026-10-19. Personal best 1223 (July 2026). **Target: 1600** |
| Tactics | 1871 | Puzzle Rush best: 22. Unchanged since July 2026 |
| Blitz | 804 | As of 2026-10-19. Best: 1146 |

**The defining gap:** ~678 points between Tactics (1871) and Rapid (1193). Omri can find combinations but struggles to convert winning positions under real-game conditions -- this is the thing he's actively working on, not raw tactical vision.

## Study Resources

- **How to Win at Chess: Intermediate** (Levy Rozman / GothamChess) -- bought 2026-10-19, the current primary study text

## Openings

- **Black:** Caro-Kann (main weapon, very consistent)
- **White:** London System / d4 setups

## Study Habits

- GothamChess on YouTube (primary resource)
- Nimzowitsch's *My System* (Hebrew edition) -- advanced for his current level but starting to connect to real positions (e.g. the e5 restraint concept clicked in a real game)
- Occasional lessons with NM Dane Mattson through the Improvers Club (first one June 2026)

## Local Analysis Toolchain

- **Stockfish:** `C:\Users\User\OneDrive\Documents\stockfish\stockfish-windows-x86-64-avx2.exe`
- **python-chess:** 1.11.2 (pip installed)
- **Pattern:** `chess.engine.SimpleEngine.popen_uci()`, analyze at depth 18, classify moves by centipawn delta
- Lichess's cloud eval API only caches popular positions -- not reliable for personal games, use local Stockfish instead

## Improvers Club (chess.com)

Monthly club competition with three categories: **Annotated Game of the Month**, **Post of the Month**, **Video of the Month**.

- Submission form: https://docs.google.com/forms/d/e/1FAIpQLSf2Vi81dBVfaHGt_7Bs55jrS73FDPySXEsdtf2is0KnjYuatg/viewform
- Forum thread: https://www.chess.com/clubs/forum/view/game-analysis-36389

**What tends to win the Annotated Game category** (from studying past winners):
- A clear one-sentence hook ("beat someone 400 points higher", "3 rook sacs", "annotated my worst game")
- Genuine honesty about mistakes, not just showcasing good play
- A personal narrative the whole club can relate to
- Engine-verified key moments add weight

## Local Learning System (build in progress)

Full plan: `learning-system-plan.md`.

- **M0 (foundation + clock analyzer) done 2026-10-21** -- see `clock-analysis-report.md` for the verdict (clock is not the bottleneck behind slow-dissolve losses; M4 proceeds as scoped).
- **M1 (engine layer + cliff/decay detectors) code done 2026-10-21, batch analysis running unattended in the background** -- Stockfish depth-18 analysis, resumable, checkpointed per-game. Scoped to the 60 most recent rapid games (real per-game pace came in slower and more variable than first estimated, and that's roughly the sample size that already produced the diagnosis -- see `learning-system-plan.md` M1). Report refreshes via `python scripts/chess/detect.py --write` at `engine-analysis-report.md` as coverage grows.
- **M2 (`/chess-review` slash command) done 2026-10-21** -- run it at the end of a session. Self-review guess first, then engine findings, then the gap between them, logged to `study-log.md`. All 1,506 pre-existing games bulk-marked reviewed on rollout, so it only ever surfaces genuinely new games.
- **M3 (drill generator + HTML board) done 2026-10-21** -- `drill-board.html` (self-contained, offline-capable, theme-aware), drawing from his own blunders, his own quiet "null" positions, and a rating-matched Lichess puzzle pool, shuffled together so he can never assume a drill has a win. Browser-tested with Playwright (not just file-checked) -- caught and fixed a real bug where the board didn't update after a committed move. Regenerate anytime with `python scripts/chess/drills.py --write && python scripts/chess/build_board.py` as more games get analyzed. Not yet published as a shareable Artifact -- ask before doing that, since the plan calls for it but it's a distinct step from the local build.

Scripts at `scripts/chess/`, documented in `scripts/README.md`.

## Automated Workflow (consolidated 2026-10-21)

One scheduled cloud routine now feeds `tracker.md`:

1. **Chess tracker auto-update** (every 3 days, `trig_01BaX2JcLCMbWYVAHh792kSd`) -- checks the public chess.com API and always appends a Rating Log row (rapid/tactics/blitz ratings, plus games-played-per-format since the last row), even when ratings are flat. The games-played column exists specifically because a flat rating looked identical to zero play -- it hid a 6.5-week rapid blackout (Sept 4-Oct 19) that only a direct archive query caught. Also flags a new Improvers Club monthly submission cycle when one opens.

**Retired the same day:** the metadata-only game flagger (flagged almost everything at this rating level, discriminated almost nothing) and the bi-weekly cloud Stockfish analysis routine (`trig_01JFSQUYQf78TzhRxQmxuHoQ`, disabled not deleted) that fed on it. Both prompts are mirrored in full at `routine-prompts.md`, including the lesson worth carrying into the real replacement: long engine-best streaks are frequently hollow (king shuffles in lost endgames, book moves, trivial promotions) and must not be scored as skill.

The real replacement is `learning-system-plan.md` M1 (local cliff/decay detectors) and M2 (`/chess-review`), not yet built. Improvers Club candidate selection becomes a query against that local store once it exists. Manage the live routine at https://claude.ai/code/routines.
