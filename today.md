# Today - 2026-07-31

**Date:** 2026-07-31
**Updated:** 2026-07-31

---

## Current Priority

- **University:** Economics paper presentation -- script finalized, first-draft slide deck built and sent to Tomer for messaging/storytelling feedback. Thursday July 30 presentation. Prep call with lecturer Osnat proposed for Tuesday 7/28 -- Omri asked to move it earlier to 14:30, no reply yet as of 7/24. Final LCA (due Aug 1) -- full draft + submission-ready .docx built, handed to Omri for his own final edits in Word (functionally done). Final Sustainability Project (due Aug 15) is the one real assignment left in the whole degree, still TBD.
- **EcoTraders (scope locked 2026-07-26):** Daniel confirmed no new assignments before Omri's Aug 22 last day -- remaining work is exactly 3 items: (1) finish the tax incentive model, including the market analysis, (2) write the tax incentive chapter for the national program, (3) write the loan fund chapter for the actual national program (appendix version reuses the already-written position paper, only the full chapter needs writing). Going into that meeting, the model already had the payback-threshold reframe live (3-year hurdle, Rafi's own number) -- only chillers (100RT/500RT) show genuine additionality, heat pumps and VSD are worth it without the incentive (deadweight); electricity tariff fixed to 39.54 agorot/kWh (real HV תעו"ז average); a 3-page meeting-prep PDF covered the reframe, technology emphasis, dual fiscal-cost reporting, and the PRTR market-sizing lead (`brainstorms/2026-07-26_payback-threshold-and-meeting-prep.md`). Full day-by-day block schedule built 2026-07-27 covering Jul 27 -- Aug 20 (Sun/Mon/Wed full days, Thu half days -- Omri's real EcoTraders work schedule), see `projects/energy-program/tracker.md`. No career future here (coasting) but genuinely engaged -- interesting Excel modeling work.
- **Through the Gap -> "Window Winners":** newsletter direction dropped entirely. New concept locked via a full discovery session (7/24): a Premier League transfer-window prediction game -- hybrid model (Omri's own scoring engine for squad fit/impact + a credibility-weighted valuation aggregator from news/social, not scraped from Transfermarkt for legal reasons) plus fan predictions and a leaderboard. Traction + technical growth prioritized over revenue for now. **Launch target locked (7/25): Aug 21, 2026 -- PL season kickoff**, not Sept 1. Full v1 sized at ~85-115 hours (too much alongside the Sustainability Project + EcoTraders wind-down), so scoped down: prediction game/leaderboard/sharing ships in full, valuation uses a manually curated list of ~15-20 transfers instead of the full automated aggregation engine (that becomes a post-launch upgrade). Revised estimate ~40-55 hours (~10-14 hrs/week) over the 4 weeks to launch. Full capture: `brainstorms/2026-07-24_through-the-gap-direction.md`.
- **Norway trip:** given a formal priority slot (constant background project, not the main focus) -- family member gave real travel/equipment/food info, prep session still pending.

---

## Today's Completed

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
