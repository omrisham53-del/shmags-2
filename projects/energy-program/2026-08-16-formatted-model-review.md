# Review: Formatted Tax Incentive Model (v0.3, national program format)

Reviewed 2026-08-16 against everything agreed in prior sessions. File: `מודל פחת מואץ 0.3.xlsx`, sheets `נתונים והנחות - כללי` + `ניתוח פחת מואץ`.

**Verification method:** LibreOffice recalc is broken in this sandbox, so the full formula chain was independently re-implemented in Python. The replication reproduces the workbook's payback figures exactly (heat pump 3.374, chiller 4.652, VSD 0.671), so the logic below is confirmed, not inferred. No formula errors anywhere in the workbook (no `#REF!`, `#NAME?`, `#DIV/0!`).

---

## Blockers -- fix before results go into the chapter

### 1. Emissions and external-cost savings are zero. Row 318 was never wired up. -- FIXED 2026-08-16

**Resolution:** Omri wired the electricity row and applied the resulting externality savings to the economy-wide economic benefit row. Original finding below for the record.

The whole reason for the format transition was that this format has built-in emissions calculations off energy savings. Those calculations exist and are correct -- but their input is not connected.

- `R296/R297` correctly compute total electricity saved (1,514,774,236 kWh over 2026-2050).
- `R305` (final-energy savings, industry) correctly references it.
- **`R318` (חשמל, inside the חיסכון בצריכת דלקים table) is hardcoded `0` in every year.**
- `R337` (emissions) and `R345` (external costs) both read `R318`, so both return 0 for all 25 years.

Net effect: the chapter's tCO2 and external-cost figures are currently **zero**.

**Fix:** `G318:AE318` = `G296:AE296`. Note it must be **kWh, not MWh** -- the electricity emission factor (`נתונים והנחות - כללי'!F50` = 0.000436) is tCO2e **per kWh**, and the external-cost factor (`F75` = 0.1204) is ₪ **per kWh**. Referencing R297 (MWh) instead would understate both by 1000x.

Once wired, the chapter gains: **~660,000 tCO2e avoided** and **~₪182M in avoided external costs**.

### 2. The headline finding has changed -- heat pumps now show additionality

Every prior session, and the already-drafted chapter sections 1-4, are built on: *"only chillers show real additionality; heat pumps and VSD are deadweight."*

The formatted model now says:

| Technology | Payback B (no incentive) | Payback C (with) | Verdict |
|---|---|---|---|
| Heat pump 55 kW | **3.374** | 2.287 | **incentive flips the decision** |
| Chiller 300 RT | 4.652 | 2.705 | incentive flips the decision |
| VSD 97.5 kW | 0.671 | 0.621 | worth it anyway (deadweight) |

Two of three technologies are now additional, not one. Driven by two changes made today that both cut annual savings: the tariff moving to ex-VAT (43.63 → 36.97, -15%) and heat pump hours (5,475 → 5,000, -8.7%).

This is not a small edit to the chapter -- it changes the central conclusion and the entire asymmetric-rigor argument built on it (2026-07-26 decision). It also removes the awkwardness of a policy where only one of three technologies works.

### 3. ...and that new heat pump verdict is fragile

Payback B is 3.374 against a 3.0 threshold -- about 12% of headroom. It flips back to non-additional under plausible corrections:

| Scenario | Payback B | Verdict |
|---|---|---|
| As-is in the file | 3.374 | additional |
| Fix the degradation asymmetry (finding 4) | 3.179 | additional |
| Hours back to 5,475 | 3.043 | additional (barely) |
| Degradation fix **+** hours 5,475 | 2.897 | **not additional** |
| Tariff at the national program's own 54.51 (finding 5) | 2.21 | **not additional** |

Chillers (4.652) and VSD (0.671) are both robust -- neither is near the threshold. Only the heat pump is knife-edge. **The chapter should not present heat pump additionality as a firm finding without stating the sensitivity.** This makes the hours sensitivity analysis the single most important one in the model, not a nice-to-have.

---

## Real methodology issues

### 4. Degradation is applied to only one side of the comparison

- Scenario A (baseline): OPEX flat, no degradation -- `R117`, `R182`, `R247`
- Scenario B/C (efficient): OPEX × `(1+0.005)^(t-1)` -- `R123`, `R188`, `R253`

Since the Aug 5 baseline change, both sides of every comparison are the **same technology class** (heat pump vs heat pump, chiller vs chiller, VSD vs VSD). There's no basis for degrading only the efficient unit. The effect is that modelled savings *shrink* year over year (heat pump: 8,605 kWh in year 1 down to ~5,175 by year 10) when they should stay roughly flat. It biases against the efficient technology, i.e. against the incentive's case.

