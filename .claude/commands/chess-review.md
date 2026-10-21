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

## 2. Ask for his self-review guess BEFORE showing anything

This is rule 1 of the four hard training rules (`learning-system-plan.md`): commit before explain. Before you reveal any engine finding, ask him something like: "What's your gut read on what went wrong (or right) in today's games?" Wait for his answer. Do not hint, do not reference the engine data you already have, do not ask a leading question that gives away the finding.

If he skips this or says he doesn't have a guess, note that explicitly in the log rather than inventing one for him.

## 3. Reveal the engine's findings, per game

`review_session.py`'s output (from step 1) has, per unreviewed game: `cliffs` (single-move collapses >= 200cp, with the ply, move, cp_loss, time_spent, phase) and `decays` (a lead eroding over >= 10 plies with no single cliff -- the slow-bleed pattern, with the window's moves and their time_spent).

For each finding, write the natural-language explanation yourself -- don't just print the numbers. Say what the position actually was, why the move loses (what it missed, what the opponent's resource was), and whether it correlates with a fast move (`time_spent` is right there in the data -- this is the direct test from M1 of "do blunders come from fast moves?"). If a game has neither cliffs nor decays, say so plainly -- a clean game is a real, useful finding too, not a non-event.

cp_loss values are capped at 2000 -- a move showing exactly 2000 crossed into a decisively lost/mate position; don't read it as a precise number, just "very bad."

## 4. Compare his guess to the engine's answer

State the gap plainly: did his guess land on the same moment the engine flagged, a different one, or nothing at all? This comparison is the actual metric this system tracks over time (`learning-system-plan.md` measurement table: "gap between his self-review guess and the engine" -- down is the goal). Don't soften it and don't oversell it either way.

## 5. Write the study log entry

Append one dated entry to `projects/chess/study-log.md`: his guess (verbatim or close to it), the engine's findings (condensed, not the raw JSON), the gap assessment from step 4, and anything worth remembering as a pattern (e.g. "second time this week a cliff came in under 10s on the clock").

## 6. Mark reviewed

```
python scripts/chess/review_session.py --mark-reviewed <comma-separated game ids>
```
Use the `game_id` values from step 1's output. Do this last, after the log entry is actually written -- if something goes wrong earlier, leave the games unmarked so the next run picks them up again.

## Style

Keep the actual review conversational, not a report dump -- this runs inside a chat, right after he finished playing. Follow `.claude/rules/communication-style.md` (no AI-kill-list phrasing, no rule-of-three padding, no restating the question). Be honest about a bad session; he explicitly doesn't want this softened into encouragement he didn't ask for.
