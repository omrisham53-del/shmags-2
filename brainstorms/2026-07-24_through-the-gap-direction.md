# Through the Gap: New Direction Brainstorm

Date: 2026-07-24 · Goal: Find a new subject/format for the "Through the Gap" side project after the football-economics newsletter angle stopped feeling interesting enough. Must still hit all four original goals: (a) generate revenue, (b) be genuinely useful to Omri and people around him, (c) hone AI/product/creativity skills, (d) serve as a public portfolio piece for his next career step.

## Summary / key decisions

**The idea: "Window Winners."** A fan-facing prediction game built around the existing, widely-used phrase "who won the transfer window?" -- played *during* the transfer window itself, when fans are starved for football content and the season hasn't started. Premier League only for v1.

**Mechanic:** Hybrid. Omri builds a real scoring model (fee/valuation vs. squad need/fit vs. likely position and XI impact) that produces a "who's winning the window" verdict per club; fans make their own predictions alongside it; a leaderboard checks who was right (model vs. fans vs. real season outcomes) once the season plays out. The prediction/leaderboard layer is what gives fans a reason to share -- social stakes (bragging rights), not just information, is what actually spreads (this is why the earlier creator-distributed "calculator" idea failed -- see Q5/Q6).

**Data approach:** Playing stats from licensed free APIs (football-data.org / API-Football, both explicitly permit commercial use). Transfer valuation is NOT scraped from Transfermarkt (real EU database-rights exposure, see Q12) -- instead, Omri builds his own valuation engine by aggregating reported fees from news articles and social media, weighted by source credibility. This is a stronger technical story than reusing someone else's number.

