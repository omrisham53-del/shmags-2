# Today Log — 2026 Archive

Sections moved from today.md when "Recent Work" exceeded 3 dates. Append-only.

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

## Recent Work (June 6)

1. **Status line upgrade** - Added plan usage limits (5h + weekly windows, % left + reset countdown) as a second line in the Claude Code status bar, sourced from the native `rate_limits` field in the status line stdin JSON. Added `refreshInterval: 60` so countdowns stay current while idle. Files: `statusline-command.ps1`, `settings.json`.
2. **grill-me skill reviewed + adjusted** - Fixed the capture template em dash and the Bash date note; added a `brainstorms/` row to the CLAUDE.md folder map (raw captures stay there, polished deliverables graduate to projects/). Committed.
3. **First grill-me session: D&D campaign arc** - Ran a full discovery interview and locked the campaign's load-bearing canon. Capture at `brainstorms/2026-06-06-dnd-campaign-arc.md`. Key results: Betrayer named **Ashar** (ancient elf, dragon's jailer, presumed dead in the Fall); the truth that CONTROL caused the Fall of House Arendath (the gem), not freedom; the enslaved dragon is that same dragon; the gem->crystals->ritual method ladder; milestone pacing with Herald's Oath gating L3; Ziggy's buried-song arc. Synced all decisions into `campaign-arc.md`, `world-lore.md`, `npcs-and-characters.md` and the campaign memory. Saved a new `dnd_dm_style` memory (improv-first DM philosophy).

---

## Recent Work (June 7)

