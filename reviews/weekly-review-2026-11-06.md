# Weekly Review - 2026-11-06

Automated run. Today is Friday 2026-11-06.

---

## RECONCILED

- Today's Completed was empty. No items moved.
- Recent Work has exactly 3 dates (Oct 19, Oct 7, Sep 4). At the 3-date limit; no archiving needed.
- No changes made to today.md.

---

## PRIORITIES

**Content error in today.md -- chess milestones section is stale:**
- today.md Current Priority says "M0, M1, M2, M3 and M6 all done. M4 (conversion drills) and M5 (book loop + position-pattern matcher) remain."
- decisions/log 2026-11-02 records both M4 and M5 as built that day, with the explicit note: "all seven milestones M0 through M6 are now done."
- Git log confirms: commits "Chess M4: conversion drills" and "Chess M5: concept log + position-pattern matcher. Learning system complete (M0-M6)" both landed 2026-11-02.
- The chess section in Current Priority needs a one-line correction: the system is fully built; the blocker is now only games (zero rapid since Sept 13).

**Character mismatch -- current-priorities.md Priority 4 no longer matches reality:**
- States: "Intent only so far -- no project defined yet. Omri has two specific project ideas to discuss and shape in an upcoming session."
- Reality as of 2026-11-02: HoTake is defined as a no-deadline portfolio project; chess learning system is fully built (M0-M6 complete). Both ARE the independent projects. The discussion happened and projects are scoped.
- Priority 4 warrants a rewrite, not just a status patch, in the next live session.

**Character mismatch -- current-priorities.md Priority 1 Open items are stale:**
- Open item: "Whether the Worldpackers host confirms the Sagres placement" -- decisions/log 2026-11-03 confirms no host replied and farm near Lagos is the plan. The placement is closed.
- Open item: "How Porto/Lisbon and the Rota Vicentina trail fit around the Oct 25/Nov 3 anchors" -- both anchors have changed. The trip is now anchored around Lagos farm volunteering with a flexible Dec 8 end.
- The 2026-11-03 update note at the top of Priority 1 captures the farm decision but the Open items block was not updated to match. It now contradicts the decision log.

**Still unresolved -- EcoTraders reference letter decision:**
- Reminder sent Oct 7. As of today (Nov 6) that is 30 days with no reply, up from the "26 days" note in today.md.
- today.md This Week's Focus (Nov 2 onward) flags "Ron's reference letter -- 26 days since the reminder. Chase again or let it go." That call has not been logged in decisions/log.
- No hard deadline, but a decision (chase or close out) is overdue.

---

## DEADLINES

No past-due open items and no hard deadlines within the next 7 days.

**Ongoing horizon items:**
- Trip end: approximately Dec 8, 2026 -- explicitly marked flexible in decisions/log 2026-11-03.
- Farm volunteering near Lagos: start date, length, and coverage (bed, meals) not yet captured per today.md This Week's Focus.

---

## FOLLOW-UPS

Job search is intentionally paused since 2026-07-10. No applications in Applied or In Review status. Skipping nudge; pause is still in effect.

---

## CRUFT FLAGGED

No new cruft identified this week. Items from prior reviews remain as documented:

- `.claude/skills/dnd-session-prep/` -- D&D confirmed dead 2026-07-24 but kept per explicit decision in case the campaign revives. Not actioning without confirmation.
- `.claude/skills/job-tracker.md` and `scripts/job-tracker.py` -- both dormant during trip pause; distinct artifacts (skill prompt vs. Python automation). Not cruft.
- `scripts/sync_jobs.py` -- Notion job sync, out of scope and dormant. Not new.

Chess scripts (`scripts/chess/`) are all actively used by the chess automation routine (last committed 2026-11-02). Not cruft.
