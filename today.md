# Today - 2026-07-13

**Date:** 2026-07-13
**Updated:** 2026-07-13

---

## Current Priority

- Through the Gap: reconsidering format -- elevate beyond a newsletter into a revenue-generating tool/app that also hones AI/product/creativity skills and doubles as a portfolio piece
- University: two remaining assignments (Final LCA, due Aug 1; Final Sustainability Project, due Aug 15), plus the poster presentation July 30
- Energy Program (EcoTraders): coast-to-Aug-22 wind-down, not active investment -- opportunistic only (baseline data review with Daniel, verification with Rafi)

---

## Saved for Later / To Check

- **outsourcerer** (GitHub repo) - https://github.com/alexgreensh/outsourcerer - Omri wants to look at this when he's home (saved 2026-07-13, came in via a LinkedIn share link)

---

## Today's Completed

---

## Recent Work (July 12)

1. **Grants program chapter and loan fund position paper finished and sent to the Ministry of Energy client** - Both documents completed and sent directly to the client after review (not routed through Daniel first). Closes out two of the three incentive-section chapters Omri owns (grants, tax incentive, loan fund) -- tax incentive model is the one still in progress.

2. **Tax incentive model — chiller section fully completed with real grant-program data** - Merged the unmerged `claude/tax-incentive-data-points-iy616v` branch (was sitting unpushed, holding the original baseline-technology-data.md). Locked chiller kW/ton baseline-vs-efficient split (ASHRAE 90.1 code-minimum vs. DOE FEMP efficient tier at 500 RT; reciprocating vs. screw/scroll at 100 RT) with hours locked at 3,000 (working number, above the ~2,080-8,760 range an EcoTraders engineer gave verbally). Then Omri uploaded `capex_all_rounds_annotated.xlsx` with a chiller-specific sheet (96 real line items from the 2017-2022 grant rounds, by far the best-represented technology) - used the real median ₪4,186/ton for efficient CapEx, and derived an estimated ₪3,562/ton baseline CapEx by backing it out through a sourced 10-25% efficiency cost premium (DOE FEMP + market commentary), since grant data structurally can't contain a baseline-tier price. Chillers are now the most complete technology in `projects/energy-program/baseline-technology-data.md`.

