# Chess Study Log

Dated entries written by `/chess-review` (see `.claude/commands/chess-review.md`, `learning-system-plan.md` M2), run at the end of a session on whatever games were just played. Each entry: the self-review guess (written before engine output, per the four hard training rules in `learning-system-plan.md`), the engine's actual findings, and the gap between them -- the recorded gap is the board-reading metric this whole mechanism exists to track over time, per the M0-M6 build plan.

Resources/habits (book, lessons, etc.) stay in `tracker.md`'s Study Log section. This file is the per-session narrative record.

---

## 2026-11-02

First full session run of the system since it was built. 3 rapid games, 2 wins 1 loss, rating around 1203-1212. First rapid games played since Sept 13, ending a 7-week blackout.

### His self-review, before seeing any engine output

The five-question block was used for the first time (added earlier the same day). Answers were specific and move-numbered, not vague, which made them genuinely scorable.

- **Game 1 (win, black):** comfortable apart from "the fork I got into," which led to a counter-attack that worked. Would take back **Nf5** and play **Bxf3** instead, to open the white king and prevent the fork. Thought the final position was winning. No time burned. "Played it very well but didn't notice that fork."
- **Game 2 (win, white):** opening and middlegame comfortable, **endgame stressful, "felt like I couldn't convert a winning position."** Would take back **move 39**, which he felt gave the opponent's rook a good square and made the passed pawn dangerous. Winning once he took the bishop; tried to trade rooks to make conversion easier and "failed to trade all of them." Time consistent. Would watch for passed pawns more.
- **Game 3 (loss, black):** good opening, "key mistakes in the middlegame" lost it. Two candidates: **move 18** (missing a bishop capture of a rook) and **move 25** (left the f5 pawn hanging, giving up two pawns and control). **Move 16 fork won a pawn, "only a slight advantage"**; couldn't find the right plan, was thinking of rook to the g-file to break the pawns near the white king. Little time burned. Would play slower.

### What the engine found

| Game | Result | Cliffs | Worst |
|---|---|---|---|
| 1507 | win | 1 | move 15 `Bxg4`, 375cp, 6.1s (best: `Nxe3`) |
| 1508 | win | **0** | nothing, across 95 plies |
| 1509 | loss | 3 | move 31 `b6`, **775cp**, 4.5s (best: `Rb6`) |

No decay episodes in any game. Game 1509's other cliffs: move 25 `Qxb3` 361cp/11.4s (best `Qd7`), move 30 `Qg5` 369cp/6.8s (best `Qb5`).

Peak my-perspective eval: 1507 mate, 1508 mate, **1509 only +278** at move 17.

### Gap assessment

- **Q2, game 3: direct hit.** He named move 25 and the exact reason (abandoning f5). That is the engine's first cliff, same move, same mechanism: `Qxb3` grabbed the b-pawn and `Bxf5` followed. Precise self-diagnosis.
- **Q2, game 3: missed the one that lost the game.** Move 31 `b6` at 775cp is the largest error of the whole session and he never mentioned it, nor move 30 `Qg5`. His move-18 candidate was not a cliff at all, and on the moves as played White's 17.Re1 had already moved the rook off f1, so the capture he remembers missing was not actually available.
- **Q2, game 1: near miss in location, sound in cause.** He named Nf5 (move 12); the engine flagged `Bxg4` (move 15). But his reasoning identified the real setup, since 15.g4 forks the h5 bishop and the f5 knight at once. What he did not see is that the fork had an answer: `Nxe3` saved the material and `Bxg4` threw a piece for a pawn. He diagnosed the cause of the trouble and missed the escape from it.
- **Q2, game 2: named a move the engine thinks was fine.** Move 39 is clean. So is every other move in the game.
- **Q3, game 3: accurate.** "Only a slight advantage" against a measured peak of +278, just below the +300 bar. Good calibration.
- **Q3, game 2: wrong in the pessimistic direction, and this is the session's headline.** He felt he could not convert a winning position. The engine found **zero errors above 200cp in 95 plies**. He converted it cleanly and his own read of that was anxiety, not evidence.
- **Q4: he was right, and a tempting conclusion is wrong.** All four cliffs came in under 12s, which looks damning until his actual pace is checked: medians are 5.6s / 7.1s / 9.4s. Against that, the 6.1s cliff is exactly typical and the 11.4s one is slower than his norm. Only move 31 `b6` (4.5s against a 9.4s median) is genuinely quick. His "time was consistent" is a fair description of what happened.

### Patterns worth carrying

1. **The conversion anxiety is not matched by the conversion data.** The one long conversion this session was flawless, and he experienced it as a failure. Worth watching whether this repeats, because the whole learning system was built partly on "I fail to capitalize on leads," and today's single data point points the other way.
2. **In game 3 the plan was the error, not just the moves.** He stated his plan in Q3 (rook to the g-file, break the pawns near the white king) and `Qg5` at move 30 executes exactly that, while the queenside was collapsing. 361, 369 and 775cp all landed on the queenside story he was not watching. Drilling individual moves will not fix a wrong plan.
3. **Blunders are not coming from fast moves on this evidence.** Four cliffs, one of them fast. The M1 hypothesis gets weak and mixed support, not confirmation. Needs more sessions before any conclusion.
4. Clock remaining at the end: 449s, 141s, 122s of 600s. Game 1 used only a quarter of his clock, consistent with M0's verdict that he has time to spare.
