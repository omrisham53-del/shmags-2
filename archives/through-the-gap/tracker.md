# Through the Gap - Tracker

**Last updated:** 2026-07-24

## Direction Change (2026-07-24)

Newsletter direction dropped. New product: **Window Winners** -- a Premier League transfer-window prediction game. Full reasoning and discovery process in `brainstorms/2026-07-24_through-the-gap-direction.md`. Old newsletter milestones below are superseded (kept for history, not active).

## Recurring Work Schedule (set 2026-07-24)

Two weekly recurring calendar blocks for Window Winners build time, created via `gws calendar`:
- **Tuesday evenings, 19:00-21:00** (starting 2026-07-28)
- **Friday late mornings, 10:00-12:00** (starting 2026-07-31)

## Window Winners - Setup Status

- [x] Concept locked: transfer-window prediction game, hybrid model+fan mechanic
- [x] Name locked: Window Winners
- [x] Scope locked: Premier League only for v1
- [x] Data strategy locked: licensed stats API (football-data.org / API-Football) + own credibility-weighted valuation engine (not scraped from Transfermarkt)
- [x] **Launch target locked (2026-07-25): Friday Aug 21, 2026 (PL 2026/27 season kickoff)**, not the transfer-window close
- [x] **v1 scope cut to fit 4-week timeline**: fan prediction game + leaderboard + sharing ships in full; valuation uses a manually curated list of ~15-20 marquee transfers instead of the full automated aggregation engine (that becomes a post-launch upgrade). Estimated ~40-55 hours / ~10-14 hrs/week over the 4 weeks.
- [x] **Technical architecture locked (2026-07-28)** -- see below
- [x] **Data coverage scope revised (2026-07-28)**: full PL transfer list at launch (not just 15-20), auto-scored wherever API-Football has a real reported fee, rest shown as "not yet graded" -- see below
- [ ] Data pipeline (automated transfer list + fee ingestion via API-Football)
- [ ] Scoring model (squad fit / likely position / XI impact) -- design session planned
- [ ] Fan prediction + leaderboard + sharing UX
- [ ] Repo scaffold (React + Vite + PWA + Supabase)
- [ ] Launch by Aug 21, 2026

## Technical Architecture (locked 2026-07-28)

**Stack:** React + Vite (frontend) + Supabase (Postgres DB, auto-generated API, no custom backend code) + Vercel/Netlify (hosting). Chosen for being the least new-concept path for someone new to backend work -- Supabase tables are defined in a web UI and queried directly from React, no server to write or run.

**App-like feel, cross-device:** PWA via `vite-plugin-pwa` -- installs to home screen on iOS/Android, runs full-screen, no app store needed. Predictions/leaderboard live in Supabase (shared, not local storage), so it's genuinely one competition across everyone's phones, not siloed per device.

**Auth:** No email signup for v1 -- nickname + a device-local ID (stored in browser) mapped to a Supabase row. Removes signup friction that would kill shareability.

**Data model (3 tables):**
1. `transfers` -- full Premier League transfer list, pulled automatically from API-Football's transfers endpoint (player, from/to club, date, fee). Fee comes back as a formatted field: a real amount ("EUR 45M") when publicly reported, or Free/Loan/N/A when not. Where a real fee exists, the scoring model runs automatically against it (position fit, XI impact, valuation verdict). Where it's N/A, the transfer still shows in the list but is marked "not yet graded" rather than faked or skipped.
2. `predictions` -- nickname/device_id + transfer_id + fan's guess + timestamp.
3. Leaderboard is not a stored table -- it's a query comparing `predictions` against the `transfers` verdict (and later, real season outcomes once the season plays out).

**Resolves the "full PL coverage" ask (2026-07-28)** without reopening the 85-115 hour full-automation estimate that got cut on 2026-07-25 -- auto-pulling the transfer list + auto-scoring wherever real fee data exists is a much smaller lift than the credibility-weighted news/social aggregation pipeline that's still deferred as a post-launch upgrade.

**Next session:** scoring model design -- look at reference points (FPL-style points systems, media "grading the transfer window" formats, WhoScored/Sofascore rating methodology) before shaping Omri's own formula, since this is the real technical-growth centerpiece of the project.

## Window Winners - Milestones

| Milestone | Target | Status |
|-----------|--------|--------|
| v1 launch (Premier League, scoped-down valuation, full prediction/leaderboard/sharing) | Aug 21, 2026 (season kickoff) | Not started |
| Automated valuation-aggregation engine (upgrade from manual list) | During trip, before Jan window | Not started |
| Continued build during trip | Sept 2026 - Jan 2027 | Not started |
| Real launch for winter window (full automated pipeline) | January 2027 | Not started |
| Traction goal: real usage/sharing established | By next summer window | Not started |
| Revenue: creator-sponsorship model | Next summer window (~2027) | Parked -- deliberately not the near-term focus (traction + technical growth prioritized first, per Omri's own trilemma call) |

---

## Legacy: Newsletter Tracker (superseded 2026-07-24)

### Setup Status
- [x] Concept locked (football economics + inequality, visual-first)
- [x] Name locked: Through the Gap
- [ ] Substack account created (in progress - Omri walking through signup)
- [ ] URL confirmed (target: throughthegap.substack.com)
- [ ] Logo / header image (placeholder fine for launch)
- [ ] Twitter/X account for distribution

### Article Pipeline

| Article | Status | Target |
|---------|--------|--------|
| The £116 Million Illusion (Anderson / SCR / flat tax) | Draft written 2026-07-07, charts pending | First publish |

### Milestones (superseded)

| Milestone | Target | Status |
|-----------|--------|--------|
| First article published | July 2026 | Superseded -- direction changed |
| 3 articles live + Twitter active | Before trip (Sept 8) | Superseded |
| First 100 free subscribers | During trip | Superseded |
| Turn on paid tier | After 2-3 pieces + early readers | Superseded |
| €100/month | Within ~year one | Superseded |
| €1,000/month | ~2031 | Superseded |