3. **Heat pump baseline corrected from electric resistance to mazut/diesel-fired boilers, then re-sourced with real capacity/COP data** - Rafi's notes (per Omri's re-check) confirmed heat pumps replace mazut/diesel ovens, not electric water heaters as originally assumed and as still hardcoded in `generate_tax_model.py`. Rebuilt as a fuel-combustion-vs-electric comparison (reusing electric steam's 82-85% ASME PTC4 combustion efficiency), added real MRV-sourced fuel caloric values from Omri's Excel (diesel 0.085 ton/MWh, mazut 0.088 ton/MWh) and a point-of-use (~4-5x) + well-to-heat (~2x, after Rafi's ~50% grid factor) efficiency comparison. Omri then caught real sourcing errors on review: the cited source only supported a 70kW capacity ceiling, not the 150kW originally used, and each product page actually lists a specific COP (4.13 at 40kW, 3.23-3.24 at 70kW - inversely related to capacity) instead of the flat 3.5-4.0 band used. Corrected and split heat pump (1a) and boiler (1b) data into separate tables. Heat pump hours (3,000-4,000) and CapEx both remain open - hours pending an EcoTraders engineer consult, CapEx to come from Omri's grant-program extraction.

4. **CapEx sourcing strategy resolved after a same-day reversal** - Initially concluded (incorrectly) that CapEx should be open-sourced like everything else; Omri corrected this - he already has real CapEx pulled from the grant program rounds (the June 1 `capex_pipeline.py` extraction work) and uses that directly for heat pumps, VSD, and electric steam. Chillers are the one exception, kept in `baseline-technology-data.md` directly since that technology's grant data is uniquely strong (96 units vs. 49/5/1 for the others).

5. **Reviewed Omri's latest tax-incentive-model Excel draft, found real issues before he sends anything to Daniel** - No real market fuel price (₪/ton) for diesel/mazut anywhere in the workbook, only environmental externality costs (a different concept - would be a methodology error to conflate them) and blank "market prices" rows. Every discounted-cashflow formula in the analysis sheet has a broken `#REF!` reference where the discount rate should be. The heat pump baseline row label was manually renamed to "תנור סולר" but the underlying formula still computes OPEX as electricity kWh x electricity price - the structural fuel-vs-electric code fix genuinely hasn't been done yet, just cosmetically relabeled.

6. **Wrote 3 prompts for Omri's pre-send document review workflow** - A Word-extension prompt checking for unresolved tracked changes/comments, placeholder text, inconsistent terminology, and broken citations before sending a chapter to the Ministry of Energy; and two short client-email-drafting prompts (one each for the grants program chapter and the loan fund chapter) for Claude on the company account to use once the actual documents are attached there.

7. **September trip route reordered for a London meetup** - Omri wants to book a flight to Oslo and is meeting friends in London ~Oct 8. Original route (Norway -> Scotland -> London -> Ireland -> Portugal) didn't reach London until Oct 19. Swapped to Norway -> London -> Scotland -> Ireland -> Portugal since Norway's 4-week leg already ends ~Oct 5, right before the meetup. Oslo confirmed as the flight destination; still open whether it replaces Bergen as the actual Norway entry point (originally Bergen-first).

8. **Trip promoted to a full project** - Created `projects/travel/` (README + tracker) at Omri's request, same pattern as chess. `september_trip` memory now points to it as the live record instead of holding full details itself.

9. **Trip budget analyzed and built into an Excel tracker** - Funding: ₪15,000 military service grant + ₪3,000 savings = ₪18,000 confirmed baseline (excludes flights); parents will help with costs "when needed" but no fixed amount, and a planned work/volunteer exchange (room+board) are both tracked as separate buffers, not part of the baseline. Researched real 2026 daily costs per leg (Norway/London/Scotland/Ireland/Portugal) and current EUR/GBP/NOK exchange rates. Estimated real cost range: ₪15,800 (frugal, disciplined) to ₪24,100 (moderate comfort) -- Norway flagged as the main risk (highest daily cost). Built `projects/travel/Travel_Budget_Tracker.xlsx` with 5 linked tabs (Summary, Funding Sources, Budget Plan, Expense Log, Rates) for trip prep and live expense tracking while traveling.

10. **Session pushed to master** - Committed and pushed all of the above (commit `dd93edf`).

---

## Recent Work (July 10)

1. **Full priorities re-derivation, not just a status patch** - First pass updated status text inside the same old buckets; Omri caught that priorities themselves had changed, not just their progress. Rebuilt `context/current-priorities.md` from scratch: Through the Gap elevated to Priority 1 (reconsidering newsletter -> tool/app), Job Search reframed as "Career Direction Exploration" (genuine reconsideration of career path during the trip via alumni/professor conversations, not a logistics pause), University and EcoTraders both explicitly deprioritized, D&D moved to an "On Hold" section (group scheduling killed his motivation), and a new "Hobbies" section added for chess. Updated `context/goals.md`, `projects/dnd-campaign/README.md`, `projects/through-the-gap/README.md`, and 3 memory files to match. Folded a standing "priorities re-derivation" step into the Friday `/weekly-review` cloud routine so this doesn't have to wait for another big context dump.

2. **Job search tracker fully closed out** - Bank of Israel confirmed rejected (formal no); Mobileye, Realplay, Nexxen, Primis marked Rejected by default after 40+ days of silence. MoonActive Junior Acquisition Manager corrected from a mislabeled "Rejected" to "Paused" (the planned October reach-out no longer works since Omri will be traveling then). Tracker summary: 7 Rejected, 1 Paused, 1 Lead (Avishai referral), clean slate for post-trip.

3. **University tracker reconciled + 2 new assignments added** - Confirmed submitted: Economics Final Paper (with Tomer), the distinction-prize poster (July 7 deadline met, presentation July 30 still ahead), HW #3 (LCA cups), and HW #2 (fixed a self-contradiction where the tracker said both "In Progress" and "Submitted"). Added two new assignments: Final LCA Assignment (due Aug 1) and Final Sustainability Project (due Aug 15) -- both details TBD, flagged as overlapping the EcoTraders wind-down and the Sept 8 trip departure.

4. **Style consistency audit + fix** - Prompted by Omri asking whether communication-style.md rules actually get applied everywhere. Audit found real em-dash violations: 8 in current-priorities.md and 4 in university/tracker.md (both written earlier same session), plus 106 across 20 memory files, 44 in a D&D session plan, and 18 in decisions/log.md (pre-existing, left alone -- log is append-only). Root cause: `dnd-session-prep/SKILL.md` had no Style section at all, unlike the `assignment` skill which already had Hebrew/English writing rules baked in. Fixed: added a Style section to dnd-session-prep, added a "Skill-Owned Style" principle + output-type register table to `communication-style.md`, and baked the requirement into `skill-creator/SKILL.md`'s checklist so future skills get this by default.

5. **Chess given a full project + two-stage automation** - Created `projects/chess/README.md` + `tracker.md` (ratings, openings, study habits, Improvers Club context) at Omri's request for full tracking, not just a memory note. Built two scheduled cloud routines: "Chess tracker auto-update" (every 3 days, flags candidate games from chess.com metadata -- upset wins, checkmate finishes, short decisive games) and "Chess bi-weekly Stockfish analysis" (1st and 16th of each month, installs Stockfish + python-chess in its own cloud sandbox, runs real depth-18 analysis on everything pending, picks the batch's best candidate, and once two batches exist in a month, recommends one for that month's Improvers Club submission). Omri still writes the actual hook/annotation himself.

---

## Recent Work (July 7)

1. **"Through the Gap" newsletter launched (Skill 6 project)** - Brainstormed passion-first income streams for the trip; landed on football economics + inequality as the niche (deepest knowledge + economics background + visual data journalism format). Name: Through the Gap. Platform: Substack (signup in progress, free tier first). First article drafted: "The £116 Million Illusion" - the Anderson £116m transfer as a lens on Forest's PSR survival-selling, the SCR flat-tax problem (85% of unequal revenues = permanent gap), and the private votes (SCR passed 14-6, anchoring killed 12-7). Draft + 5 chart specs + verify-before-publish list at `projects/through-the-gap/articles/2026-07-07_the-116-million-illusion.md`; reusable 9-step article workflow in the project README. Next: finish Substack setup, fact-check pass, build charts in Python. (Note: format now under active reconsideration -- see today's Priority 1 above.)

2. **Git sync + EcoTraders notice outcome logged** - Merged two work-PC branches to master (resolved decisions/log.md conflict), pushed. Logged meeting outcome: Daniel accepted politely, last day Aug 22, no handoff plan discussed. Saved ecotraders-exit memory.

---

## Recent Work (July 6)

1. **Economics seminar POSTER — design direction locked + built via Claude Design MCP** - Iterated the distinction-prize poster through several concepts (electricity bill → thermal map → editorial charts → Economist cover) before landing on an Economist-style cover with a hand-drawn ISOMETRIC bird's-eye illustration (warm terracotta field, Frank Ruhl Libre + Assistant). Corrected the core message: NOT "efficiency beats the source" but "energy independence is most beneficial" — a data center on its own solar + efficient gas plant pays ~54% less for power (Alt 2, ₪0.172 vs ₪0.373/kWh), with PUE efficiency (~25%) as the complementary lever. Workflow: illustration generated in Claude Design, Hebrew text/layout authored in code and pushed back via the DesignSync MCP. Files in the "Israel's Overheating Grid" Claude Design project + local mirror at `Economics Final\Poster\design\`; final assembly = `Poster - Final.dc.html`. Confirmed submitted by the July 7 deadline; presentation July 30.

2. **Improvers Club — July annotated game submission written** - Set up Stockfish (C:\Users\User\OneDrive\Documents\stockfish\) + python-chess for local engine analysis. Analyzed two candidate games at depth 18. Selected game vs. gannu8709049607 (July 1, Re1# back-rank mate). Hook: 4 consecutive engine-best moves (23...Bxd4, 24...Rxc2, 25...Rxe2, 26...Bxb1) converting a won position after a queen/rook fork on move 16. Full written annotation + PGN with embedded comments ready. To submit: import PGN to chess.com/analysis, save as public study, post study link + annotation text to club forum, paste #comment- permalink into the form.

3. **Ronni's psychobiology assignment review** - Read all 4 source articles (Bojesen 2026, Jauhar 2018, Wulff 2015, Kegeles 2010) + assignment brief + tips doc. Extracted text from the submitted .docx via Word COM. Generated full Hebrew review report covering: science accuracy per article, 3 missing bibliography entries (Carlsson 2006, Lieberman 1993, Howes et al. 2009), citation formatting errors throughout (first initials in in-text citations, missing commas, Staufer/Stauffer misspelling), figure references that need replacing with text descriptions, integration paragraph word count flag, and science precision notes on GABA-K3 in AN-FEP and the Kegeles causal reversal claim. Assignment folder: `C:\עמרי ורוני\לימודים\מטלת הכירו את המדע\`.

4. **Energy Program — tax incentive baseline data built, key finding on electric steam** - Per Daniel's 3-step unblocking process, gathered baseline data (2 capacity points, efficiency indicator, annual hours, power) for all 4 model technologies at `projects/energy-program/baseline-technology-data.md`. Revised once after review to use real technology-specific standards (AHRI 550/590 IPLV, EN 14511 COP at A7/W55, CAGI specific power, ASME PTC 4) and manufacturer sourcing (Carrier/Trane/York) instead of generic COP. Key finding: Rafi's ~50% grid-efficiency factor means electric steam conversion's primary-energy "savings" don't clearly beat the fuel-oil baseline (~49% well-to-steam vs ~82-85%) — leaning toward dropping that technology from the model rather than forcing a weak example, pending Daniel's review. Next: review baseline data with Daniel, decide on electric steam, then verify remaining flags with Rafi.

---

## Recent Work (July 1)

1. **September Europe trip — route and destination planning** - Locked core 3-month route: Norway → Scotland → London → Ireland → Portugal (Sept 8 - ~Dec 8). Built out conceptual frameworks for each leg: Norway (DNT huts, Jotunheimen, allemannsretten), Scotland (West Highland Way, Glasgow/Edinburgh), Ireland (Galway/Connemara, west coast surf, trad sessions), Portugal (Rota Vicentina, Peniche/Sagres surf, Porto/Lisbon). Discussed and set aside flex destinations (Iceland, Faroe Islands, Basque Country, Galicia, Azores). Trip is also now the mechanism for career direction exploration (alumni/professor conversations) -- see Priority above.

2. **Repo audit — pruned dead weight** - Reviewed the whole second-brain structure. Archived three abandoned systems to `archives/deprecated-2026-07-01/` (nothing deleted): the daily dashboard automation (stopped running May 31), the Cowork surface (COWORK.md + sessions/ + templates/, still referencing deleted status/next-steps files), and the unused "Routine creator" project. Fixed CLAUDE.md folder map + scripts/README to match; deleted the dead `daily_dashboard_system` memory. Committed + pushed.

3. **Built /weekly-review + scheduled it as a Friday cloud routine** - New command at `.claude/commands/weekly-review.md` is the anti-cruft ritual (reconcile today.md, priorities re-derivation, deadline radar, stale-application flags, stale-automation sweep). Set it to run automatically every Friday 10:00 AM Israel via a scheduled cloud routine. Cloud run is repo-only + non-interactive: auto-reconciles today.md and writes a report to `reviews/weekly-review-YYYY-MM-DD.md`, but does NOT archive cruft or rewrite priorities on its own. Manage at https://claude.ai/code/routines/trig_013e68sBVgyjkdU3UwfBXCR1.

---

## Pending — Needs Rafi's Data

- Annual energy consumption per technology (kWh/year)
- Equipment degradation rate (%/year)
- Heat pump annual operating hours (engineer consult in progress)

*(CapEx no longer Rafi-dependent — Omri has it from his own grant-program extraction, chillers directly sourced in `baseline-technology-data.md`.)*

## Pending — Needs Daniel's Decision

- Discount rate: 6% (social/national) vs 10% (private/industrial)

---

## This Week's Focus

1. **Through the Gap** - Decide on the tool/app direction (or continue the newsletter as-is)
2. **University** - Get briefs for the Final LCA Assignment (due Aug 1) and Final Sustainability Project (due Aug 15) and start once details are in hand
3. **Energy Program** - Opportunistic only: review baseline data with Daniel when there's a natural moment; not a push priority

---

## Quick Links

**Work Projects:**
- [Energy Program](projects/energy-program/)
- [Job Search](projects/job-search/)
- [University](projects/university/)
- [Through the Gap](projects/through-the-gap/)
- [Chess](projects/chess/)
- [Travel](projects/travel/)
- [D&D Campaign](projects/dnd-campaign/) (on hold)

**Workflows & References:**
- [Daily Routine](routine.md)
- [Assignment Tracker](projects/university/tracker.md)
- [Current Priorities](context/current-priorities.md)
- [Job Tracker](projects/job-search/tracker.md)
