# Energy Program -- Schedule & Status

**Last updated:** 2026-08-19
**STATUS: CLOSED. All deliverables complete.** Omri's last working day at EcoTraders was
2026-08-19. Everything in the locked scope shipped. The day-by-day schedule further down this
file is kept as a historical record, not a live to-do list: its unchecked boxes are stale
schedule entries, not outstanding work. See "Unresolved at handoff" at the bottom for the real
known limitations that were never closed.

**Scope locked 2026-07-26 (Daniel), amended 2026-08-16:** originally 3 deliverables before Omri's Aug 22 last day; Daniel added a 4th. In priority/sequencing order (Omri's call, 2026-08-16):

1. **Tax incentive model, including the market analysis** -- DONE, submitted to Daniel 2026-08-17.
2. **Tax incentive chapter** for the national program -- DONE, submitted to Daniel 2026-08-17 alongside the model.
3. **Tax model documentation file** (Daniel's 4th deliverable, 2026-08-16) -- DONE 2026-08-17, `tax-model-documentation.docx`. Built on the personal account from the final submitted model + chapter.
4. **Grants model documentation file** -- DONE (confirmed 2026-08-19). Built on the work computer/company account. `work-handoff.md` is the briefing that drove it, kept for the record.
5. **Loan fund chapter** -- DONE 2026-08-19. Not a drafting task in the end: the appendix version (done 2026-08-03) already had every section, so this was a trim from ~6 pages toward ~3. Run in two phases, lossless cuts first (redundancy, padding, prose-to-table compression) with a decision gate before anything that would cost substance. Plan: `loan-chapter-outline.md`. Company-account prompt used: `2026-08-19-final-day-prompt.md`.

---

## Final status (2026-08-19)

| Deliverable | Status | Where it went |
|---|---|---|
| Grants program chapter | Done | Sent to Ministry client 2026-07-12 |
| Loan fund position paper | Done | Sent to Ministry client 2026-07-12 |
| Tax incentive model | Done | Submitted to Daniel 2026-08-17 |
| Tax incentive chapter | Done | Submitted to Daniel 2026-08-17. Shipped as an **appendix version, ~10 pages**, not trimmed to the 4-page in-body ceiling. All the flagged content issues were closed first: ₪875/kW baseline CapEx disclosed, technology/capacity list added ahead of Results, footnotes added, section 4.5 rewritten as an explicit placeholder, checked in real Word |
| Tax model documentation | Done | Built 2026-08-17, `tax-model-documentation.docx` |
| Grants model documentation | Done | Built on the company account, confirmed 2026-08-19 |
| Loan fund chapter (full) | Done | Trimmed 2026-08-19, landed at ~4 pages (from ~6) on the lossless pass alone, no substance cuts needed |

**Remaining action:** one closing email to Daniel bundling the tax model documentation, the
grants model documentation, and the loan fund chapter. Nothing else is outstanding.

**Sequencing constraint (2026-08-19):** the work PC goes back today and all three attachments
live on it. The email has to be sent, and confirmed sent with attachments, before the machine
is returned.

---

## Confirmed

1. **Thursday Aug 20 is the real last working day** (confirmed 2026-07-27) -- Aug 22 itself is a Saturday, not a work day.
2. **Thursday Jul 30 is presentation day** (economics seminar, distinction track) as well as a normal half-work-day. Scheduled light on purpose -- move blocks if the day gets eaten entirely.
3. **Additionality split resolved (2026-07-26, recovered from a branch that wasn't merged until 2026-07-27):** the adoption rule is now a 3-year payback-period threshold (Rafi's own number), not a 20-year NPV sign. At that threshold, only chillers (100RT/500RT) show real additionality -- heat pumps and VSD clear the bar with or without the incentive (deadweight). This changes the schedule below: chillers get the full rigorous market-sizing treatment, heat pumps/VSD get a lighter order-of-magnitude pass (they only need to support the fiscal-cost/deadweight number, not an impact claim). Full reasoning: `brainstorms/2026-07-26_payback-threshold-and-meeting-prep.md`.
4. **Fiscal cost reporting is dual, not single:** total fiscal cost = the incentive's tax-shield benefit (C-B) summed across every adopting unit in all 3 technologies (the tax break doesn't discriminate on additionality). Cost-effectiveness (₪/tCO2, ₪/MWh) can only be honestly computed for chillers, where there's real additional abatement to divide by -- dividing HP/VSD's cost by non-additional savings would credit the policy for reductions it didn't cause.
5. **PRTR (Ministry of Environmental Protection facility-level data) identified as a better source** than the borrowed international benchmarks (DOE/Radgen 10% compressed-air share, unsourced low-temp heat share) for narrowing the heat-pump/VSD addressable pool. Not yet pulled -- worth checking whether EcoTraders has existing portal/contact access.
6. **Schedule slipped ~1 week (confirmed 2026-08-03):** the Wed Jul 29 Daniel meeting never happened -- it's today, Mon Aug 3 at 15:30, and it's specifically about the market analysis. Thu Jul 30's chiller-sizing blocks (presentation day) didn't happen either, and the Week 2 Sun Aug 2 blocks (chiller sizing, HP/VSD light pass, PRTR check, fiscal-cost rollup) are also not done -- none of the market-sizing work has started yet. Loan fund appendix got pulled forward instead and is done. Today's block plan below is rebuilt around this reality; the rest of the multi-week schedule further down is stale by about a week and will get re-sequenced as work actually lands rather than rewritten speculatively now.
7. **Daniel meeting happened 2026-08-05 (moved from Aug 3) -- major market-analysis pivot.** Full outcomes in decisions/log.md. Summary: (a) the 3-year payback threshold confirmed as "probably the strongest conclusion we can provide" -- the core reframe stands; (b) real per-technology market sizing (chiller RT/m², heat pump fuel-balance, VSD compressed-air-share) is paused -- none of them reliably answer "how many projects happen per year," a flow, and all three were sizing a stock instead; (c) the chapter now shows savings **per 1,000 units, per technology** as a placeholder, chillers included, fiscal cost the same C-B calc x 1,000; (d) heat pump baseline changed from a mazut/diesel furnace to a **standard-efficiency heat pump** (same structure as chillers: baseline vs. efficient tier of the same technology) -- this makes most of Rafi's still-owed furnace data (CapEx, maintenance delta) obsolete, see the updated Reference section below; (e) the Cyprus-style chillers-only differentiated-multiplier recommendation was rejected by Daniel as too narrow to propose; (f) plan going forward is an email to Yaniv Giat (Ministry of Energy) asking for import data on all three technologies -- if that lands, it's a real annual flow figure and market sizing gets revisited with Daniel.
8. **Model verified essentially complete 2026-08-16, national-program-format version (v0.3):** all findings from `2026-08-16-formatted-model-review.md` closed except items requiring the hours sensitivity (which is now load-bearing, not a nicety -- heat pump additionality sits at payback 3.179 against a 3.0 threshold, the closest of the three to flipping). Verified independently (Python re-implementation, matches every cell exactly, zero formula errors in the workbook): tariff (36.97 agorot/kWh industrial HV, ex-VAT) approved by Daniel; row-318 emissions wiring fixed (820,897 tCO2e, ₪226,762,267 external costs unlocked); degradation now symmetric across baseline and efficient equipment on all 3 technologies; fiscal cost moved to the 3% social discount rate as its own deferred-tax calculation (no longer `=C-B`, since that identity only held under one shared rate) -- total fiscal cost dropped 41% to ₪21,126,029; firm's own adoption decision (payback, verdict, additionality) correctly stays at the 6% private rate. All 3 verdicts held through both fixes: chillers and heat pumps show additionality, VSD is deadweight. Still open: hours sensitivity, cohort-discounting convention (must match the grants chapter), double-counting vs. grants/loan fund (Daniel question), chiller lifespan inconsistency (truncated not equalized, opposite treatment from heat pumps).

