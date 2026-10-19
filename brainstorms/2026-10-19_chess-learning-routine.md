# Chess Learning Routine & Tools: Brainstorm / Discovery Notes

Date: 2026-10-19 · Goal: design a chess learning routine + a set of Claude Code tools that get Omri from 1193 to 1600 rapid, without a paid chess.com membership, while also growing his Claude Code skills

## Locked before the session started

- **Ultimate goal: 1600 rapid (10-minute) on chess.com.** Recorded in `projects/chess/README.md`, `tracker.md`, `context/current-priorities.md`, and the chess-journey memory.
- Current: Rapid 1193, Tactics 1871, Blitz 804 (2026-10-19).
- Bought Levy Rozman's *How to Win at Chess: Intermediate*.
- Wants: more engine analysis of own games, more puzzles, better routine, no paid membership, and the build itself should sharpen his Claude Code skills.

## Facts pulled from the repo before asking anything

These are real and shape the whole design, so they go in up front rather than being asked about blind:

1. **Rapid rating has not moved since 2026-09-13** -- 1193 for five straight weeks across 8 consecutive auto-update rows. He is chasing a rapid goal while playing essentially no rapid.
2. **All recent games are blitz.** Flagged-game opponents since late September sit at 776-821, which is the blitz pool, not the rapid pool.
3. **Tactics has been frozen at 1871 since 2026-07-06** -- 3.5 months with no rated puzzle movement, despite "more puzzles" being a stated want.
4. **The existing automation only finds games, it never teaches.** The 3-day routine flags on metadata (checkmate finish, short decisive game, upset win) and the bi-weekly Stockfish routine picks one "most tellable" game per batch for an Improvers Club submission. Both are optimized for *storytelling*, not for *improvement* -- nothing in the current system tells him what he keeps getting wrong.
5. **Flag heuristics are noise-heavy.** ~100 flagged games, nearly all "decisive finish (checkmate)". At this level almost every game ends in mate, so the filter barely filters.
6. **Local toolchain already exists and works:** Stockfish at `C:\Users\User\OneDrive\Documents\stockfish\stockfish-windows-x86-64-avx2.exe`, python-chess 1.11.2, depth-18 pattern established.
7. **Travel constraint:** Omri is abroad until ~Dec 8 (London now, Ericeira surf camp Oct 25, Sagres volunteering Nov 3 pending).

## Summary / key decisions

### The diagnosis
- **Goal: 1600 rapid.** Currently 1193. Realistically a 6-12 month climb; **December success is measured by blunder rate and conversion rate, not rating.**
- **The rapid stall had a mundane cause:** no laptop time. He won't play rapid on a phone (can't concentrate), so five weeks without a laptop meant five weeks without rapid. Not avoidance -- access. Now solved (~2h/day from here on).
- **Two failure modes, one root cause.** (1) One-move blunders from winning positions. (2) Slow failure to capitalize on a lead over many moves. Underneath both, in his own words: **"thinking about my opponent's possible move under the time pressure."** A process gap, not a knowledge gap.
- **"Improve my endgames" is not a third item** -- it is the same problem as failure mode 2. Converting a lead at this level means steering into a won endgame and executing it. Treat as one workstream.
- **Tactics 1871 vs Rapid 1193 does not mean "do more puzzles."** Vision is not the bottleneck. The likely reason the rating doesn't transfer: puzzles always announce that a win exists, and real games never do.

### The pedagogical constraints (Omri's own objection, now load-bearing)
He raised the risk that liking hinted formats would degrade his unaided mid-game board-reading. Four rules answer it:
1. **Commit before explain.** Position shown cold, move committed, *then* explanation. Feedback after a commitment teaches; commentary before it is a crutch.
2. **Never state a win exists.** Don't reveal whether a position is winning, equal, or lost.
3. **Include null positions** where the right answer is a quiet move or "there's nothing here, don't lose." Highest-leverage single design choice in the build.
4. **Clock the drills.** Training harder than the game, not easier.
- Same principle applied to game review: **he writes his own guess at what went wrong before seeing any engine output.** The recorded gap between his guess and the engine's answer *is* his board-reading skill, measured over time.

