# Weekly Review -- 2026-07-31

*Automated cloud run. today.md reconciled automatically. Everything else is flags for Omri to action live.*

---

## RECONCILED

- Moved 5 "Recent Work" date blocks out of today.md to keep the dashboard lean.
- July 12: already in the archive from a prior run; removed from today.md (was a duplicate).
- July 13, 20, 21, 22: appended to `archives/today-log-2026.md` in chronological order.
- Kept in today.md: July 26, July 25, July 24 (the 3 most recent dates).
- "Today's Completed" was already empty; no clearing needed.

---

## DEADLINES

**Due tomorrow (Aug 1):**
- Final LCA Assignment (Industrial Ecology and LCA, 5040) -- functionally done (.docx built, visually verified), but still needs Omri's own edits in Word and Moodle submission. This is a real action item for today.

**Due within 7 days:**
- Nothing else falls in the Aug 1-7 window beyond the LCA above.

**Upcoming hard deadlines:**
- Aug 15: Final Sustainability Project -- not started, brief still TBD. This is the last assignment in the entire degree. With 15 days left and no brief yet, flag if you don't have the brief by Monday Aug 3.
- Aug 20: EcoTraders real last working day (per tracker.md -- Aug 22 is a Saturday). 3 deliverables still open: tax incentive model + market analysis, tax incentive chapter, loan fund chapter.
- Aug 21: Window Winners launch target (PL season kickoff). Build not yet started as of the last session. First recurring calendar block (Fri 10:00-12:00) was today.

**Past-due event to close out:**
- Economics seminar presentation: was July 30 (yesterday). Today.md and the university tracker still show it as upcoming. Mark it done and log the outcome when you have a moment. The university tracker's "Notes" field still reads "selected to present -- presenting Thursday July 30" -- worth a status update.

**Goal milestones check:**
- Goal 2 (Energy Program, target Aug 20/22): on track per the block schedule in `projects/energy-program/tracker.md`. No slippage yet, but 3 deliverables across 4 weeks with Rafi's data still outstanding is tight.
- Goal 3 (Graduate, target Aug 15): at risk if the Sustainability Project brief doesn't surface in the next few days. Brief still TBD.

---

## FOLLOW-UPS

Job search is explicitly paused (since 2026-07-10, for the Sept-Dec trip and career direction reconsideration). No applications in "Applied" or "In Review" status. Pause confirmed still in effect -- no nudging needed.

---

## CRUFT FLAGGED

*Report only. Do not act on these without confirming with Omri.*

**today.md content stale (not cruft, but flag):**
- "Pending -- Needs Daniel's Decision: Discount rate 6% vs 10%" -- resolved at 6% with Daniel on 2026-07-13 (confirmed in `projects/energy-program/tracker.md` Reference section and decisions log). This pending item is stale and safe to remove.
- "This Week's Focus" item 1 says "Brainstorm a new direction (football-economics angle dropped 7/17)" -- direction was locked as Window Winners on 7/24. This section is 7 days stale and should be rewritten for the current week's actual focus.

**projects/energy-program/ -- superseded generators:**
- `generate_tax_model.py` -- v1, superseded by v2 and v3. Last substantive change was before v2 was built. Candidate for archiving.
- `generate_tax_model_v2.py` -- superseded by v3. Built 2026-07-13 and then rebuilt as v3 the same session. Candidate for archiving.
- `tax_incentive_model.xlsx` -- output of v1 generator. The live model Omri works on is a different file. Candidate for archiving alongside v1.
- `tax_incentive_model_v2.xlsx` -- output of v2 generator. Candidate for archiving alongside v2.

**projects/energy-program/ -- completed extraction scripts:**
- `capex_pipeline.py`, `extract_capex.py`, `diag_walk.py` -- CapEx extraction pipeline, run in June to produce `capex_all_rounds.csv`. Extraction is complete; these are low-risk to archive, but keep if you expect to re-run the extraction against updated grant data.

**scripts/ -- dormant job search automation:**
- `scripts/job-tracker.py` -- moved from `.claude/skills/` on 2026-07-24. Dormant while job search is paused. No action needed until search resumes.
- `.claude/skills/job-tracker.md` -- the skill trigger file for the above. Also dormant. Worth noting that the skill file and the script are now split across two locations (`skills/` and `scripts/`); may want to consolidate or add a note in the skill file pointing to the script when the search resumes.

---

## PRIORITY CHECK

*Flags only. No rewrites made to current-priorities.md. These need a live re-derivation with Omri.*

**Temporary Priority 1 has expired:**
- University was elevated to Priority 1 temporarily for the July 30 presentation. That event was yesterday. The stated framing ("presentation -- script finalized... Thursday July 30 presentation") is now past. The remaining university items are Final LCA (due Aug 1, action: submit) and Final Sustainability Project (due Aug 15, status: not started). Priority ranking should be revisited -- this is the explicit "drops back down" case noted in current-priorities.md itself.

**Window Winners build not yet started:**
- Priority 2, launched July 24/25, recurring calendar blocks set. As of the last session the direction and scope are locked but no build work is logged in today.md. With Aug 21 launch target and ~40-55 hours of work estimated, the first build session was scheduled for today (Fri 10:00-12:00). No character mismatch yet, but worth noting as a watch item if the next session shows no build progress.

**Norway prep session still pending:**
- The family-member logistics info was gathered on July 20 and a follow-up prep session was flagged as "still pending" -- this is now 11 days old with no update in today.md.