---

## Exit logistics (status 2026-08-19)

Separate from the deliverables. These are Omri's own, not EcoTraders'.

| Item | Status |
|---|---|
| Final hours reported in Fireberry | Done |
| Work PC returned | Today. **Send the closing email before handing it back** -- all 3 attachments are on it |
| Handoff documentation | Not needed. Omri asked Daniel directly; Daniel wanted only the technical documentation |
| Reference / employment letter | **The only open item.** Asked for 2026-08-19 (Ron meeting). Draft written for Ron 2026-09-03: `reference-letter-draft.md`, English, all-round emphasis. Send before Sept 8 |
| Pension fund release letter (מכתב שחרור) | Not needed (confirmed 2026-09-03) |
| Unused vacation payout | Done, already settled (confirmed 2026-09-03) |
| Closing email to Daniel (2 doc files + loan fund chapter) | **Sent** (confirmed 2026-09-03), with the final two deliverables attached, before the work PC went back |

The last two are money owed and are much harder to chase as a former employee, especially with
the Sept 8 departure for Europe. They belong in the same conversation as the reference letter.

---

## Daily block schedule (Jul 27 -- Aug 20) -- HISTORICAL, CLOSED

**Read this before trusting any checkbox below.** This section is a record of how the work was
planned, not of what remains. Every deliverable shipped (see Final status above). The unchecked
boxes fall into three groups, none of which is outstanding work:

