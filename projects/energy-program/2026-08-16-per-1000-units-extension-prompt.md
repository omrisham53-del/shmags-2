# Extension Prompt: Per-1,000-Units Results, All 3 Technologies

Paste this into the Claude-in-Excel extension, running on the live tax incentive model file.

---

Per the Aug 5 pivot with Daniel, real per-technology market sizing is paused. The tax chapter's results section shows savings **per 1,000 units, per technology** as a placeholder instead of a real adoption forecast. The model already computes everything per single unit (one heat pump, one chiller, one VSD) -- this is a scaling layer on top of numbers that already exist, not a new calculation.

**Core principle governing every column below:** the incentive only gets credit for impact it actually caused. A technology's verdict cell (already in the model, "הכרעה — מבחן סף החזר ההשקעה") tells you which case applies:
- **"התמריץ הפך את ההחלטה"** (the incentive flipped the decision) -- additionality confirmed. The firm would NOT have invested without the incentive, so the full value of the switch is attributable to the policy.
- **"כדאי גם ללא תמריץ"** (worth it without the incentive) -- deadweight. The firm invests regardless; the incentive changes nothing about the investment, it just hands the firm a tax-timing benefit it would have gotten from the same equipment purchase either way.

This distinction gates every column except fiscal cost.

**What to build:** extend the existing summary table (bottom of the ניתוח sheet, one row per technology with NPV/fiscal-cost/payback/verdict) with these columns, applied to all 3 technology rows:

1. **Fiscal cost per 1,000 units** = the technology's existing "עלות פיסקלית של התמריץ למדינה" row (C−B) × 1,000. **Always computed, for all 3 technologies, additionality or not.** A rational firm that's already buying the efficient equipment claims the accelerated-depreciation election too, since it's strictly better than standard depreciation with no downside -- so the state pays this out regardless of whether the incentive changed the investment decision. That's exactly what makes deadweight cases "deadweight": real money spent, no behavior change bought.

2. **Economic value per 1,000 units** -- a single column whose formula depends on the verdict:
   - If additionality ("התמריץ הפך את ההחלטה"): `= (C−A row − C−B row) × 1,000`. Algebraically this equals (B−A) × 1,000 -- the pure resource/efficiency gain from switching technology, net of the government-to-firm transfer. That's the real number, not the gross C−A figure, because C−A double-counts the transfer that fiscal cost already accounts for separately.
   - If NOT additionality ("כדאי גם ללא תמריץ"): `= the same fiscal cost figure from column 1`. There's no efficiency gain to attribute to the policy here (the firm switches either way), so the only real economic consequence of the incentive existing is the money it costs the state -- reported as the "economic value" for this row specifically to keep the column meaningful without a second column, per Omri's call. **Add a cell comment on this column's header explaining the dual meaning** (net welfare gain when additionality holds, pure cost when it doesn't) -- a reader skimming numbers without checking the adjacent verdict column would otherwise misread a deadweight technology's entry as a benefit.

3. **MWh saved per 1,000 units** -- gated the same way as economic value:
   - If additionality: `= (baseline annual consumption − efficient annual consumption, kWh, from assumptions sheet section 4) × 1,000`, converted to MWh.
   - If NOT additionality: leave blank or "-- (לא תוסף, החלטה לא השתנתה)" -- the energy savings happen regardless of the policy, so crediting them to the incentive would overclaim, same logic already used for chillers-only cost-effectiveness in the 2026-07-26 decision.

**One thing to flag directly in the sheet, not just note here -- needs a real cell comment, since it'll look like a mistake to anyone reviewing without context:**

- **Where MWh saved IS shown, it'll be numerically identical to "kWh saved per single unit."** kWh-per-unit × 1,000 units ÷ 1,000 (kWh→MWh conversion) cancels out. Not a formula error.

**Deliberately NOT in scope for this pass:** tCO2e saved. That needs a grid emissions factor to convert MWh → tCO2, which hasn't been sourced here and is exactly what the national program model format already carries built in (per today's plan to transition into that format next). Building a standalone emissions-factor conversion now would be sourcing work that gets thrown away once the transition happens. Leave a placeholder column header ("tCO2e saved -- ל-1,000 יחידות") with no formula and a note that it's pending the format transition, so the table's final shape is visible even though the column is empty for now.

**Formatting:** live formulas referencing the existing per-unit cells (not hardcoded results), consistent with the rest of the sheet -- black font for formulas, source note/comment on the flagged cells per above. Match the existing summary table's column styling.
