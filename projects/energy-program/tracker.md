# Energy Program -- Schedule & Status

**Last updated:** 2026-07-27
**Scope locked 2026-07-26 (Daniel):** no new assignments before Omri's Aug 22 last day. Exactly 3 deliverables remain, in priority order:

1. **Tax incentive model, including the market analysis** (Priority 1)
2. **Tax incentive chapter** for the national program (Priority 2 -- results section depends on the model)
3. **Loan fund chapter** for the national program (Priority 3 -- appendix version reuses the existing position paper; the full chapter still needs writing)

Work happens in parallel across all 3, but the model comes first because the tax chapter's results section pulls numbers straight from it.

---

## Two things to confirm before trusting this schedule

1. **Aug 22 is a Saturday.** Your normal work days are Sun/Mon/Wed (full) + Thu (half) -- Saturday isn't one of them. That makes **Thursday Aug 20 your last real working day**, not Aug 22, unless the plan is to come in specially on a Saturday. This schedule assumes Aug 20 is the real cutoff. Flag if that's wrong.
2. **Thursday Jul 30 is presentation day** (economics seminar, distinction track). It's also a normal half-work-day on the EcoTraders schedule. Scheduled light on purpose -- move blocks if the day gets eaten entirely.

---

## Daily block schedule (Jul 27 -- Aug 20)

Full days (Sun/Mon/Wed, 9:00-18:00 with a 1hr lunch at 12): 5 blocks -- 2 morning (90 min each), 3 afternoon (90 min each), 30 min buffer at the end of the day.
Half days (Thu, 4.5hrs): 3 blocks of 90 min.

Check off blocks as you go. Order within a day is a suggestion, not a hard rule -- move things around, just don't skip Priority 1 work to do Priority 3 work.

### Week 1 (Jul 27 -- Jul 30)

**Mon Jul 27 (today, FULL)** -- unblock the model's highest-leverage gap first
- [ ] 9:00-10:30 -- Open the model's ניתוח sheet. Check whether fiscal cost is computed, and if so whether it's timing-based (NPV of deferred tax) or wrongly counting the full deduction.
- [ ] 10:30-12:00 -- Fix or build the fiscal-cost calc as NPV of the deferred tax if it's missing or wrong. This gates the whole cost-effectiveness story in the chapter.
- [ ] 13:00-14:30 -- Apply Daniel's tweak: electricity tariff -> average across תעו"ז time bands (peak/off-peak/shoulder), high-voltage.
- [ ] 14:30-16:00 -- Apply Daniel's tweak: sanity-check kW/ton unit consistency across all 3 technologies (ton/kW vs kW/ton mix-ups).
- [ ] 16:00-17:30 -- Add the "would the firm invest with the incentive" row (A-C, conditional formatting) per result section -- this is the adoption switch the whole market analysis hangs off.

**Wed Jul 29 (FULL)** -- quick win + tax chapter kickoff
- [ ] 9:00-10:30 -- Loan fund appendix: pull the existing position paper, adapt/format into the appendix version. Should be fast -- get it off the list.
- [ ] 10:30-12:00 -- Tax chapter: outline the full chapter, mirroring the grant chapter's structure. Note which sections already exist (international review) vs. need writing.
- [ ] 13:00-14:30 -- Tax chapter: write the background / policy-basis section (accelerated depreciation, מפעל מאושר mechanism in Israel).
- [ ] 14:30-16:00 -- Tax chapter: write the מפעל מאושר (approved factory) method explanation section.
- [ ] 16:00-17:30 -- Tax chapter: slot in the already-written international review doc, light edit pass so the tone matches the rest.

**Thu Jul 30 (HALF -- presentation day, keep it light)**
- [ ] Block 1 -- Chiller market sizing: pull CBS non-residential construction-starts data, last 5 years.
- [ ] Block 2 -- Chiller market sizing: source a real RT/m2 figure (ASHRAE rule-of-thumb or Israeli standard SI 5282) -- pull an actual citation, don't pick a number.
- [ ] Block 3 -- open/flex, in case the presentation runs long.

