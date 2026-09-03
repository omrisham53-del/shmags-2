# Through the Gap [ARCHIVED -- DEAD]

> **Killed 2026-09-03** on Omri's explicit instruction: no work on it, no future work planned.
> The Aug 21 launch target passed with the build never started, and it had been flagged as
> stalled in three consecutive weekly reviews. Both recurring calendar build blocks were deleted.
> Everything below this line is historical record, not a live plan.

Football side project. Skill 6 project: a passion-first revenue stream that runs through the September trip and beyond, and doubles as a public portfolio piece.

**Status (2026-07-24): New direction locked -- "Window Winners."** The original football-inequality Substack newsletter is dropped entirely (see brainstorm below for why: no real cost/ceiling to pure article output, and Omri wants to build something more complex). New concept, developed in a full discovery session at `brainstorms/2026-07-24_through-the-gap-direction.md`:

**The product:** A fan prediction game built around the existing, widely-used phrase "who won the transfer window?" -- played during the transfer window itself, when fans are starved for football content and the season hasn't started. Premier League only for v1.

**Mechanic:** Hybrid. Omri builds a real scoring model (fee/valuation vs. squad need/fit vs. likely position and XI impact) that produces a "who's winning the window" verdict per club. Fans make their own predictions alongside it. A leaderboard checks who was right (model vs. fans vs. real season outcomes) once results play out. The prediction/leaderboard layer is the actual shareability engine -- social stakes (bragging rights, being provably right), not information alone, is what makes something spread.

**Data approach:** Playing stats from licensed free APIs (football-data.org / API-Football -- both explicitly permit commercial use). Transfer valuation is deliberately NOT scraped from Transfermarkt (real EU database-rights exposure for a German site with a proprietary valuation database) -- instead, Omri builds his own valuation engine by aggregating reported fees from news articles and social media, weighted by source credibility (e.g. a Fabrizio Romano report weighted higher than an unverified account). This is a stronger technical story than just reusing someone else's number, and it's genuinely original.

**Strategic framing (Omri's own call):** of traction / technical growth / revenue, this project is strongest on the first two -- revenue is explicitly secondary for now. Plan: launch fast and rough to learn, keep developing through the trip and the January winter window, and aim for real scale plus a creator-sponsorship revenue model at **next summer's** window -- once there's actual traction to make that partnership worth a creator's time (a direct fix for why the original creator-distribution idea was rejected: no incentive for a creator to adopt something unproven for free).

**Launch target locked (2026-07-25): Friday Aug 21, 2026 -- Premier League 2026/27 season kickoff**, not the transfer-window close (~Sept 1) originally assumed. That's 4 weeks out, and a full-scope v1 (automated valuation-aggregation pipeline + scoring model + fan prediction/leaderboard) was sized at ~85-115 hours -- too much alongside the Sustainability Project (due Aug 15) and EcoTraders wind-down. **Scoped down to hit the date:**
- v1 ships the fan-facing prediction game + leaderboard + sharing UX in full -- this is the real traction/shareability engine, don't cut it
- Valuation for v1 uses a **manually curated list of ~15-20 marquee Premier League transfers** instead of the full automated news/social aggregation engine
- The automated credibility-weighted valuation pipeline becomes a **post-launch upgrade**, built during the continued-development phase through the trip and the January window
- Revised estimate: ~40-55 hours over 4 weeks (~10-14 hrs/week) -- tight but realistic alongside other August deadlines

**Still open:**
- Whether this becomes a deliberate football-industry-career portfolio piece, or stays separate from Career Direction Exploration (genuinely undecided, not blocking)
- Whether the fan-prediction/sharing UX is really as low-effort as assumed (flagged for a reality check once real build scoping starts)
- Whether the project folder/repo name stays "Through the Gap" or renames to match the product name "Window Winners"

**Name logic (legacy):** "Through the Gap" was originally a double meaning -- a football phrase (a pass threaded through a tight space) and the club-inequality gap that was the newsletter's editorial spine. That inequality storyline is dropped; the name may or may not still fit "Window Winners" going forward.

---

## Legacy: Newsletter Workflow (superseded, kept for reference)

The original concept (July 2026) was a football-economics Substack newsletter with a 9-step article workflow (idea -> saturation check -> research sprint -> narrative lock -> structure+charts -> draft -> fact check -> build charts -> publish+distribute). One article was published ("The £116 Million Illusion"). This workflow is no longer the active direction but is kept here in case any piece of it becomes useful again (e.g. research/fact-checking discipline).

## Files

- `articles/` - Legacy newsletter article(s) from the original direction.
- `tracker.md` - Project status; will track Window Winners build milestones going forward.
