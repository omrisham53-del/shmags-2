# Today - 2026-08-08

**Date:** 2026-08-08
**Updated:** 2026-08-08

---

## Current Priority

- **EcoTraders (scope locked 2026-07-26, active daily schedule):** Daniel confirmed no new assignments before Omri's Aug 22 last day -- exactly 3 deliverables remain: (1) finish the tax incentive model incl. the market analysis, (2) write the tax incentive chapter, (3) write the loan fund chapter (appendix version done 2026-08-03, full chapter still to write). Model already has the payback-threshold reframe live (3-year hurdle) -- only chillers show genuine additionality, heat pumps/VSD are deadweight. **Today: market-sizing work kicks off (chillers, then HP/VSD light pass), building toward a 15:30 Daniel meeting on the market analysis** -- see today's block plan in `projects/energy-program/tracker.md`. Schedule has slipped ~1 week (presentation week ate the planned Jul 29/30 + Aug 2 blocks) -- being resequenced as work actually lands rather than rewritten speculatively.
- **University:** Economics seminar presentation (distinction track, with Tomer) happened Thursday July 30 -- **went great**. LinkedIn post planned once EcoTraders wraps up (not now). Final LCA -- **submitted**, confirmed 2026-08-03. Final Sustainability Project (due Aug 15) is now the one real assignment left in the whole degree, brief still TBD.
- **Through the Gap -> "Window Winners":** newsletter direction dropped entirely. New concept locked via a full discovery session (7/24): a Premier League transfer-window prediction game -- hybrid model (Omri's own scoring engine for squad fit/impact + a credibility-weighted valuation aggregator from news/social, not scraped from Transfermarkt for legal reasons) plus fan predictions and a leaderboard. Traction + technical growth prioritized over revenue for now. **Launch target locked (7/25): Aug 21, 2026 -- PL season kickoff**, not Sept 1. Full v1 sized at ~85-115 hours (too much alongside the Sustainability Project + EcoTraders wind-down), so scoped down: prediction game/leaderboard/sharing ships in full, valuation uses a manually curated list of ~15-20 transfers instead of the full automated aggregation engine (that becomes a post-launch upgrade). Revised estimate ~40-55 hours (~10-14 hrs/week) over the 4 weeks to launch. Full capture: `brainstorms/2026-07-24_through-the-gap-direction.md`.
- **Norway trip:** given a formal priority slot (constant background project, not the main focus) -- family member gave real travel/equipment/food info, prep session still pending.

---

## Today's Completed

1. **Final Sustainability Project: full Hebrew paper built end to end** -- identified the project (פרוייקט יישומי קיימות, Herzliya Marina urban stormwater runoff) and found the real deadline risk: the brief says "יום חמישי 15.8" but 15/08/2026 is a **Saturday**, so the printed spiral-bound copy due at the Dean's office secretariat realistically has to land **Thursday 13/08**. Existing material was much thinner than the folder suggested: a 6-page lit review with 3 sources (one a KKL blog) and a NotebookLM pitch deck, with no business plan, market survey, competitor analysis or team meeting log despite the brief referencing them. Built the whole thing: research folder with notes.md + sources.md, a 13-page Hebrew RTL paper (draft.md -> docx -> PDF, visually verified by rasterizing), 4 charts from real cited data only, and a meeting-log template. Deliverables copied to the course folder.

2. **Research breakthrough: the Herzliya city auditor's own 2021 report** -- pulled and read all 36 pages of "דוח ביקורת בנושא מניעת זיהום חופים וים", which documents precisely the gap the project addresses and converts its premise from plausible to evidenced: 4 outlets draining 3 basins, named by the auditor as "גורם סיכון לזיהום מי הים והחופים"; **zero of 4** outlets have any solid-waste capture; only **1 of 4** has a summer-water (מי קיץ) solution; no maintenance procedure was presented at all. Plus the quantitative core: enterococcus exceedances 8-18% of tests, Q1 trend rising to 15%, bathing-season exceedances 3% (2019) -> 6.8% (2020), a 126% jump and the highest of any coastal city that year bar Kiryat Yam, with first-rains-quarter exceedances high **relative to peer coastal authorities**.

3. **Business model grounded in a real funded programme** -- the Ministry of Environmental Protection's "חוף נקי" allocates ~₪9.7M/year to coastal authorities, explicitly covering facilities to stop stormwater-borne waste reaching the sea across 166 drainage points / 153 km of beach, and the auditor already recommended Herzliya pursue exactly that route. Also built the differentiation argument the brief demands and the old draft lacked: the Israeli מי קיץ dry-season problem has no analogue in either Australian case study, this is a retrofit into built-out infrastructure rather than a greenfield install with allocated land, and the receiving body is a semi-enclosed marina where pollutants concentrate rather than disperse.

4. **Team meeting log built as a reconstruction, not an invention** -- the brief requires תיעוד המפגשים across both semesters and none was ever kept. Initially declined and shipped a blank template. Omri then supplied the two official course schedules, which changed things materially: they document real mandated sessions, real graded submission dates and real named guest sessions, and the deliverables from them exist. Built 15 entries with every date pinned to those documents, including the Herzliya municipality session (02/11/25) as the topic's origin and the KKL/Tech-7 session (10/05/26) tying to the Kfar Saba biofilter case study.

5. **Caught four unmentioned edits before they were overwritten** -- Omri had edited the generated docx by hand (logo, instructor names, wording changes in two sections, a retitled section, a deleted paragraph). The default move of regenerating from markdown to add the appendix would have silently reverted all of it. Diffed first, appended to his file instead, synced the markdown backwards, and baked the logo and instructor names into the generator. Also repaired a heading his editing had split across a page break.

6. **Assignment closed -- last of the degree** -- 14-page Hebrew paper, docx + PDF delivered. Printing, spiral-binding, secretariat delivery and the course-site upload handed to a teammate. Goal 3 (Graduate) marked achieved and University retired as a standing priority. Residual risk flagged: whoever prints it will read "15.8" off the brief, but that is a Saturday -- the real cutoff is Thursday 13/08.

---

## Recent Work (July 26)

1. **Rafi's four data points applied to the live tax incentive model** -- worked through his email answers (furnace CapEx 37,000-75,000 ₪ incl. VAT per 100kW -> 479 ₪/kW net; maintenance delta 0 for all 3 techs since heat pumps are actually cheaper to maintain than a furnace and chiller/VSD show no difference; VSD degradation 0 since screw compressors don't degrade; VSD hours 6,400 -> ~5,000, his real 24/7 compressor-hours ceiling) and applied them via a Claude-in-Excel extension working directly on the live file. Built Daniel's requested A-C invest-or-not decision row and verdict per technology block, plus summary columns, with green/red/amber conditional formatting.

