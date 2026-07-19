# Today - 2026-07-19

**Date:** 2026-07-19
**Updated:** 2026-07-19

---

## Current Priority

- Through the Gap: reconsidering format -- elevate beyond a newsletter into a revenue-generating tool/app that also hones AI/product/creativity skills and doubles as a portfolio piece
- University: two remaining assignments (Final LCA, due Aug 1; Final Sustainability Project, due Aug 15), plus the poster presentation July 30
- Energy Program (EcoTraders): coast-to-Aug-22 wind-down, not active investment -- opportunistic only (baseline data review with Daniel, verification with Rafi)

---

## Today's Completed

*(nothing yet)*

---

## Recent Work (July 15)

1. **Built a new England vs Argentina edition of the World Cup party quiz for tonight** - New guest (`world-cup-eng-arg.html`) and host (`world-cup-eng-arg-host.html`) versions alongside the original files (not overwritten, in case they're reused later), routed via `vercel.json` at `/world-cup-eng-arg.html` and `/world-cup-eng-arg-host.html`. Same proven structure (predictions, bingo, halftime quiz, ask-Omri, bonus shots) with fixture-specific trivia: 1966 England win, Argentina's 3 titles, the 1986 Maradona "Hand of God"/"Goal of the Century" match, Beckham's 1998 red card. Added knockout-stage fields to predictions/scoring (extra time, penalty winner) since tonight is likely a knockout match. Deliberately left the "current managers" Ask Omri answer blank for Omri to fill in rather than guess at unverifiable 2026 details.
2. **Hardened the WhatsApp share flow for the iPhone sharing issue flagged from last time** - Root cause was never pinned down (Omri didn't specify the exact symptom), so rebuilt the share section defensively: a direct `https://wa.me/?text=` deep link (works on iOS/Android without depending on Web Share API support) plus an always-visible "copy text" fallback with manual paste instructions, replacing the old `navigator.share().catch(() => {})` that could fail silently with no fallback. Added iOS web-app meta tags too, in case the original issue was about opening/pinning the page rather than the in-app share button. **Not yet deployed** - files are built and pushed to the branch, ready for Omri to review and push live once he's home.

---

## Recent Work (July 14)

1. **Started `projects/claude-code-lessons/` to capture lessons from the 6-hour Claude Code manual** - README + tracker built for a multi-session, multi-day backlog (not a one-off brainstorm capture). Wired `/save-context` to also auto-feed it with Claude Code meta-lessons from regular work sessions, not just the manual. Tracker rows are color-coded HTML (green/amber/gray/dark-gray by status), rendered in VS Code Markdown Preview.

2. **Built an explicit "AI Kill List" in communication-style.md** - First lesson from the manual. Concrete banned buzzwords/phrases/structural patterns (AI slop), replacing the old vague "keep it real" line. Applies everywhere including academic docs, living list to keep adding to.

3. **Audited SHMAGS 2 for leaked secrets** - Second lesson (the .env pattern). Confirmed clean: `.env` gitignored and never committed, zero real secret hits across all 225 tracked files and full git history. Urban Analytics/Economics Final folders aren't git repos at all.

4. **Installed and fully configured the gws CLI (googleworkspace/cli)** - Full Google Workspace access (Drive, Gmail, Calendar, Sheets, Docs, Slides, Tasks, Chat) from the terminal. Installed via npm, set up Google Cloud SDK + a new GCP project (`omri-gws-cli`, 44 APIs enabled), manually created the OAuth consent screen + client in Cloud Console, logged in as omrisham53@gmail.com. Verified with live Drive and Calendar queries. Known limitation: Testing-mode refresh tokens expire every 7 days, re-login needed weekly (open item, not yet resolved).

5. **VS Code settings tuned** - New Claude Code sessions default to terminal view (`claudeCode.useTerminal`); all `.md` files default to rendered Preview instead of raw source (`workbench.editorAssociations`).

6. **Built a visual 9-slide Google Slides deck for Itai showcasing Claude Code + gws** - First draft (bullet-based) was rejected in favor of a fully visual rebuild: knowledge-graph diagram, hub-and-spoke app grid, terminal mockups, comparison pills, a security flow diagram, a bar chart, a pipeline flow, and a numbered stepper, all built as native Slides shapes through `gws slides presentations batchUpdate`. Consistent navy/gold/Playfair Display design system. Deck itself demonstrates the tool (built via plain-English brief, no manual Slides editing). Saved as a durable `slide_deck_preferences` memory so future decks start visual-first by default.

7. **Emailed and shared the deck with Itai via gws** - Sent through `gws gmail +send` (not the Gmail MCP, per Omri's request) and shared the deck with him directly on Drive. First draft had the wrong tone (read like a cold pitch, wrongly implied Itai didn't already know about the system) - corrected and saved as a `feedback_friend_emails` memory: match tone to the specific audience, check what the recipient already knows, and accumulate corrections over time into Omri's real per-audience voice.

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

## Pending — Needs Rafi's Data

- Annual energy consumption per technology (kWh/year)
- Equipment degradation rate (%/year)
- Heat pump annual operating hours (engineer consult in progress)

*(CapEx no longer Rafi-dependent -- Omri has it from his own grant-program extraction, chillers directly sourced in `baseline-technology-data.md`.)*

## Pending -- Needs Daniel's Decision

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
- [Claude Code Lessons](projects/claude-code-lessons/)
- [D&D Campaign](projects/dnd-campaign/) (on hold)

**Workflows & References:**
- [Daily Routine](routine.md)
- [Assignment Tracker](projects/university/tracker.md)
- [Current Priorities](context/current-priorities.md)
- [Job Tracker](projects/job-search/tracker.md)
