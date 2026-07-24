# Through the Gap

Football side project. Skill 6 project: a passion-first revenue stream that runs through the September trip and beyond, and doubles as a public portfolio piece.

**Status (2026-07-24): New direction locked -- "Window Winners."** The original football-inequality Substack newsletter is dropped entirely (see brainstorm below for why: no real cost/ceiling to pure article output, and Omri wants to build something more complex). New concept, developed in a full discovery session at `brainstorms/2026-07-24_through-the-gap-direction.md`:

**The product:** A fan prediction game built around the existing, widely-used phrase "who won the transfer window?" -- played during the transfer window itself, when fans are starved for football content and the season hasn't started. Premier League only for v1.

**Mechanic:** Hybrid. Omri builds a real scoring model (fee/valuation vs. squad need/fit vs. likely position and XI impact) that produces a "who's winning the window" verdict per club. Fans make their own predictions alongside it. A leaderboard checks who was right (model vs. fans vs. real season outcomes) once results play out. The prediction/leaderboard layer is the actual shareability engine -- social stakes (bragging rights, being provably right), not information alone, is what makes something spread.

**Data approach:** Playing stats from licensed free APIs (football-data.org / API-Football -- both explicitly permit commercial use). Transfer valuation is deliberately NOT scraped from Transfermarkt (real EU database-rights exposure for a German site with a proprietary valuation database) -- instead, Omri builds his own valuation engine by aggregating reported fees from news articles and social media, weighted by source credibility (e.g. a Fabrizio Romano report weighted higher than an unverified account). This is a stronger technical story than just reusing someone else's number, and it's genuinely original.

**Strategic framing (Omri's own call):** of traction / technical growth / revenue, this project is strongest on the first two -- revenue is explicitly secondary for now. Plan: launch fast and rough for the current summer window (closing ~Sept 1) to learn, keep developing through the trip and the January winter window, and aim for real scale plus a creator-sponsorship revenue model at **next summer's** window -- once there's actual traction to make that partnership worth a creator's time (a direct fix for why the original creator-distribution idea was rejected: no incentive for a creator to adopt something unproven for free).

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