1. **Economics final paper — collaboration setup + drafting (with Tomer)** - CBA policy paper on energy sourcing for a 20MW data center in Gush Dan. Folder at `C:\עמרי\אוניברסיטה\שנה ג\סמסטר ב\Economics Final` (kept OUT of SHMAGS 2 for privacy; shared with Tomer via Live Share). Read the brief, the existing Hebrew draft, the Excel CBA model, and Tomer's Consensus AI research report (~30 sources). Chose "lighter alignment" to the brief's 8-section structure. Drafted the **סקירת ספרות** and **דיון** sections in Hebrew (formal register, author-year citation tags). Flagged two Excel data bugs (CO2 sheet SCC ~1000x too high; misleading "Year 20 OPEX" replacement spike).
2. **Built 6 professional Hebrew charts** - matplotlib + Segoe UI + python-bidi (RTL); consistent per-alternative palette. Total cost, blended rate, energy mix, investment payoff, PUE sensitivity, OPEX composition. Saved to `Economics Final\charts\` with `build_charts.py`.

---

## Recent Work (June 8)

1. **grill-me session: Energy grants chapter** - Ran a discovery interview on the Grant program chapter (one of three incentive-section chapters: grants / tax / loan fund). Locked the framing for the old-vs-new-rounds section that goes to Omer (CEO): "same instrument, new purpose" - the grant mechanism barely changed but its legal basis/purpose is new, it's the complementary carrot to the carbon-tax stick from Government Decision 1261 (14.01.2024). Read the full decision text: grants = Section 2b (₪500M/2025-2027 industry support to adapt to the fossil-fuel tax). Captured the analytical spine (societal CBA, investment-weighted ₪/MWh + ₪/tCO2 ratios, no additionality assumed) and 6 gaps to pressure-test before Omer (legal contingency on the tax; gas is also taxed; frame as "accelerate" not "compensate"). Capture at `brainstorms/2026-06-08-energy-policy-chapter.md`; memory `energy_grants_chapter` created.

2. **CV revision for Avishai's consulting firm (kibbutz economic projects)** - New referral lead: friend Avishai offered to bring Omri into his workplace, a small economics-consulting firm doing economic projects with kibbutzim. Reviewed and repositioned the Hebrew CV across 3 revisions. Subtitle changed from a degree restatement to a value prop ("אנליסט כלכלי"); profile rewritten economics-first (was sustainability/data-science-first); EcoTraders bullets rewritten so each owns one dimension (modeling / client-facing presentation / AI-process / policy analysis) to kill overlap; kept noun-form bullets to match the rest of the CV; education set to 2023-2026 with "בוגר" framing (graduating July 2026), GPA shown as 93; merged "אקסל" + "תוכנות office" into one skill line; kept English at "רמת שפת אם" (writing reviewed, consistent with the claim). CV is interview-ready.

3. **Built the dnd-session-prep skill (+ live session-2 prep, paused)** - Used skill-creator to build a D&D session-prep skill. Key pivot: it is a 4-stage INTERACTIVE thinking partner (Orient -> Develop -> Build assets -> Write), not a one-shot generator, because the session has to live in Omri's head and be built from his ideas (rejected the generator draft twice; added the asset stage himself). Bundles two reusable scripts: `plan_to_docx.py` (plan -> docx, replaces the hand-written create_docx scripts) and `make_item_card.py` (parchment/gold printable cards in his style; tested working). Then ran it LIVE on his unplayed session 2 and built a lot: the interrogation crystal-horror beat, Aerendil's Dream 1, the journey beats (Carrion Crawler shortcut + Burton crucible + Darkling-squad signs + a remembering-shrine), and a full 4-rung "bond-and-binding sense" mini-system for Herald (his spine, parallel to Aerendil's drums). Paused mid-Develop; full WIP saved to `brainstorms/2026-06-08-session-2-prep.md`. Corrected session_1_notes.md (a young monk pointed Herald to Gali; Gali never approached). Memory: `feedback_interactive_prep_skills` created; `skills_built` + `dnd_campaign_overview` updated.

---

## Recent Work (June 9)

1. **D&D Session 2 prep — completed** - Finished all 6 open questions from the 2026-06-08 WIP session: named the Scholar (Sera, "more broken" direction), built her full voice/appearance/gesture profile, locked cavern fight (3 Darklings + 2 Kobolds, one Darkling flees), shaped both Scholar scene endings (5-min tense vs 30-60-min quiet, both avoid combat-cliffhanger repeat), chose early-arrival reveals 1+3. Built Scholar's camp map spec and all stat blocks (Darkling, Kobold, Carrion Crawler). Wrote final session_2_plan.md at projects/dnd-campaign/sessions/session_2_plan.md.

2. **Climeworks presentation - RTL layout fix + rehearsal** - Fixed Hebrew alignment in v2.pptx: wrote fix_rtl.py to scan all slides and apply rtl="1" + algn="r" on every Hebrew paragraph, lang="he-IL" on run properties. Saved as v3.pptx at `C:\עמרי\אוניברסיטה\שנה ג\סמסטר ב\חדשנות טכנולוגית\Climeworks - Climate Innovation v3.pptx`. Ran slide-by-slide rehearsal and wrote speaker scripts for slides 2-5 (Omri's 3 slides + Gal's bizmodel slide). Added Climeworks CDR portfolio content to slide 3 script (DAC + nature-based: biochar, reforestation, enhanced weathering, BECCS; 450k+ tons certified). Slides 6-8 scripts still pending.

---

## Recent Work (June 22)

1. **Repo housekeeping** - Git pull from work PC brought in world-cup-party files (guest + host HTML + vercel.json). Moved HTML files to projects/world-cup-party/, updated vercel.json routes to match. Root stays clean, Vercel URLs unchanged.

2. **Economics seminar paper -- full paper written** - Completed the entire 7-section Hebrew paper (per Prof. Lifshitz's PPTX structure). Sections 1-3 (תקציר, הקדמה, סקירת ספרות) written in prior session; sections 4-8 (ניתוח, סיכום, המלצות, ביבליוגרפיה, נספחים) completed this session. In-text (author, year) citations throughout. Charts 01-05 placed: [איור 3] in 4.2, [איורים 1, 2, 4] in 4.3, [איור 5] in 4.4. Chart 06 excluded. Next: Tomer pastes into Word, converts citations to footnotes, assembles final doc.

3. **Upstart program email sent to Ofir** - Explained missed sessions, team presenting without Omri, requested personal assignment option or withdrawal. CC'd Naor (academic instructor). Ofir replied warmly: "need to check what we can do, will update soon." No action needed -- awaiting his decision.

4. **Urban Analytics final assignment -- reviewed + docs fixed + presentation guide written** - Reviewed all deliverables for Monday's presentation. Regenerated Backup_Memo_v2.docx (clean formatting: Times New Roman 12, 1.15 spacing, proper bold/italic, no markdown artifacts) with all 6 figures embedded. Regenerated Policy_Report_Clean.docx. Removed analysis/eda.py references. Verified all 5 open datasets and both academic articles (Sallis 2016, Oja 2011) exist. Wrote full presentation script as Presentation_Guide.md in the final assignment folder for tomorrow's review with Yonatan. Still pending: convert docs to PDF, get poster from Yonatan, confirm who-did-what split.

---

## Recent Work (June 25)

1. **Economics paper -- chart 07 built (net savings chart)** - Created new PUE net savings chart showing TCO savings vs PUE 2.2 baseline for all 3 alternatives. Optimal PUE = 1.4 for all alternatives. Peak savings: ₪392M (Alt 0), ₪259M (Alt 1), ₪152M (Alt 2). Script at `Economics Final\charts\build_chart_07.py`.

2. **Economics paper -- chart 03 updated** - New title "מקורות האנרגיה: רשת לאומית וייצור עצמי לפי חלופה"; added right-side bracket annotation grouping gas + solar as "ייצור עצמי" with combined %; bars repositioned for spacing.

3. **Economics paper -- sensitivity analysis paragraph written** - Hebrew paragraph for section 4.4 explaining PUE sensitivity analysis and optimal PUE finding.

4. **PwC 2025 citation identified** - Found source of US data center GDP contribution figures ($355B in 2017 to $727B in 2023): PwC report commissioned by Data Center Coalition (Feb 2025). In-text citation should be (PwC, 2025) not (WEF, 2025). Full APA citation provided.

---

## Recent Work (July 1)

1. **September Europe trip -- route and destination planning** - Locked core 3-month route: Norway -> Scotland -> London -> Ireland -> Portugal (Sept 8 - ~Dec 8). Built out conceptual frameworks for each leg: Norway (DNT huts, Jotunheimen, allemannsretten), Scotland (West Highland Way, Glasgow/Edinburgh), Ireland (Galway/Connemara, west coast surf, trad sessions), Portugal (Rota Vicentina, Peniche/Sagres surf, Porto/Lisbon). Discussed and set aside flex destinations (Iceland, Faroe Islands, Basque Country, Galicia, Azores). Trip is also now the mechanism for career direction exploration (alumni/professor conversations) -- see Priority above.

2. **Repo audit -- pruned dead weight** - Reviewed the whole second-brain structure. Archived three abandoned systems to `archives/deprecated-2026-07-01/` (nothing deleted): the daily dashboard automation (stopped running May 31), the Cowork surface (COWORK.md + sessions/ + templates/, still referencing deleted status/next-steps files), and the unused "Routine creator" project. Fixed CLAUDE.md folder map + scripts/README to match; deleted the dead `daily_dashboard_system` memory. Committed + pushed.

3. **Built /weekly-review + scheduled it as a Friday cloud routine** - New command at `.claude/commands/weekly-review.md` is the anti-cruft ritual (reconcile today.md, priorities re-derivation, deadline radar, stale-application flags, stale-automation sweep). Set it to run automatically every Friday 10:00 AM Israel via a scheduled cloud routine. Cloud run is repo-only + non-interactive: auto-reconciles today.md and writes a report to `reviews/weekly-review-YYYY-MM-DD.md`, but does NOT archive cruft or rewrite priorities on its own. Manage at https://claude.ai/code/routines/trig_013e68sBVgyjkdU3UwfBXCR1.

---

## Recent Work (July 6)

1. **Economics seminar POSTER -- design direction locked + built via Claude Design MCP** - Iterated the distinction-prize poster through several concepts (electricity bill -> thermal map -> editorial charts -> Economist cover) before landing on an Economist-style cover with a hand-drawn ISOMETRIC bird's-eye illustration (warm terracotta field, Frank Ruhl Libre + Assistant). Corrected the core message: NOT "efficiency beats the source" but "energy independence is most beneficial" -- a data center on its own solar + efficient gas plant pays ~54% less for power (Alt 2, ₪0.172 vs ₪0.373/kWh), with PUE efficiency (~25%) as the complementary lever. Workflow: illustration generated in Claude Design, Hebrew text/layout authored in code and pushed back via the DesignSync MCP. Files in the "Israel's Overheating Grid" Claude Design project + local mirror at `Economics Final\Poster\design\`; final assembly = `Poster - Final.dc.html`. Confirmed submitted by the July 7 deadline; presentation July 30.

2. **Improvers Club -- July annotated game submission written** - Set up Stockfish + python-chess for local engine analysis. Analyzed two candidate games at depth 18. Selected game vs. gannu8709049607 (July 1, Re1# back-rank mate). Hook: 4 consecutive engine-best moves (23...Bxd4, 24...Rxc2, 25...Rxe2, 26...Bxb1) converting a won position after a queen/rook fork on move 16. Full written annotation + PGN with embedded comments ready. To submit: import PGN to chess.com/analysis, save as public study, post study link + annotation text to club forum, paste #comment- permalink into the form.

3. **Ronni's psychobiology assignment review** - Read all 4 source articles + assignment brief + tips doc. Extracted text from the submitted .docx via Word COM. Generated full Hebrew review report covering science accuracy, 3 missing bibliography entries, citation formatting errors, figure reference issues, integration paragraph word count, and science precision notes. Assignment folder: `C:\עמרי ורוני\לימודים\מטלת הכירו את המדע\`.

4. **Energy Program -- tax incentive baseline data built, key finding on electric steam** - Per Daniel's 3-step unblocking process, gathered baseline data (2 capacity points, efficiency indicator, annual hours, power) for all 4 model technologies at `projects/energy-program/baseline-technology-data.md`. Revised to use real technology-specific standards (AHRI 550/590 IPLV, EN 14511 COP at A7/W55, CAGI specific power, ASME PTC 4) and manufacturer sourcing. Key finding: electric steam conversion's primary-energy "savings" don't clearly beat the fuel-oil baseline -- leaning toward dropping that technology from the model, pending Daniel's review.

---

## Recent Work (July 7)

1. **"Through the Gap" newsletter launched (Skill 6 project)** - Brainstormed passion-first income streams for the trip; landed on football economics + inequality as the niche. Name: Through the Gap. Platform: Substack (signup in progress, free tier first). First article drafted: "The £116 Million Illusion" - the Anderson £116m transfer as a lens on Forest's PSR survival-selling, the SCR flat-tax problem (85% of unequal revenues = permanent gap), and the private votes (SCR passed 14-6, anchoring killed 12-7). Draft + 5 chart specs + verify-before-publish list at `projects/through-the-gap/articles/2026-07-07_the-116-million-illusion.md`; reusable 9-step article workflow in the project README.

2. **Git sync + EcoTraders notice outcome logged** - Merged two work-PC branches to master (resolved decisions/log.md conflict), pushed. Logged meeting outcome: Daniel accepted politely, last day Aug 22, no handoff plan discussed. Saved ecotraders-exit memory.

---

## Recent Work (July 10)

1. **Full priorities re-derivation, not just a status patch** - Rebuilt `context/current-priorities.md` from scratch: Through the Gap elevated to Priority 1 (reconsidering newsletter -> tool/app), Job Search reframed as "Career Direction Exploration" (genuine reconsideration of career path during the trip via alumni/professor conversations, not a logistics pause), University and EcoTraders both explicitly deprioritized, D&D moved to an "On Hold" section (group scheduling killed his motivation), and a new "Hobbies" section added for chess. Updated `context/goals.md`, `projects/dnd-campaign/README.md`, `projects/through-the-gap/README.md`, and 3 memory files to match. Folded a standing "priorities re-derivation" step into the Friday `/weekly-review` cloud routine.

2. **Job search tracker fully closed out** - Bank of Israel confirmed rejected (formal no); Mobileye, Realplay, Nexxen, Primis marked Rejected by default after 40+ days of silence. MoonActive Junior Acquisition Manager corrected from a mislabeled "Rejected" to "Paused" (the planned October reach-out no longer works since Omri will be traveling then). Tracker summary: 7 Rejected, 1 Paused, 1 Lead (Avishai referral), clean slate for post-trip.

3. **University tracker reconciled + 2 new assignments added** - Confirmed submitted: Economics Final Paper, distinction-prize poster (July 7 deadline met, presentation July 30 still ahead), HW #3, and HW #2. Added two new assignments: Final LCA Assignment (due Aug 1) and Final Sustainability Project (due Aug 15).

4. **Style consistency audit + fix** - Audit found real em-dash violations across memory files, project docs, and a D&D session plan. Root cause: `dnd-session-prep/SKILL.md` had no Style section. Fixed: added Style section to dnd-session-prep, added a "Skill-Owned Style" principle + output-type register table to `communication-style.md`, and baked the requirement into `skill-creator/SKILL.md`'s checklist so future skills get it by default.

5. **Chess given a full project + two-stage automation** - Created `projects/chess/README.md` + `tracker.md`. Built two scheduled cloud routines: "Chess tracker auto-update" (every 3 days, flags candidate games from chess.com metadata) and "Chess bi-weekly Stockfish analysis" (1st and 16th of each month, real depth-18 analysis). Omri still writes the actual hook/annotation himself.

---

## Recent Work (July 12)

1. **Grants program chapter and loan fund position paper finished and sent to the Ministry of Energy client** - Both documents completed and sent directly to the client after review (not routed through Daniel first). Closes out two of the three incentive-section chapters Omri owns (grants, tax incentive, loan fund) -- tax incentive model is the one still in progress.

2. **Tax incentive model -- chiller section fully completed with real grant-program data** - Merged the unmerged `claude/tax-incentive-data-points-iy616v` branch (was sitting unpushed, holding the original baseline-technology-data.md). Locked chiller kW/ton baseline-vs-efficient split (ASHRAE 90.1 code-minimum vs. DOE FEMP efficient tier at 500 RT; reciprocating vs. screw/scroll at 100 RT) with hours locked at 3,000 (working number, above the ~2,080-8,760 range an EcoTraders engineer gave verbally). Then Omri uploaded `capex_all_rounds_annotated.xlsx` with a chiller-specific sheet (96 real line items from the 2017-2022 grant rounds) -- used the real median 4,186 ILS/ton for efficient CapEx, and derived an estimated 3,562 ILS/ton baseline CapEx by backing it out through a sourced 10-25% efficiency cost premium (DOE FEMP + market commentary), since grant data structurally can't contain a baseline-tier price. Chillers are now the most complete technology in `projects/energy-program/baseline-technology-data.md`.

3. **Heat pump baseline corrected from electric resistance to mazut/diesel-fired boilers, then re-sourced with real capacity/COP data** - Rafi's notes (per Omri's re-check) confirmed heat pumps replace mazut/diesel ovens, not electric water heaters as originally assumed and as still hardcoded in `generate_tax_model.py`. Rebuilt as a fuel-combustion-vs-electric comparison (reusing electric steam's 82-85% ASME PTC4 combustion efficiency), added real MRV-sourced fuel caloric values from Omri's Excel (diesel 0.085 ton/MWh, mazut 0.088 ton/MWh). Corrected and split heat pump (1a) and boiler (1b) data into separate tables. Heat pump hours (3,000-4,000) and CapEx both remain open.

4. **CapEx sourcing strategy resolved after a same-day reversal** - Omri clarified he already has real CapEx pulled from the grant program rounds (the June 1 `capex_pipeline.py` extraction work) and uses that directly for heat pumps, VSD, and electric steam. Chillers are the one exception, kept in `baseline-technology-data.md` directly.

5. **Reviewed Omri's latest tax-incentive-model Excel draft, found real issues** - No real market fuel price (ILS/ton) for diesel/mazut anywhere in the workbook. Every discounted-cashflow formula in the analysis sheet has a broken #REF! reference where the discount rate should be. The heat pump baseline row label was manually renamed but the underlying formula still computes OPEX as electricity kWh x electricity price -- the structural fuel-vs-electric code fix genuinely hasn't been done yet, just cosmetically relabeled.

6. **Wrote 3 prompts for Omri's pre-send document review workflow** - A Word-extension prompt checking for unresolved tracked changes/comments, placeholder text, inconsistent terminology, and broken citations; and two short client-email-drafting prompts (one each for the grants program chapter and the loan fund chapter).

7. **September trip route reordered for a London meetup** - Swapped to Norway -> London -> Scotland -> Ireland -> Portugal since Norway's 4-week leg already ends ~Oct 5, right before the ~Oct 8 London meetup. Oslo confirmed as the flight destination.

8. **Trip promoted to a full project** - Created `projects/travel/` (README + tracker). `september_trip` memory now points to it as the live record.

9. **Trip budget analyzed and built into an Excel tracker** - Funding: 15,000 ILS military service grant + 3,000 ILS savings = 18,000 ILS confirmed baseline. Estimated real cost range: 15,800 (frugal) to 24,100 (moderate comfort) -- Norway flagged as the main risk. Built `projects/travel/Travel_Budget_Tracker.xlsx` with 5 linked tabs.

10. **Session pushed to master** - Committed and pushed all of the above (commit dd93edf).

---

## Recent Work (July 14)

1. **Started `projects/claude-code-lessons/` to capture lessons from the 6-hour Claude Code manual** - README + tracker built for a multi-session, multi-day backlog. Wired `/save-context` to also auto-feed it with Claude Code meta-lessons from regular work sessions, not just the manual.

2. **Built an explicit "AI Kill List" in communication-style.md** - First lesson from the manual. Concrete banned buzzwords/phrases/structural patterns (AI slop), replacing the old vague "keep it real" line.

3. **Audited SHMAGS 2 for leaked secrets** - Confirmed clean: `.env` gitignored and never committed, zero real secret hits across all 225 tracked files and full git history.

4. **Installed and fully configured the gws CLI (googleworkspace/cli)** - Full Google Workspace access (Drive, Gmail, Calendar, Sheets, Docs, Slides, Tasks, Chat) from the terminal. Installed via npm, set up Google Cloud SDK + a new GCP project (`omri-gws-cli`, 44 APIs enabled), manually created the OAuth consent screen + client in Cloud Console, logged in as omrisham53@gmail.com. Known limitation: Testing-mode refresh tokens expire every 7 days, re-login needed weekly (open item, not yet resolved).

5. **VS Code settings tuned** - New Claude Code sessions default to terminal view (`claudeCode.useTerminal`); all `.md` files default to rendered Preview instead of raw source (`workbench.editorAssociations`).

6. **Built a visual 9-slide Google Slides deck for Itai showcasing Claude Code + gws** - Rebuilt with knowledge-graph diagram, hub-and-spoke app grid, terminal mockups, comparison pills, security flow diagram, bar chart, pipeline flow, and numbered stepper. Navy/gold/Playfair Display design system. Saved as a durable `slide_deck_preferences` memory so future decks start visual-first by default.

7. **Emailed and shared the deck with Itai via gws** - Sent through `gws gmail +send`. First draft had the wrong tone; corrected and saved as a `feedback_friend_emails` memory.

---

## Recent Work (July 15)

1. **Built a new England vs Argentina edition of the World Cup party quiz for tonight** - New guest (`world-cup-eng-arg.html`) and host (`world-cup-eng-arg-host.html`) versions alongside the original files, routed via `vercel.json`. Same proven structure with fixture-specific trivia and knockout-stage fields.

2. **Hardened the WhatsApp share flow for the iPhone sharing issue flagged from last time** - Rebuilt the share section with a direct `https://wa.me/?text=` deep link and an always-visible "copy text" fallback, replacing the old `navigator.share()` with no fallback. Added iOS web-app meta tags.

