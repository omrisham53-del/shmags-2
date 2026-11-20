# Weekly Review -- 2026-11-20

Automated run. All changes in this report are flags only; nothing was acted on except the today.md reconcile described below.

---

## RECONCILED

- Moved "Recent Work (September 4)" (11 items) from today.md to archives/today-log-2026.md. This was the fourth and oldest date block; the last 3 (November 13, October 19, October 7) are kept.
- "Today's Completed" was already clear ("Nothing yet today.") -- no items to move.

---

## PRIORITIES

**Stale section -- This Week's Focus (Nov 2 onward) in today.md**
- This section is 18 days old and partially resolved. Items 3 (farm confirmed, decision logged 2026-11-03) and 4 (Q4 goals set on 2026-11-13) are done. Items 1 (chess) and 2 (HoTake) are intentionally parked. The whole section can be replaced with a current-state summary on next live session.

**HoTake API key expired today (2026-11-20 UTC)**
- today.md records "the Anthropic API key `hotake` expires 2026-11-20 (UTC); rotate it in the Console before the first live-LLM test." Today is that date. The key is in "omri's Individual Org." Action: create a new key in the Anthropic Console, update the local env var in the HoTake project, delete the old key. HoTake is parked and runs only on the fallback path right now, so nothing is broken -- but this needs to be done before any live-LLM test at laptop time.

**Priorities look accurate**
- Portugal farm (P1), career direction clarity (P2), chess and HoTake parked, job search, D&D and Through the Gap dead/shelved, EcoTraders and university retired. All consistent with decisions since the last re-derivation on 2026-11-13. No character mismatches or missing priorities detected.

---

## DEADLINES

**Past-due / slipping goals**

- Q4 Goal 2 (chess): "36 rapid games analyzed" -- zero rapid games played since ~Nov 3, now six consecutive zero-rapid rows in the Rating Log. The blocker is explicit (no laptop time), and the goal is intentionally parked, so this is not a surprise. Flag for awareness: at the current 0-games rate, the 36-game target has no path to completion without laptop access. No action expected until laptop time.

- Q4 Goal 3 (HoTake demo + LinkedIn posts): parked same reason. No path until laptop time. The API key expiry above is the one concrete thing to handle.

**No hard dated deadlines found in any active tracker.** University is complete, job search is paused, energy program is closed.

---

## FOLLOW-UPS

Job search is paused per current-priorities.md ("Job search to restart on a light schedule at that point, no pressure while abroad"). No applications are in "Applied" or "In Review" status -- all prior applications closed as rejected or paused (confirmed 2026-07-10). No follow-ups to surface.

---

## CRUFT FLAGGED

**scripts/job-tracker.py**
- Lives in scripts/ (moved there 2026-07-24 from .claude/skills/). Last real commit pre-dates the Jul 24 move. The job-tracker skill in .claude/skills/job-tracker/SKILL.md calls this file or is a parallel mechanism -- unclear which is active. Confirm whether the .py file is the actual engine the skill calls, or dead weight.

**projects/travel/**
- The Norway trip is complete (ended ~Nov 2026 when Omri arrived at the Lagos farm). The travel tracker likely still describes Norway route detail as though it were live. Not confirmed from this run, but worth checking and marking historical on next live session if that is the case.

**today.md "This Week's Focus (Nov 2 onward)" section**
- Not cruft per se, but it lists four items three of which are resolved or parked. Worth clearing and replacing with a current-state one-liner on next live session.

**No other cruft found.** Scripts in scripts/chess/ all have recent commits (Nov 2026 chess routine runs). Skills in .claude/skills/ all have SKILL.md files and no obvious duplicates. .claude/commands/ has three well-defined commands (chess-review, save-context, weekly-review). .claude/agents/research.md is the only agent and is referenced in CLAUDE.md.
