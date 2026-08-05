# Energy Program -- Schedule & Status

**Last updated:** 2026-08-05
**Scope locked 2026-07-26 (Daniel):** no new assignments before Omri's Aug 22 last day. Exactly 3 deliverables remain, in priority order:

1. **Tax incentive model, including the market analysis** (Priority 1)
2. **Tax incentive chapter** for the national program (Priority 2 -- results section depends on the model)
3. **Loan fund chapter** for the national program (Priority 3 -- appendix version done 2026-08-03, adapted from the existing position paper; the full chapter still needs writing)

Work happens in parallel across all 3, but the model comes first because the tax chapter's results section pulls numbers straight from it.

---

## Confirmed

1. **Thursday Aug 20 is the real last working day** (confirmed 2026-07-27) -- Aug 22 itself is a Saturday, not a work day.
2. **Thursday Jul 30 is presentation day** (economics seminar, distinction track) as well as a normal half-work-day. Scheduled light on purpose -- move blocks if the day gets eaten entirely.
3. **Additionality split resolved (2026-07-26, recovered from a branch that wasn't merged until 2026-07-27):** the adoption rule is now a 3-year payback-period threshold (Rafi's own number), not a 20-year NPV sign. At that threshold, only chillers (100RT/500RT) show real additionality -- heat pumps and VSD clear the bar with or without the incentive (deadweight). This changes the schedule below: chillers get the full rigorous market-sizing treatment, heat pumps/VSD get a lighter order-of-magnitude pass (they only need to support the fiscal-cost/deadweight number, not an impact claim). Full reasoning: `brainstorms/2026-07-26_payback-threshold-and-meeting-prep.md`.
4. **Fiscal cost reporting is dual, not single:** total fiscal cost = the incentive's tax-shield benefit (C-B) summed across every adopting unit in all 3 technologies (the tax break doesn't discriminate on additionality). Cost-effectiveness (₪/tCO2, ₪/MWh) can only be honestly computed for chillers, where there's real additional abatement to divide by -- dividing HP/VSD's cost by non-additional savings would credit the policy for reductions it didn't cause.
5. **PRTR (Ministry of Environmental Protection facility-level data) identified as a better source** than the borrowed international benchmarks (DOE/Radgen 10% compressed-air share, unsourced low-temp heat share) for narrowing the heat-pump/VSD addressable pool. Not yet pulled -- worth checking whether EcoTraders has existing portal/contact access.
6. **Schedule slipped ~1 week (confirmed 2026-08-03):** the Wed Jul 29 Daniel meeting never happened -- it's today, Mon Aug 3 at 15:30, and it's specifically about the market analysis. Thu Jul 30's chiller-sizing blocks (presentation day) didn't happen either, and the Week 2 Sun Aug 2 blocks (chiller sizing, HP/VSD light pass, PRTR check, fiscal-cost rollup) are also not done -- none of the market-sizing work has started yet. Loan fund appendix got pulled forward instead and is done. Today's block plan below is rebuilt around this reality; the rest of the multi-week schedule further down is stale by about a week and will get re-sequenced as work actually lands rather than rewritten speculatively now.
7. **Daniel meeting happened 2026-08-05 (moved from Aug 3) -- major market-analysis pivot.** Full outcomes in decisions/log.md. Summary: (a) the 3-year payback threshold confirmed as "probably the strongest conclusion we can provide" -- the core reframe stands; (b) real per-technology market sizing (chiller RT/m², heat pump fuel-balance, VSD compressed-air-share) is paused -- none of them reliably answer "how many projects happen per year," a flow, and all three were sizing a stock instead; (c) the chapter now shows savings **per 1,000 units, per technology** as a placeholder, chillers included, fiscal cost the same C-B calc x 1,000; (d) heat pump baseline changed from a mazut/diesel furnace to a **standard-efficiency heat pump** (same structure as chillers: baseline vs. efficient tier of the same technology) -- this makes most of Rafi's still-owed furnace data (CapEx, maintenance delta) obsolete, see the updated Reference section below; (e) the Cyprus-style chillers-only differentiated-multiplier recommendation was rejected by Daniel as too narrow to propose; (f) plan going forward is an email to Yaniv Giat (Ministry of Energy) asking for import data on all three technologies -- if that lands, it's a real annual flow figure and market sizing gets revisited with Daniel.