---

## Recent Work (July 17)

1. **Energy Policy final exam surfaced and tracked** - Discovered mid-session it's the final exam of the whole degree, Monday July 20. Added to `projects/university/tracker.md`, promoted to temporary Priority 1. Course materials uploaded (12 lecture decks + sample exam) and mapped against the sample exam's structure.

2. **gws OAuth 7-day re-login issue fixed for good** - Published the app from Testing to Production in Cloud Console (no formal Google verification needed for personal single-user use), re-authenticated, verified live.

3. **Final LCA assignment unblocked** - Real brief surfaced. Topic locked to a comparative EPD analysis: ready-mix concrete, Interbeton (Greece) vs. JSW (India), both under PCR 2019:14 + c-PCR-003. Found a genuine methodological gap between the two EPDs (different declared system boundaries despite citing the identical PCR version) to build the comparative analysis around.

4. **Travel: flight confirmed booked, Norway route planning** - Confirmed the Sept 8 Oslo flight is booked. Decided on the overnight sleeper train to Oslo area. Researched every Norway trek candidate against real season/hut-closure constraints.

5. **Travel: Bergen dropped entirely, full Oslo->Jotunheimen->Breheimen route locked with real dates** - Omri picked two published hut-to-hut routes ("6 Days in Jotunheimen's Peaks" and "From Fjord to Mountain in Breheimen"). Cross-referenced every hut on both routes against the official DNT maps. Found the route's Day 5 night (Sept 14, Memurubu) falls one day past the confirmed Sept 13 DNT closure date -- flagged as the top question for Omri's planned in-person DNT center visit in Oslo on Sept 9. Full itinerary logged in `projects/travel/tracker.md`.


