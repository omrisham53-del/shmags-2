# Today - 2026-07-10

**Date:** 2026-07-10
**Updated:** 2026-07-10

---

## Current Priority

- Economics final paper (with Tomer): paste full paper into Word, convert in-text citations to footnotes, assemble with charts, submit
- Energy program: gather baseline data for the COMPARISON systems (less efficient/conventional baselines -- e.g. standard boilers, fixed-speed compressors, standard chillers, conventional heat sources) to pair with the efficient-system data already built in `baseline-technology-data.md`
- Job search: follow up on active applications

---

## Today's Completed

(nothing yet)

---

## Recent Work (July 8)

1. **"Through the Gap" newsletter launched (Skill 6 project)** - Brainstormed passion-first income streams for the trip; landed on football economics + inequality as the niche (deepest knowledge + economics background + visual data journalism format). Name: Through the Gap. Platform: Substack (signup in progress, free tier first). First article drafted: "The £116 Million Illusion" - the Anderson £116m transfer as a lens on Forest's PSR survival-selling, the SCR flat-tax problem (85% of unequal revenues = permanent gap), and the private votes (SCR passed 14-6, anchoring killed 12-7). Draft + 5 chart specs + verify-before-publish list at `projects/through-the-gap/articles/2026-07-07_the-116-million-illusion.md`; reusable 9-step article workflow in the project README. Next: finish Substack setup, fact-check pass, build charts in Python.

2. **Git sync + EcoTraders notice outcome logged** - Merged two work-PC branches to master (resolved decisions/log.md conflict), pushed. Logged meeting outcome: Daniel accepted politely, last day Aug 22, no handoff plan discussed. Saved ecotraders-exit memory.

---

## Recent Work (July 6)

1. **Economics seminar POSTER — design direction locked + built via Claude Design MCP** - Iterated the distinction-prize poster through several concepts (electricity bill → thermal map → editorial charts → Economist cover) before landing on an Economist-style cover with a hand-drawn ISOMETRIC bird's-eye illustration (warm terracotta field, Frank Ruhl Libre + Assistant). Corrected the core message: NOT "efficiency beats the source" but "energy independence is most beneficial" — a data center on its own solar + efficient gas plant pays ~54% less for power (Alt 2, ₪0.172 vs ₪0.373/kWh), with PUE efficiency (~25%) as the complementary lever. Workflow: illustration generated in Claude Design, Hebrew text/layout authored in code and pushed back via the DesignSync MCP. Files in the "Israel's Overheating Grid" Claude Design project + local mirror at `Economics Final\Poster\design\`; final assembly = `Poster - Final.dc.html`. Still open: polish the illustration (grey cooling units density, tile fit), optionally sync fixes to standalone Isometric Campus, then export print-ready 50×70 PDF.

2. **Improvers Club — July annotated game submission written** - Set up Stockfish (C:\Users\User\OneDrive\Documents\stockfish\) + python-chess for local engine analysis. Analyzed two candidate games at depth 18. Selected game vs. gannu8709049607 (July 1, Re1# back-rank mate). Hook: 4 consecutive engine-best moves (23...Bxd4, 24...Rxc2, 25...Rxe2, 26...Bxb1) converting a won position after a queen/rook fork on move 16. Full written annotation + PGN with embedded comments ready. To submit: import PGN to chess.com/analysis, save as public study, post study link + annotation text to club forum, paste #comment- permalink into the form.

2. **Ronni's psychobiology assignment review** - Read all 4 source articles (Bojesen 2026, Jauhar 2018, Wulff 2015, Kegeles 2010) + assignment brief + tips doc. Extracted text from the submitted .docx via Word COM. Generated full Hebrew review report covering: science accuracy per article, 3 missing bibliography entries (Carlsson 2006, Lieberman 1993, Howes et al. 2009), citation formatting errors throughout (first initials in in-text citations, missing commas, Staufer/Stauffer misspelling), figure references that need replacing with text descriptions, integration paragraph word count flag, and science precision notes on GABA-K3 in AN-FEP and the Kegeles causal reversal claim. Assignment folder: `C:\עמרי ורוני\לימודים\מטלת הכירו את המדע\`.

3. **Energy Program — tax incentive baseline data built, key finding on electric steam** - Per Daniel's 3-step unblocking process, gathered baseline data (2 capacity points, efficiency indicator, annual hours, power) for all 4 model technologies at `projects/energy-program/baseline-technology-data.md`. Revised once after review to use real technology-specific standards (AHRI 550/590 IPLV, EN 14511 COP at A7/W55, CAGI specific power, ASME PTC 4) and manufacturer sourcing (Carrier/Trane/York) instead of generic COP. Key finding: Rafi's ~50% grid-efficiency factor means electric steam conversion's primary-energy "savings" don't clearly beat the fuel-oil baseline (~49% well-to-steam vs ~82-85%) — leaning toward dropping that technology from the model rather than forcing a weak example, pending Daniel's review. Also found this session's Claude Code environment has a restrictive "trusted network access" policy blocking WebFetch to most external sites (Omri adjusted settings, needs a fresh session to confirm it took). Next: review baseline data with Daniel, decide on electric steam, then verify remaining flags with Rafi.
---

## Recent Work (July 1)

1. **September Europe trip — route and destination planning** - Locked core 3-month route: Norway → Scotland → London → Ireland → Portugal (Sept 8 - ~Dec 8). Built out conceptual frameworks for each leg: Norway (DNT huts, Jotunheimen, allemannsretten), Scotland (West Highland Way, Glasgow/Edinburgh), Ireland (Galway/Connemara, west coast surf, trad sessions), Portugal (Rota Vicentina, Peniche/Sagres surf, Porto/Lisbon). Discussed and set aside flex destinations (Iceland, Faroe Islands, Basque Country, Galicia, Azores). Next: consult with family member on Norway specifics, then plan each leg in more detail.

2. **Repo audit — pruned dead weight** - Reviewed the whole second-brain structure. Archived three abandoned systems to `archives/deprecated-2026-07-01/` (nothing deleted): the daily dashboard automation (stopped running May 31), the Cowork surface (COWORK.md + sessions/ + templates/, still referencing deleted status/next-steps files), and the unused "Routine creator" project. Fixed CLAUDE.md folder map + scripts/README to match; deleted the dead `daily_dashboard_system` memory. Committed + pushed.

3. **Built /weekly-review + scheduled it as a Friday cloud routine** - New command at `.claude/commands/weekly-review.md` is the anti-cruft ritual (reconcile today.md, deadline radar, stale-application flags, stale-automation sweep). Set it to run automatically every Friday 10:00 AM Israel via a scheduled cloud routine (first run July 3). Cloud run is repo-only + non-interactive: auto-reconciles today.md and writes a report to `reviews/weekly-review-YYYY-MM-DD.md`, but does NOT archive cruft on its own. Manage at https://claude.ai/code/routines/trig_013e68sBVgyjkdU3UwfBXCR1.

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