- **Deliberately abandoned:** all the chiller / heat pump / VSD market-sizing blocks. Killed by
  the Aug 5 Daniel pivot, which replaced real per-technology sizing with the per-1,000-units
  placeholder. They were never done because they were called off, not because they slipped.
- **Done on the company account:** the tax chapter sections, the chapter trim, the Aug 17
  finalization blocks, and the Aug 19 loan fund trim. The work happened on the work computer,
  so it was never checked off in this repo.
- **Overtaken by the calendar:** the Thu Aug 20 blocks. Aug 19 turned out to be the real last
  working day, so Aug 20 never ran.

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
- [x] Tax chapter: outline built -- `tax-chapter-outline.md`. 5 sections (background/policy context, mechanism, international review, methodology, results), mirroring the grants chapter's confirmed structure convention from `work-handoff.md`. Folds in today's pivot (per-1,000-units methodology, payback-threshold confirmed, Cyprus multiplier explicitly excluded). Flagged 4 open items, incl. locating the real grants chapter + international review files on the work computer for a side-by-side check.
- [x] Tax chapter: first draft written (Hebrew, .docx, RTL-verified) -- `tax-chapter-draft.docx`. Sections 1 (background/policy), 2 (mechanism), and 4 (methodology, all 4 sub-sections) drafted in full prose. Sections 3 (international review) and 5 (results) are marked placeholders, not fabricated -- 3 needs the real file from the work computer, 5 is blocked on final per-1,000-units model numbers. One open flag inside section 1: the exact legal basis (same Government Decision 1261 as the grants chapter, or separate) isn't confirmed in this repo's notes. Omri's own call to extend past the original "outline only, keep it calm" plan.
- [ ] Loan fund full chapter: gap-check -- deferred to tomorrow.
- [ ] Update the Rafi data-request list (Reference section below) -- deferred to tomorrow.

**Thu Aug 6 (HALF)**
- [ ] Block 1 -- Tax chapter: keep drafting (background/method sections should be close to done by now given the freed-up time).
- [ ] Block 2 -- Loan fund chapter: start drafting whatever the gap-check surfaced.
- [ ] Block 3 -- Buffer / whichever of the 3 deliverables needs it most.

### Week 3 (Aug 9 -- Aug 13)