---

## Recent Work (July 13)

1. **Tax incentive model rebuilt twice (v2 then v3) — now 6-capacity-point, fully sourced, NPV-only** - Built v2 fresh (not patched) to kill two silent bugs in Omri's hand-edited draft: a broken `#REF!` discount-rate formula and a heat pump baseline still computing electricity x price despite being relabeled "תנור סולר". Electric steam dropped. Omri then hand-edited v2 directly (compacted layout, diesel as default fuel) and asked for a v3 rebuilt fresh against *his* edited file rather than the old script: two capacity points per technology (6 columns total: heat pump 40/70kW, chiller 100/500RT, VSD 45/150kW — this also restored chiller efficiency correctly varying by capacity, which v2 had flattened), real units shown directly on every cell instead of a placeholder, sources written directly in the מקור column (no more [n] citations), and analysis trimmed to NPV only (ROI and payback removed). Chillers and VSD are now essentially complete; heat pumps still need hours + baseline CapEx.

2. **Real grant-data CapEx locked for VSD and heat pumps** - VSD: ₪1,500/kW (median of 3 real grant line items — the mean was skewed to ~₪2,030 by one outlier nearly 2x the others, same median-over-mean pattern already used for chillers). Heat pump: ₪1,050/kW, from Omri's own analysis of 2 grant results. Both applied flatly across their two capacity points, same convention as chillers' flat ₪/ton rate. Baseline CapEx derived for VSD (₪1,500 ÷ 1.225 VSD-premium ≈ ₪1,224/kW) but still PENDING for heat pumps — no efficiency-premium methodology transfers to a combustion oven the way it does between two tiers of the same equipment type.

