# Extension Prompt: Per-1,000-Units Results, All 3 Technologies

Paste this into the Claude-in-Excel extension, running on the live tax incentive model file.

---

Per the Aug 5 pivot with Daniel, real per-technology market sizing is paused. The tax chapter's results section shows savings **per 1,000 units, per technology** as a placeholder instead of a real adoption forecast. The model already computes everything per single unit (one heat pump, one chiller, one VSD) -- this is a scaling layer on top of numbers that already exist, not a new calculation.

**What to build:** extend the existing summary table (the one at the bottom of the ניתוח sheet, one row per technology with NPV/fiscal-cost/payback/verdict) with two new columns, applied to all 3 technology rows:

1. **NPV per 1,000 units** = the technology's existing "עלות פיסקלית של התמריץ למדינה" value (the C−B row in that technology's block) × 1,000.
2. **MWh saved per 1,000 units** = (baseline annual consumption − efficient annual consumption, in kWh, from the assumptions sheet section 4 for that technology) × 1,000, converted to MWh.

**Two things to flag directly in the sheet, not just note here -- both need a real cell comment or adjacent note, since they'll look like mistakes to anyone reviewing without context:**

- **"NPV per 1,000 units" and "fiscal cost per 1,000 units" will be the identical number**, because both reference the same C−B row. This isn't a duplicate-by-accident -- the model's own timing-cost design (2026-07-22) means the firm's incentive-derived benefit and the state's fiscal cost are the same figure once both are discounted at one shared rate. Reference the same source cell for both rather than computing it twice. This still needs to be raised with Daniel as a chapter-presentation question (is reporting the same number under two labels the right way to show this, or should the chapter only carry one of the two labels).
- **"MWh saved per 1,000 units" will be numerically identical to "kWh saved per single unit."** kWh-per-unit × 1,000 units ÷ 1,000 (kWh→MWh conversion) cancels out. Not a formula error -- flag it with a note so it doesn't get "corrected" later by someone who doesn't spot the coincidence.

**Deliberately NOT in scope for this pass:** tCO2e saved. That needs a grid emissions factor to convert MWh → tCO2, which hasn't been sourced here and is exactly what the national program model format already carries built in (per today's plan to transition into that format next). Building a standalone emissions-factor conversion now would be sourcing work that gets thrown away once the transition happens. Leave a placeholder column header ("tCO2e saved -- ל-1,000 יחידות") with no formula and a note that it's pending the format transition, so the table's final shape is visible even though the column is empty for now.

**Formatting:** live formulas referencing the existing per-unit cells (not hardcoded results), consistent with the rest of the sheet -- black font for formulas, source note/comment on both flagged cells per above. Match the existing summary table's column styling.