**Reality check (2026-08-16):** Aug 9-10 did not happen as scheduled below -- university (Sustainability Project) took that time instead, zero EcoTraders progress those two days. Real work did happen on the work computer separately, tracked through the company-account chat rather than this file: tax chapter sections 1, 2, 3, 4 are drafted (further along than the Aug 5/6 log here shows), but a company-chat status report surfaced real problems -- 6 pages used against a 4-page ceiling for sections 1-4 alone (before results exist), the additionality finding has no section, section 4.5 overstates how far market sizing has actually gotten, section 2 lost its technology/capacity list mid-edit, footnotes from the international review aren't carried in, and the Excel model has 13 flagged issues plus a capacity-collapse restructure that were never confirmed fixed. Loan fund chapter: still zero progress since Aug 6. **Wed Aug 12 and Thu Aug 13's real status isn't tracked in this repo** -- this file was mistakenly worked on as if Aug 12 were "today" for that whole session (a stale in-file "TODAY" label got trusted over the actual date), so whatever happened those two real days, if anything, isn't captured here. The real model-rebuild work below happened Sun Aug 16, correctly dated after catching the mislabel.

~~**Sun Aug 9 (FULL)** -- loan fund chapter drafting continues~~ -- did not happen.
~~**Mon Aug 10 (FULL)**~~ -- did not happen.
**Wed Aug 12 / Thu Aug 13** -- status unknown, not tracked here (see reality-check note above).

### Week 4 (Aug 16 -- Aug 20) -- revisions + wrap-up buffer

