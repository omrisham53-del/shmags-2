# Notes — Final LCA Assignment (Comparative EPD Analysis, Ready-Mix Concrete)

Topic: Ready-mix concrete. PCR 2019:14 (Construction products) + c-PCR-003 (Concrete and concrete elements, EN 16757). Comparing Interbeton Building Materials S.A. (Greece) vs. JSW Green Cement Pvt Ltd (India). Not the same company — confirmed different owners (TITAN Group subsidiary vs. JSW Group subsidiary).

## PCR (c-PCR-003 v1.0.0, 2025-04-08)

Thin complementary document — most substantive rules (functional/declared unit, system boundary, LCI/LCIA, data quality, allocation, cut-off, databases) are not set independently but say "As in PCR 2019:14 and EN 16757:2022." c-PCR-003 itself only adds: product scope definition (UN CPC 375, excludes autoclaved aerated concrete) and standards conformance (EN 16757:2022). Valid until 2030-04-07.

Both EPDs actually cite an EARLIER version of the concrete c-PCR than the one downloaded:
- Interbeton cites "c-PCR-003 Concrete and concrete elements (EN 16757); Version 2019-12-20"
- JSW cites "'Sub-PCR-G Concrete and concrete elements'" (no version number given) — same underlying document, different internal label used by JSW's report author
- Both cite the SAME core PCR version: PCR 2019:14 Construction products (EN 15804:A2), Version 1.11, 2021-02-05

## General / administrative comparison

| | Interbeton (Greece) | JSW (India) |
|---|---|---|
| EPD number | S-P-05027 | S-P-06471 |
| Published / valid until | 2021-12-16 / 2026-12-15 | 2022-11-01 / 2027-10-31 |
| Product | Ready-mix concrete, C12/15 (15 MPa) | Ready-mix concrete, grades M-7.5 to M-60 (11 grades, volume-weighted) |
| Verifier | Eurocert S.A. (accredited by E.SY.D.) | Dr. Hüdai Kara, Metsims Sustainability Consulting (independent individual, approved by the International EPD System) |
| Geographic scope | National (Greece), 29 ready-mix plants | India (Dolvi, Vijaynagar, Deonar plants) |
| LCA software / database | GCCA Industry EPD Tool for Cement and Concrete v3.1 (built on Ecoinvent v3.5) | GaBi 10.5 (Sphera), GaBi professional database |
| Data collection window | Aug 2020 – Jul 2021 | Apr 2021 – Mar 2022 |
| Declared/functional unit | 1 m³ (declared unit) | 1 m³ (declared unit) — SAME |
| Reference service life | 50 years, explicitly stated | Not stated (consistent with declaring no B-stage) |

## System boundary — the key comparability finding

Interbeton: full cradle-to-grave, A1-A5, B1-B7, C1-C4, D all declared "X" (all modules included, not MND). Notably includes a B1 carbonation credit (negative GWP contribution during use, per c-PCR methodology) and models C3 (50% recycled) / C4 (50% landfilled) end-of-life split.

JSW: nominally also called "Cradle-to-Grave" in prose (section 3.2), but the actual declared-modules table (Table 4-6) shows A5 = MND and ALL of B1-B7 = MND. Declared modules are really only A1-A4 + C1-C4 + D. No use-stage modeling, no installation stage, no reference service life needed because there's nothing being used/maintained/replaced in the declared scope.

**This is the central methodological gap**: both cite the identical parent PCR version (1.11, 2021-02-05) and the same concrete-specific c-PCR, yet declare materially different system boundaries. A naive "cradle-to-grave total" comparison between the two EPDs would not be comparing like with like — Interbeton's total includes an entire use-stage credit and installation-stage impacts that JSW's total structurally cannot include.

## Data quality / methodology

- Allocation: neither EPD needed allocation (no co-products in either case) — same treatment.
- Cut-off: both apply ~1% mass/energy cut-off consistent with EN 15804; JSW states it includes flows even under 1% "as all these were environmentally relevant" — marginally more conservative/inclusive in stated intent, though both ultimately rely on Ecoinvent/GaBi default cut-off rules for background processes.
- LCIA indicator set: identical — both report the full EN 15804:2012+A2:2019 core indicator set (GWP-total/fossil/biogenic/luluc, ODP, AP, EP-freshwater/marine/terrestrial, POCP, ADP-minerals&metals, ADP-fossil, WDP) plus the same resource-use and waste-category parameters. Same method, same units, same acronyms in both documents — this part of the PCR is doing its job.
- LCA software/database differ (GCCA/Ecoinvent v3.5 vs. GaBi/Sphera database) — a real, underlying driver of numeric differences even where methodology matches.
- Transparency: Interbeton documents module-by-module transport distances, fuel assumptions, per-plant variance (±10%), and a full "Product Data Sources" table with per-flow data quality ratings (High/Medium/Proxy-Medium). JSW's methodology section is comparatively more generic/templated (declares "first-hand industry data... combination with consistent upstream LCA information" without a matching itemized sourcing table). Interbeton is the more transparent of the two.

## Impact category results — best available matched comparison