3. **Mazut price scare resolved** - Omri's edited file briefly showed ₪2.345/ton (three decimal places short of the real ₪2,344.72). He pushed back initially, then independently verified against government import rates and confirmed the original sourced figure was right. Caught before it mattered since diesel was the active fuel type at the time, but would have produced ~1000x-too-cheap fuel costs if mazut had been selected.

4. **Real hotel-pool heat pump project used to sanity-check operating hours, not adopted directly** - Omri surfaced a real ESCO pre-project calc (Jerusalem hotel, gas-to-heat-pump for pool + hot water). Fully reverse-engineered and triple-verified its annual electricity consumption (381,994 kWh/year) and derived an implied capacity factor of ~100.15% — i.e. this installation is sized to run essentially continuously (~8,760 EFLH). Flagged as a real, well-verified upper-bound reference point for the engineer consult, not locked in as the model's general hours assumption, since a hotel pool is about as high-utilization a load as exists and likely isn't representative of the broader grant-recipient population.

---

## Recent Work (July 20)

1. **Energy Policy final exam taken -- final exam of the whole degree, done** -- exam happened Monday morning (7/20), went well per Omri. Closed out the temporary Priority 1 from Thursday.

2. **Tax incentive model presented to Daniel -- approved with follow-up work** -- Daniel liked the model despite the still-missing data points, asked Omri to email Rafi to close the gaps plus make a few tweaks. Omri has the details on paper (photographed notes, not uploaded) -- specifics pending before the Rafi email can be drafted (now deferred to the work PC).