### The routine (locked)
Per-session cycle, **4 sessions/week, ~12 rapid games/week**:
| Block | Time | What |
|---|---|---|
| Play | ~40 min | 2-3 rapid games on chess.com |
| Self-review | 5 min | His guess at what went wrong, **before** any engine output |
| Engine pass | automatic | Pipeline runs on the games just played |
| Drill | 15 min | Positions from *previous* sessions, cold and clocked |
| Book | 20 min | Rozman, one concept, logged in his own words |

### The build (locked)
1. **`scripts/chess/` Python package** -- pulls rapid games from the chess.com public API, runs local Stockfish, writes a structured annotated-game store. Two detectors: a **cliff detector** (single-move collapses) and a **decay detector** (sustained winning eval eroding with no single large swing -- this one is new and is the only thing that catches failure mode 2).
2. **`/chess-review` slash command** -- runs the pipeline, then *Claude* writes the natural-language explanations. Division of labour: Stockfish supplies the number, the model supplies the "why this move loses." Reads his self-review note and sets his guess beside the engine's answer.
3. **Two-phase drill runner** -- Python generates a baked drill set offline (positions + answers + engine lines + written explanations as JSON); a **self-contained HTML board** serves them cold and clocked, revealing explanations only after a committed move. No live engine needed, so it works offline and publishes as a shareable Artifact. **Portfolio value is an explicit requirement** ("something I can show off"), so it gets a real design pass.
4. **Conversion-drill runner (terminal)** -- replays his own blown winning positions against live local Stockfish, repeatedly. The only honest way to train failure mode 2 and endgame technique together. Needs a live engine, hence terminal, hence lower frequency.
5. **Position-pattern matcher** -- back-searches the whole archive for positions matching a studied concept's structural conditions. Feeds the book loop.
6. **Clock-usage analyzer** -- derives per-move time from the `[%clk ]` annotations already in his chess.com PGNs, buckets it by game phase, and correlates time-spent against blunders. Works retroactively on the whole archive. **Run this first: it can test whether failure mode 2 is actually a time-allocation problem rather than an endgame-knowledge one, which would redirect a whole workstream.**

**Format locked: 10+0.** Pipeline filters rapid games on this.

### Platform and sourcing (locked)
- **chess.com is the scoreboard only.** The 1600 lives there; games come out free via the public API (already proven working). No membership needed.
- **All analysis is local Stockfish.** Makes the free-tier Game Review cap irrelevant; depth-18 local is stronger anyway.
- **Lichess as a platform is out** -- no account, dislikes it. But its **openly-licensed puzzle CSV is in**, as a data file, for volume and theme coverage.
- **Drill sessions shuffle database puzzles together with his own-game positions (including nulls)** so the format never signals whether a win exists. This mixing is what preserves rule 2 while still getting volume.

### Routine consolidation (locked)
- **Keep Routine A, fixed:** split its two jobs, and **add a games-played-per-format column** so inactivity is never again indistinguishable from a flat rating. (Eight rows since Sept 13 read "Rapid unchanged" and hid a five-week blackout; this column would have caught it in mid-September.)
- **Retire the metadata flagger** -- ~100 rows, almost all "checkmate finish", flags nearly everything so discriminates nearly nothing.
- **Retire Routine B** (bi-weekly cloud Stockfish) -- superseded by the local pipeline on depth, no sandbox reinstall, and a coaching rather than storytelling objective.
- **Carry over Routine B's hard-won judgment:** long engine-best streaks are frequently hollow (king shuffles in lost endgames, opening-book moves, trivial promotions) and must not be scored as skill.
- **Mirror both routine prompts into the repo before retiring anything** -- they currently exist only in the claude.ai UI and are unauditable and unrecoverable from here.
- **Improvers Club selection becomes a query** against the local store, not its own routine.

## Q&A log

