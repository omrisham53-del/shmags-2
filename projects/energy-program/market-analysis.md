# Tax Incentive Chapter -- Market Analysis Data

Working file for the market-sizing engines (chillers / heat pumps / VSD). Methodology: `brainstorms/2026-07-22_tax-incentive-market-analysis.md`. Feeds the tax incentive chapter's results section; numbers here get multiplied by the model's per-unit results (NPV, MWh saved, tCO2 saved, fiscal cost) to produce market-level totals.

---

## 1. Chiller engine

### 1a. Non-residential construction starts (CBS, last 5 years) -- SOURCED

**Source:** Israel CBS (הלשכה המרכזית לסטטיסטיקה), "התחלות וגמר בנייה -- סיכום שנת 2025" (Construction Begun and Completed in 2025), publication 089/2026, released 19/03/2026. Table 7 -- "שטח בנייה, לפי ייעוד ושלב בנייה" (Construction area, by purpose and construction stage), CONSTRUCTION BEGUN (התחלות בנייה) section.
https://www.cbs.gov.il/he/mediarelease/DocLib/2026/089/04_26_089b.pdf (media release) + companion table https://www.cbs.gov.il/he/mediarelease/DocLib/2026/089/04_26_089t7.xls

Units: thousand m². Real CBS categories, annual, 2021-2025:

| Year | Agriculture | Other public bldgs | Health | Education | Industry & storage | Transport & comms | Commercial | Offices | Hotels | Non-res total | Residential | Grand total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 309 | 253 | 134 | 708 | 991 | 203 | 467 | 1,163 | 154 | 4,383 | 12,120 | 16,503 |
| 2022 | 161 | 296 | 57 | 640 | 1,349 | 229 | 540 | 1,248 | 175 | 4,697 | 12,901 | 17,598 |
| 2023 | 241 | 414 | 45 | 627 | 1,391 | 388 | 500 | 1,353 | 216 | 5,175 | 12,206 | 17,381 |
| 2024 | 206 | 264 | 40 | 440 | 966 | 151 | 486 | 816 | 178 | 3,549 | 12,971 | 16,520 |
| 2025 | 283 | 350 | 226 | 648 | 1,089 | 154 | 823 | 577 | 194 | 4,347 | 14,972 | 19,319 |

Non-res total = sum of the 9 category columns (CBS's own definition, confirmed by re-summing).

**Live, sourced Excel version:** `chiller-market-sizing.xlsx` (same folder) -- Section 1 has all 15 raw CBS columns entered exactly as published plus a live SUM check against CBS's own reported non-res total; Section 2 derives the chiller-relevant series and 5-year average via formulas that reference Section 1 directly (change a raw input, the derived numbers recalculate). Note: LibreOffice can't recalc in this sandbox (same limitation hit on 2026-07-26 with the tax model), so cached values aren't baked in -- Excel/LibreOffice on Omri's machine will compute them on open. Every formula's output was independently verified in plain Python before delivery and matches the table below exactly.

### 1b. Chiller-relevant construction starts (derived)

Per the methodology's own category list (offices, commercial, hotels, institutional, industry -- explicitly excludes agriculture and infrastructure), chiller-relevant floor area = **non-res total minus Agriculture minus Transport & communications**. Agriculture (barns, greenhouses, farm structures) and transport/communications infrastructure don't carry comfort-cooling loads the way office/commercial/institutional/industrial floor area does.

| Year | Chiller-relevant (thousand m²) | Calculation |
|---|---|---|
| 2021 | 3,871 | 4,383 - 309 - 203 |
| 2022 | 4,307 | 4,697 - 161 - 229 |
| 2023 | 4,546 | 5,175 - 241 - 388 |
| 2024 | 3,192 | 3,549 - 206 - 151 |
| 2025 | 3,910 | 4,347 - 283 - 154 |

**5-year average: ~3,965 thousand m²/year (~3.97M m²/year).** No strong trend either direction (2023 peak at 4.55M, 2024 trough at 3.19M -- likely war-related construction-sector disruption per the same CBS release's own commentary on labor/activity constraints since Oct 2023). Flat 5-year average is a defensible, simple growth parameter -- a fitted trend line would be noisy given the 2023-2024 swing and isn't obviously better than a flat average for a policy-horizon projection.

**OPEN QUESTION for Daniel:** should "industry & storage" be split (only the "industry" portion needs comfort/process cooling; pure storage/warehousing often doesn't)? CBS's own category bundles them together with no further breakdown available at this level -- would need a different data source to split it. Flagging as a methodology call rather than guessing a split.

### 1c. RT/m² -- NOT YET SOURCED

Next step: pull a real cooling-load-density figure (ASHRAE rule-of-thumb or Israeli standard SI 5282) to convert m² -> installed cooling capacity (RT). Needs to vary by building type ideally (office vs. industrial cooling-load density differs a lot) -- or a single blended figure if a type-specific breakdown isn't available/practical.

### 1d. Sizing calc -- NOT YET BUILT

Once RT/m² is sourced: chiller-relevant m²/year x RT/m² -> installed cooling capacity added per year. Plus the replacement-demand sensitivity (existing stock RT / lifetime, per the model's own 15-17yr lifetime rows).

---

## 2. Heat pump engine -- NOT STARTED

Sizing base: national energy balance (CBS/Ministry of Energy) industrial mazut/diesel heat use, bounded by the heat pump's low-temp ceiling (~80-90C). See methodology doc for the hard constraint reasoning.

## 3. VSD engine -- NOT STARTED

Sizing base: national industrial electricity x ~10% compressed-air-share benchmark (DOE/Radgen & Blaustein 2001), narrowed to variable-load compressors only.

---

## 4. Fiscal cost rollup -- NOT STARTED

Total fiscal cost (sum C-B row x adoption count, all 6 blocks) + chillers-only cost-effectiveness ratio (₪/tCO2, ₪/MWh). See `tracker.md` for the block schedule.