3. **Economics paper presentation confirmed for the distinction track -- Thursday July 30, presenting with Tomer** -- 5-7 minute slot. Found a strong real-world anchor for the presentation: Calcalist reported the Electricity Authority ordered a 140-day freeze on new data-center grid-connection requests (incoming requests ~27,000 MW, 3x Israel's average consumption, exceeds grid capacity) -- directly validates the paper's headline finding that self-generation (Alt 2, ~54% cheaper power) isn't just economically optimal but now the only path around a real regulatory bottleneck.

4. **Email sent to Osnat (lecturer)** -- confirming they're presenting, thanking her for a year of support and mentorship, requesting pointers for the format, and proposing Tuesday 7/28 for a prep call. Omri's actual sent version led with genuine warmth before the ask and skipped re-explaining the paper (she already knows it) -- sharper than my first draft, saved as a lecturer/mentor email-tone lesson.

5. **Norway trip: consulted a family member on real travel/equipment/food logistics** -- prep session still pending to work through what came out of that conversation.

---

## Recent Work (July 21)

1. **Economics presentation script finalized** -- refined paragraph by paragraph against the real paper (`_paper_dump.txt`) and Excel model outputs, not invented content. Added the PUE finding (₪222.6M, highest-ROI lever in the model) as a secondary point after the 54% self-generation savings; added the paper's real carbon-pricing recommendation (was missing from the draft), blended with the Ireland/Germany renewable-obligation precedent; rewrote the closing summary to focus on Israel's structural future (6-12% of peak demand by decade end, ~20 years of gas reserves, 22%/year market growth, Feb 2026 Treasury interim recommendations) rather than on the presenters themselves. Edited directly into `presentation/script.docx` (closed/reopened once to clear a Word file-lock).

2. **First-draft slide deck built and verified -- 11 slides** -- built with python-pptx (navy+terracotta system matching the poster), embedding real assets: a live screenshot of the actual Calcalist article headline (captured via headless Chrome, not a mockup) and the real chart PNGs from the paper (total cost, blended rate, PUE sensitivity). Uploaded via `gws` and converted to native Google Slides. Verified every unique slide layout via API thumbnails before calling it done -- caught and fixed one real image/text overlap on the hook slide. Explicitly a messaging/structure draft; visual design polish deferred to a later pass per Omri's request.

3. **Sent script + deck to Tomer for storytelling feedback** -- emailed with the script attached and the Slides link, framed around messaging/story rather than design (not final yet). Shared Drive edit access afterward so the link actually opens for him.

4. **Two corrections logged for future Hebrew/friend emails** -- Omri's name is spelled עמרי, not עומרי (fixed in `context/me.md` and the wrong spelling used in the Tomer email); casual peer emails should skip the closing signature entirely, unlike mentor-register emails like the one to Osnat.

5. **Final LCA assignment -- full draft written, then revised twice, then converted to a submission-ready .docx** -- comparative EPD analysis (ready-mix concrete, PCR 2019:14 + c-PCR-003) comparing Interbeton Building Materials S.A. (Greece) vs. JSW Green Cement Pvt Ltd (India), built with the assignment skill directly from the actual brief's own question structure. Real research pulled from all three source PDFs (the c-PCR + both EPDs) plus two genuine external sources (GCCA's 2050 net-zero roadmap, a 2024 *Resources, Conservation and Recycling* review on concrete LCA comparability). Central finding: both EPDs cite the identical PCR version but declare materially different EN 15804 system boundaries -- Interbeton is full cradle-to-grave, JSW's own module table marks the entire use stage "Module Not Declared" despite calling itself cradle-to-grave in prose. After Omri's first read, did a full line-edit pass (European DD/MM/YYYY dates, every citation dated, no bold/italic outside headers, redundant words removed, functional-unit ambiguity resolved, APA 7 references on their own page) and built 5 real-data matplotlib charts (manufacturing/construction-stage flowchart, an EN 15804 module-declaration diagram, a 2x2 grid of A1-A3 impact comparisons, and two market-cap pie charts for global majors + India peers). A second feedback round fixed a real technical error Omri caught (placement/hardening is construction-stage, not manufacturing), pie-chart label overlap, and chart layout. Converted to `research/academic/final-lca-assignment/Final_Assignment_LCA_Comparative_EPD.docx` via a custom python-docx script, visually verified by rendering to PDF through Word COM and rasterizing pages with PyMuPDF -- caught one leftover em dash on the cover page this way. Cover page lists both Omri and Tomer as students; Tomer is under load this cycle so Omri did the actual work solo, per his own call. Handed off for Omri's final edits in Word.

