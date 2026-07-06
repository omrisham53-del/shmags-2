# Today - 2026-07-05

**Date:** 2026-07-05
**Updated:** 2026-07-05

---

## Current Priority

- Economics final paper (with Tomer): paste full paper into Word, convert in-text citations to footnotes, assemble with charts, submit
- Energy program: review `capex_all_rounds.csv` in Excel, compute AVERAGEIF per tech → 4 model CapEx numbers
- Job search: follow up on active applications

---

## Today's Completed

1. **Improvers Club — July annotated game submission written** - Set up Stockfish (C:\Users\User\OneDrive\Documents\stockfish\) + python-chess for local engine analysis. Analyzed two candidate games at depth 18. Selected game vs. gannu8709049607 (July 1, Re1# back-rank mate). Hook: 4 consecutive engine-best moves (23...Bxd4, 24...Rxc2, 25...Rxe2, 26...Bxb1) converting a won position after a queen/rook fork on move 16. Full written annotation + PGN with embedded comments ready. To submit: import PGN to chess.com/analysis, save as public study, post study link + annotation text to club forum, paste #comment- permalink into the form.

2. **Ronni's psychobiology assignment review** - Read all 4 source articles (Bojesen 2026, Jauhar 2018, Wulff 2015, Kegeles 2010) + assignment brief + tips doc. Extracted text from the submitted .docx via Word COM. Generated full Hebrew review report covering: science accuracy per article, 3 missing bibliography entries (Carlsson 2006, Lieberman 1993, Howes et al. 2009), citation formatting errors throughout (first initials in in-text citations, missing commas, Staufer/Stauffer misspelling), figure references that need replacing with text descriptions, integration paragraph word count flag, and science precision notes on GABA-K3 in AN-FEP and the Kegeles causal reversal claim. Assignment folder: `C:\עמרי ורוני\לימודים\מטלת הכירו את המדע\`.
---

## Recent Work (July 1)

1. **September Europe trip — route and destination planning** - Locked core 3-month route: Norway → Scotland → London → Ireland → Portugal (Sept 8 - ~Dec 8). Built out conceptual frameworks for each leg: Norway (DNT huts, Jotunheimen, allemannsretten), Scotland (West Highland Way, Glasgow/Edinburgh), Ireland (Galway/Connemara, west coast surf, trad sessions), Portugal (Rota Vicentina, Peniche/Sagres surf, Porto/Lisbon). Discussed and set aside flex destinations (Iceland, Faroe Islands, Basque Country, Galicia, Azores). Next: consult with family member on Norway specifics, then plan each leg in more detail.

2. **Repo audit — pruned dead weight** - Reviewed the whole second-brain structure. Archived three abandoned systems to `archives/deprecated-2026-07-01/` (nothing deleted): the daily dashboard automation (stopped running May 31), the Cowork surface (COWORK.md + sessions/ + templates/, still referencing deleted status/next-steps files), and the unused "Routine creator" project. Fixed CLAUDE.md folder map + scripts/README to match; deleted the dead `daily_dashboard_system` memory. Committed + pushed.

3. **Built /weekly-review + scheduled it as a Friday cloud routine** - New command at `.claude/commands/weekly-review.md` is the anti-cruft ritual (reconcile today.md, deadline radar, stale-application flags, stale-automation sweep). Set it to run automatically every Friday 10:00 AM Israel via a scheduled cloud routine (first run July 3). Cloud run is repo-only + non-interactive: auto-reconciles today.md and writes a report to `reviews/weekly-review-YYYY-MM-DD.md`, but does NOT archive cruft on its own. Manage at https://claude.ai/code/routines/trig_013e68sBVgyjkdU3UwfBXCR1.

---

## Recent Work (June 25)

1. **Economics paper — chart 07 built (net savings chart)** - Created new PUE net savings chart showing TCO savings vs PUE 2.2 baseline for all 3 alternatives. Optimal PUE = 1.4 for all alternatives. Peak savings: ₪392M (Alt 0), ₪259M (Alt 1), ₪152M (Alt 2). Script at `Economics Final\charts\build_chart_07.py`.

2. **Economics paper — chart 03 updated** - New title "מקורות האנרגיה: רשת לאומית וייצור עצמי לפי חלופה"; added right-side bracket annotation grouping gas + solar as "ייצור עצמי" with combined %; bars repositioned for spacing.

3. **Economics paper — sensitivity analysis paragraph written** - Hebrew paragraph for section 4.4 explaining PUE sensitivity analysis and optimal PUE finding.

4. **PwC 2025 citation identified** - Found source of US data center GDP contribution figures ($355B in 2017 → $727B in 2023): PwC report commissioned by Data Center Coalition (Feb 2025). In-text citation should be (PwC, 2025) not (WEF, 2025). Full APA citation provided.

---

## Recent Work (June 22)

1. **Repo housekeeping** - Git pull from work PC brought in world-cup-party files (guest + host HTML + vercel.json). Moved HTML files to projects/world-cup-party/, updated vercel.json routes to match. Root stays clean, Vercel URLs unchanged.

2. **Economics seminar paper — full paper written** - Completed the entire 7-section Hebrew paper (per Prof. Lifshitz's PPTX structure). Sections 1-3 (תקציר, הקדמה, סקירת ספרות) written in prior session; sections 4-8 (ניתוח, סיכום, המלצות, ביבליוגרפיה, נספחים) completed this session. In-text (author, year) citations throughout. Charts 01-05 placed: [איור 3] in 4.2, [איורים 1, 2, 4] in 4.3, [איור 5] in 4.4. Chart 06 excluded. Next: Tomer pastes into Word, converts citations to footnotes, assembles final doc.

3. **Upstart program email sent to Ofir** - Explained missed sessions, team presenting without Omri, requested personal assignment option or withdrawal. CC'd Naor (academic instructor). Ofir replied warmly: "need to check what we can do, will update soon." No action needed — awaiting his decision.

4. **Urban Analytics final assignment — reviewed + docs fixed + presentation guide written** - Reviewed all deliverables for Monday's presentation. Regenerated Backup_Memo_v2.docx (clean formatting: Times New Roman 12, 1.15 spacing, proper bold/italic, no markdown artifacts) with all 6 figures embedded. Regenerated Policy_Report_Clean.docx. Removed analysis/eda.py references. Verified all 5 open datasets and both academic articles (Sallis 2016, Oja 2011) exist. Wrote full presentation script as Presentation_Guide.md in the final assignment folder for tomorrow's review with Yonatan. Still pending: convert docs to PDF, get poster from Yonatan, confirm who-did-what split.

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
