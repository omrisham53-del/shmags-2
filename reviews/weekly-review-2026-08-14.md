# Weekly Review -- 2026-08-14

*Automated review. Safe fix applied automatically (today.md reconcile). All other items are flags for Omri to act on.*

---

## RECONCILED

- today.md had 5 "Recent Work" sections (August 8, August 5, July 26, July 25, July 24).
- Moved "Recent Work (July 24)" and "Recent Work (July 25)" to `archives/today-log-2026.md`. today.md now holds the 3 most recent dates only.
- "Today's Completed" was empty; nothing to move.

---

## PRIORITIES

**Character mismatch: "This Week's Focus" in today.md is stale in two places.**
- University entry still reads "Final Sustainability Project (due Aug 15) is the one assignment left in the degree; get the brief once details land." Degree is done. Final Sustainability Project was submitted 2026-08-12. This entire item should be dropped.
- Energy Program entry says "market-sizing work + Daniel meeting today." The Daniel meeting happened on Aug 5, not today. Real per-technology market sizing was paused at that meeting. The placeholder pivot (per 1,000 units) and the Ministry of Energy import-data request are the current state -- the phrasing no longer matches.

**Stale data in today.md dashboard.**
- "Pending -- Needs Daniel's Decision: Discount rate: 6% (social/national) vs 10% (private/industrial)" -- the discount rate was resolved at 6% in decisions/log.md (2026-07-13 and confirmed 2026-07-27). This section is no longer accurate.

**Possibly stalled: Window Winners build.**
- Launch target: Aug 21, 2026 -- 7 days away.
- tracker.md (last updated 2026-07-24) and today.md both still say "build not yet started."
- Three weeks of Tue/Fri work blocks have passed since the first session (July 28) with no progress logged in any tracked file. Either the build has started and nothing was captured, or it genuinely has not started. Either way the tracker is out of sync. This is the highest-urgency flag in this review.

**Possibly stalled: Loan fund full chapter.**
- Per `projects/energy-program/tracker.md` (last updated 2026-08-12): zero progress on the loan fund full chapter since Aug 6.
- EcoTraders last real working day: Aug 20 (Thu) -- 6 days from today.
- This is 1 of 3 remaining deliverables, and it has had no working blocks since Aug 6 confirmed.

---

## DEADLINES

**Past-due or imminently due:**

- Aug 20, 2026 (Thu) -- EcoTraders last real working day (Aug 22 is a Saturday, confirmed in tracker.md)
  - Tax incentive model: v4 built (2026-08-12), not yet opened in real Excel for a first-open #REF? check; sensitivity Data Tables being rebuilt by Omri directly; some flags still open. Actively being worked on the company account.
  - Tax incentive chapter: over page limit (6 pages used, 4-page ceiling), results section not yet written, several structural issues flagged in tracker.md. Company account is ahead of this repo's log.
  - Loan fund full chapter: not started. Zero progress since Aug 6.
  
- Aug 21, 2026 (Fri) -- Window Winners v1 launch (PL 2026/27 season kickoff)
  - Build not started per all tracked sources.
  - 7 days to launch.

- Sept 8, 2026 -- Europe trip departs.

**Goal milestones with slipped dates:**
- Goal 2 (Deliver Energy Program): original target was June 2026. Updated target is Aug 22 (before last day). On track to finish EcoTraders work by Aug 20 if the loan fund chapter gets unblocked -- but no working blocks are logged for it since Aug 6.

---

## FOLLOW-UPS

Job search is explicitly paused. Per `context/current-priorities.md` (Priority 4: Career Direction Exploration), active search resumes ~Dec 2026 after the trip. No applications in "Applied" or "In Review" status in the tracker. Pause still in effect -- no nudging needed.

---

## CRUFT FLAGGED

- `.claude/skills/job-tracker.md` -- skill for job-application tracking. The matching Python script (`scripts/job-tracker.py`) was moved out of `.claude/skills/` to `scripts/` in the 2026-07-24 cleanup because skills are `.md`-only. The `.md` skill file itself remains. Job search is paused indefinitely (active search not resuming until ~Dec 2026). Whether to keep the skill warm or archive until the search resumes is a judgment call.

- `today.md` "Pending -- Needs Daniel's Decision" section -- not a file artifact but a stale dashboard item. Discount rate (6%) was resolved months ago (decisions/log.md 2026-07-13). This section should be cleared or updated to reflect any genuinely open Daniel decisions.

- `today.md` "This Week's Focus" -- two stale entries (University + Daniel meeting). Suggest rewriting to reflect actual current state: EcoTraders crunch (loan fund chapter + model/chapter revisions), Window Winners (launch in 7 days).

Memory folder is not accessible from this cloud run; stale-memory flags from the local `MEMORY.md` file skipped this pass.