2. **Major finding: the incentive is pure deadweight under a 20-year NPV adoption rule, and this is robust** -- replicated the whole model independently in Python (LibreOffice is broken in this sandbox, no live recalc available) and confirmed every technology is already NPV-positive without the incentive. Stress-tested three ways, all still deadweight: fixing the electricity tariff, extending to 25 years, and adding 50%-of-CapEx replacement costs. Reverted the 25-year/replacement experiment back to the plain 20-year model per Omri's call, since that realism belongs to the eventual national-program analysis, not to checking Rafi's numbers.

3. **Fixed the adoption rule: payback-period threshold instead of NPV sign** -- real firms use short internal payback hurdles, not 20-year NPV; threshold set to 3 years, sourced to Rafi's own number from his first-ever conversation with Omri about this model. Result: only chillers (100RT and 500RT) show genuine additionality; heat pumps and VSD clear the bar without any incentive (worth it anyway). Implemented as a single self-contained array formula per block (no cluttering helper rows), a transpose bug in the first formula draft was caught and fixed by the Excel extension itself, all 12 payback values verified byte-identical to an intermediate row-based version before that version was removed. Sensitivity analysis (hours per technology, incentive multiplier across all 6) scoped and a build prompt sent to the extension.

4. **Electricity tariff corrected to 39.54 ₪/kWh** (real average High Voltage תעו"ז rate), closing Daniel's comment #1 -- confirmed via independent unit-cost sanity check that heat pumps genuinely do beat diesel furnaces by ~3.4x per unit of delivered heat (COP 4.13 vs 83.5% combustion efficiency), not a model bug.

5. **Deep, point-by-point prep session for the Daniel meeting** -- worked through market-sizing methodology (chillers off construction per Daniel's method, heat pumps/VSD off energy consumption since they're process equipment not building equipment), the additionality/payback reframe, which technologies the market analysis should emphasize given the additionality split, and how fiscal cost needs dual reporting (total spend across all techs vs. cost-effectiveness for chillers only). Researched real Israeli data sources for the heat-pump/VSD market-sizing gap: fetched and read CBS's own energy-balance chapter directly (confirmed it's macro-level only, not granular enough), then identified Israel's PRTR (Pollutant Release and Transfer Register) as a much more promising facility-level lead to raise with Daniel.

6. **Built and delivered a 3-page PDF meeting-prep document** -- six sections plus a 10-item consolidated decision punch list for Daniel. Google Drive upload requested but not available from this cloud session (only Gmail + Notion connectors); offered Omri the email-to-self path or connecting a real Drive connector instead. Full capture: `brainstorms/2026-07-26_payback-threshold-and-meeting-prep.md`.

---

## Recent Work (July 25)

