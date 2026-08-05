# Extension Prompt: Show the TAOZ Tariff Calculation in the Live Model

Paste this into the Claude-in-Excel extension, running on the live `tax_incentive_model_v3.xlsx` (or whichever is the current working copy).

---

Daniel asked to see the calculation behind the electricity tariff figure (39.54 agorot/kWh), not just the final hardcoded number. Please build this directly in the assumptions sheet, near wherever that 39.54 value currently lives.

**What to build:**

1. A small table with the real High Voltage TAOZ rates for general IEC customers (כלל צרכנות חח"י, מתח גבוה), sourced from the Israel Electricity Authority's official tariff appendix effective 1.1.2026 ("נספח ה' - לוחות תעריפים החל מיום ה-1.1.2026", Table 5.2-1 "תעו"ז לפי רמות מתח"):

| Season | Off-peak (שפל), agorot/kWh | Peak (פסגה), agorot/kWh |
|---|---|---|
| Winter (חורף) | 30.40 | 86.28 |
| Transition (מעבר) | 29.65 | 33.04 |
| Summer (קיץ) | 33.67 | 133.13 |

Source: https://www.gov.il/BlobFolder/policy/78206/he/Files_Hachlatot_luhot_tariff_221225.pdf

2. A weighting column showing the number of hours each season/period actually covers over a year (peak hours are a small fraction of total hours, which is why the blended average lands much closer to the off-peak rates than a flat average of the 6 numbers would -- a plain unweighted average of the 6 rates above comes to ~57.7 agorot/kWh, well above the 39.54 currently in the model, confirming this has to be an hour-weighted average, not a flat one).

3. Please source or confirm the Israel Electricity Authority's own official season date ranges and peak-hour windows to build the real weights (I found summer peak = 17:00-23:00 and winter peak = 17:00-22:00 from a secondary source, but not the exact calendar boundaries for each season or the transition-season peak window -- please pull these from the primary tariff/regulation source rather than reusing my secondary-sourced figures, and confirm or correct them).

4. Build the weighted average as a live formula (SUMPRODUCT of rate x hours, divided by total hours), not a hardcoded result, so the existing 39.54 cell becomes a formula referencing this new table instead of a bare number. Every input cell (the 6 rates, the season/period hour counts) should be in its own labeled cell that the formula references, per this project's usual convention.

5. **Important: check the formula's result against the existing 39.54 figure before treating this as done.** If it lands close, that's confirmation the number was right. If it's meaningfully different, don't silently overwrite -- flag it, since 39.54 may have been sourced from a slightly different tariff table vintage or a different weighting assumption, and that discrepancy itself is worth knowing about rather than papering over.

6. Keep formatting consistent with the rest of the sheet (blue font for hardcoded inputs, black for formulas, source citations in an adjacent cell or comment).
