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

## Automated Candidate-Finding Workflow

Two scheduled cloud routines feed `tracker.md` so good games don't slip by between Omri's own reviews:

1. **Chess tracker auto-update** (every 3 days, `trig_01BaX2JcLCMbWYVAHh792kSd`) -- checks the public chess.com API for rating changes and flags recent games matching simple heuristics (upset win, checkmate finish, short decisive game) into "Flagged Game Opportunities (auto)". Metadata only, no engine.
2. **Chess bi-weekly Stockfish analysis** (1st and 16th of each month, `trig_01JFSQUYQf78TzhRxQmxuHoQ`) -- installs Stockfish + python-chess in its own cloud sandbox, runs real depth-18 analysis on every game flagged since the last pass, and picks that batch's strongest candidate. Once two batches exist in the same calendar month, it compares both picks and recommends one for that month's submission in "Monthly Submission Candidate (auto)".

Omri still writes the actual hook and annotation and submits it manually -- the routines only narrow down which game is worth that effort. Manage both at https://claude.ai/code/routines.
