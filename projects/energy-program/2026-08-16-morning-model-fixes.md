# Morning Model Fixes -- 2026-08-16

Brief to take into the work-computer session. Two parts: (1) capacity collapse, (2) the 7 quick/confirmed fixes from the company-chat status report. Everything below references the model's live sheet as described in that report (`מודל_פחת_מואץ_0_1.xlsx`).

---

## 1. Capacity collapse -- 6 blocks to 3, simple average

Collapse each technology from 2 capacity points to 1 (Omri's call: plain arithmetic midpoint, no weighting). Where a parameter was already flat across both capacity points (most CapEx, hours, VSD specific power), it carries over unchanged -- only the capacity value itself and any capacity-linked efficiency figure actually need averaging.

### Heat pumps: 40kW / 70kW -> **55 kW**

| Parameter | Value | Note |
|---|---|---|
| Capacity | 55 kW | midpoint |
| Efficient COP | **3.68** | midpoint of 4.13 / 3.235 -- this also softens (doesn't resolve) the flagged tension where the 70kW-only efficient COP sat at/below the new 3.3 baseline |
| Baseline (standard-efficiency HP) COP | 3.3 | already flat across both points, unchanged |
| Efficient CapEx | ₪1,050/kW x 55 = **₪57,750** | rate already flat, just apply to new capacity |
| Baseline CapEx | not cleanly sourced -- if used, ~840-915 ILS/kW x 55 = **₪46,200-50,325**, labeled as illustrative, not a real quote | see baseline-technology-data.md 1c |
| Efficient electrical input | 55/3.68 = **14.95 kW** | derived |
| Baseline electrical input | 55/3.3 = **16.67 kW** | derived |
| Hours | 5,475 | already locked (Rafi's data), unchanged |

### Chillers: 100RT / 500RT -> **300 RT**

| Parameter | Value | Note |
|---|---|---|
| Capacity | 300 RT | midpoint |
| Baseline kW/ton | **0.775** | midpoint of 0.95 / 0.60 -- blurs the real reciprocating-vs-centrifugal compressor-class distinction between the two original points, that's an accepted side effect of collapsing |
| Efficient kW/ton | **0.64** | midpoint of 0.80 / 0.48 |
| Baseline power | 300 x 0.775 = 232.5 kW | derived |
| Efficient power | 300 x 0.64 = 192 kW | derived |
| CapEx efficient | ₪4,186/ton x 300 = **₪1,255,800** | rate already flat |
| CapEx baseline | ₪3,562/ton x 300 = **₪1,068,600** | rate already flat |
| Hours | 3,000 | already locked, unchanged |

### VSD: 45kW / 150kW -> **97.5 kW**

| Parameter | Value | Note |
|---|---|---|
| Capacity | 97.5 kW | midpoint |
| Specific power baseline / efficient | 21.5 / 16.5 kW/100cfm | already flat across capacity, unchanged |
| Savings % | 23.26% | already flat, unchanged |
| CapEx efficient | ₪1,500/kW x 97.5 = **₪146,250** | rate already flat |
| CapEx baseline | ₪1,224/kW x 97.5 = **₪119,340** | rate already flat |
| Hours | ~5,000 | already locked (Rafi's data), unchanged |

**Chapter side-effect:** once this is live, section 2's technology/capacity list can be restored (55kW heat pump / 300RT chiller / 97.5kW VSD) -- that's today's afternoon chapter block.

---

## 2. Quick/confirmed model fixes (flags from the status report)

Do these alongside the collapse -- most are one-cell fixes, bundle them into the same session so the model only gets touched once today.

1. **Heat pump baseline still wrong (flag #3, confirmed needs changing).** Baseline is currently mazut/diesel oven formulas -- swap to the standard-efficiency heat pump baseline per `baseline-technology-data.md` section 1c: baseline OPEX = capacity / 3.3 (COP) x hours x electricity tariff, same structural formula as the efficient side, not a fuel-cost formula. This also removes the baseline-side fuel-price/fuel-CapEx references entirely -- no more mazut/diesel line items in this block.
2. **OPEX-אחר `#REF!` in every block (flag #9).** Broken cell reference, likely from an earlier row/column shift (probably the C-A row addition or the capacity collapse itself). Repoint to the correct source cell; confirm the delta still resolves to 0 as intended once fixed.
3. **Documentation note B58 (flag #13).** Says default payback threshold is 2.5 years; live parameter is 3. Fix the label to read 3.
4. **Depreciation schedule doesn't sum to 100% (flag #5).** `ROUND(1÷(0.1×multiplier))` gives ~105% at 1.5x and ~90% at 3x -- the rounded year-count doesn't divide back cleanly. Fix: don't round the year count itself; instead let the final depreciation year absorb the rounding residual (100% minus the sum of all prior years) so the schedule always totals exactly 100%.
5. **VSD payback-C formula empty (flag #4, cells F241 and F286).** Copy the payback-B array formula pattern into these two cells, adjusted for the C-column cash-flow references. Currently doesn't change the headline result (B already clears the 3yr threshold) but breaks the sensitivity tables that reference these cells.
6. **Efficient-equipment OPEX degradation sign flipped (flag #1).** Currently `(1-0.005)^n`, which makes cost fall over time -- degrading equipment should cost *more* over time (needs more energy for the same output), so this should be `(1+0.005)^n`. Flip the sign.
7. **Winter peak hours costed 7 days/week (flag #8).** Other seasons use a 5/7 weekday factor; winter peak should too for consistency. Applying it moves the average tariff from 44.60 to 43.60 agorot/kWh -- expect that shift and don't treat it as a new bug when the number moves.

---

## 3. MWh/tCO2 output rows (flag #10) -- afternoon, not morning

Not part of this morning's block, but next in line once the above is stable: add a conversion layer off the existing energy-savings rows (37-38) plus an emissions factor, so the chapter's Results section has something to pull from. Tracked separately in `tracker.md`.

---

## 4. Items NOT for today -- raise with Daniel/Rafi instead

- **Flag #2** -- asymmetric equipment lifespans in a flat 20yr window, no replacement/salvage value (heat pump: 15yr baseline vs 10yr efficient). Real: ~166K ₪ of a 495K ₪ NPV gap traces to this. Needs a methodology call, not a formula fix.
- **Flag #6** -- VSD savings % derived from full-load specific power applied to full-load baseline consumption; doesn't represent the load-following behavior that's VSD's actual selling point. Open pending a conversation with Rafi on control type and load factor.
- **Flag #7** -- electricity tariff is hour-weighted only, not weighted by when each technology actually runs. Conservative specifically for chillers -- the one technology carrying the additionality claim. Worth flagging to Daniel, not urgent to fix.
- **Flag #11** -- fiscal cost discounted at the firm's 6% rate rather than a separate government rate. Reasonable simplification, may revisit.
- **Flag #12** -- heat pump hours (5,475) sit at the top of Rafi's own range and are what drive the heat-pump deadweight conclusion. Load-bearing for a headline finding; worth a direct check with Rafi rather than treating it as settled.
