# Today - 2026-07-27

**Date:** 2026-07-27
**Updated:** 2026-07-27

---

## Current Priority

- **University:** Economics paper presentation -- script finalized, first-draft slide deck built and sent to Tomer for messaging/storytelling feedback. Thursday July 30 presentation. Prep call with lecturer Osnat proposed for Tuesday 7/28 -- Omri asked to move it earlier to 14:30, no reply yet as of 7/24. Final LCA (due Aug 1) -- full draft + submission-ready .docx built, handed to Omri for his own final edits in Word (functionally done). Final Sustainability Project (due Aug 15) is the one real assignment left in the whole degree, still TBD.
- **EcoTraders (scope locked 2026-07-26):** Daniel confirmed no new assignments before Omri's Aug 22 last day -- remaining work is exactly 3 items: (1) finish the tax incentive model, including the market analysis, (2) write the tax incentive chapter for the national program, (3) write the loan fund chapter for the actual national program (appendix version reuses the already-written position paper, only the full chapter needs writing). Full day-by-day block schedule built 2026-07-27 covering Jul 27 -- Aug 20 (Sun/Mon/Wed full days, Thu half days -- Omri's real EcoTraders work schedule), see `projects/energy-program/tracker.md`. No career future here (coasting) but genuinely engaged -- interesting Excel modeling work.
- **Through the Gap -> "Window Winners":** newsletter direction dropped entirely. New concept locked via a full discovery session (7/24): a Premier League transfer-window prediction game -- hybrid model (Omri's own scoring engine for squad fit/impact + a credibility-weighted valuation aggregator from news/social, not scraped from Transfermarkt for legal reasons) plus fan predictions and a leaderboard. Traction + technical growth prioritized over revenue for now. **Launch target locked (7/25): Aug 21, 2026 -- PL season kickoff**, not Sept 1. Full v1 sized at ~85-115 hours (too much alongside the Sustainability Project + EcoTraders wind-down), so scoped down: prediction game/leaderboard/sharing ships in full, valuation uses a manually curated list of ~15-20 transfers instead of the full automated aggregation engine (that becomes a post-launch upgrade). Revised estimate ~40-55 hours (~10-14 hrs/week) over the 4 weeks to launch. Full capture: `brainstorms/2026-07-24_through-the-gap-direction.md`.
- **Norway trip:** given a formal priority slot (constant background project, not the main focus) -- family member gave real travel/equipment/food info, prep session still pending.

---

## Today's Completed

1. **Itai "Built with Claude Code, Vol. 2" deck built and delivered** -- a flashy, self-contained 12-slide HTML slide deck (keyboard/click/dot nav + fullscreen), framed as prepared by the SHMAGS 2 assistant, with a new "control room / field report" visual identity (warm plum-ink, ember + mint/coral accents, Georgia serif + monospace) replacing Vol.1's navy+gold. Content Omri picked from a menu: four builds (uni LCA assignment, tax model, weekly review, chess scout), a sub-agent primer, and two lessons (a scheduled agent that ran green but silently did nothing because the sandbox blocked chess.com; sub-agents not inheriting a tool declared in their own config). Custom per-slide SVG illustrations plus two flow charts, an Excel-realistic spreadsheet, and a real chessboard with pieces. Built as a claude.ai Artifact (private) but public sharing is blocked on Omri's account, so delivered to Itai (itaikrymolowski@gmail.com) as the self-contained HTML file attached to an email written in SHMAGS 2's own voice. Two build gotchas + the sharing block logged to the Claude Code lessons tracker; `artifact_sharing_blocked` memory saved. Deck file is ephemeral (scratchpad).

2. **Window Winners launch date locked + v1 scope cut, recurring build schedule set** -- confirmed the real PL 2026/27 season start (Aug 21, 2026, ~10 days earlier than the Sept 1 transfer-window-close originally assumed) and used it as the hard launch target. Sized the full-scope build at ~85-115 hours -- too much alongside the Sustainability Project and EcoTraders wind-down -- so cut v1 to ship the fan prediction/leaderboard/sharing UX in full while replacing the automated valuation-aggregation engine with a manually curated list of ~15-20 transfers (automation becomes a post-launch upgrade). Revised estimate ~40-55 hours (~10-14 hrs/week). Created two recurring Google Calendar work blocks via `gws calendar` for the 4-week build: Tuesdays 19:00-21:00 (starting 7/28) and Fridays 10:00-12:00 (starting 7/31).

---

## Recent Work (July 24)

1. **Weekly review (2026-07-24) processed** -- worked through the first automated `/weekly-review` report. Full priorities re-derivation in `context/current-priorities.md` (Through the Gap elevated, D&D confirmed dead, EcoTraders reframed, Norway trip given a Priority 5 slot), `context/goals.md` retargeted (Energy Program -> Aug 22, Graduate -> Aug 15), cruft cleanup (`job-tracker.py` moved to `scripts/`, `desktop-setup.sh` archived), decisions logged.

2. **Through the Gap rebuilt as "Window Winners"** -- full discovery session (`brainstorms/2026-07-24_through-the-gap-direction.md`) replacing the football-inequality newsletter with a Premier League transfer-window prediction game: hybrid model (Omri's own squad-fit/impact scoring + a credibility-weighted valuation aggregator built from news/social reports, deliberately not scraped from Transfermarkt after a real legal check on EU database rights) plus fan predictions and a leaderboard for shareability. Strategic call: traction + technical growth over revenue for now, rough v1 targeted before Sept 8, real scale-up planned for the January window and a creator-sponsorship revenue model next summer. `projects/through-the-gap/README.md` and `tracker.md` rewritten to match.

---

## Recent Work (July 22)

1. **Rafi data-request email drafted, grounded in the live model, and sent** -- opened the actual model file (`b2c10692...0.1.xlsx`, 2 sheets: נתונים והנחות + ניתוח) with openpyxl and read its own color legend to separate missing (yellow) / to-verify (orange) / settled (green + peach) data, rather than trusting the drifted project notes. That caught real drift: electric steam is no longer in the model (only 3 techs remain -- heat pumps, chillers, VSD), and fuel prices are now sourced from משרד האנרגיה (so both were dropped from the email). Final email asks Rafi for only 4 things: (1) CapEx of the mazut/diesel furnace = heat pump baseline (row 39, blank), (2) incremental annual maintenance cost efficient-vis-baseline for all 3 techs (rows 45-46, blank), (3) equipment degradation rate (0.5% placeholder), (4) confirm annual operating hours (5,475 / 3,000 / 6,400). Numbers-only framing on purpose (past meetings ran long), CC Daniel. Omri edited and sent.

2. **Tax incentive chapter -- market analysis methodology brainstormed** -- the macro view that turns the model's per-unit results into total-market impact + fiscal cost + ₪/MWh and ₪/tCO2 (same ruler as the grant chapter). Full capture in `brainstorms/2026-07-22_tax-incentive-market-analysis.md`; key calls logged in decisions/log.md.

---

## Recent Work (July 21)

1. **Economics presentation script finalized** -- refined paragraph by paragraph against the real paper (`_paper_dump.txt`) and Excel model outputs, not invented content. Added the PUE finding (₪222.6M, highest-ROI lever in the model) as a secondary point after the 54% self-generation savings; added the paper's real carbon-pricing recommendation (was missing from the draft), blended with the Ireland/Germany renewable-obligation precedent; rewrote the closing summary to focus on Israel's structural future (6-12% of peak demand by decade end, ~20 years of gas reserves, 22%/year market growth, Feb 2026 Treasury interim recommendations) rather than on the presenters themselves. Edited directly into `presentation/script.docx` (closed/reopened once to clear a Word file-lock).

2. **First-draft slide deck built and verified -- 11 slides** -- built with python-pptx (navy+terracotta system matching the poster), embedding real assets: a live screenshot of the actual Calcalist article headline (captured via headless Chrome, not a mockup) and the real chart PNGs from the paper (total cost, blended rate, PUE sensitivity). Uploaded via `gws` and converted to native Google Slides. Verified every unique slide layout via API thumbnails before calling it done -- caught and fixed one real image/text overlap on the hook slide. Explicitly a messaging/structure draft; visual design polish deferred to a later pass per Omri's request.

3. **Sent script + deck to Tomer for storytelling feedback** -- emailed with the script attached and the Slides link, framed around messaging/story rather than design (not final yet). Shared Drive edit access afterward so the link actually opens for him.

4. **Two corrections logged for future Hebrew/friend emails** -- Omri's name is spelled עמרי, not עומרי (fixed in `context/me.md` and the wrong spelling used in the Tomer email); casual peer emails should skip the closing signature entirely, unlike mentor-register emails like the one to Osnat.

5. **Final LCA assignment -- full draft written, then revised twice, then converted to a submission-ready .docx** -- comparative EPD analysis (ready-mix concrete, PCR 2019:14 + c-PCR-003) comparing Interbeton Building Materials S.A. (Greece) vs. JSW Green Cement Pvt Ltd (India), built with the assignment skill directly from the actual brief's own question structure. Real research pulled from all three source PDFs (the c-PCR + both EPDs) plus two genuine external sources (GCCA's 2050 net-zero roadmap, a 2024 *Resources, Conservation and Recycling* review on concrete LCA comparability). Central finding: both EPDs cite the identical PCR version but declare materially different EN 15804 system boundaries -- Interbeton is full cradle-to-grave, JSW's own module table marks the entire use stage "Module Not Declared" despite calling itself cradle-to-grave in prose. After Omri's first read, did a full line-edit pass (European DD/MM/YYYY dates, every citation dated, no bold/italic outside headers, redundant words removed, functional-unit ambiguity resolved, APA 7 references on their own page) and built 5 real-data matplotlib charts (manufacturing/construction-stage flowchart, an EN 15804 module-declaration diagram, a 2x2 grid of A1-A3 impact comparisons, and two market-cap pie charts for global majors + India peers). A second feedback round fixed a real technical error Omri caught (placement/hardening is construction-stage, not manufacturing), pie-chart label overlap, and chart layout. Converted to `research/academic/final-lca-assignment/Final_Assignment_LCA_Comparative_EPD.docx` via a custom python-docx script, visually verified by rendering to PDF through Word COM and rasterizing pages with PyMuPDF -- caught one leftover em dash on the cover page this way. Cover page lists both Omri and Tomer as students; Tomer is under load this cycle so Omri did the actual work solo, per his own call. Handed off for Omri's final edits in Word.

---

## Recent Work (July 20)

1. **Energy Policy final exam taken -- final exam of the whole degree, done** -- exam happened Monday morning (7/20), went well per Omri. Closed out the temporary Priority 1 from Thursday.

2. **Tax incentive model presented to Daniel -- approved with follow-up work** -- Daniel liked the model despite the still-missing data points, asked Omri to email Rafi to close the gaps plus make a few tweaks. Omri has the details on paper (photographed notes, not uploaded) -- specifics pending before the Rafi email can be drafted (now deferred to the work PC).

3. **Economics paper presentation confirmed for the distinction track -- Thursday July 30, presenting with Tomer** -- 5-7 minute slot. Found a strong real-world anchor for the presentation: Calcalist reported the Electricity Authority ordered a 140-day freeze on new data-center grid-connection requests (incoming requests ~27,000 MW, 3x Israel's average consumption, exceeds grid capacity) -- directly validates the paper's headline finding that self-generation (Alt 2, ~54% cheaper power) isn't just economically optimal but now the only path around a real regulatory bottleneck.

4. **Email sent to Osnat (lecturer)** -- confirming they're presenting, thanking her for a year of support and mentorship, requesting pointers for the format, and proposing Tuesday 7/28 for a prep call. Omri's actual sent version led with genuine warmth before the ask and skipped re-explaining the paper (she already knows it) -- sharper than my first draft, saved as a lecturer/mentor email-tone lesson.

5. **Norway trip: consulted a family member on real travel/equipment/food logistics** -- prep session still pending to work through what came out of that conversation.

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

1. **Through the Gap** - Brainstorm a new direction (football-economics angle dropped 7/17); elevated priority, working on it 7/24
2. **University** - Final Sustainability Project (due Aug 15) is the one assignment left in the degree; get the brief once details land
3. **Energy Program** - Active: finish the tax incentive chapter + model before Aug 22 departure

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