### Q1 - When does the routine actually start: now (on the road) or on return (~Dec)?
- Asked: build tooling now, run a thin "travel mode" routine now, thicken it in December?
- Captured: **Start now, full stop.** Currently in Portugal (not London -- correction to the repo's assumed position), with no fixed departure date from there. Surf camp still Oct 25 and he can keep working through it, though focus shifts toward surfing and socializing that week. Worldpackers volunteering (Sagres, Nov 3) is **not confirmed** -- no replies from any host he applied to, so November is genuinely open, not committed.
- Laptop time: **~2 hours/day minimum, effectively unlimited** from now on. This is new -- it's the thing that was missing.
- Willing to play rapid on the road, **laptop only**. Phone is too small to concentrate on. This is the actual explanation for the five-week rapid stall: not reluctance, just no laptop.
- **Competing commitment this week:** a hackathon project, being worked in a parallel Claude Code session. So this week's chess capacity is real but shared.
- Flags: Omri's travel tracker still says London through ~Oct 24 -- `projects/travel/tracker.md` is stale and needs correcting (he's in Portugal already, Ireland already dropped). Not this session's job, but worth a pass.

### Q2 - What is actually losing you rapid games?
- Asked: proposed from his own engine data that the signature is single-move collapses from winning positions, and argued (against his stated want) that more puzzles is the wrong main lever since Tactics 1871 proves vision isn't the bottleneck.
- Captured: **Confirmed as a real pattern, with an important correction.** In his words: "I often lead and blow leads." But it is *two* failure modes, not one:
  1. **One-move blunders** -- the cliff-edge collapses the engine data already shows.
  2. **Failing to capitalize on a lead over many moves** -- a slow dissolve, no single identifiable blunder. This one the engine's "biggest swing" view would miss entirely.
- **Root mechanism, in his own diagnosis: "thinking about my opponent's possible move under the time pressure."** He names opponent-threat blindness under clock as the thing underneath both failure modes. This is the single most important sentence of the session -- it's a process gap, not a knowledge gap.
- **Endgames explicitly named as a second thing he really wants to improve.**
- Synthesis worth holding on to: failure mode 2 and the endgame want are probably *the same problem*. Converting a material lead at this level usually means steering into a won endgame and executing it; weak endgame technique is exactly how a lead dissolves over many moves without a visible blunder. Treat them as one workstream, not two.
- Design consequence: a diagnostic that only finds big eval cliffs catches failure mode 1 and is **blind to failure mode 2**. The tool needs a second detector for slow advantage decay (sustained winning eval that erodes without any single large swing).

### Q3 - Where do puzzles, drills, and analysis come from, given no paid membership?
- Asked: proposed a three-layer split -- chess.com as scoreboard only (games free via public API), all analysis local on his own Stockfish (makes the free-tier Game Review cap irrelevant), and a custom layer 3 of drills generated from his own games (blunder replay + conversion drills). Asked whether engine drills would bore him.
- Captured: **Drills confirmed wanted**, and he sharpened what he actually wants out of engine analysis: not the raw score, but **the explanation behind the score**. His words: "I want to analyze my games with the engine but want to understand the explanations for the engine analysis of the score... look at positions and get a short description that basically presents or hints at the thing I should focus on."
- **He raised the single best objection of the session himself:** he worries that liking the hinted/explained format will **damage the way he looks at the board mid-game, where there are no explanations or hints.** Hint-dependency as a trained crutch.
- **This concern is correct and is now a hard architectural constraint, not a worry to reassure away.** Resolved by four rules:
  1. **Commit before explain.** The drill shows the position with zero commentary. He must commit a move first. Explanation appears only after. Explanation after a committed move is feedback; explanation before it is a crutch. This one rule preserves the entire benefit and removes the risk.
  2. **Never state that a win exists.** Standard puzzle sites always imply "there is something here," which is itself a hint -- and is very likely part of why 1871 Tactics does not transfer to 1193 Rapid. Drills must not reveal whether the position is winning, equal, or lost.
  3. **Include null positions.** Some drills must have "quiet consolidating move" or "there is no tactic, just don't lose" as the correct answer. This is the closest thing to real-game conditions and is probably the highest-leverage single design choice in the whole build -- it directly attacks the tactics-to-rapid transfer gap.
  4. **Clock the drills.** Make the training environment harder than the game, not easier.
- Measurement consequence: success is **not** drill accuracy. Success is blunder-rate-per-rapid-game falling over weeks, and rapid rating rising. Track transfer, not drill score.

