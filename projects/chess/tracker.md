# Chess Tracker

Rating progress and Improvers Club submission log.

---

## Rating Log

| Date | Rapid | Tactics | Blitz | Notes |
|---|---|---|---|---|
| 2026-07-06 | 1223 (PB) | 1871 | 852 (best 1146) | Snapshot taken when the local Stockfish toolchain was set up |
| 2026-07-13 | 1154 | 1871 | 828 | Rapid -69, Blitz -24 since July 6 -- heavy volume week (80+ games in July), auto-update routine failed silently since July 10 (see decision log), this row backfilled manually |
| 2026-07-16 | 1148 | 1871 | 828 | Rapid -6, Tactics/Blitz unchanged |

---

## Improvers Club Submissions

| Month | Category | Entry | Result |
|---|---|---|---|
| July 2026 | Annotated Game of the Month | vs. gannu8709049607 (July 1) -- Re1# back-rank mate. Hook: 4 consecutive engine-best moves (23...Bxd4, 24...Rxc2, 25...Rxe2, 26...Bxb1) converting a won position after a queen/rook fork on move 16 | Submitted -- ready to import PGN to chess.com/analysis, post to forum |

---

## Flagged Game Opportunities (auto)

Candidates surfaced by the 3-day chess tracker routine, from game metadata only (upset win, checkmate finish, short decisive game). Status moves to "Analyzed" once the twice-monthly Stockfish pass processes it.

| Date | Opponent (rating) | Result | Why flagged | Link | Status |
|---|---|---|---|---|---|
| 2026-07-10 | blenimal (842) | Win (checkmate) | Decisive finish (checkmate) | [Game](https://www.chess.com/game/live/171397150856) | Analyzed |
| 2026-07-11 | Kushal_222222 (1194) | Loss (checkmate) | Decisive finish (checkmate) | [Game](https://www.chess.com/game/live/171422126774) | Analyzed |
| 2026-07-13 | OrganicOlid (846) | Loss (checkmate) | Decisive finish (checkmate) | [Game](https://www.chess.com/game/live/171511675562) | Analyzed |
| 2026-07-13 | Daz_W_89 (1182) | Loss (checkmate) | Decisive finish (checkmate) | [Game](https://www.chess.com/game/live/171527662322) | Analyzed |
| 2026-07-13 | mati3368 (1173) | Loss (checkmate) | Decisive finish (checkmate) | [Game](https://www.chess.com/game/live/171529583478) | Analyzed |
| 2026-07-13 | slizig (1150) | Loss (resignation) | Notably short decisive game (14 moves) | [Game](https://www.chess.com/game/live/171530420658) | Analyzed |
| 2026-07-15 | PubliusAugustus (1193) | Loss (checkmate) | Decisive finish (checkmate) | [Game](https://www.chess.com/game/live/171602305848) | Analyzed |

*(Backfilled manually 2026-07-13 after the automated 3-day routine failed to flag anything since July 10 -- see decision log. Window covers July 10 19:30 UTC through July 13 19:45 UTC, same heuristics the routine uses: upset win, checkmate finish, or <20-move decisive game. No upset wins or notably short games in this window, but 5 checkmate finishes qualified. Auto-update 2026-07-14: 1 new game flagged, rest of the 3-day window's games already covered by the backfill. Auto-update 2026-07-16: 1 new game flagged (checkmate loss); other games in the window were wins/draws/timeouts by lower/similar-rated opponents or non-checkmate losses of ordinary length, so no upset wins or short decisive games qualified.)*

---

## Bi-Weekly Stockfish Analysis (auto)

Twice a month, all pending flagged games get run through Stockfish (depth 18) in the cloud routine's own sandbox. Each row is one batch's best candidate.

| Date Run | Games Analyzed | Batch Pick | Engine Reasoning |
|---|---|---|---|
| 2026-07-16 | 7 | vs. PubliusAugustus (1193), 2026-07-15, [Game](https://www.chess.com/game/live/171602305848) | Depth-18 analysis (Threads=3) found the longest engine-best-move streak of the batch: 8 consecutive best moves from 38.Kh3 through 45.Kxe6, well clear of the next-best streak (6, mati3368 game). Real story arc, not just a clean win: Omri (White) blundered -2594cp at move 32 (32.Kxg1, a king capture that gave back the advantage), then fought back with that 8-move defensive/technical streak, but still lost by checkmate. Other games in the batch (Kushal_222222, OrganicOlid, Daz_W_89, mati3368) had inflated cp-loss totals from mate-score artifacts in long endgames, making their raw numbers unreliable for comparison -- streak count was the trustworthy signal across all 7. |

---

## Monthly Submission Candidate (auto)

Once both batches for a month are done, the routine compares the two batch picks and recommends one. Omri still writes the actual hook/annotation and submits it himself -- this is a recommendation, not a finished submission.

| Month | Recommended Game | Reasoning | Status |
|---|---|---|---|

---

## Study Log

- June 2026: First online lesson with NM Dane Mattson (Improvers Club)
- Ongoing: Nimzowitsch's *My System* (Hebrew), GothamChess YouTube

---

## Open Goals

- Close the Tactics (1871) vs. Rapid (1223) gap -- the core improvement focus
- Keep submitting to Improvers Club monthly when a good game/hook comes up
