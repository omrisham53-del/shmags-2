# Weekly Review -- 2026-08-07

*Automated cloud run. today.md reconciled automatically. Everything else is flags for Omri to action live.*

---

## RECONCILED

- "Today's Completed" was already empty; no items to move.
- "Recent Work" had exactly 3 date blocks (July 26, July 25, July 24) -- at the 3-date limit, no archiving needed.
- No changes made to today.md this run.

---

## DEADLINES

**Due within 7 days:**
- Final Sustainability Project (Aug 15, 8 days away) -- status: Not Started. Brief still TBD as of the last update (Aug 3). This is the last assignment in the entire degree. With no brief in hand and 8 days to the deadline, this needs immediate attention.

**Upcoming hard deadlines:**
- Aug 20 (Thursday, 13 days) -- EcoTraders last real working day. 3 deliverables remain: tax incentive model + market analysis, tax incentive chapter, loan fund full chapter. Market analysis actively in progress; chapters not yet started.
- Aug 21 (Friday, 14 days) -- Window Winners launch target. Build not yet started per git log (last commit to `projects/through-the-gap/` was July 25, the calendar-schedule save). Estimated 40-55 hours of work remaining.
- Sep 8 (32 days) -- Norway trip departure.

**Goal milestone check:**
- Goal 3 (Graduate, Aug 15): at real risk. Sustainability Project not started, brief unknown, 8 days left.
- Goal 2 (Energy Program, Aug 20/22): tight but active. CBS chiller sizing started Aug 3. Tax chapter and loan fund chapter not yet drafted. 3 deliverables across 13 days with Rafi data still outstanding.

---

## FOLLOW-UPS

Job search is explicitly paused (since 2026-07-10, for the Sept-Dec trip and career direction reconsideration). No applications in "Applied" or "In Review" status. Pause still in effect -- no nudging needed.

One referral lead (Avishai's consulting firm, status: Lead since 2026-06-08) remains open with no recorded action. This is deliberately dormant during the pause; flag to revisit when search resumes.

---

## PRIORITY CHECK

*Flags only. No rewrites made. These need a live re-derivation with Omri.*

**Window Winners (Priority 2) -- likely stalled:**
- Four scheduled build sessions have passed since the recurring blocks were set (Jul 28 Tue, Jul 31 Fri, Aug 4 Tue, Aug 7 Fri). Zero git commits to `projects/through-the-gap/` in that window. The tracker still reads "Technical architecture / build plan (not yet started)."
- With 14 days to launch and an estimated 40-55 hours of work, this is now urgent. If build work is happening outside the repo (no commits), that is a documentation gap. If it hasn't started, the Aug 21 launch is at serious risk. Either way, this needs a live call: launch on Aug 21 with further scope cuts, slip the date, or acknowledge the launch won't happen.

**today.md "Current Priority" content is Aug 3 framing, not Aug 7:**
- The section still says "Today: market-sizing work kicks off (chillers, then HP/VSD light pass), building toward a 15:30 Daniel meeting on the market analysis." The hook updated the date header but not the narrative content. The Aug 3 Daniel meeting has happened; its outcomes are not reflected here. Worth a live update to capture what changed.

**today.md stale pending item:**
- "Pending -- Needs Daniel's Decision: Discount rate: 6% (social/national) vs 10% (private/industrial)" -- resolved at 6% per the energy-program tracker Reference section and decisions/log.md entry 2026-07-13. This item is stale and safe to remove live.

---

## CRUFT FLAGGED

*Report only. Do not act without confirming with Omri.*

**projects/energy-program/ -- superseded generators (carried from July 31 review, still unactioned):**
- `generate_tax_model.py` -- v1 generator, superseded by v2 then v3. Candidate for archiving.
- `generate_tax_model_v2.py` -- v2 generator, superseded by v3. Candidate for archiving.
- `tax_incentive_model.xlsx` -- v1 model output. The live model is a different file. Candidate for archiving.
- `tax_incentive_model_v2.xlsx` -- v2 model output. Candidate for archiving.

**projects/energy-program/ -- completed extraction scripts (carried from July 31 review):**
- `capex_pipeline.py`, `extract_capex.py`, `diag_walk.py` -- CapEx extraction ran in June, produced `capex_all_rounds.csv`. Extraction is complete. Low-risk to archive unless you expect to re-run against updated grant data.

**scripts/ -- dormant job search automation (carried from July 31 review):**
- `scripts/job-tracker.py` and `.claude/skills/job-tracker.md` are split across two locations and both dormant during the search pause. No action needed now; worth reconnecting them when search resumes.
