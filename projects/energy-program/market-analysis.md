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

**Live, sourced Excel version:** `chiller-market-sizing.xlsx` (same folder, 5 sections) -- Section 1 has all 15 raw CBS columns entered exactly as published plus a live SUM check against CBS's own reported non-res total; Section 2 derives the chiller-relevant series and 5-year average via formulas that reference Section 1 directly; Section 3 sources RT/m² per category; Section 4 derives installed chiller capacity by category and year (weighted); Section 5 is notes/open questions. Change a raw input in Section 1 and everything downstream recalculates. Note: LibreOffice can't recalc in this sandbox (same limitation hit on 2026-07-26 with the tax model), so cached values aren't baked in -- Excel/LibreOffice on Omri's machine will compute them on open. Every formula's output was independently verified in plain Python before delivery and matches the tables below exactly.

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

### 1c. RT/m² -- SOURCED, weighted by CBS category

Decision (2026-08-03): no single blended figure -- Daniel's original scoping assumed one, but cooling-load density genuinely varies by building type (roughly 10-37 m²/RT across the sources found), so each of the 7 chiller-relevant CBS categories gets its own sourced sq ft/ton figure, weighted by that category's actual construction share each year. SI 5282 was checked and ruled out -- it's a building energy-rating standard (envelope/glazing/orientation score), not an equipment-capacity sizing standard, so it has no RT/m² figure to cite.

| CBS category | sq ft/ton | m²/RT | Source | Basis |
|---|---|---|---|---|
| Other public buildings | 400 | 37.16 | Trane (general commercial catch-all) | Proxy -- no source specific to civic/municipal buildings found |
| Health | 275 | 25.55 | HVAC-ENG.com (patient rooms & medical offices, 250-300 range midpoint) | Sourced -- matches category directly |
| Education | 213 | 19.79 | cfm Distributors (Brad Telker, VP Sales -- classrooms, stated design assumptions) | Sourced -- matches category directly |
| Industry & storage | 400 | 37.16 | Trane (general commercial catch-all) | Proxy -- CBS bundles active industrial floor with pure storage, no disaggregated source found |
| Commercial | 321 | 29.82 | cfm Distributors (retail sales floor) | Sourced -- matches category directly |
| Offices | 373 | 34.65 | cfm Distributors (office space) | Sourced -- matches category directly |
| Hotels | 362.5 | 33.68 | HVAC-ENG.com (unweighted average of public spaces 250-300 and guest rooms 400-500 midpoints) | Sourced but blended -- no floor-area split between the two sourced |

Full source links and the weakest-link discussion (the two proxy categories) are in Section 3 of the workbook and Section 5's notes.

**Open question flagged by Omri (2026-08-03):** the 400 sq ft/ton proxy makes Industry & storage the *least* cooling-intensive category of the 7 -- counterintuitive, since industrial process cooling can be far more intensive than office/retail comfort cooling. This is a real tension, not a solved question: CBS's category bundles active industrial floor space (which could need intensive process cooling) with pure storage (often not cooled at all -- roughly 45% of warehouses aren't refrigerated per one source checked). Which way the blended average actually leans depends on whether this model's "chillers" are scoped to building comfort cooling or also cover industrial process cooling -- CBS's data can't answer that. One piece of supporting evidence for the comfort-cooling-only scope: Daniel already confirmed the core tax model's 3,000 hrs/year assumption is a good one "especially for comfort chillers," which implies the model's chiller technology is comfort-scoped, and comfort-scoped industrial floor space (offices/control rooms within a factory, not the production floor) genuinely wouldn't be cooling-intensive. Not resolved -- needs a direct conversation with Daniel/Rafi on the chiller technology's actual scope before treating either direction as settled.

### 1d. Sizing calc -- BUILT (Section 4 of the workbook)

Per-category RT = (category m², thousand) x 1000 / (category m²/RT). Summed across the 7 categories = total new chiller capacity (RT) added that year.

| Year | Other public | Health | Education | Industry & storage | Commercial | Offices | Hotels | Total (RT) | Blended m²/RT (check) |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 6,808 | 5,245 | 35,779 | 26,668 | 15,660 | 33,562 | 4,573 | 128,293 | 30.17 |
| 2022 | 7,965 | 2,231 | 32,342 | 36,301 | 18,108 | 36,014 | 5,196 | 138,158 | 31.17 |
| 2023 | 11,141 | 1,761 | 31,685 | 37,432 | 16,766 | 39,044 | 6,414 | 144,243 | 31.52 |
| 2024 | 7,104 | 1,566 | 22,235 | 25,995 | 16,297 | 23,548 | 5,286 | 102,030 | 31.28 |
| 2025 | 9,418 | 8,846 | 32,747 | 29,305 | 27,597 | 16,651 | 5,761 | 130,324 | 30.00 |

**5-year average: ~128,610 RT/year installed chiller capacity from new non-residential construction.** The blended m²/RT this implies each year stays fairly stable (~30-31.5) despite the category mix shifting year to year, since Education (dense, ~19.8 m²/RT) and the two proxy categories (less dense, ~37.2 m²/RT) partly offset.

**Not yet built:** the replacement-demand sensitivity (existing stock RT / lifetime, per the model's own 15-17yr lifetime rows) -- this covers new-construction demand only, the conservative base case per the methodology doc.

---

## 2. Heat pump engine -- NOT STARTED

Sizing base: national energy balance (CBS/Ministry of Energy) industrial mazut/diesel heat use, bounded by the heat pump's low-temp ceiling (~80-90C). See methodology doc for the hard constraint reasoning.

## 3. VSD engine -- NOT STARTED

Sizing base: national industrial electricity x ~10% compressed-air-share benchmark (DOE/Radgen & Blaustein 2001), narrowed to variable-load compressors only.

---

## 4. Fiscal cost rollup -- NOT STARTED

Total fiscal cost (sum C-B row x adoption count, all 6 blocks) + chillers-only cost-effectiveness ratio (₪/tCO2, ₪/MWh). See `tracker.md` for the block schedule.
