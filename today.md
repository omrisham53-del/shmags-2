# Today - June 2, 2026

**Date:** 2026-06-02
**Updated:** 2026-06-02

---

## Current Priority

- Energy program: review `capex_all_rounds.csv` in Excel, compute AVERAGEIF per tech → 4 model CapEx numbers
- Job search: follow up on active applications
- University: monitor HW #2 and HW #3 grades

---

## Today's Completed

*(nothing yet)*

---

## Recent Work (May 31 - June 1)

**May 31 (work PC):**
1. **Meeting with Daniel** - Finished first version of grant analysis and chapter. Tax incentive analysis still needed.
2. **Tax incentive model v1-v3** - Built Excel model (7 sheets) with NPV/ROI for 4 technologies (heat pumps, chillers, VSD compressors, electric steam). Iterated to v2 (multiplier, degradation, 2-sheet structure) and v3 (3-scenario comparison with OPEX and incremental CapEx). Removed absolute payback rows (NPV stays negative). Consolidated tech assumptions to Sheet 1.

**June 1 (work PC):**
1. **CapEx pipeline built** - Python extraction script for grant request Excel files. Handles 2017-era format and newer "אתר 1/2/3" format.
2. **All 5 rounds extracted** - 2017/2018/2019/2020/2022 ran clean. 686 line items total.
3. **Master CSV created** - `capex_all_rounds.csv` (686 rows) in מענקים folder, ready for Excel review.
4. **Daniel's feedback logged** - Tax incentive model review notes saved to decisions log.

---

## Pending — Needs Rafi's Data

- CapEx per technology (₪)
- Annual energy consumption per technology (kWh/year)
- Equipment degradation rate (%/year)

## Pending — Needs Daniel's Decision

- Discount rate: 6% (social/national) vs 10% (private/industrial)

---

## This Week's Focus

1. **Energy Program** - Review `capex_all_rounds.csv` in Excel: filter junk rows, verify technology tags, compute AVERAGEIF per tech → 4 model CapEx numbers
2. **Job Search** - Follow up on active applications (Primis, Mobileye, Realplay, Nexxen)
3. **University** - Monitor HW #2 and HW #3 grades

## Active Applications

- **Primis** (Junior Business Analyst) - Applied 2026-05-24, awaiting response
- **Nexxen** (Junior Revenue Operations Manager) - Applied 2026-05-27, messaged Itamar Bilu on LinkedIn
- **Realplay** (Business Strategy Analyst) - Applied 2026-05-28, awaiting response
- **Mobileye** (Global Share Plans Analyst) - Applied 2026-05-31, awaiting response

---

## Next Session: Energy Program

1. Run gut-check on classification before filtering:
```powershell
$dest = "C:\Users\OmriShamgar\EcoTraders Ltd\Communication site - מסמכים\Data\משרד האנרגיה\אגף אנרגיה מקיימת\תכנית לאומית להתייעלות אנרגטית\תכנית 2025\אמצעי מדיניות\תוכניות מענקים\מענקים\capex_all_rounds.csv"
Import-Csv $dest | Group-Object suggested_technology | Select-Object Name, Count | Sort-Object Count -Descending
```
2. If classification looks off, tune keywords before manual review
3. Filter master CSV in Excel → AVERAGEIF per technology → model inputs

---

## Quick Links

**Work Projects:**
- [Energy Program](projects/energy-program/)
- [Job Search](projects/job-search/)
- [University](projects/university/)
- [D&D Campaign](projects/dnd-campaign/)

**Workflows & References:**
- [Daily Routine](routine.md)
- [Assignment Tracker](projects/university/tracker.md)
- [Current Priorities](context/current-priorities.md)
- [Job Tracker](projects/job-search/tracker.md)