**Strategic framing (Omri's own trilemma):** traction and technical growth are the real goals; revenue is explicitly secondary for now. Launch fast and rough for the current window (closing ~Sept 1) to learn, keep developing through the trip and the January window, and aim for real scale + a creator-sponsorship revenue model at next summer's window -- once there's actual traction to make that partnership worth a creator's time (which is what killed the idea at Q6 in its original form).

**Still open:** whether this becomes a deliberate football-industry portfolio piece or stays separate from career exploration (genuinely undecided, not blocking); whether the fan-prediction/sharing UX is really as easy as assumed (flagged for a reality check at build time); and whether the project folder renames from "Through the Gap" to match "Window Winners."

## Q&A log

### Q1 - Subject vs. format: what actually stopped landing
- Asked: Is football still the domain, or has enthusiasm shifted away from football entirely?
- Captured: Football/football-industry-as-career-adjacent subject is NOT the problem -- it's still real passion and knowledge. The actual rejection is narrower and more specific than "format": Omri doesn't want to be an "article spam" operation writing football-inequality pieces with no real cost/no real ceiling. He wants to build something more complex -- an app/website/platform that (1) demonstrates he can build real things with AI, (2) is a place for football passion, (3) generates some revenue, and (4) exists for personal growth as much as career signaling. New thread surfaced: working IN the football industry, in an economics-graduate-adjacent role, is "a really interesting direction" he hasn't explored much but has real passion + knowledge for -- this may reframe the whole project from "content about football" to something connected to actually working in football.
- Flags: Whether "working in football industry" is (a) a hint that Through the Gap should function as a portfolio/audition piece aimed at football-industry roles specifically, or (b) a separate career-direction thread from Career Direction Exploration (Priority 3) that just surfaced here -- needs resolving next.

### Q2 - Dual-purpose (audition piece) vs. staying separate from career exploration
- Asked: Does the football-industry-career idea sharpen Through the Gap into a deliberate audition piece, or stay a separate thread for Priority 3 (Career Direction Exploration)?
- Captured: Genuinely undecided, not a stall -- "in the middle of both." Don't force a hard commitment either way right now.
- Flags: Design the project so it doesn't require this to be resolved yet -- build something that's real/useful/impressive on its own merits, which keeps optionality open for both (A) and (B) rather than picking a lane prematurely.

### Q3 - What the platform actually does
- Asked: What specific thing would make Omri proud to have built -- analytical tool, interactive explainer, or fan utility?
- Captured: **Fan utility, built around transfers**, not the inequality storyline -- inequality doesn't hold fan attention long enough to be the product. Transfers are the right subject because it's a live, recurring, high-attention moment (the transfer window is happening right now). Omri mapped out how fans currently get transfer info, in three tiers: (1) highlight reels on YouTube -- visual, fast, but shallow (just "does this player look good"); (2) real underlying data -- deep and real, but only a small minority of fans ever go there; (3) fan channels/pundits -- narrative, opinionated, entertaining, and this is the tier Omri himself actually follows and trusts. Explicitly looking for a **gap**: something that doesn't already exist for fans to play with or use to understand a transfer window signing.
- Flags: The precise nature of the gap (what's missing between highlights/data/pundit-opinion) isn't pinned down yet -- next question.

### Q4 - Naming the actual gap
- Asked: Of speed / translation / verdict / social comparison (or something else), which is the real missing piece?
- Captured: **All four combined, not a single pick.** Key points in Omri's own words:
  - **Speed is non-negotiable** -- long-form articles/docs are not how fans consume content anymore. Whatever this is, it has to be fast.
  - **Data should sit alongside highlights**, not replace them -- highlights alone "don't tell the whole story," but a wall of stats isn't the answer either. The data needs to be translated into something as consumable as a highlight clip.
  - **A verdict is the core deliverable**: fans want to know the player's likely position, what the club's starting XI looks like next season with them in it, and how much real impact this signing can have. Not raw stats -- a conclusion.
  - **Positioning vs. existing social-media discussion**: the tool should analyze a transfer "much deeper, faster" than fans arguing on social media can -- essentially a calculator/indicator of real club impact, not another voice in the debate.
  - **The business/financial side matters and is trending** -- fee, valuation, financial context -- this is Omri's own natural strength (economics background) and should be a real layer of the tool, not just player performance.
  - **Revenue model idea**: not primarily a consumer subscription -- lean toward **partnering with social media creators/fan channels** (the tier Omri himself already follows and trusts) by giving them a real tool to lean on and present with, forming their on-camera opinion faster/better. Creator tool / B2B(2C) angle, not just a direct-to-fan product.
- Flags: none -- this is now a clear, coherent shape: a fast transfer-impact tool (position/XI-fit/impact verdict + business context) built partly *for* the creator tier as a presentation aid, not just for solo fan consumption.

### Q5 - Who's the direct user: fan, creator, or both
- Asked: Self-serve public tool, a content-as-a-service pipeline for creators, or both on the same engine?
- Captured: **(C) Both** -- one underlying engine, two surfaces. Reasoning: creators can act as a marketing/distribution channel -- if they use the tool on camera, their audience follows the link and comes to use it themselves / share their own opinions. But Omri immediately self-caught a real gap in this logic: **there's no established reason for a creator to actually use it, unless they're paid for it.** Visibility for the tool isn't automatically valuable to a creator who already has their own process and audience.
- Flags: The creator's actual incentive to adopt the tool (absent direct payment) is unresolved -- this is the load-bearing open question before revenue model can be finalized. Next question.

### Q6 - Creator incentive, and the verdict on this idea
- Asked: What makes a creator use the tool for free -- time savings, a visual edge, or accept it as pure marketing spend?
- Captured: **Omri rejected the creator-distribution model outright.** His reasoning: this kind of tool would only ever reach fans through someone they already follow using it first -- meaning discovery is entirely bottlenecked on creator adoption, which has no real incentive behind it (per Q5/Q6). A distribution plan that depends completely on a group with no reason to participate is a dead end, not a detail to patch later.
- **VERDICT: "Transfer impact calculator distributed via creators" idea shelved.** Not because the fan-utility direction or the transfer-window subject was wrong -- specifically because the distribution mechanism (creator-dependent) doesn't hold up. Omri wants to keep brainstorming for a different idea.
- Flags: none -- clean rejection with a clear, specific reason (useful to remember so the next idea doesn't repeat the same distribution trap).

### Q7 - Why would fans share this at all (shareability problem)
- Asked: Fan-to-fan distribution alone would be slow -- what would actually make a fan want to share their take on a transfer, vs. just commenting or making a meme?
- Captured: Real problem correctly identified -- static information/verdicts don't spread, only things with social stakes (ego, bragging rights, being provably right) do, same reason fantasy football is shareable and a stats page isn't. Claude proposed a prediction/scoring game mechanic (fans predict impact, checkable later, leaderboard vs. friends) as one way to create that stake without needing creator distribution.
- This directly sparked the real idea below.

### Q8 - THE IDEA: "Who won the transfer window?" as a fantasy game
- Captured: Omri landed on a concrete concept -- **a fantasy-style game built around the already-existing, widely-used phrase "Who won the transfer window?"** Instead of a static verdict tool or a creator-distributed calculator, this is something fans directly predict and play with **during the transfer window itself** -- exactly the dead-time period when the season hasn't started yet and fans are starved for anything football-related to obsess over. This solves multiple open problems at once: it doesn't need creator adoption to spread (Q6's dead end), it has an inherent reason to be shared (predicting/competing, same mechanic as fantasy football, per Q7), and it uses a real cultural phrase/moment that already has built-in fan attention rather than needing to manufacture interest.
- Flags: Core mechanic still needs to be defined -- what determines "who won" (a data-driven model Omri builds vs. fan community consensus/voting vs. a hybrid where fan predictions are scored against a model and real season outcomes) -- next question.

### Q9 - Core mechanic confirmed + strategic framing
- Asked: Pure fan voting, Omri's own model, or a hybrid (model + fan predictions + real season outcomes later)?
- Captured: **Hybrid confirmed.** Omri is genuinely excited about this project for two specific reasons: (1) it's a real test of whether something he creates can gain organic popularity/traction, and (2) it's a technically complex analytical build that shows off real skill -- both matter to him more than the money.
- **Explicit trilemma framing (Omri's own words): traction, technical growth, and revenue -- pick where the weight goes.** He places this project as strongest on **traction** and **technical growth**, with **revenue explicitly weaker/secondary**. This should govern every downstream build decision -- don't over-optimize for monetization mechanics early; optimize for something people actually use/share and that is technically real (not a shallow wrapper).
- Flags: none -- this is a clear, decided prioritization that should be referenced whenever a build tradeoff comes up later (e.g. MVP scope, what to build first).

### Q10 - Timeline: chase this window or build for January
- Asked: Rush something real for the current (closing ~Sept 1) window, or build deliberately for a January winter-window launch?
- Captured: **Launch as fast as possible, now.** Reasoning: an early rough launch lets Omri experiment and learn how to actually develop the product before the bigger winter-window version. Explicit long-horizon plan: the project keeps developing continuously (through the trip, presumably lower-intensity) from now through the January window and on to **next summer's window** as the real target for scale. Revenue plan reopens at that later stage too -- if the free/organic period builds real traction, Omri would look at **sponsoring through creators** for next summer's window. This resolves the earlier creator-incentive dead end (Q6): creators would have real reason to partner once the tool already has proven traction/an audience to point to, rather than being asked to adopt something unproven for free.
- Flags: MVP scope for the fast initial launch isn't defined yet (what leagues/transfers/features are actually feasible before Sept 8, given Omri also has the Sustainability Project due Aug 15, EcoTraders wind-down, and Norway trip prep competing for time) -- next question.

### Q11 - MVP scope
- Asked: What's realistically shippable before Sept 8, given competing deadlines (Sustainability Project, EcoTraders, Norway prep)?
- Captured: **Premier League only** for v1 (highest attention, most available data). **Transfer data pipeline must be automated, not manually curated** -- Omri is explicit this is "the true technical growth" he wants out of the project, i.e. the point isn't just the idea, it's building a real automated system. The **model score is the real development effort** and where he wants to invest build time. The **fan-prediction/sharing layer he considers comparatively easy** -- "not complex analytical work, just UX and sharing options" -- so he'd expect that to ship alongside the model without much extra effort.
- Flags: Omri flagged his own uncertainty on this ("I'm not sure on this") re: how easy the fan-prediction/sharing layer really is. Worth a gentle challenge later -- sharing/virality UX is a common place builders underestimate real effort (the mechanic that makes something spread is usually its own hard design problem, per Q7). Not resolved now, just noted so it doesn't get waved through unchallenged when scoping actual build work.

### Q12 - Data sourcing legality (research, not a preference question)
- Asked: Is scraping Transfermarkt (or similar) legally risky for a revenue-generating product, vs. using a licensed API?
- Researched: Public-page scraping generally doesn't violate computer-fraud law (hiQ v. LinkedIn precedent), but two separate risks remain regardless: (1) breach-of-contract exposure if a site's ToS prohibits scraping (they can cease-and-desist / IP-ban / sue for breach, even if not "hacking"), and (2) **EU sui generis database rights** -- Transfermarkt is German, and the EU has a database-protection right (separate from copyright) specifically designed to protect sites with "substantial investment" in their database against systematic extraction/reuse, which is a real and specific exposure for a proprietary sports-valuation site like this. Could not fetch Transfermarkt's actual ToS text directly (blocked in this environment) -- Omri should read it himself before deciding. Circumstantial signal: no official Transfermarkt API exists, but a whole paid scraping-tool ecosystem (Apify/Bright Data/ScrapingBee) does -- proves technical feasibility, not legal safety. A comparable site (FotMob) explicitly bans commercial scraping in its own ToS.
- **Recommendation given**: football-data.org and API-Football both explicitly permit commercial use (paid tiers, some free) and cover fixtures/squads/transfers/stats -- a genuinely licensed path. They don't include Transfermarkt's proprietary "market value" number specifically, which reframes as a positive: build Omri's **own** valuation/impact model from licensed raw data instead of re-displaying someone else's proprietary number -- stronger technical-growth story (Q9/Q11) and avoids the legal question entirely.
- Flags: Omri should personally read Transfermarkt's actual ToS before ruling it fully out, since this session's research was necessarily circumstantial (couldn't access the source directly). Licensed-API path (football-data.org / API-Football) is the safe default recommendation either way.

### Q13 - Valuation approach without scraping a proprietary database
- Captured: Omri proposed a genuinely original approach -- **actual playing stats sourced from free licensed APIs** (football-data.org / API-Football), while **transfer value is estimated by aggregating reported fees from public news articles and social media posts, weighted by source credibility** (e.g. a Fabrizio Romano report weighted higher than an unverified account). This sidesteps the Transfermarkt database-rights question entirely -- reported fee figures in news coverage are widely-republished factual reporting, not a single site's curated proprietary database -- while also being a more interesting technical build (source aggregation + credibility weighting is a real NLP/data problem, not just an API call).
- Flags: none -- this resolves the data-sourcing question cleanly and reinforces the technical-growth angle (Q9/Q11) even further: the "verdict" layer isn't just squad-fit math, it's also Omri's own credibility-weighted valuation consensus engine.

### Q14 - Product name
- Asked: Does a shorter real football phrase work better than the literal "Who won the transfer window?"
- Captured: **"Window Winners" confirmed.** Omri had already independently thought of it before it was offered as an option -- strong signal it's the right fit, not just an acceptable pick. This is the product/game name; whether the umbrella project folder stays named "Through the Gap" or also renames is a small open item, not decided here.
- Flags: none.

## Open flags (pending input)
- Whether Through the Gap ends up read as a football-industry audition piece or stays a separate passion/skill project -> genuinely open, revisit later (maybe during the trip's career exploration, Priority 3)
- Whether the fan-prediction/sharing layer is really as low-effort as assumed -> flagged for a later reality check when actual build scoping starts
- Omri to personally verify Transfermarkt's ToS wording before fully ruling out that data source -> his own follow-up (lower priority now that the aggregation approach avoids needing it)
- Monetization mechanics (creator sponsorship model) -> parked until next summer's window per Omri's own plan
- Whether the project folder/repo stays "through-the-gap" or renames to match "Window Winners" -> small housekeeping decision, not blocking
