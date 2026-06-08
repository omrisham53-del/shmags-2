# Today - 2026-06-08

**Date:** 2026-06-08
**Updated:** 2026-06-08

---

## Current Priority

- Economics final paper (with Tomer): edit lit review + discussion in Google Docs, then hand back for full-document assembly
- Energy program: review `capex_all_rounds.csv` in Excel, compute AVERAGEIF per tech → 4 model CapEx numbers
- Job search: follow up on active applications

---

## Today's Completed

1. **CV revision for Avishai's consulting firm (kibbutz economic projects)** - New referral lead: friend Avishai offered to bring Omri into his workplace, a small economics-consulting firm doing economic projects with kibbutzim. Reviewed and repositioned the Hebrew CV across 3 revisions. Subtitle changed from a degree restatement to a value prop ("אנליסט כלכלי"); profile rewritten economics-first (was sustainability/data-science-first); EcoTraders bullets rewritten so each owns one dimension (modeling / client-facing presentation / AI-process / policy analysis) to kill overlap; kept noun-form bullets to match the rest of the CV; education set to 2023-2026 with "בוגר" framing (graduating July 2026), GPA shown as 93; merged "אקסל" + "תוכנות office" into one skill line; kept English at "רמת שפת אם" (writing reviewed, consistent with the claim). CV is interview-ready.

---

## Recent Work (June 7)

1. **Economics final paper — collaboration setup + drafting (with Tomer)** - CBA policy paper on energy sourcing for a 20MW data center in Gush Dan. Folder at `C:\עמרי\אוניברסיטה\שנה ג\סמסטר ב\Economics Final` (kept OUT of SHMAGS 2 for privacy; shared with Tomer via Live Share). Read the brief, the existing Hebrew draft, the Excel CBA model, and Tomer's Consensus AI research report (~30 sources). Chose "lighter alignment" to the brief's 8-section structure. Drafted the **סקירת ספרות** and **דיון** sections in Hebrew (formal register, author-year citation tags). Flagged two Excel data bugs (CO2 sheet SCC ~1000x too high; misleading "Year 20 OPEX" replacement spike).
2. **Built 6 professional Hebrew charts** - matplotlib + Segoe UI + python-bidi (RTL); consistent per-alternative palette. Total cost, blended rate, energy mix, investment payoff, PUE sensitivity, OPEX composition. Saved to `Economics Final\charts\` with `build_charts.py`.

---

## Recent Work (June 6)

1. **Status line upgrade** - Added plan usage limits (5h + weekly windows, % left + reset countdown) as a second line in the Claude Code status bar, sourced from the native `rate_limits` field in the status line stdin JSON. Added `refreshInterval: 60` so countdowns stay current while idle. Files: `statusline-command.ps1`, `settings.json`.
2. **grill-me skill reviewed + adjusted** - Fixed the capture template em dash and the Bash date note; added a `brainstorms/` row to the CLAUDE.md folder map (raw captures stay there, polished deliverables graduate to projects/). Committed.
3. **First grill-me session: D&D campaign arc** - Ran a full discovery interview and locked the campaign's load-bearing canon. Capture at `brainstorms/2026-06-06-dnd-campaign-arc.md`. Key results: Betrayer named **Ashar** (ancient elf, dragon's jailer, presumed dead in the Fall); the truth that CONTROL caused the Fall of House Arendath (the gem), not freedom; the enslaved dragon is that same dragon; the gem->crystals->ritual method ladder; milestone pacing with Herald's Oath gating L3; Ziggy's buried-song arc. Synced all decisions into `campaign-arc.md`, `world-lore.md`, `npcs-and-characters.md` and the campaign memory. Saved a new `dnd_dm_style` memory (improv-first DM philosophy).

---

## Recent Work (June 1-2)

1. **Repo audit + cleanup** - Reviewed all .md files, identified dead weight, deleted 7 stale status/next-steps files, archived old agent-memory and assignment skill evals (55 files).
2. **Session-start hook fixed** - settings.json had duplicate "hooks" key bug silently discarding the date updater. Fixed + updated session-start.sh to update today.md date fields on every session.
3. **save-context skill updated** - Added Step 5: merge branch to master + push before ending session.
4. **CLAUDE.md overhauled** - Added folder map with rules, fixed malformed section headers, added session-start instruction for stale completed items.
5. **Work PC branches merged** - Pulled and merged claude/beautiful-albattani (tax incentive model, May 31) and claude/gracious-babbage (CapEx pipeline, June 1) into master.
6. **Audited CapEx extraction scripts** - Read + grep-scanned `capex_pipeline.py`, `extract_capex.py`, `diag_walk.py`. Confirmed clean: no network/subprocess/eval/destructive ops, openpyxl read-only. Safe to trust.
7. **Built work-PC security kit** - `references/work-pc-security/` with deny rules (settings.json), a PreToolUse hook (block-network.ps1), and a README. Deterministic alternative to a "guardian agent." Committed + pushed.
8. **Clarified work-PC setup** - All work-PC tasks run on Claude Code online (sandbox, can't harm the PC). Security kit parked for desktop use only; real online safety = anonymize uploads (no real company names/tax IDs).

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