### Q4 - What is the weekly shape: how much playing vs. training, and what volume of rapid games?
- Asked: proposed a per-session cycle (play ~40min / self-review 5min / auto engine pass / drill 15min / book 20min) at 4 sessions and ~12 rapid games per week, plus an honest note that 1193 -> 1600 is realistically a 6-12 month climb and that blunder rate and conversion rate are the leading indicators that should move by December, not the rating.
- Captured: **Accepted in full, no changes** -- "yes this all sounds perfect." So the following are now locked:
  - **Session cycle:** play 2-3 rapid games -> write his own guess at what went wrong *before* any engine output -> automated engine pass -> 15 min cold clocked drills from *previous* sessions -> 20 min Rozman, one concept, into his own notes.
  - **Volume target: 4 sessions/week, ~12 rapid games/week.** This is the fuel supply for the whole system; the diagnostic needs roughly 3 weeks of this to find real patterns.
  - **Self-review-before-engine is a required step, not optional.** The recorded gap between his guess and the engine's answer *is* his board-reading skill, measured over time. Same commit-before-explain principle as the drills, applied to game review.
  - **Timeline expectation set explicitly: 1600 is a 2027 target, not a December one.** December success = blunder rate and conversion rate improving. Rating follows.
- Flags: **10+0 vs 10+5 not answered** -- need his actual rapid format before the pipeline filters games by time control.

### Q5 - What does this get built as, architecturally?
- Asked: proposed three components -- (1) `scripts/chess/` Python package with a cliff detector and a new decay detector, (2) a `/chess-review` slash command where Stockfish supplies numbers and Claude supplies the natural-language explanations, (3) a two-phase drill runner (offline Python generates a baked drill set, self-contained HTML board serves it cold and clocked). Conversion drills run in the terminal against live Stockfish. Asked whether to build the HTML board or just hand him FEN strings to drill inside Lichess.
- Captured: **Build the HTML drill board.** Three reasons given, all of which change requirements:
  1. It's "cooler" and more motivating -- engagement matters more than code economy here, since an abandoned tool is worth nothing.
  2. **"Something I can show off."** Portfolio value is now an explicit requirement, not a side effect. Consistent with the four goals he set for the dead Window Winners project (revenue / utility / skill-building / portfolio piece) -- this build hits three of those four.
  3. More customizable to his specific needs than a generic platform board.
- **Correction to Q3, layer 2: the Lichess option is dead.** He has no Lichess account and does not like the platform. So the "use Lichess for free unlimited themed puzzles" fallback is off the table entirely.
- **Consequence, and it raises the stakes on the build:** with Lichess out and no chess.com membership, our own generated drills become his *primary* puzzle source, not a supplement to someone else's. The drill generator has to carry real volume, not just serve a handful of replays. Worth revisiting whether it should also pull from a free public puzzle dataset (e.g. the openly licensed Lichess puzzle database, which is a downloadable CSV and needs no account) to pad volume alongside his own-game positions.
- Design consequence of "show off": the drill board should be publishable as an Artifact with a real shareable link, and should look designed, not like a debug tool.

### Q6 - What happens to the two existing chess cloud routines?
- Asked: proposed keeping the rating-log half of the 3-day routine (extended with blunder-rate and conversion-rate columns), retiring the metadata flagger as noise, and retiring the bi-weekly cloud Stockfish routine as superseded by the local pipeline -- with Improvers Club selection becoming a query rather than its own routine.
- Captured: **Omri declined to decide without first understanding what the routines actually do** -- "don't want to make a decision before I understand it fully." Correct instinct; these have been running unattended for 3 months and he has not had to think about them.

**Audit performed. Findings:**

**Routine A -- "Chess tracker auto-update", every 3 days, `trig_01BaX2JcLCMbWYVAHh792kSd`.** Does two unrelated jobs in one run:
  - *Rating log:* hits the public chess.com API, appends a row to the Rating Log table (rapid/tactics/blitz + a delta note). Reliable since the July 14 network-allowlist fix. 23 rows of history.
  - *Metadata flagging:* scans games from the last 3 days and flags any that match three heuristics -- upset win, checkmate finish, or decisive game under 20 moves -- into "Flagged Game Opportunities". No engine involved. Also opens each new month's Improvers Club cycle row.

