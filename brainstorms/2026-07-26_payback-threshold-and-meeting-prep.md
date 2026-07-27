# Tax Incentive Model -- Payback-Threshold Reframe & Daniel Meeting Prep

**Date:** 2026-07-26 (meeting with Daniel: 2026-07-27)
**Context:** Continuation of the 2026-07-22 market-analysis brainstorm, after Rafi replied with his four data points. Covers the deadweight discovery, the payback-threshold fix, and the full agenda built for the Daniel meeting.

---

## Rafi's answers applied to the model

- Furnace baseline CapEx: 479 ILS/kW net of VAT (midpoint of his 37,000-75,000 ILS incl. VAT per 100kW complete-installed-project range), matched to the grant-sourced efficient CapEx basis (also net)
- Incremental maintenance: 0 for all three technologies (chiller/VSD efficient=baseline; heat pump actually cheaper than a furnace -- no annual combustion safety/efficiency test, no stoker -- so 0 is the conservative direction, not an overstatement)
- VSD degradation: 0 (screw compressors hold efficiency until failure)
- VSD hours: ~5,000 (his 24/7 compressor-hours ceiling; the old 6,400 looked like open-hours, not compressor run-hours)

Applied via a Claude-in-Excel extension working directly on Omri's live file, not by regenerating xlsx copies each session. Values independently verified by replicating the model's NPV logic in Python.

## Built: A-C investment decision row

Per Daniel's request: a decision row and verdict per technology block, C (efficient+incentive) minus A (existing baseline), plus summary columns, green/red/amber conditional formatting.

## The deadweight discovery

Replicating the model in Python (needed because LibreOffice is broken in this sandbox and can't recalc live) surfaced that **every technology is already NPV-positive without the incentive** under the original 20-year NPV adoption rule. Stress-tested three ways, all confirmed the finding is robust:
1. Electricity tariff fix (14 -> 39.54 agorot, real HV TAOZ average): still deadweight everywhere. Chillers/VSD save electricity so a higher tariff strengthens their case; heat pumps stay hugely positive regardless since diesel is the pricier fuel either way.
2. Extending to a 25-year horizon: still deadweight everywhere.
3. Adding 50%-of-CapEx replacement costs at end-of-life: still deadweight everywhere (replacement lands harder on the heat pump, 2 replacements vs. the furnace's 1, but the annual energy-cost gap swamps it).

Per Omri's call, the 25-year/replacement experiment was reverted back to the plain 20-year model -- that realism belongs to the eventual national-program market analysis, not to checking Rafi's four numbers.

## The fix: payback-threshold adoption rule

Real firms approve efficiency capex on short internal payback hurdles, not a 20-year social NPV. This is also a genuine conceptual distinction: predicting *whether a firm adopts* is a different question from valuing *the policy's welfare benefit* (which can still use the social discount rate, once adoption is known).

**Threshold = 3 years, sourced to Rafi's own number from his first-ever conversation with Omri about this tax model** (not a generic literature placeholder).

Implemented as a single self-contained array formula per block (`LET` + `SEQUENCE` + `MMULT`), computing the cumulative-cash-flow crossover with interpolation inline, no visible year-by-year helper row (Omri didn't want 21-column clutter). A transpose bug in the first draft (`TRANSPOSE(SEQUENCE(n))` breaks the broadcast into a triangular matrix; `SEQUENCE(n,1)` is correct) was caught and fixed by the extension itself. All 12 payback values (B and C, 6 blocks) verified byte-identical before the old row-based version was deleted.

### Result at threshold = 3

| Technology | Payback B | Payback C | Verdict |
|---|---|---|---|
| Heat pumps 40kW | 0.48 | 0.47 | worth anyway (deadweight) |
| Heat pumps 70kW | 0.55 | 0.54 | worth anyway (deadweight) |
| **Chillers 100RT** | 3.60 | 2.36 | **incentive flips it** |
| **Chillers 500RT** | 4.53 | 2.73 | **incentive flips it** |
| VSD 45kW | 0.63 | 0.58 | worth anyway (deadweight) |
| VSD 150kW | 0.63 | 0.58 | worth anyway (deadweight) |

Sensitivity analysis (hours per technology, using Rafi's own quoted ranges, plus the depreciation multiplier across all 6) was scoped and a build prompt sent to the extension, to show how robust this split is -- not yet confirmed complete as of this capture.

## What this reframes for the chapter

1. **Which technologies matter for the impact claim.** Only chillers show real additionality; multiplying HP/VSD per-unit results by a market size measures a transition happening anyway, not incentive impact.
2. **Effort allocation.** Chillers get rigorous market sizing (real impact claim). HP/VSD get a lighter, order-of-magnitude estimate (only feeds a deadweight/fiscal-cost figure).
3. **A policy recommendation falls out of this.** Restrict/target the accelerated-depreciation multiplier to chillers specifically, rather than one uniform multiplier. Precedented by Cyprus's own differentiated-multiplier design, already documented in the international review Omri wrote.
4. **Fiscal cost needs two numbers, not one.** Total fiscal cost = C-B summed across every adopting unit in all technologies (the tax benefit doesn't discriminate on additionality). Cost-effectiveness (ILS/tCO2, ILS/MWh) can only be honestly computed for chillers, where there's real additional abatement to divide by.
5. **A real methodological asymmetry vs. the grant chapter, worth flagging to Daniel directly.** The grant chapter explicitly avoided an additionality claim ("not a but-for causal claim"). The tax chapter, built this way, would make one.

## Market-sizing research done this session

Checked CBS's own published energy-balance chapter (fetched and read directly) -- confirmed it's macro/sector-level only (e.g. industry = 22.6% of national electricity, not broken down further), not granular enough for narrowing heat-pump/VSD addressable pools.

**New lead: Israel's PRTR (Pollutant Release and Transfer Register, Ministry of Environmental Protection)** -- facility-level, public, explicitly requires reporting both fuel and electricity consumption by sector (energy, metals, chemicals, food & beverage, etc.). Could replace the borrowed international benchmarks (DOE/Radgen 10% compressed-air share; unsourced low-temp heat share) with a real Israeli anchor. Worth asking Daniel whether EcoTraders has existing access/contact there beyond the public portal.

Also floated: reuse the grant program's own data not for total market count (already ruled out as biased) but for **typical unit size per facility type**, combined with an independent facility count -- a less-biased use of the same dataset.

## Deliverable

3-page PDF built and delivered to Omri: `Tax_Incentive_Market_Analysis_Discussion_Points.pdf` -- six sections (quick wins, payback-threshold reframe, technology emphasis, fiscal-cost reporting, market sizing, consolidated punch list of 10 decisions needed from Daniel). Google Drive upload requested but not possible from this cloud session (only Gmail + Notion connectors available, no Drive) -- Omri offered email-to-self or connecting a real Drive connector instead.

## Next steps

1. Meeting with Daniel, 2026-07-27, using the PDF + this capture
2. Confirm/complete the hours + multiplier sensitivity build
3. Once Daniel signs off on the payback-threshold reframe: build the chiller market-sizing engine (construction-based, per his own method), explore the PRTR lead
4. Loan fund chapter for the national program still pending, deferred behind the tax incentive chapter
