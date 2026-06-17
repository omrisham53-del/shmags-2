# Today - 2026-06-17

**Date:** 2026-06-17
**Updated:** 2026-06-17

---

## Current Priority

- Economics final paper (with Tomer): paste full paper into Word, convert in-text citations to footnotes, assemble with charts, submit
- Energy program: review `capex_all_rounds.csv` in Excel, compute AVERAGEIF per tech → 4 model CapEx numbers
- Job search: follow up on active applications

---

## Today's Completed

1. **Economics seminar paper — full paper written** - Completed the entire 7-section Hebrew paper (per Prof. Lifshitz's PPTX structure). Sections 1-3 (תקציר, הקדמה, סקירת ספרות) written in prior session; sections 4-8 (ניתוח, סיכום, המלצות, ביבליוגרפיה, נספחים) completed this session. In-text (author, year) citations throughout. Charts 01-05 placed: [איור 3] in 4.2, [איורים 1, 2, 4] in 4.3, [איור 5] in 4.4. Chart 06 excluded. Next: Tomer pastes into Word, converts citations to footnotes, assembles final doc.

---

## Recent Work (June 9)

1. **D&D Session 2 prep — completed** - Finished all 6 open questions from the 2026-06-08 WIP session: named the Scholar (Sera, "more broken" direction), built her full voice/appearance/gesture profile, locked cavern fight (3 Darklings + 2 Kobolds, one Darkling flees), shaped both Scholar scene endings (5-min tense vs 30-60-min quiet, both avoid combat-cliffhanger repeat), chose early-arrival reveals 1+3. Built Scholar's camp map spec and all stat blocks (Darkling, Kobold, Carrion Crawler). Wrote final session_2_plan.md at projects/dnd-campaign/sessions/session_2_plan.md.

2. **Climeworks presentation - RTL layout fix + rehearsal** - Fixed Hebrew alignment in v2.pptx: wrote fix_rtl.py to scan all slides and apply rtl="1" + algn="r" on every Hebrew paragraph, lang="he-IL" on run properties. Saved as v3.pptx at `C:\עמרי\אוניברסיטה\שנה ג\סמסטר ב\חדשנות טכנולוגית\Climeworks - Climate Innovation v3.pptx`. Ran slide-by-slide rehearsal and wrote speaker scripts for slides 2-5 (Omri's 3 slides + Gal's bizmodel slide). Added Climeworks CDR portfolio content to slide 3 script (DAC + nature-based: biochar, reforestation, enhanced weathering, BECCS; 450k+ tons certified). Slides 6-8 scripts still pending.

---

## Recent Work (June 8)

1. **grill-me session: Energy grants chapter** - Ran a discovery interview on the Grant program chapter (one of three incentive-section chapters: grants / tax / loan fund). Locked the framing for the old-vs-new-rounds section that goes to Omer (CEO): "same instrument, new purpose" - the grant mechanism barely changed but its legal basis/purpose is new, it's the complementary carrot to the carbon-tax stick from Government Decision 1261 (14.01.2024). Read the full decision text: grants = Section 2b (₪500M/2025-2027 industry support to adapt to the fossil-fuel tax). Captured the analytical spine (societal CBA, investment-weighted ₪/MWh + ₪/tCO2 ratios, no additionality assumed) and 6 gaps to pressure-test before Omer (legal contingency on the tax; gas is also taxed; frame as "accelerate" not "compensate"). Capture at `brainstorms/2026-06-08-energy-policy-chapter.md`; memory `energy_grants_chapter` created.

2. **CV revision for Avishai's consulting firm (kibbutz economic projects)** - New referral lead: friend Avishai offered to bring Omri into his workplace, a small economics-consulting firm doing economic projects with kibbutzim. Reviewed and repositioned the Hebrew CV across 3 revisions. Subtitle changed from a degree restatement to a value prop ("אנליסט כלכלי"); profile rewritten economics-first (was sustainability/data-science-first); EcoTraders bullets rewritten so each owns one dimension (modeling / client-facing presentation / AI-process / policy analysis) to kill overlap; kept noun-form bullets to match the rest of the CV; education set to 2023-2026 with "בוגר" framing (graduating July 2026), GPA shown as 93; merged "אקסל" + "תוכנות office" into one skill line; kept English at "רמת שפת אם" (writing reviewed, consistent with the claim). CV is interview-ready.

3. **Built the dnd-session-prep skill (+ live session-2 prep, paused)** - Used skill-creator to build a D&D session-prep skill. Key pivot: it is a 4-stage INTERACTIVE thinking partner (Orient → Develop → Build assets → Write), not a one-shot generator, because the session has to live in Omri's head and be built from his ideas (rejected the generator draft twice; added the asset stage himself). Bundles two reusable scripts: `plan_to_docx.py` (plan → docx, replaces the hand-written create_docx scripts) and `make_item_card.py` (parchment/gold printable cards in his style; tested working). Then ran it LIVE on his unplayed session 2 and built a lot: the interrogation crystal-horror beat, Aerendil's Dream 1, the journey beats (Carrion Crawler shortcut + Burton crucible + Darkling-squad signs + a remembering-shrine), and a full 4-rung "bond-and-binding sense" mini-system for Herald (his spine, parallel to Aerendil's drums). Paused mid-Develop; full WIP saved to `brainstorms/2026-06-08-session-2-prep.md`. Corrected session_1_notes.md (a young monk pointed Herald to Gali; Gali never approached). Memory: `feedback_interactive_prep_skills` created; `skills_built` + `dnd_campaign_overview` updated.

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
