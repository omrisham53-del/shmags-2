# M0 Clock Analysis: Report and Verdict

**Run:** 2026-10-21
**Source:** `scripts/chess/clock.py`, parsing chess.com's `[%clk ]` PGN annotations across the full rapid 10+0 archive (1,506 games, 2020-2026), stored locally via `scripts/chess/store.py`.
**Why this ran first:** per `learning-system-plan.md` M0, it's cheap and can redirect or remove a whole planned workstream (M4) before that workstream gets built.

---

## The hypothesis being tested

From the 2026-10-19 diagnosis: two failure modes, one suspected root cause. Failure mode 2 ("slow failure to capitalize on a lead over many moves") was suspected to possibly be **a time-allocation problem, not an endgame-knowledge problem** -- i.e. burning most of the clock early and reaching won endgames with almost nothing left to think with.

## Results

**2026 games only** (670 games, the era the original six-batch diagnosis was built from -- full 2020-2026 history shows the same pattern, see below):

| Result | Clock remaining entering the endgame phase | n |
|---|---|---|
| Win | avg 381s (median 405s) | 326 |
| Loss | avg 327s (median 346s) | 303 |
| Draw | avg 224s (median 223s) | 40 |

Games reaching the endgame phase with under 60 seconds remaining: **31 of 669 (4.6%)**.

Full 2020-2026 history (1,506 games) shows the same shape: win avg 384s, loss avg 341s, draw avg 226s, 4% of games under 60s entering the endgame. Time spent by phase (my moves, averaged per game): opening ~67s, middlegame ~167s, endgame ~79s -- out of a 600s budget, meaning on average well over half the clock is never used at all.

Clock remaining at fixed move milestones (my moves): move 10 ~520s, move 20 ~382s, move 30 ~268s, move 40 ~211s remaining. Steady, unremarkable drawdown -- no sign of an early-game clock dump.

## Verdict

**The time-allocation hypothesis does not hold.** Clock is not the bottleneck: he enters the endgame phase with an average of 6-6.5 minutes remaining even in games he eventually loses, and only about 1 in 20 games sees him under a minute by that point. This holds both across the full 6-year archive and when restricted to 2026 alone, so it isn't an artifact of older, faster-paced habits diluting a real recent pattern.

**What this means for the build plan (M4):** per `learning-system-plan.md`, M4 (conversion drills) was gated on this verdict and would be reshaped or dropped if the answer came back "pacing problem." It didn't. **M4 proceeds as originally scoped** -- failure mode 2 looks like a genuine technique/decision-quality gap in converting advantages, not a clock-management gap. The fix is studying conversion technique (M4/M5), not pacing drills.

**Caveat:** this is clock-data-only. It doesn't yet confirm these are genuinely winning positions at endgame entry (that needs M1's real evaluations) -- a player can have plenty of clock left and still be objectively lost. But it does rule out the specific mechanism Omri named himself ("thinking about my opponent's possible move under the time pressure" leading to a clock crunch) as the dominant driver, at least at the phase-transition level measured here. Worth re-checking the finer-grained version (clock remaining at the exact moment a winning advantage starts eroding, not just at the opening/endgame phase boundary) once M1's cliff/decay detectors exist and can be joined against this clock data.

## What's built

- `scripts/chess/store.py` -- SQLite store (`scripts/chess/chess.db`, gitignored), schema for games/moves/evaluations/annotations/drills (the latter two tables created now for M2/M3, empty until then).
- `scripts/chess/fetch.py` -- pulls the full chess.com archive, filters to rapid 10+0, stores new games idempotently (safe to re-run).
- `scripts/chess/clock.py` -- parses `[%clk ]` annotations into per-move time spent, buckets by phase (opening/middlegame/endgame, with a short-game fallback to even thirds), and produces this report.

Re-run anytime with:
```
python scripts/chess/fetch.py      # pull any new games since last run
python scripts/chess/clock.py      # parse + re-report
```
