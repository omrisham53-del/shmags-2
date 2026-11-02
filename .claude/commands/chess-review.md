Run Omri's end-of-session chess review. This is M2 of the learning system (`projects/chess/learning-system-plan.md`) -- the daily driver, meant to run once at the end of a session after he's played his rapid games. The division of labour: Stockfish supplies the number, you supply the reason the move loses. That translation is the thing he actually asked for.

## 1. Pull and prep new games

Run, in order:
```
python scripts/chess/fetch.py
```
Then check for anything to review:
```
python scripts/chess/review_session.py
```
If it returns `{"status": "no_new_games", ...}`, tell him there's nothing new since the last review and stop here -- don't fabricate a session that didn't happen.

## 2. Ask his five self-review questions BEFORE showing anything

This is rule 1 of the four hard training rules (`learning-system-plan.md`): commit before explain. At this point you are holding `review_session.py`'s output, which already names his blunders. Say none of it. Do not hint, do not reference the data, do not ask a leading question that gives the finding away.

**Ask exactly these five, as one block, and let him answer in a line each.** They are fixed rather than improvised so the gap between his read and the engine's is comparable across sessions, which is the whole metric. "What's your gut read?" on its own is too open-ended to answer cold right after playing, which is why this list exists (added 2026-11-02 at his request).

```
1. Result of each game, and how it felt: comfortable, messy, or never in it?
2. Is there one move you would take back? Which, and what do you think you missed?
3. Did you reach a position you thought was winning? If so, what happened to it?
4. Where did you burn the most time, and where did you move fastest?
5. One thing you would do differently next game.
```

Rules for asking them:

- **Question 3 asks what HE thought, never what was true.** Do not confirm, deny or soften it, even if the engine disagrees flatly. His perception versus the engine's answer is the measurement.
- Short answers are correct. Bullets, not prose. If he does not know, "no idea" is a real answer worth logging.
- If he skips the block entirely, note that explicitly in the log rather than inventing answers for him.
- Never reorder or add questions mid-session to fish for something you already know from the engine output.

If he skips this or says he doesn't have a guess, note that explicitly in the log rather than inventing one for him.

## 3. Reveal the engine's findings, per game

`review_session.py`'s output (from step 1) has, per unreviewed game: `cliffs` (single-move collapses >= 200cp, with the ply, move, cp_loss, time_spent, phase) and `decays` (a lead eroding over >= 10 plies with no single cliff -- the slow-bleed pattern, with the window's moves and their time_spent).

For each finding, write the natural-language explanation yourself -- don't just print the numbers. Say what the position actually was, why the move loses (what it missed, what the opponent's resource was), and whether it correlates with a fast move (`time_spent` is right there in the data -- this is the direct test from M1 of "do blunders come from fast moves?"). If a game has neither cliffs nor decays, say so plainly -- a clean game is a real, useful finding too, not a non-event.

cp_loss values are capped at 2000 -- a move showing exactly 2000 crossed into a decisively lost/mate position; don't read it as a precise number, just "very bad."

## 4. Compare his guess to the engine's answer

State the gap plainly: did his guess land on the same moment the engine flagged, a different one, or nothing at all? This comparison is the actual metric this system tracks over time (`learning-system-plan.md` measurement table: "gap between his self-review guess and the engine" -- down is the goal). Don't soften it and don't oversell it either way.

Three of the five questions map onto something the engine measured, so score those specifically rather than giving one vague overall verdict:

| Question | Compare against | A hit looks like |
|---|---|---|
| Q2, the move he would take back | the largest cliff in the game | same move, or within a move or two of it |
| Q3, whether he thought he was winning | peak my-perspective eval | he believed he was winning and the engine agrees it was +300 or better, or he correctly sensed he never was |
| Q4, where he moved fastest | `time_spent` on the flagged cliffs | the cliff actually did come on one of his fast moves |

Q1 and Q5 are not scored. They are there to anchor him and to catch his own read of what to change, which is worth logging even though no engine number corresponds to it.

Call out the interesting failure explicitly when it happens: naming a move he would take back that the engine thinks was *fine*, while missing the one that actually cost 300cp, is a more useful finding than a clean miss, because it says the board-reading is active but mis-aimed.

## 5. Write the study log entry

Append one dated entry to `projects/chess/study-log.md`: his guess (verbatim or close to it), the engine's findings (condensed, not the raw JSON), the gap assessment from step 4, and anything worth remembering as a pattern (e.g. "second time this week a cliff came in under 10s on the clock").

## 6. Mark reviewed

```
python scripts/chess/review_session.py --mark-reviewed <comma-separated game ids>
```
Use the `game_id` values from step 1's output. Do this last, after the log entry is actually written -- if something goes wrong earlier, leave the games unmarked so the next run picks them up again.

## Style

Keep the actual review conversational, not a report dump -- this runs inside a chat, right after he finished playing. Follow `.claude/rules/communication-style.md` (no AI-kill-list phrasing, no rule-of-three padding, no restating the question). Be honest about a bad session; he explicitly doesn't want this softened into encouragement he didn't ask for.