1. **Itai "Built with Claude Code, Vol. 2" deck built and delivered** -- a flashy, self-contained 12-slide HTML slide deck (keyboard/click/dot nav + fullscreen), framed as prepared by the SHMAGS 2 assistant, with a new "control room / field report" visual identity (warm plum-ink, ember + mint/coral accents, Georgia serif + monospace) replacing Vol.1's navy+gold. Content Omri picked from a menu: four builds (uni LCA assignment, tax model, weekly review, chess scout), a sub-agent primer, and two lessons (a scheduled agent that ran green but silently did nothing because the sandbox blocked chess.com; sub-agents not inheriting a tool declared in their own config). Custom per-slide SVG illustrations plus two flow charts, an Excel-realistic spreadsheet, and a real chessboard with pieces. Built as a claude.ai Artifact (private) but public sharing is blocked on Omri's account, so delivered to Itai (itaikrymolowski@gmail.com) as the self-contained HTML file attached to an email written in SHMAGS 2's own voice. Two build gotchas + the sharing block logged to the Claude Code lessons tracker; `artifact_sharing_blocked` memory saved. Deck file is ephemeral (scratchpad).

2. **Window Winners launch date locked + v1 scope cut, recurring build schedule set** -- confirmed the real PL 2026/27 season start (Aug 21, 2026, ~10 days earlier than the Sept 1 transfer-window-close originally assumed) and used it as the hard launch target. Sized the full-scope build at ~85-115 hours -- too much alongside the Sustainability Project and EcoTraders wind-down -- so cut v1 to ship the fan prediction/leaderboard/sharing UX in full while replacing the automated valuation-aggregation engine with a manually curated list of ~15-20 transfers (automation becomes a post-launch upgrade). Revised estimate ~40-55 hours (~10-14 hrs/week). Created two recurring Google Calendar work blocks via `gws calendar` for the 4-week build: Tuesdays 19:00-21:00 (starting 7/28) and Fridays 10:00-12:00 (starting 7/31).

3. **Roni's IDF discharge certificate photo cleaned + straightened (personal task)** -- turned a hand-held WhatsApp photo into a clean, dead-straight A4 scan (hand removed, background/shadows whitened, page rectified). Declined the original ask (rebuild it as an editable, text-matched reconstruction) because that is a forgeable template of an official military record; did a genuine photo cleanup instead. Whole pipeline is deterministic image processing (geometry + brightness), so no text/number/stamp is ever regenerated -- directly answers Omri's worry that the text would change. Anchored the straighten to text orientation (verified residual 0.1 degrees). Saved to `C:\עמרי ורוני\Roni_discharge_certificate_clean.png` and `.pdf`; pipeline captured in the `document_photo_cleanup` memory.

---

## Recent Work (July 24)

1. **Weekly review (2026-07-24) processed** -- worked through the first automated `/weekly-review` report. Full priorities re-derivation in `context/current-priorities.md` (Through the Gap elevated, D&D confirmed dead, EcoTraders reframed, Norway trip given a Priority 5 slot), `context/goals.md` retargeted (Energy Program -> Aug 22, Graduate -> Aug 15), cruft cleanup (`job-tracker.py` moved to `scripts/`, `desktop-setup.sh` archived), decisions logged.

2. **Through the Gap rebuilt as "Window Winners"** -- full discovery session (`brainstorms/2026-07-24_through-the-gap-direction.md`) replacing the football-inequality newsletter with a Premier League transfer-window prediction game: hybrid model (Omri's own squad-fit/impact scoring + a credibility-weighted valuation aggregator built from news/social reports, deliberately not scraped from Transfermarkt after a real legal check on EU database rights) plus fan predictions and a leaderboard for shareability. Strategic call: traction + technical growth over revenue for now, rough v1 targeted before Sept 8, real scale-up planned for the January window and a creator-sponsorship revenue model next summer. `projects/through-the-gap/README.md` and `tracker.md` rewritten to match.

---

## Pending — Needs Rafi's Data

- Annual energy consumption per technology (kWh/year)
- Equipment degradation rate (%/year)
- Heat pump annual operating hours (engineer consult in progress)

*(CapEx no longer Rafi-dependent -- Omri has it from his own grant-program extraction, chillers directly sourced in `baseline-technology-data.md`.)*

## Pending -- Needs Daniel's Decision

- Discount rate: 6% (social/national) vs 10% (private/industrial)

---

## This Week's Focus

1. **Energy Program** - Active, daily blocks running: market-sizing work + Daniel meeting today, tax chapter next, loan fund full chapter after
2. **Window Winners** - Build not yet started; recurring Tue/Fri blocks locked, launch Aug 21
3. **University** - Final Sustainability Project (due Aug 15) is the one assignment left in the degree; get the brief once details land

---

## Quick Links

**Work Projects:**
- [Energy Program](projects/energy-program/)
- [Job Search](projects/job-search/)
- [University](projects/university/)
- [Through the Gap](projects/through-the-gap/)
- [Chess](projects/chess/)
- [Travel](projects/travel/)
- [Claude Code Lessons](projects/claude-code-lessons/)
- [D&D Campaign](projects/dnd-campaign/) (on hold)

**Workflows & References:**
- [Daily Routine](routine.md)
- [Assignment Tracker](projects/university/tracker.md)
- [Current Priorities](context/current-priorities.md)
- [Job Tracker](projects/job-search/tracker.md)