### Week 2 (Aug 2 -- Aug 6)

**Sun Aug 2 (FULL)** -- chiller + heat pump engines
- [ ] 9:00-10:30 -- Chiller engine: build the sizing calc (construction trend x RT/m2 -> installed cooling capacity by year).
- [ ] 10:30-12:00 -- Chiller engine: replacement-demand sensitivity (existing stock RT / lifetime, using the model's own 15-17yr lifetime).
- [ ] 13:00-14:30 -- Heat pump market sizing: pull national energy balance data (CBS / Ministry of Energy) for industrial mazut/diesel heat use.
- [ ] 14:30-16:00 -- Heat pump market sizing: source/estimate the low-temp addressable share (~80-90°C ceiling) -- flag for Rafi if it can't be sourced cleanly.
- [ ] 16:00-17:30 -- Heat pump engine: build the sizing calc (addressable pool x adoption switch).

**Mon Aug 3 (FULL)** -- VSD engine + rollup
- [ ] 9:00-10:30 -- VSD market sizing: pull national industrial electricity data (CBS / Electricity Authority / Noga).
- [ ] 10:30-12:00 -- VSD market sizing: apply the ~10% compressed-air-share benchmark, narrow to variable-load compressors only.
- [ ] 13:00-14:30 -- VSD engine: build the sizing calc.
- [ ] 14:30-16:00 -- Link each technology's sizing output to its per-unit model results (NPV, MWh saved, tCO2 saved, fiscal cost).
- [ ] 16:00-17:30 -- Build the market-level rollup: ₪/MWh and ₪/tCO2 summary, same ruler as the grant chapter.

**Wed Aug 5 (FULL)** -- tax chapter methodology + model hardening
- [ ] 9:00-10:30 -- Tax chapter: write the methodology section intro (mirrors the sizing engines + adoption logic + fiscal-cost approach).
- [ ] 10:30-12:00 -- Tax chapter: methodology section -- chillers + heat pumps write-up.
- [ ] 13:00-14:30 -- Tax chapter: methodology section -- VSD + the fiscal-cost timing explanation (why it's cheaper per tCO2 than the grant, if that's how it lands).
- [ ] 14:30-16:00 -- Model: sensitivity pass -- chiller/heat pump operating hours, discount rate (6% social vs 10% private).
- [ ] 16:00-17:30 -- Chase/check Rafi's data (CapEx of the mazut/diesel furnace, incremental maintenance delta, degradation rate, confirmed hours). Incorporate anything that's landed.

**Thu Aug 6 (HALF)**
- [ ] Block 1 -- Work-computer task: fix `generate_tax_model.py`'s hardcoded heat pump baseline name (still says "דוד חשמל קונבנציונלי", should be the mazut/diesel oven baseline).
- [ ] Block 2 -- Model: full QA pass on formulas/units across all 3 technologies.
- [ ] Block 3 -- Loan fund full chapter: gap-check -- what does the existing position paper NOT cover that the full national-program chapter needs?

### Week 3 (Aug 9 -- Aug 13)

**Sun Aug 9 (FULL)** -- loan fund chapter drafting starts
- [ ] 9:00-10:30 -- Loan fund chapter: write background/context section (mirrors grant + tax chapter structure).
- [ ] 10:30-12:00 -- Loan fund chapter: write the mechanism/how-it-works section.
- [ ] 13:00-14:30 -- Loan fund chapter: methodology section.
- [ ] 14:30-16:00 -- Tax chapter: draft the results section off whatever model numbers are locked so far -- flag placeholders for anything still pending Rafi.
- [ ] 16:00-17:30 -- Model: incorporate any new Rafi data that's landed, re-run affected numbers.

**Mon Aug 10 (FULL)**
- [ ] 9:00-10:30 -- Loan fund chapter: continue drafting (numbers/impact section).
- [ ] 10:30-12:00 -- Loan fund chapter: continue drafting.
- [ ] 13:00-14:30 -- Tax chapter: finish the results section, ₪/MWh & ₪/tCO2 comparison against the grant chapter.
- [ ] 14:30-16:00 -- Model: end-to-end test -- walk one technology fully through sizing -> adoption -> fiscal cost, check nothing breaks.
- [ ] 16:00-17:30 -- Buffer: whichever of the 3 deliverables is furthest behind.

**Wed Aug 12 (FULL)** -- first full drafts done
- [ ] 9:00-10:30 -- Loan fund chapter: finish first full draft.
- [ ] 10:30-12:00 -- Tax chapter: finish first full draft.
- [ ] 13:00-14:30 -- Model: polish pass -- formatting, labels, comments for Daniel's review.
- [ ] 14:30-16:00 -- Cross-check: chapter numbers match model outputs exactly, no drift.
- [ ] 16:00-17:30 -- Buffer.

**Thu Aug 13 (HALF)**
- [ ] Block 1 -- Loan fund chapter: review/edit pass.
- [ ] Block 2 -- Tax chapter: review/edit pass.
- [ ] Block 3 -- Send model + both chapter drafts to Daniel for review.

### Week 4 (Aug 16 -- Aug 20) -- revisions + wrap-up buffer

**Sun Aug 16 (FULL)**
- [ ] 9:00-10:30 -- Model: revisions from Daniel's feedback.
- [ ] 10:30-12:00 -- Model: revisions cont'd.
- [ ] 13:00-14:30 -- Tax chapter: revisions from Daniel's feedback.
- [ ] 14:30-16:00 -- Loan fund chapter: revisions from Daniel's feedback.
- [ ] 16:00-17:30 -- Buffer.

**Mon Aug 17 (FULL)**
- [ ] 9:00-10:30 -- Finalize model.
- [ ] 10:30-12:00 -- Finalize tax chapter.
- [ ] 13:00-14:30 -- Finalize loan fund chapter.
- [ ] 14:30-16:00 -- Final QA across all 3.
- [ ] 16:00-17:30 -- Buffer.

**Wed Aug 19 (FULL)**
- [ ] 9:00-10:30 -- Final polish pass, all 3 deliverables.
- [ ] 10:30-12:00 -- Prepare final versions for the Ministry/client.
- [ ] 13:00-14:30 -- Any leftover handoff notes (no formal handoff plan exists yet -- worth writing a short one even informally).
- [ ] 14:30-16:00 -- Buffer.
- [ ] 16:00-17:30 -- Buffer.

**Thu Aug 20 (HALF -- last real working day)**
- [ ] Block 1 -- Final sign-off tasks.
- [ ] Block 2 -- Wrap-up/handoff documentation.
- [ ] Block 3 -- Buffer / anything still open.

---

## Reference -- open items carried forward

**Rafi is still owed (email sent 2026-07-22):**
- CapEx of the mazut/diesel furnace (heat pump baseline)
- Incremental annual maintenance cost, efficient vs. baseline, all 3 techs
- Equipment degradation rate (0.5% placeholder)
- Confirmed annual operating hours (5,475 heat pump / 3,000 chiller / 6,400 VSD)

**Daniel's decision pending:** discount rate -- 6% (social/national) vs. 10% (private/industrial).

**Full open-flags list (sourcing gaps, unresolved assumptions):** see `baseline-technology-data.md`.

**Market analysis methodology (full reasoning behind the sizing engines above):** see `brainstorms/2026-07-22_tax-incentive-market-analysis.md`.

**Parked for a later Daniel discussion:** additionality/deadweight -- whether already-profitable segments should count as incentive impact or get netted out. Not blocking this schedule.