Interbeton's declared product is C12/15 (15 MPa / ~C15 strength class). JSW's EPD covers 11 grades from M-7.5 to M-60; the closest strength match with a full results table is **M-20** (in the Annexure, ~20 MPa, closest to C12/15's 15 MPa of the fully-tabulated grades — M-15 exists in production-volume terms but has no full LCIA table in the base document).

A1–A3 (product stage, "cradle to gate" — the most robust comparison point since it's unaffected by the system-boundary gap above):

| Indicator | Unit | Interbeton C12/15 (representative plant) | JSW M-20 |
|---|---|---|---|
| GWP-total | kg CO2 eq | 147–162 (range across the 2 representative-plant groups reported) | 166 |
| Acidification (AP) | Mole H+ eq | 0.347–0.384 | 0.605 |
| Eutrophication, freshwater (EP-fw, as kg P eq) | kg P eq | 0.0100–0.0107 | 0.0000487 |
| Water use (WDP) | m³ world equiv. | 98.7–99.7 | 7.32 |

Observations:
- GWP-total lands within ~2–13% of each other despite different countries, tech, and LCA software — a genuinely close result given how different the two supply chains are.
- Acidification is ~50-75% higher for JSW despite similar GWP — a real hotspot shift, not just a rounding difference (JSW's own interpretation table attributes AP mostly to cement, similar attribution logic to Interbeton, so this reflects the underlying cement/fuel/grid emission factors used in each background database, not a different formula).
- Freshwater eutrophication differs by roughly 200x (Interbeton higher) — too large a gap to read as a real environmental difference; more likely reflects how differently Ecoinvent (Europe-centric) and the GaBi/Sphera India-adapted database model phosphorus-related emissions in fertilizer/mining background processes. Flagged as a comparability limitation, not a genuine performance difference.
- Water use (deprivation-weighted, WDP/AWARE-based) is ~13x higher for Interbeton — plausibly reflects real regional water-scarcity weighting (Mediterranean Greece vs. the JSW plant regions), since WDP is scarcity-weighted per m³, not a raw volume metric.

## Interbeton's own interpretation table (A1-A3 hotspots, C12/15-equivalent M-7.5-ish products in JSW's own table)

Interbeton GWP A1-A3: cement contributes ~70%, aggregate ~16%.
JSW M-20/M-25 GWP A1-A3: cement contributes ~69-70%, aggregate ~16% — nearly identical hotspot attribution despite different absolute values. Strong internal consistency signal that both LCAs are capturing the same real-world physics (cement/clinker is the dominant driver in both), even though the underlying background databases differ.

## Answers to the brief's PCR evaluation-criteria table (Section 2.2)

Since c-PCR-003 itself defers nearly everything to PCR 2019:14 (which was not separately downloaded — out of scope per Omri's minimum-research-effort instruction), these answers are built from what c-PCR-003 states directly plus what is actually declared/applied identically in both EPDs (which is the practical, EPD-level evidence of how the PCR's requirements were implemented):

- Functional/declared unit: declared unit, 1 m³ — explicit in c-PCR-003 Figure 2 (PCR 2019:14 without a c-PCR is declared-unit-only; the concrete c-PCR does not override this).
- System boundary definition: not fixed by the c-PCR itself ("as in PCR 2019:14") — hence EPD authors can legitimately choose different module sets, which is exactly what happened.
- Reference service life: not mandated by c-PCR-003; Interbeton states 50 years, JSW states none.
- Data quality requirements: not spelled out in c-PCR-003; both EPDs separately state ISO 14044 data-quality assessment was applied, with primary data from company ERP/production systems and generic secondary data from Ecoinvent/GaBi.
- Recommended databases: not specified by c-PCR-003; each EPD author chose their own (Ecoinvent v3.5 via GCCA tool; GaBi 10.5 database).
- Allocation rules: not specified by c-PCR-003 beyond "as in PCR 2019:14"; both EPDs state no allocation needed.
- Cut-off criteria: not specified by c-PCR-003; both apply ~1% cut-off consistent with EN 15804 general practice.
- Impact categories: not specified by c-PCR-003 directly, but both EPDs report the full EN 15804:2012+A2:2019 core set identically — this consistency actually comes from EN 15804 itself (the core standard both the PCR and c-PCR sit on top of), not from c-PCR-003's own text.
- EPD reporting format: c-PCR-003 Section 5 says "as in PCR 2019:14 and EN 16757:2022" — both EPDs follow a near-identical modular A-D table layout, consistent with a shared reporting template.
- Consistency with ISO/GPI: both EPDs explicitly cite ISO 14025:2006 and (JSW additionally) ISO 14040/44; c-PCR-003 explicitly sits under EN 15804/ISO 21930 per its own hierarchy diagram (Figure 1).

## For section 4.7 (recommended improvements to this EPD comparison)

- Recommend both EPDs disclose full raw LCI flows (or at least a harmonized mid-point comparison table for A1-A3 only), since A1-A3 is the only truly like-for-like basis given the system-boundary gap.
- Recommend the c-PCR be strengthened to mandate a minimum declared module set (e.g., require A1-A5 as a floor) rather than leaving system boundary entirely to "as in PCR 2019:14," which is what allowed this exact divergence.
- Recommend both EPDs disclose background database version/region-adaptation explicitly against a shared reference (e.g., both reporting the same fraction of impact from grid electricity vs. process heat) to make the large freshwater-eutrophication gap interpretable rather than opaque.