Same asymmetry appears in the savings rows (`R149:R163` etc.), consistently -- so it's one decision applied throughout, not a stray cell.

### 5. Tariff diverges from the national program's own shared assumption -- RESOLVED: approved by Daniel

**Resolution (2026-08-16):** Omri confirmed the industrial high-voltage TAOZ rate (36.97 agorot/kWh ex-VAT) is already approved by Daniel. The divergence from the shared sheet's 54.51 is deliberate. Keeping the analysis below since the sensitivity it documents is still worth knowing -- it shows how much rides on this parameter.

The model computes its own industrial high-voltage TAOZ average (36.97 agorot/kWh ex-VAT). The national program's shared assumptions sheet carries electricity at **54.51 agorot/kWh ex-VAT** (`F84`, ביתי וכללי), which this model never references.

Using the industrial HV rate is *more accurate* for industrial equipment, and is defensible. But the divergence needs to be a deliberate, documented decision, because it drives everything:

| Tariff used | Heat pump | Chiller | VSD |
|---|---|---|---|
| 36.97 (model's own industrial HV) | additional | additional | deadweight |
| 54.51 (national program shared) | **not additional** | additional (3.05 -- razor thin) | deadweight |

At the shared rate, the chapter would have essentially **no robust additionality finding at all**. Worth raising with Daniel explicitly rather than leaving as an unremarked divergence.

*(The ex-VAT conversion itself is correct and deliberate -- all six TAOZ rates divided by exactly 1.18. Right call, since firms reclaim VAT.)*

### 6. Social discount rate is defined but never used — RESOLVED 2026-08-16, see below

**Resolution (answered in session):** the rate follows whose money the number represents.

*Stays at 6% (private):* the firm's cash flows as used for the adoption test, payback B and C, the verdict row, the additionality factor. A firm discounts at its own cost of capital; using 3% here would model a firm that doesn't exist, and would shorten paybacks enough to lose legitimate additionality findings.

*Moves to 3% (social):* the fiscal cost (deferred tax revenue is a government stream), the external-cost savings, and the economy-wide benefit feeding the national program.

**Structural consequence:** once the two rates differ, fiscal cost can no longer be `=C−B` — that identity only held under one shared rate. It needs its own row: the annual difference between the accelerated and standard tax shields (`מגן מס מואץ − מגן מס סטנדרטי`), discounted at 3% and summed.

**Impact (verified against the workbook — the 6% figure reproduces F136 = ₪1,414 exactly):**

| | at 6% | at 3% | change |
|---|---|---|---|
| Heat pump / unit | ₪1,414 | ₪836 | −41% |
| Chiller / unit | ₪30,750 | ₪18,174 | −41% |
| VSD / unit | ₪3,581 | ₪2,117 | −41% |
| Total × 1,000 units | ₪35.7M | ₪21.1M | −41% |

Uniform −41%, because the lower rate discounts the state's later recoupment less. Cost-effectiveness improves from ~₪54 to **~₪32 per tCO2e** against the ~660,000 tCO2e unlocked by the row-318 fix. **Check the grants chapter's own discount rate before quoting that ratio** — the comparison is only meaningful if both chapters use the same one.

**Open caveat, flagged not fixed:** the economy-wide benefit currently reuses B−A, which includes tax shields. Those are transfers between firm and state, not real resource flows, so strictly they don't belong in a societal benefit figure. A clean version would be −ΔCapEx + energy savings + external benefits, all at 3%, with no tax terms. Agreed to state this as a methodology limitation in the chapter rather than restructure an already-formatted row.

### 6a. Original finding (for the record)

`F32` = 3% (the real government rate confirmed earlier today) sits in the sheet **unreferenced**. All 225 discounting formulas use `F31` = 6%, the private rate.

That means the `תועלת כלכלית משקית` figures feeding the national program's benefit tables are discounted at the *firm's* rate. For a societal CBA feeding a national program this is the wrong rate -- and it's exactly the fix that was deferred to "the format transition," which has now happened.

At minimum the fiscal cost and the economy-wide benefit should use 3%. The firm's own payback/adoption decision correctly stays at 6%.

### 7. Per-unit lifetime NPVs are dropped undiscounted into each deployment year

`R165` / `R230` / `R292` place the full per-unit NPV (already discounted to that unit's *own* year 0) × 66.67 units into each of years 0-14, with no discounting back to 2026.

For heat pumps: model reports ₪14,792,108; discounting each cohort back to 2026 gives ₪10,152,301 -- **31% lower**. If the national program discounts these annual streams itself, the result is an NPV-of-NPVs.

This has to match whatever the grants chapter did, since both feed the same program totals. Worth checking that chapter directly rather than guessing.

### 8. Chiller lifespans were not actually equalized

You mentioned equalizing them. The file still has chiller baseline 15 / efficient 17 (`F71`/`F72`); the mismatch is instead handled by setting the analysis horizon to the *baseline* life and truncating the extra 2 years.

That's defensible on its own, but it's the **opposite** treatment from heat pumps, where the efficient life was *extended* 10 → 15. So one technology's efficient equipment gets a favourable extension and another's gets an unfavourable truncation. Worth making consistent, or documenting why they differ.

(Minor: the note explaining the chiller truncation sits on `R93`, inside the **VSD** block, where lifespans are 12/12 and there's nothing to truncate. It belongs on `R73`.)

### 9. OPEX-אחר delta is wired to the wrong scenario (latent, no effect today)

`F57`/`F77`/`F97` are labelled *"הפרש יעיל מול בסיסי"* (the efficient-minus-baseline difference) but are applied as a cost to **scenario A**, the baseline (`R118`, `R183`, `R248`), while scenario B hardcodes `0` (`R124`, `R189`, `R254`).

A positive delta means the efficient unit costs more -- so it should be charged to B/C, not A. All three values are currently 0, so there is no numerical impact. But if anyone ever enters a real maintenance delta, it will land on the wrong side and with the wrong sign.

---

## Open / incomplete (correctly flagged in the file itself)

### 10. Double-counting against the grants and loan fund chapters

`R21`/`R22` flag this as `לבירור`, and `R372` (`ייחוס התקנות מול פרק המענקים`) is empty. The grants chapter and this chapter target the same technologies; if both claim the same installations, the national program counts the savings twice.

This is a genuine unresolved question for Daniel, and it's the kind of thing that surfaces when the full program is assembled. Worth raising this week rather than leaving it as an open cell.

### 11. Demand forecast is a placeholder growing 5%/year

`R10` note: *"הועתק מהפורמט של התכנית הלאומית - לברר מאיפה לשאוב את הנתונים"*. At 5%/yr compounding, industrial demand triples (30.7M → 99M MWh by 2050), which is not a plausible forecast.

It doesn't affect the results (savings are computed bottom-up), but it does feed `R377:R382`, the post-measure demand forecast that the **next measure in the chain consumes**. Worth either sourcing it or flagging clearly that downstream chapters shouldn't rely on it.

### 12. Min and max economy-wide benefit are identical

`R352`/`R358` and `R360`/`R366` both equal `R298`. The format asks for a range (`ערך מינימום` / `ערך מקסימום`) and there isn't one. Either populate a real range (the hours sensitivity would give you one) or note that a point estimate is deliberate.

### 13. Sensitivity analyses still absent

Known and on your list. Given finding 3, hours-sensitivity for the heat pump is now load-bearing for the chapter's central claim.

---

## What checks out

- Ex-VAT tariff conversion: all six TAOZ rates divided by exactly 1.18. Correct and deliberate.
- Winter-peak 5/7 weekday fix carried through correctly from this morning.
- Depreciation schedule sums to exactly 100% of CapEx -- the last-year residual plug survived the transition.
- Payback formula logic is correct (independently replicated to 3 decimal places on all three technologies).
- Additionality gating works exactly as agreed: economic value = B−A when additional and = −fiscal cost when not; energy savings zeroed for non-additional technologies; fiscal cost reported for all three regardless.
- The per-1,000-units placeholder is now a real named parameter (`F36`), explicitly labelled as not a market estimate.
- Later-cohort truncation at 2050 is real but acknowledged in the file's own note (`R102`) and is conservative.
- No formula errors anywhere in the workbook.

---

## Status / remaining order

- [x] **1. Wire `R318`** -- done, externality savings also applied to the economy-wide benefit row.
- [x] **5. Tariff** -- resolved, industrial HV rate approved by Daniel.
- [x] **6. Discount rate** -- answered: 6% for the firm's adoption test, 3% for fiscal cost + externalities + economy-wide benefit. Fiscal cost needs its own row (can no longer be `=C−B`). Drops the total ~41%, to ~₪21.1M.
- [ ] **4. Degradation asymmetry** -- decide, then re-check the heat pump verdict (it moves 3.374 → 3.179, still additional on its own, but flips to non-additional if combined with hours back at 5,475).
- [ ] **3/13. Hours sensitivity** -- now load-bearing, since heat pump additionality sits ~12% above the threshold. Also supplies the min/max range (finding 12).
- [ ] **7. Cohort discounting** -- check what the grants chapter does before finalising, they must match.
- [ ] **2. Chapter rewrite** -- the headline changed from "only chillers" to "chillers and heat pumps," with the heat pump caveat stated plainly.
- [ ] **10. Double-counting vs. grants/loan fund** -- needs Daniel regardless of timing.

Findings 8, 9, 11 are cleanup and can ride alongside.
