# Today - June 1, 2026

**Date:** 2026-06-01
**Updated:** 2026-06-01

---

## Current Priority

- Energy program: CapEx pipeline complete, review master CSV in Excel
- Job search: active applications need follow-up

---

## Today's Completed ✅

1. **CapEx pipeline: 2017 format support** - Root cause of 0 matches found and fixed. 2017-era files use "1. פרטים כלליים ועלויות" sheet (flat table) vs newer "אתר 1/2/3" format. Both now supported.
2. **Pipeline simplified to Option A** - Single output: `capex_lineitems.csv` only. No auto-averaging. User filters in Excel + AVERAGEIF for model numbers.
3. **All 5 rounds extracted** - 2017/2018/2019/2020/2022 ran clean. 127/253 selected requests matched, 686 line items total.
4. **Master CSV created** - `capex_all_rounds.csv` (686 rows) in מענקים folder, ready for Excel review.

---

## This Week's Focus

1. **Energy Program** - Review `capex_all_rounds.csv` in Excel: filter junk rows, verify technology tags, compute AVERAGEIF per tech → 4 model CapEx numbers
2. **Job Search** - Follow up on active applications (Primis, Mobileye, Realplay, Nexxen)
3. **University** - Monitor HW #2 and HW #3 grades

## Active Applications

- **Primis** (Junior Business Analyst) - Applied 2026-05-24, awaiting response
- **Mobileye** (Global Share Plans Analyst) - Applied 2026-05-31, awaiting response
- **Realplay** (Business Strategy Analyst) - Applied 2026-05-28, awaiting response
- **Nexxen** (Junior Revenue Operations Manager) - Applied 2026-05-27, awaiting response

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