**Sun Aug 16 (FULL, TODAY)** -- model rebuild + tax chapter triage, loan fund gets nothing today
- [x] 9:00-10:30 -- Capacity collapse: rebuilt all 3 technology blocks from 2 capacity points to 1 averaged point each (heat pump 55kW, chillers 300RT, VSD 97.5kW -- plain midpoint). Heat pump baseline COP averaged to 3.68; new standard-efficiency-HP baseline COP is flat at 3.3 either way.
- [x] 10:30-12:00 -- All 7 quick/confirmed model fixes applied in the same rebuild (more efficient than a second pass over the same cells): heat pump baseline swapped to standard-efficiency HP (flag #3, baseline CapEx derived at ₪875/kW by the same premium-based method already used for chiller/VSD baseline CapEx, flagged peach/estimated not green/sourced -- still needs a firmer number from Rafi/Daniel), OPEX-אחר hardcoded to 0 instead of a broken `#REF!` (flag #9), depreciation schedule now always sums to exactly 100% via a last-year rounding plug (flag #5), payback-C array formula generated for every block so none are empty anymore (flag #4), OPEX degradation sign fixed to `(1+degr)^(i-1)` (flag #1), winter-peak TAOZ weighting fixed to the same 5/7 factor as the other seasons -- tariff moves from 44.60 to 43.63 agorot/kWh as expected (flag #8), methodology note corrected from "2.5 years" to "3 years" to match the live F21 parameter (flag #13). New file: `generate_tax_model_v4.py` / `tax_incentive_model_v4.xlsx`.
- [x] **Verification:** LibreOffice recalc (the usual automated check) hung/timed out repeatedly in this session's sandbox, confirmed unrelated to the file itself (even a trivial one-formula test file hung -- looks like a font-directory symlink loop breaking headless LO startup here). Independently re-implemented the full formula chain in Python instead and cross-checked: depreciation schedule sums to exactly CapEx, TAOZ average lands at 43.63 agorot/kWh as expected, and the qualitative finding holds -- chillers show real additionality (payback flips from 3.88yrs to 2.43yrs, crossing the 3yr threshold), heat pumps and VSD clear the threshold with or without the incentive (deadweight), matching the original per-capacity-point model's core conclusion. **Not yet opened in real Excel -- do a first-open check for stray `#REF!`/`#NAME?` before trusting it fully**, since automated verification wasn't possible this session.
- [x] **Afternoon: Omri working directly in the live Excel file** (not the repo's v4 copy, which is now stale relative to it -- do not regenerate blind). Resolved: flag #2 (asymmetric lifespans) -- heat pump and chiller lifespans both equalized (heat pump 15/15, was 15/10; chiller equalized, was 15/17), removing a real distortion (~166K of a 495K NPV gap for heat pumps alone traced to it). Flag #6 (VSD load-following representation) -- confirmed fine after a Rafi conversation, closed. Flag #12 (heat pump hours) -- lowered from 5,475 to 5,000, still Rafi's number, not independently re-verified. Flag #10 (MWh/tCO2 rows) and flag #11 (discount-rate fix, real government rate confirmed at 3%) both deferred on purpose to a later "format transition" into the national program model, which already has built-in emissions calcs off energy savings -- not being built into this workbook. Sensitivity Data Tables being rebuilt by Omri directly in Excel, not a repo task.
- [x] Flag #7 robustness-checked: verdict only flips above ~55 agorot/kWh (~26% jump from 43.63) -- still a real caveat to raise with Daniel, but not a fragile result. Still open, not today's fix.

**Real sequencing for the rest of the model + chapter (Omri's call, 2026-08-16 afternoon)** -- trim happens LAST, once all real content exists, not before:
1. [x] Transition the tax incentive model into the national program model's format -- done, company account. This is also where MWh/tCO2 and the discount-rate fix (3% government rate, confirmed real) get handled, per that format's built-in emissions calcs off energy savings.
2. [x] Insert the per-1,000-units calculation, all 3 technologies -- done via `2026-08-16-per-1000-units-extension-prompt.md`, run through the Claude-in-Excel extension, Omri now has a formatted result. Final structure landed on an additionality-gated design, not a flat x1,000: fiscal cost per 1,000 units always shown (deadweight still costs real money, rational firms claim the accelerated-depreciation election regardless), a single "economic value" column that reads as (C−A)−fiscal cost = B−A (the real efficiency gain) when the incentive flipped the decision, or just the fiscal cost when it didn't (Option A, one shared column per Omri's call), MWh saved gated the same way as economic value (no crediting the policy with savings it didn't cause). tCO2e still deferred to the format transition.
3. [x] **Format transition finished, company account -- generating a detailed section-by-section report now** for review before moving to the tax chapter.
4. [ ] Rebuild sensitivity analyses (Data Tables) against the new consolidated capacity points.
5. [x] **Put the real results into the tax chapter (section 5)** -- done 2026-08-16. `tax-chapter-draft-with-results.docx` (new file, built off the uploaded `taxchapterdraft_1.docx`). Four subsections: 5.1 per-unit paybacks/verdicts (table), 5.2 economic value + fiscal cost per 1,000 units (table, additionality-gated per the Option A design), 5.3 energy savings/emissions/external costs (additional technologies only), 5.4 cost-effectiveness (₪23.2/tCO2e, additionality-restricted, explicitly flagged as needing to match the grants chapter's ruler before finalizing). Heat pump's narrow margin (3.18 vs 3.0 threshold) stated plainly in the text, not glossed over. Numbers verified against the model exactly (see `2026-08-16-formatted-model-review.md`). Validated: XML well-formed, schema validation passed against the original. Could not visually render (LibreOffice broken in this sandbox for both the original and edited file -- confirmed environment-wide, not an artifact of the edit) -- **do a first-open check in real Word before sending to Daniel.**
6. [ ] Trim the whole chapter to the 4-page ceiling, now that all content actually lives in it -- company account.

**Other chapter issues found while reading the draft (2026-08-16), still open, not fixed today -- flagged to Omri, not silently fixed since they're outside "insert results":**
- [ ] Heat pump baseline CapEx assumption (₪875/kW) still needs explicit disclosure in the chapter text (Omri's own requirement from earlier today).
- [ ] Section 4.5 (אמידת היקף השוק) still reads in present tense as if import-data market sizing is active ("מבוססת על נתוני ייבוא... נתוני השנים האחרונות משמשים לבניית תחזית") when it's actually paused -- needs rewording to future/conditional tense, flagged originally in the Aug 12 status report and still unaddressed in this draft.
- [ ] No technology/capacity list (55kW heat pump / 300RT chiller / 97.5kW VSD) anywhere before the Results section -- section 2 (אופן פעולת המנגנון) doesn't name them, and section 4.1 (מבנה הניתוח) references "נקודת קיבולת ממוצעת" without stating what it is. Results now names them in its opening paragraph, but the earlier sections still don't.
- [ ] Zero real footnotes in the document (footnotes.xml is empty, no footnote references in the body) -- the international review table's country-by-country claims have no citations attached.
- [ ] Page count: ~1,823 words across sections 1-4 before this session's Results addition (+1,050 words) -- worth an actual page count once opened in Word, given the known 4-page ceiling for the whole chapter.

**2026-08-16, later same day -- chiller capacity correction + 3 more chapter sections:** Omri caught that chillers were carrying ~93% of the program's total benefit and cross-checked capacity against the real grant-program median (117 RT, not 300) -- corrected to 120 RT. Payback verdicts unaffected (scale-invariant), but every ₪/kWh magnitude for chillers drops by 0.4x. Also asked for three additions: (1) a new §5.2 explaining the total-benefit calculation method (the honest answer: per-cohort NPV summed without cross-cohort re-discounting to 2026 -- flagged as needing to match the grants chapter's convention, same open question as finding #7); (2) a new §5.5 explaining the annual savings/emissions profile shape (ramp-up to a 2041 peak as cohorts accumulate, then decline as the earliest cohorts retire with no replacement modeled -- explicitly flagged as an artifact of a single deployment round, not a real forecast of declining impact); (3) a table for 2030 and 2035 specifically. Combined extension prompt (model change + chapter updates + new content) at `2026-08-16-chiller-capacity-and-chapter-additions-extension-prompt.md`, with full computed expected values for verification (new totals: economic value ₪139.3M, fiscal cost ₪10.2M, ~360,935 tCO2e).

**Mon Aug 17 (FULL)**
- [ ] 9:00-10:30 -- Finalize model.
- [ ] 10:30-12:00 -- Finalize tax chapter.
- [ ] 13:00-14:30 -- Finalize loan fund chapter.
- [ ] 14:30-16:00 -- Final QA across all 3.
- [ ] 16:00-17:30 -- Buffer.

**Wed Aug 19 (FULL) -- loan fund chapter, the final deliverable -- a trim, not a draft**
- [x] Trim plan built (`loan-chapter-outline.md`) -- correction from this morning's original plan: the appendix version (done 2026-08-03) already has every required section, this is purely a 6-page -> 3-page trim. Cut order: redundant explanation first, then non-load-bearing examples, then compress any international comparison to a table, then tighten background prose, mechanism/methodology sections last. Work-computer handoff updated to match (`loan-fund-work-handoff.md`).
- [ ] 9:00-10:00 -- On the work computer: open the appendix version, confirm the page-format convention (font/spacing/margins) against the grants/tax chapters so "3 pages" matches, running page-count check as you read.
- [ ] 10:00-12:00 -- Cut passes 1-3: redundant explanation, non-load-bearing examples, international comparison to table form. Re-check page count after each pass.
- [ ] 13:00-14:30 -- Cut pass 4 (background tightening) if still over target; only touch mechanism/methodology as a last resort. Stop as soon as 3 pages is hit.
- [ ] 14:30-15:30 -- Full read-through of the trimmed version -- confirm it reads as a complete chapter, not fragments. Flag to Daniel any real number/claim that had to be cut.
- [ ] 15:30-17:30 -- Send to Daniel. Closes out all 4 locked EcoTraders deliverables -- the whole Energy Program scope for Omri's tenure.

**Thu Aug 20 (HALF -- last real working day)**
- [ ] Block 1 -- Final sign-off tasks.
- [ ] Block 2 -- Wrap-up/handoff documentation.
- [ ] Block 3 -- Buffer / anything still open.

---

## Unresolved at handoff (2026-08-19)

Everything shipped, but these were never closed. They're documented in the model documentation
files where they affect a number, so this list is a summary, not the only record. Whoever picks
this project up should read them before treating any of these figures as settled.

**Data requested from Rafi that never arrived.** No further response after 2026-07-26, so all of
the below stand as they are in the shipped model (email sent 2026-07-22, updated 2026-08-05 when
the heat pump baseline changed):
- CapEx of a standard-efficiency heat pump baseline. Never cleanly sourced from Rafi or from a
  web pass, so the model uses ₪875/kW derived by the same premium-based method used for the
  chiller and VSD baselines. Flagged in the workbook as estimated, not sourced.
- Incremental annual maintenance cost, efficient vs. baseline heat pump. Set to 0 across all
  three technologies on Rafi's earlier answer; never revisited for the new baseline.
- Equipment degradation rate: still a 0.5% placeholder.
- Annual operating hours: heat pump lowered to 5,000 as a working correction, still Rafi's
  number and never independently re-verified.
- The COP tension in `baseline-technology-data.md` 1c: the sourced "efficient" 70kW heat pump
  (COP 3.23-3.24) sits at or below the code-minimum baseline (COP 3.3). The 2026-08-16 capacity
  collapse to a single averaged point softened this but did not resolve it.

**Methodology, confirmed status 2026-08-19:**
- **Still open: cohort-discounting convention.** Total benefit is per-cohort NPV summed without
  re-discounting each cohort back to a common 2026 base. Never confirmed against the grants
  chapter's convention. Low stakes in practice, since the cross-chapter cost-effectiveness
  comparison was dropped (below), but it would matter if anyone puts the tax chapter's totals
  next to the grants chapter's on the same ruler.
- Double-counting across the grants, tax, and loan fund instruments: raised with Daniel.
- Tariff weighting (flag #7): raised with Daniel as a caveat. The model uses a flat blended
  rate; a chiller-specific peak-weighted tariff would be higher. Robustness-checked 2026-08-16:
  the chiller additionality verdict only flips above ~55 agorot/kWh against the current 43.63,
  so it is a real caveat but not a fragile result.
- Chiller lifespan: RESOLVED. All lifespans equalized, consistent with the heat pump treatment.
- Cost-effectiveness (₪23.2/tCO2e, additionality-restricted): not used in the end, not needed.
  The open question about matching the grants chapter's ruler is therefore moot.

**Sensitivity Data Tables: rebuilt** against the consolidated single-capacity-point blocks.

**Model bugs: all fixed.** The v4 workbook was opened and checked in real Excel; no stray
`#REF!` / `#NAME?` survived. (This was flagged as unverifiable from the repo side, since
LibreOffice was broken in the sandbox.)

**Market sizing:** paused, not solved, and both routes out of it closed.
- The import-data request to Yaniv Giat and Amos at the Ministry of Energy (sent 2026-08-05, cc
  Daniel) never got a reply. That was the route to a real annual flow figure.
- PRTR (Ministry of Environmental Protection facility-level data) was checked and turned out not
  to be relevant.
- The chapter therefore reports per 1,000 units as an explicit placeholder. Section 4.5 is
  written as a placeholder with a comment rather than claiming active sizing work.

**Discount rates, for the record:** 6% private rate for the firm's own adoption decision
(payback, verdict, additionality), 3% social rate for the state's fiscal cost. Split confirmed
and implemented 2026-08-16.

**Full open-flags list (sourcing gaps, unresolved assumptions):** see `baseline-technology-data.md`.

**Market analysis methodology (full reasoning behind the sizing engines above):** see `brainstorms/2026-07-22_tax-incentive-market-analysis.md`.

**Resolved 2026-08-05 (was "parked for a later Daniel discussion"):** additionality/deadweight was resolved 2026-07-26 (payback-threshold reframe, chillers-only additionality) and the payback-threshold rule itself was confirmed by Daniel 2026-08-05 as the chapter's strongest conclusion. The chillers-only differentiated-multiplier policy recommendation (Cyprus precedent) was raised and rejected -- Daniel felt it would look "a bit silly" to recommend a tax incentive scoped to only one of three technologies, too narrow. Drop this from future chapter drafts.