---

## Daily block schedule (Jul 27 -- Aug 20)

Full days (Sun/Mon/Wed, 9:00-18:00 with a 1hr lunch at 12): 5 blocks -- 2 morning (90 min each), 3 afternoon (90 min each), 30 min buffer at the end of the day.
Half days (Thu, 4.5hrs): 3 blocks of 90 min.

Check off blocks as you go. Order within a day is a suggestion, not a hard rule -- move things around, just don't skip Priority 1 work to do Priority 3 work.

### Week 1 (Jul 27 -- Jul 30)

**Mon Jul 27 (today, FULL)** -- close out the model's last two structural gaps
- [x] Electricity tariff -> תעו"ז average (39.54 agorot/kWh) -- done 2026-07-26, recovered from the merged branch. **Superseded 2026-08-05:** the TAOZ extension prompt built the underlying weighted calculation live in the model, sourced from IEC's own tariff page (https://www.iec.co.il/content/tariffs/contentpages/taozb-gavoaa), and it landed at **44.60 agorot/kWh**. The model now uses 44.60, with the calculation shown transparently per Daniel's ask.
- [x] Payback-threshold adoption row + decision test per block -- already live in the model (this replaced the originally-planned A-C row as the adoption signal).
- [x] Added the C-A row (NPV of the incentivized investment vs. doing nothing) and the fiscal-cost row (direct reference to C-B, per the dual-reporting decision) to all 6 blocks, plus two summary-table columns and a totals row (L305 = ₪71,491 total fiscal cost across all technologies). Verified: C-A = (B-A)+(C-B) in all 6 rows, fiscal cost matches C-B exactly, conditional formatting live (green confirmed on all 6 -- everything's currently positive, so the red branch is unverified but the rule is present).
- [x] kW/ton (and kW/100cfm for VSD) unit consistency check across all 6 blocks -- recomputed every efficiency/consumption/CapEx-per-unit figure by hand against the model's cached values, all consistent, no ton/kW mix-ups. Chillers scale via capacity x kW/ton x hours; VSD's specific-power comparison is correctly applied as a % savings on top of capacity x hours, not multiplied directly (would have been dimensionally wrong if it had been).
- [x] Confirmed the sensitivity-analysis build (hours per technology, all 6 blocks) -- all 6 Data Tables exist and their "current hours" row matches the live model's actual result in 5 of 6 blocks. Two things caught and resolved along the way: (1) an accidental click into a Data Table cell briefly corrupted all 6 tables -- fixed by Ctrl+Z, but left one stale value behind (VSD 45kW's 5,000hr row showed payback-B as 0.63 when the table's own internal pattern and the live reference value both say 0.62 -- needs Ctrl+Alt+F9 forced recalc to clear); (2) HP70's 1,000hr row showed payback-B as exactly "3.00" with a verdict that only makes sense if it's over the 3yr threshold -- checked full precision, it's 3.00218, so the verdict is correct, not a bug. Depreciation-multiplier table not yet separately confirmed.
- [x] Loan fund appendix -- pull the existing position paper, adapt/format into the appendix version. (Slipped past today's original slot; completed 2026-08-03.)

**Wed Jul 29 (FULL)** -- ~~Daniel meeting day + tax chapter kickoff~~ -- did not happen as scheduled. Meeting moved to Mon Aug 3, 15:30. Tax chapter kickoff tasks below carry forward, not yet started:
- [ ] Tax chapter: outline the full chapter, mirroring the grant chapter's structure. Note which sections already exist (international review) vs. need writing.
- [ ] Tax chapter: write the background / policy-basis section (accelerated depreciation, מפעל מאושר mechanism in Israel).
- [ ] Tax chapter: write the מפעל מאושר (approved factory) method explanation section.
- [ ] Tax chapter: slot in the already-written international review doc, light edit pass so the tone matches the rest.

**Thu Jul 30 (HALF -- presentation day)** -- day went to the presentation as expected, market-sizing blocks below carry forward, not yet started:
- [ ] Chiller market sizing: pull CBS non-residential construction-starts data, last 5 years.
- [ ] Chiller market sizing: source a real RT/m2 figure (ASHRAE rule-of-thumb or Israeli standard SI 5282) -- pull an actual citation, don't pick a number.

**Sun Aug 2 (FULL)** -- did not happen (or wasn't market-sizing work) -- all blocks below carry forward into today, Mon Aug 3, unstarted:
- [ ] Chiller engine: pull CBS non-residential construction-starts data (last 5 years) + a sourced RT/m2 figure (ASHRAE rule-of-thumb or Israeli standard SI 5282).
- [ ] Chiller engine: build the sizing calc (construction trend x RT/m2 -> installed cooling capacity by year) + replacement-demand sensitivity (existing stock RT / lifetime).
- [ ] Heat pump + VSD sizing (light pass, order-of-magnitude only -- they only need to support the fiscal-cost/deadweight number, not an impact claim): pull national energy balance data (CBS/Ministry of Energy industrial mazut/diesel heat use) for heat pumps, national industrial electricity x ~10% compressed-air-share benchmark for VSD.
- [ ] Check the PRTR lead: is facility-level fuel/electricity consumption data actually accessible (portal or an existing EcoTraders contact)? If yes, use it to narrow the heat-pump/VSD addressable fraction instead of the borrowed international benchmarks; if not, document the international benchmarks as the fallback and move on -- don't let this become a rigor sink on a deadweight technology.
- [ ] Build the dual fiscal-cost rollup: total fiscal cost (sum the C-B row across all 6 blocks x each block's adoption count) and the separate chillers-only cost-effectiveness ratio (₪/tCO2, ₪/MWh, same ruler as the grant chapter).

**Mon Aug 3 (FULL, TODAY)** -- market sizing kicks off, built around the 15:30 Daniel meeting (this is the working session on the market analysis, not a review of finished work -- nothing above is done yet)
- [x] 9:00-10:30 (part 1) -- Chiller market sizing: pulled real CBS non-residential construction-starts data, last 5 years (2021-2025), from Table 7 of the official "התחלות וגמר בנייה -- סיכום שנת 2025" release. Chiller-relevant series (non-res total minus agriculture minus transport/comms) averages ~3,965 thousand m2/year. Full data + sourcing in `market-analysis.md`. RT/m2 still not sourced -- continuing.
- [ ] 10:30-12:00 -- Chiller engine: build the sizing calc (construction trend x RT/m2 -> installed cooling capacity by year) + replacement-demand sensitivity (existing stock RT / lifetime).
- [ ] 13:00-14:30 -- Heat pump + VSD sizing (light pass, order-of-magnitude): national energy balance data (CBS/Ministry of Energy industrial mazut/diesel heat use) for heat pumps, national industrial electricity x ~10% compressed-air-share benchmark for VSD.
- [ ] 14:30-15:30 -- Meeting prep: consolidate today's chiller + HP/VSD sizing progress and open questions into short talking points for Daniel -- PRTR access (does EcoTraders have a portal/contact?), whether he wants the accelerated-depreciation multiplier restricted to chillers only (the policy recommendation that falls out of the additionality split), confirm the adoption-count methodology per technology.
- [ ] 15:30 -- Daniel meeting (market analysis of the tax incentives).
- [ ] After the meeting -- log any new decisions (decisions/log.md), fold outcomes into this tracker, use any remaining time before end of day on whatever the meeting unblocked.

**Wed Aug 5 (FULL, TODAY)** -- post-meeting pivot: close out today's action items, then chapter work that isn't blocked by the market-sizing pause
- [x] Log the meeting pivot (decisions/log.md, tracker.md, market-analysis.md, baseline-technology-data.md) -- done first thing.
- [x] Standard-efficiency heat pump baseline sourced (real ASHRAE 90.1/DOE FEMP minimum COP, 3.3 at 47°F, both capacity points) -- real tension found and flagged (the already-sourced "efficient" 70kW unit's COP is at or below this new baseline, needs resolving before usable). CapEx premium not cleanly sourced this pass.
- [x] Built the Claude-in-Excel extension prompt for the TAOZ tariff calculation, with real sourced Israel Electricity Authority rates (effective 1.1.2026) -- `taoz-calculation-extension-prompt.md`, ready to hand to the extension whenever Omri runs it on the live model.
- [x] Yaniv Giat + Amos (Ministry of Energy) email sent 2026-08-05, cc Daniel -- import data request for all three technologies (chillers, heat pumps, VSD), industry-sector scope, framed as Daniel's suggestion to check customs import data. Waiting on a reply.
- [ ] Tax chapter: outline the full chapter, mirroring the grant chapter's structure -- not blocked by the market-sizing pause (background/method sections don't need adoption numbers).
- [ ] Tax chapter: write the background / policy-basis section (accelerated depreciation, מפעל מאושר mechanism).
- [ ] Loan fund full chapter: gap-check -- what does the existing position paper NOT cover that the full national-program chapter needs?
- [ ] Update the Rafi data-request list (Reference section below) -- furnace CapEx/maintenance ask is obsolete now, replace with standard-efficiency heat pump CapEx if Rafi's a better source than another web pass.

**Thu Aug 6 (HALF)**
- [ ] Block 1 -- Tax chapter: keep drafting (background/method sections should be close to done by now given the freed-up time).
- [ ] Block 2 -- Loan fund chapter: start drafting whatever the gap-check surfaced.
- [ ] Block 3 -- Buffer / whichever of the 3 deliverables needs it most.

### Week 3 (Aug 9 -- Aug 13)

Both chapters started earlier than originally planned (tax chapter Mon Aug 3, loan fund Thu Aug 6) since the lighter HP/VSD sizing pass freed up time in Week 2 -- treat the blocks below as "finish drafting" rather than "start drafting," and lean on the buffer blocks if Week 2 ran long instead.

**Sun Aug 9 (FULL)** -- loan fund chapter drafting continues
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

**Rafi is still owed (email sent 2026-07-22), updated 2026-08-05 for the baseline change:**
- ~~CapEx of the mazut/diesel furnace~~ -- OBSOLETE, the heat pump baseline is no longer a furnace (2026-08-05 pivot, see Confirmed #7). Replace with: CapEx of a standard-efficiency heat pump (40kW/70kW) -- not cleanly sourced from a web pass either, see `baseline-technology-data.md` section 1c. Worth asking Rafi directly rather than continuing to search.
- Incremental annual maintenance cost, efficient vs. baseline heat pump (was efficient-vs-furnace, now efficient-vs-standard-heat-pump -- same open ask, different baseline technology)
- Equipment degradation rate (0.5% placeholder)
- Confirmed annual operating hours (5,475 heat pump / 3,000 chiller / 6,400 VSD)
- **NEW:** his read on the real tension flagged in `baseline-technology-data.md` 1c -- the sourced "efficient" 70kW heat pump (COP 3.23-3.24) is at or below the new code-minimum baseline (COP 3.3). Needs resolving before the baseline change is usable.

**Discount rate:** resolved at 6% with Daniel back on 2026-07-13 (set in `generate_tax_model_v2.py`) -- this tracker previously had it listed as still-pending, caught during the 2026-07-27 branch-merge cleanup. Worth flagging to Daniel/Rafi whether 6% is meant to represent the social rate only, or the single rate the whole model uses for both the firm's private decision and the state's fiscal-cost calc -- that distinction matters once the payback-threshold adoption logic (private decision) and fiscal-cost NPV (state cost) are both live in the model.

**Full open-flags list (sourcing gaps, unresolved assumptions):** see `baseline-technology-data.md`.

**Market analysis methodology (full reasoning behind the sizing engines above):** see `brainstorms/2026-07-22_tax-incentive-market-analysis.md`.

**Resolved 2026-08-05 (was "parked for a later Daniel discussion"):** additionality/deadweight was resolved 2026-07-26 (payback-threshold reframe, chillers-only additionality) and the payback-threshold rule itself was confirmed by Daniel 2026-08-05 as the chapter's strongest conclusion. The chillers-only differentiated-multiplier policy recommendation (Cyprus precedent) was raised and rejected -- Daniel felt it would look "a bit silly" to recommend a tax incentive scoped to only one of three technologies, too narrow. Drop this from future chapter drafts.