**Routine B -- "Chess bi-weekly Stockfish analysis", 1st and 16th monthly, `trig_01JFSQUYQf78TzhRxQmxuHoQ`.** Installs Stockfish + python-chess into a fresh cloud sandbox each run, analyzes every game flagged since the last pass at depth 18, writes one row per batch naming that batch's best candidate with real engine reasoning. When two batches exist in one calendar month, it compares them and recommends one game for that month's Improvers Club submission. Both batches fired on schedule Oct 1 and Oct 16.

**Honest assessment of each:**
  - **Routine B's analysis quality is genuinely good** -- its batch write-ups repeatedly catch that long engine-best streaks are artifacts (king shuffles in lost endgames, opening book moves, trivial pawn marches) rather than skill, and pick the real story instead. That judgment is worth preserving somewhere, whatever happens to the routine.
  - **But Routine B optimizes for the wrong thing for the new goal.** Its objective function is "most tellable game for a club submission." Nothing in it asks "what does Omri keep getting wrong." It is a storytelling scout, not a coach.
  - **The metadata flagger is the weakest component** -- ~100 flagged rows, overwhelmingly "decisive finish (checkmate)", because at 1200 nearly every game ends in mate. Its own footnote log repeatedly reports "no upset wins" because opponents are always rated near him. It flags almost everything, so it discriminates almost nothing.
  - **A real gap the audit exposed, and it matters more than the consolidation question:** the Rating Log records *ratings only, never games played*. So it cannot tell "played 10 rapid games, net zero" apart from "played no rapid at all." Eight consecutive rows since Sept 13 read "Rapid unchanged" -- the routine faithfully logged a five-week rapid blackout and the blackout was invisible, because a flat rating looks identical to inactivity. **Had the log carried a games-played column, the laptop-access problem would have surfaced in mid-September instead of today.** Any kept routine must log activity volume, not just rating.
  - **Second gap: the routine prompts exist only in the claude.ai routines UI, not in this repo.** Grep found the trigger IDs in `decisions/log.md` and `projects/chess/README.md` but no prompt text anywhere. So the logic cannot be audited, diffed, or recovered from here -- if a routine is deleted its behaviour is gone. Recommend mirroring both prompts into the repo regardless of the keep/retire decision.

- **Resolved after the audit: recommendation accepted.** Decisions now locked:
  - **Keep Routine A, but fix it.** Split the two jobs apart, and add a **games-played-per-format column** to the Rating Log so inactivity is never again indistinguishable from a flat rating. This is the fix that would have caught the five-week rapid blackout.
  - **Retire the metadata flagger** (the three heuristics). Superseded by the pipeline's real-signal selection.
  - **Retire Routine B** (bi-weekly cloud Stockfish). Not for quality reasons -- the local pipeline simply does its job with more depth, no per-run sandbox reinstall, and a coaching objective rather than a storytelling one.
  - **Carry over Routine B's artifact-detection judgment** into the new pipeline's selection logic: long engine-best streaks are frequently hollow (king shuffles in lost endgames, opening-book moves, trivial pawn promotions) and must not be scored as skill. This is a real lesson learned across six batches and must not be lost with the routine.
  - **Mirror both routine prompts into the repo** before retiring anything, so the logic is auditable and recoverable.
  - **Improvers Club selection becomes a query** against the locally-analyzed game store, not its own scheduled routine.