---

## Recent Work (July 22)

1. **Rafi data-request email drafted, grounded in the live model, and sent** -- opened the actual model file (`b2c10692...0.1.xlsx`, 2 sheets: נתונים והנחות + ניתוח) with openpyxl and read its own color legend to separate missing (yellow) / to-verify (orange) / settled (green + peach) data, rather than trusting the drifted project notes. That caught real drift: electric steam is no longer in the model (only 3 techs remain -- heat pumps, chillers, VSD), and fuel prices are now sourced from משרד האנרגיה (so both were dropped from the email). Final email asks Rafi for only 4 things: (1) CapEx of the mazut/diesel furnace = heat pump baseline (row 39, blank), (2) incremental annual maintenance cost efficient-vis-baseline for all 3 techs (rows 45-46, blank), (3) equipment degradation rate (0.5% placeholder), (4) confirm annual operating hours (5,475 / 3,000 / 6,400). Numbers-only framing on purpose (past meetings ran long), CC Daniel. Omri edited and sent.

2. **Tax incentive chapter -- market analysis methodology brainstormed** -- the macro view that turns the model's per-unit results into total-market impact + fiscal cost + ₪/MWh and ₪/tCO2 (same ruler as the grant chapter). Full capture in `brainstorms/2026-07-22_tax-incentive-market-analysis.md`; key calls logged in decisions/log.md.