### Q7 - How does the Rozman book connect to the rest of the system?
- Asked: proposed reading the book **in order** rather than diagnostically (Rozman built a deliberately sequenced intermediate curriculum; skipping around breaks dependencies), but back-searching every logged concept against his entire own-game archive -- "here are 7 of your games where both kings castled opposite; in 5 you never started a pawn storm." Asked whether he wants chapter-first-then-games or games-first-then-chapter.
- Captured: **Chapter first, then see his games.** Confirmed as recommended. The concept provides the lens he then re-reads his own play through, rather than confronting mistakes first and reading only to confirm what he already noticed.
- Locked: read sequentially, 20 min per session, one concept logged per session in his own words (active recall, not highlighting), then the pipeline back-searches the archive for positions where that concept was live and shows what he actually did.
- Build consequence: this needs a **position-pattern matcher** -- "find archive positions matching these structural conditions" (e.g. opposite-side castling, isolated queen's pawn, specific pawn structures, material imbalances). Genuinely interesting software and the most technically substantial piece after the two detectors.

### Q8 - Where does puzzle *volume* come from, now that Lichess-as-a-platform is out?
- Asked: proposed padding with the openly-licensed Lichess puzzle database (a downloadable CSV, several million puzzles, pre-tagged by theme and difficulty, no account and no platform visit), while flagging honestly that every puzzle in it is by construction "there is a win here" -- which violates rule 2 and would recreate the exact chess.com non-transfer problem if used alone. Argued the fix is **mixing**, not the source.
- Captured: **Confirmed, and he restated the mechanism himself:** mixing the two kinds "makes it so I don't have any clues while helping me learn from my mistakes in the past." He has independently grasped why the mix matters -- the implied hint only exists when *every* position is guaranteed solvable.
- Locked: public database supplies volume and theme coverage; his own games supply the core and all null positions; **both are shuffled together in every drill session** so the format itself never signals what kind of position he is looking at.

### Q9 - Completeness backstop: openings, time management, human coach?
- Asked: offered three deliberately-unasked branches -- opening prep (absent from the plan), clock-usage tracking (he named time pressure as the root cause but nothing in the build measured it), and whether a human coach should be in the loop.
- Captured:
  - **Time control confirmed: 10+0.** Closes the one hard flag. The pipeline filters rapid games on this.
  - **Time-management tracking is IN SCOPE** and should be blended into the sessions so he can see his own patterns. Promoted from an unasked aside to a real build component.
  - **No human coach in the loop.** The Dane Mattson lessons are occasional online sessions he joins for extra insight, not a structured coaching relationship -- so the system does not need to prepare lesson material.
  - **Routine-prompts-only-live-in-the-cloud problem: explicitly deferred to a separate session.** Out of scope here. Note that this collides with the locked decision to mirror both prompts into the repo *before* retiring Routine B -- so **Routine B must not be retired until that other session happens.** Sequencing dependency, not a contradiction.
  - **Openings: not addressed.** He answered the other three branches and left this one alone. Treating as out of scope for v1 rather than silently dropped -- see open flags.

### Time management: component spec (added from Q9)

Chess.com PGNs carry per-move clock annotations (`[%clk ...]`), so per-move time spent is derivable from data he already has -- no new source needed, and it works retroactively on the whole archive.

Metrics worth tracking:
- Time spent per move, bucketed by game phase (opening / middlegame / endgame).
- **Correlation between time spent on a move and whether that move was a blunder.** The direct test of his own stated root cause: do his collapses come from fast moves?
- Clock remaining at the moment of the critical error.
- Clock remaining on reaching a winning endgame.

**The hypothesis this can actually test, and it may reframe failure mode 2 entirely:** if he burns most of his clock in the opening and early middlegame and then arrives at won endgames with a minute left, then "failing to capitalize over many moves" is a **time-allocation problem, not an endgame-knowledge problem** -- and the fix is pacing, not studying technique. Fully testable against his existing archive before building any endgame training. **Run this check early; it could redirect a whole workstream.**

Integration point: the drill clock (rule 4) should be calibrated to his *real* measured per-move time, not an arbitrary number.

## Open flags (pending input)

- **Openings not addressed** -- Omri skipped the question. Caro-Kann as Black, London/d4 as White. Out of scope for v1 (most points at 1200-1600 are lost in the middlegame, so this is defensible), but it is an acknowledged gap, not a resolved question.
- **Routine prompt mirroring deferred to a separate session.** Blocks retiring Routine B until done.
- `projects/travel/tracker.md` says London through ~Oct 24; Omri is already in Portugal. Needs a reconcile pass (not in scope here).
- Worldpackers Sagres placement unconfirmed -- November location genuinely open.
- Whether the drill generator's volume from the public puzzle CSV should be theme-targeted by the diagnostic's findings, or simply rating-matched. Not decided; a build-time detail.
