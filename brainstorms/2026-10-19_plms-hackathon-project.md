# Microsoft x Premier League "Inside the Game" Hackathon: Brainstorm / Discovery Notes
Date: 2026-10-19 · Goal: pick a project Omri can actually finish by Oct 27 that doubles as a LinkedIn portfolio piece, builds real AI skills, and is genuinely interesting to him

## The hackathon, as researched (not from Omri)

**Event:** Inside the Game: Developer Hackathon, Microsoft + Premier League. Free, open to the public, fully remote.
Official repo: `github.com/microsoft/insidethegamehackathon` · Platform: Microsoft "Innovation Studio"

**Dates (all Pacific Time):**
| Phase | When |
|---|---|
| Registration | Sep 29 - **Oct 20, 12:00 PT** (Omri already registered) |
| Hacking / submission | Oct 6 - **Oct 27, 23:59 PT** |
| Judging | Oct 27 - Nov 10 |
| Winners announced | by Nov 20 |

**Oct 27 23:59 PT = Oct 28, 09:59 Israel time.** From today that is 8 days and change.

**The challenge:** build an AI solution that turns *synthetic* football event data into explainable match intelligence for broadcast/streaming. The stated 5-stage pipeline: Ingest synthetic match events -> Interpret into stats/patterns -> Explain why a moment matters -> Render for on-screen display -> Personalize per audience (analyst vs casual fan, multi-language).

Suggested feature territory (not mandatory): player ID with speed/distance triggers, pass-quality metrics (distance, accuracy, difficulty), ball and shot speed, auto-eventing, narrative generation beyond raw metrics, multi-language storytelling.

**Hard rules that matter:**
- Synthetic data only. No real match footage. "Synthetic data quality" is itself a judged item, so generating believable football event data is part of the build, not a shortcut around it.
- Project must be newly built (after Sep 29).
- Teams of up to 4. One person may be on multiple teams and also submit solo.
- Public GitHub repo required.
- Demo video under 2 minutes, public URL. Judges are not obliged to watch past 2:00.
- Written pitch: what it is, which Microsoft/Azure tech, what problem it solves.
- Must be testable by judges (live demo/site, creds if gated).

**Judging - 5 criteria, 20% each:**
1. Technological Implementation (synthetic data quality, software practice, use of "hero tech": Microsoft Foundry, Agent Framework, Azure MCP, Copilot Agent Mode, Fabric, GitHub SDK/CLI, Azure Apps + AI Services, Azure DBs)
2. Agentic Design & Innovation (agent orchestration, MCP, multi-agent novelty)
3. Real-World Impact & Applicability
4. User Experience & Presentation (UX, demo clarity, front/back balance)
5. Adherence to Hackathon Category

**Prizes:** ~$50K pool. 1st: ~$4,000/member + PL match ticket (~$1,000) + store voucher. 2nd: ~$2,500/member + ticket + voucher. Plus 4 category prizes at ~$1,500/member: Best Foundry Use, Best Enterprise, Best Multi-Agent, Best Azure Cloud Native. A project can win at most one Grand + one Category.

**Observed from other entrants' public repos:** no official dataset is handed out. Teams write their own match-event generator (one team built "MatchFab", a Go synthetic match engine) and stream it, e.g. into Azure Event Hubs, then process. So the synthetic generator is a build item everyone owns themselves.

**Competition read:** the repo already has 55 stars / 12 forks and multiple public entrant repos, several of them multi-agent + Fabric + Event Hubs architectures. Field is real but not enormous.

## Summary / key decisions

Research was done before any questions. The tension going in was the deadline colliding with the trip; Q1 corrected the premise (he is already in Portugal, London is over), which freed a real build window.

**Interview complete. See "FINAL PLAN OF RECORD" at the bottom of this file for the consolidated plan.**

Headlines:
- **HoTake** - an AI football pundit called **Clive** with a CRT-monitor head. Stat-based, has opinions, provokes the room, and keeps score of its own calls as well as yours.
- Solo. Portfolio-and-skills first, prize explicitly not the goal. Target the **Best Multi-Agent** category only.
- Skill target: **multi-agent orchestration** on Microsoft Agent Framework. Frontend deliberately demoted.
- **Code-complete Oct 24**, not Oct 27. Safety submission Oct 23 (editing during the submission period is permitted). Surf-camp window Oct 25-27 is for the LinkedIn video and post only.
- Two videos: a functional one for judges (Oct 24), an AI-generated comedy one for LinkedIn (Oct 25-27). Nothing gets filmed.

## Q&A log


### Q1 - Real time budget
- Asked: how many focused hours between now and Oct 27, and where do they sit? (recommended assuming 20-25h, fragmented, surf camp ~zero)
- Captured: **Correction - Omri is already in Portugal**, not London. The London leg is over or dropped (today.md is stale on this, says "London through ~Oct 24"). Until the surf camp starts Oct 25 he has "all the time I want" to work on this. Once the surf camp starts it becomes "a hurdle" but he'd still get **at least 2 hours/day**.
- Two other things competing for the same hours, named by him: the **chess journey** and the **surf journey** (learning to surf). So this is not an exclusive time budget even in the open days.
- Working budget: **Oct 19-24, ~6 open days** of substantial time shared with chess/surf, then **Oct 25-27 at ~2h/day (~6h)**. Realistic total in the **35-50 hour** range - far more than the 20-25h assumed. This supports a materially more ambitious build than a weekend hack.
- Flags: today.md needs correcting on current location -> Omri (do at save-context)

### Q2 - Solo or team
- Asked: solo or recruit up to 3 others? (recommended solo: timezone, coordination overhead eats the uninterrupted hours, portfolio story is stronger as sole builder, prizes are per-member so a team doesn't multiply payout; registration closes Oct 20 12:00 PT so any teammate must register by then)
- Captured: **Solo. Confirmed, no hesitation.** Team question is now closed - registration closes tomorrow so it is also effectively irreversible.
- Consequence: everything downstream must be scoped to one person's 35-50 hours. No parallel workstreams, no "someone else does the frontend."

### Q3 - Goal ranking / what to optimize for
- Asked: 8 hours on Azure plumbing (Event Hubs/Fabric/Foundry, 20% of score, invisible in demo) vs the agent+UI layer (40% of score, visible to recruiters)? (recommended: portfolio-first, aim at the Best Multi-Agent *category* prize not the Grand Prize, add the cheapest credible Azure slice to clear the hero-tech bar)
- Captured: **"Yes this matches my intentions exactly. I was never expecting to win the competition, but more to develop skills and show them off."**
- **Success condition is therefore locked:** a working thing with a public link + a <2min video + a LinkedIn post that gets real engagement. Skill development and visible proof of it are the deliverables. A prize is upside, explicitly not the target.
- Design rules that fall out of this:
  - Optimize for *demoability*. If it cannot be seen in 120 seconds it is near-worthless to this project's real goal.
  - Agentic/multi-agent design is the deliberate skill target - it is the highest-value thing to be able to claim in late 2026 and it is 20% of the scorecard anyway.
  - Azure is a **box to tick cheaply**, not a thing to go deep on. Minimum credible slice only.
  - Do not chase the Grand Prize. Do not build for "enterprise readiness."

### Q4 - Skill target + honest baseline
- Asked: does "hone my AI skills" mean agent architecture, or "I can ship a real full-stack app"? Put the real baseline on the table first: Window Winners was scoped React+Vite+Supabase explicitly because he was new to backend, and the build never started before the project was killed. What he has genuinely shipped end to end is analytical (Excel models, Python data/chart/docx pipelines, papers, decks) plus very capable direction of Claude Code. He has never shipped a working web app.
- Captured: **Agent architecture.** His words: "more reasonable and actually more interesting and developing... The front end is cool but it's only the last part. I'm sure that agent architecture will be more relevant to my next job rather than design and frontend work."
- **Skill target locked: multi-agent orchestration + prompt/system design.** He owns the reasoning layer and the agent handoff design. This deliberately plays to his real strength (systems thinking, framing analytical problems, football domain depth) and away from his weakest (frontend craft).
- Frontend is explicitly demoted to "the last part" - a thin shell, built late, carried by Claude Code. It must still exist because UX/Presentation is 20% and the demo video is the portfolio artifact, but it is not where the hours or the learning go.
- Career framing is his own: agent architecture is what he judges relevant to his next role, not design/frontend.

### Q5 - What specifically about football pulls him
- Asked: fan/social layer vs tactical-analytical vs transfers? Flagged that the crowded entrant lane is broadcast-grade commentary (LiveDesk, the-ninety-labs, inside-the-game all do multilingual commentary/recaps for studios) so building an AI commentary generator means competing head-on and looking identical. Also explicitly did NOT propose football economics - ruled out by him 2026-07-17 as "not interesting enough", treated as settled.
- Captured, his words: *"the thing that I like most to do with my friends who follow football closely is discussing predictions and watching games while analyzing tactics and events throughout the game. That field is definitely the most interesting, and I need to find a way how to mix the fan engagement with the clever AI analysis of the tactics and statistics"*
- **Concept seed locked: fan engagement x clever AI tactical/statistical analysis.** Specifically the *knowledgeable* fan watching with friends - not the casual fan, not the broadcast studio. The in-group that argues tactics live and makes predictions.
- Prior-art pattern this is consistent with: two World Cup watch-party apps built for real friends (predictions, bingo, halftime quiz, bragging rights), and Window Winners framed as a prediction game because social stakes spread, not information.
- Useful consequence of the synthetic-data-only rule: there is no real live match to hook into, so a **simulated live match clock is required anyway** - a real-time "watching along" demo is the natural shape, not a workaround.

### Q6 - The AI's job in the room: feed the argument or settle it
- Asked: (a) feed it - tactical analysis companion, the smartest friend in the room; (b) settle it - prediction/hot-take referee that adjudicates the group's calls against tactical evidence; or a third framing? (recommended b with a as the engine inside it)
- Captured, his words: *"I love the third framing. It's basically a smart friend in the room that enhances the watching experience and adds a clever analysis. It's like having a pundit with you in the room, but has a very stat-based view and creates conversations constantly."*
- **This is a genuinely distinct third thing, better than either option offered.** Not passive analysis (a), not pure adjudication (b), but an **AI pundit that actively drives the conversation**: provokes takes and predictions, challenges the group, then holds them to account with stats.
- Three load-bearing properties, all his:
  1. **Pundit, not commentator.** Has opinions and a point of view. Sits with you, talks to you - does not narrate at you. This is what separates it from the crowded commentary lane.
  2. **"Very stat-based view."** Its authority comes from data, not vibes - the deliberate inversion of real TV punditry. Strong LinkedIn hook sitting right here: TV pundits talk from the gut; this one structurally cannot.
  3. **"Creates conversations constantly."** The active ingredient. Success is measured by whether the room starts talking, not whether the output is accurate. It is *generative of social interaction*, not merely responsive to it.
- Architecture implication: still maps cleanly to multi-agent (watcher on the event stream -> tactical interpreter -> pundit/persona with a POV -> adjudicator holding takes to account), so the orchestration learning goal survives intact.

### Q7 - How real does "the room" need to be
- Asked: (a) single seat - you + pundit, no accounts/multiplayer/voice; (b) real multi-user room with session codes + shared leaderboard; (c) voice input, it listens to the room. (recommended (a) built as the first seat of a multi-user product: (b) is exactly the real-time shared-state backend problem that sat in front of Window Winners and never got started AND is invisible in a 2-min video since a solo demo of a multi-user app looks identical to a single-user one; (c) is a hackathon grave - speech-to-text over a noisy living room, solo, 8 days. But flagged voice *output* as genuinely different: ~2h with a TTS call and far more convincing on video.)
- Captured: **"single seat with a voice if we have time sounds great"**
- **Decided: single seat.** No multi-user, no accounts, no shared state. Pitched as the first seat of a multi-user product - "rooms are next" goes in the written pitch, costs nothing.
- **Voice output = explicit stretch goal, not v1 scope.** Gated on time. Must not be on the critical path; the build has to be complete and demo-able with text only, then TTS layers on top if hours remain.
- The loop that must be visible in the demo: **provoke -> user's take -> match unfolds -> evidence -> verdict.** One seat shows this completely.

### Q8 - Richness of the synthetic data
- Asked: event-level (~4h) vs positional tracking (22 players at high frequency, 15h+, would eat the whole budget)? Recommended **simulating at the tactical-state level, not the player-coordinate level**: generator emits an event stream (minute, team, player, zone, outcome) *plus* a small set of declared tactical state variables that tick over the match (pressing intensity, defensive line height, territory share, momentum, shape). The generator decides those states and they drive which events become likely, rather than deriving them from simulated bodies. Plus: **seed the generator** so the demo match is reproducible and the video never depends on a lucky run, while a judge can still reseed it.
- Captured: **Agreed - "within the timeframe that's the best option."**
- **Omri's addition:** calibrate the generator against **past real games** so the generated match looks genuinely realistic in the demo video.
- Why his addition is safe and actually strengthens the submission: calibrating a generator on real *statistical distributions* is not using real match footage, and the output remains fully synthetic. It directly raises the "synthetic data quality" score, which is an explicitly judged item. Clean sources: publicly published aggregate PL stats (goals/shots/pass-completion/xG distributions) or StatsBomb Open Data for distribution shapes.
- Guardrails to respect while doing it: **do not redistribute** any real dataset in the public repo (calibrate from it, reference it, ship only the synthetic output + the generator), and avoid any scraped or licensed feed (Opta, Transfermarkt) - same EU database-right exposure already identified for Window Winners on 2026-07-24.
- Flags: **real club/player names vs fictional** -> unresolved. Rules bar "unlicensed third-party trademarks", but it is a Premier-League-sponsored hackathon so real clubs may be expected. Safest default is plausible fictional clubs, or real club names with no crests/logos. Decide before the generator is written -> Omri

### Q9 - Trigger design: when the pundit speaks, and the self-accountability twist
- Asked: proposed three trigger types - (1) **state-change triggers**, it speaks when the tactical state shifts rather than when something obvious happens (everyone sees the goal; only this pundit sees the line drop ten minutes before it and says so at the time); (2) **provocations** pre-kickoff and at half-time, putting a question to the user that becomes the take it holds them to; (3) **on demand**. Plus the twist: **the pundit makes its own falsifiable calls** with a window ("they concede again before the 70th") and gets graded in the same ledger as the user - turning an oracle into an opponent, making the hedge visible, giving the demo a real ending (the pundit's own scorecard), and handing over the LinkedIn hook (most AI products are built to never be wrong on the record; this one keeps score of its own bad takes).
- Captured: **"yes yes and yes. This sounds like such great ideas."** With one refinement of his own:
- **Omri's refinement: the pundit's own CALLS are gated.** It may only make a prediction (a) when the user explicitly asks for one, and (b) at the provocation moments (pre-kickoff, half-time). It does **not** spontaneously fire off predictions through the match.
- Why this is a good instinct: it stops the pundit being noisy, and it makes each call feel weighty and deliberate rather than a stream of hedged guesses. Scarcity is what gives a call stakes.
- Reading to confirm with him: "calls" = *predictions*, so live **state-change observations still fire automatically** during the match (that is the smart-friend-noticing-things value, and the main payoff of the tactical-state layer). Only the predictions are gated.

### Q10 - Agent vs plain code, and how many agents
- Asked: proposed "agents where judgment lives, plain code everywhere else" - 3 agents (Tactical Analyst, Pundit, Adjudicator) + a thin supervisor, with match engine / stats store / claim ledger as plain code and tools. Warned explicitly against over-agenting (five LLM agents where two would do is slower, flakier, pricier, and reads to a knowledgeable judge as architecture theatre). Recommended building on **Microsoft Agent Framework** deliberately - named hero tech, direct successor to AutoGen/Semantic Kernel, and the orchestration skill actually transfers to a CV.
- Captured: **Omri splits the Analyst into specialists.** His reason: *"that way I have control over what things are assessed during the game."* Starting set:
  1. **Set pieces**
  2. **Individual duels**
  3. **Attacking/defending numbers inside the box**
- Note he dropped "pressing" from the example offered and chose box numbers instead - his own tactical interests, not the suggestion.
- Revised architecture: **3 narrow specialist analysts + Pundit + Adjudicator + thin supervisor.** The specialists fan out over the same event stream; modular and extensible, so adding a 4th specialist later is cheap. This is a genuinely richer multi-agent learning exercise than one monolithic analyst.
- **Refinement this forces (raise with him): event-type routing, not fan-out-on-every-tick.** 3 specialists firing on every tactical state change means a lot of LLM calls, which is slow and expensive and will stutter in a live demo. The supervisor should wake **only the relevant specialist**: set-piece event -> set-piece analyst; duel event -> duels analyst; box entry/shot -> box-numbers analyst. Better engineering *and* a more sophisticated orchestration pattern to show off.
- Alignment bonus: these three map onto the hackathon's own suggested feature list (pass quality, player identification, shot/attacking metrics), which feeds criterion 5, Adherence to Hackathon Category.
- Consequence on the generator (must be designed in from the start): the event schema now has to emit **set-piece events** (type, delivery, outcome), **duel events** (attacker, defender, type, winner), and **in-box occupancy counts** at shot/cross moments - not just generic passes and shots.

### Q11 - Real deadline, build order, cut line, and the safety-submission question
- Asked: put on record that (1) the real code-complete deadline is **Oct 24, not Oct 27** - once the surf camp starts, 2h/day is enough to record a video and write a pitch but not to debug a broken agent pipeline; (2) the video, pitch and testable deployment are **eligibility, not polish** - no public repo / no sub-2-min video / no way for a judge to run it means the entry is never scored. Proposed a vertical-slice build order and a pre-agreed cut order (TTS first, then the 3rd specialist, then adjudicator richness; never cut the pundit's POV, the claim ledger, or the video). Asked whether he wants a deliberate "submit something that works" safety submission.
- Captured, three responses:
  1. **"What is TTS?"** - text-to-speech, the pundit speaking its lines aloud. Pure stretch goal. He had agreed to it in Q7 without knowing the term, so it was never a real commitment - treat as genuinely optional.
  2. **"I won't be actually building today anymore."** Oct 19 is gone. Build window is now **Oct 20-24 = 5 days**, then 2h/day Oct 25-27. One day lost off the plan; Oct 20 becomes a heavy day.
  3. **Wants the safety submission**, conditional on being able to edit later.
- **Answered from the rules directly:** Section 5 (Submission Modifications) only governs changes *after* the Submission Period, and then only narrow sponsor-permitted fixes for IP/PII problems. Nothing restricts editing *during* the period. So **yes - submit early, keep editing freely until Oct 27 23:59 PT.** The safety submission is free insurance and goes in the plan.

## Revised build schedule (Oct 19 lost)
| When | What |
|---|---|
| **Oct 20** | Generator (one event family) + claim ledger + ONE specialist + pundit, running in terminal. No UI. Loop works in text. Heavy day. |
| **Oct 21** | Other two specialists + adjudicator + supervisor routing |
| **Oct 22** | Thin UI, match clock, replay |
| **Oct 23** | Azure slice + public deploy + **safety submission** |
| **Oct 24** | Demo match tuning, record video, write pitch. **Code freeze** |
| **Oct 25-27** | 2h/day: LinkedIn post, resubmit if improved, TTS only if genuinely free |

Cut order, decided in advance: TTS -> 3rd specialist -> adjudicator richness. Never cut: pundit POV, claim ledger, demo video.

## Rules read directly (findings that change the design)

**Best Multi-Agent System Prize - the exact judged wording:** *"whether specialized agents have distinct roles, coordinate through shared state and effective handoffs, **recover from failures**, and deliver an end-to-end outcome a single agent could not achieve as effectively."*
- Distinct roles: covered. Shared state + handoffs: covered by the match-state store. End-to-end outcome a single agent couldn't match: covered.
- **GAP: "recover from failures" is explicitly judged and is not in the design.** Cheap to add and must be: every specialist and the pundit need a timeout + fallback path so one flaky agent degrades the output instead of killing the match. Worth making *visible* in the demo (e.g. a status strip showing an agent dropped and the system carrying on).
- The category also explicitly names **Microsoft Agent Framework** and A2A as supported orchestration approaches, confirming the Q10 framework choice scores directly.

**Pipeline stage (e) Personalize is pushed hard in the rules** - "the same intelligence reaches a data-hungry analyst and a casual fan as two genuinely different experiences", with customized modes, favourite club, favourite player, player-focused mode. The rules state flatly: *"a Project that only generates metrics has no audience, and a solution that only personalizes has nothing to personalize."*
- **GAP: personalization is a named pipeline stage and the current concept only has it implicitly.** Cheapest credible fix: the pundit has selectable depth/persona (analyst mode vs mate-on-the-sofa mode) over the same underlying findings. Near-free, directly answers stage (e), and genuinely fits the concept.

**Multi-language storytelling is listed as feature (vi).** One extra prompt on the pundit's output. **Hebrew is a near-free, memorable differentiator** and makes the LinkedIn post land harder with his own network.

**Not doing (optional features, explicitly "consider"):** auto-eventing from a video feed, ball/shot speed from vision. Out of scope, no penalty.

### Q12 - Covering the Personalize stage
- Asked: pundit depth toggle, Hebrew multi-language, or a different axis (favourite player/club)? (recommended depth toggle - same specialist findings underneath, two mouths on top: "analyst mode" with numbers/percentiles vs "mate on the sofa", blunt and numberless; one extra system prompt, directly answers stage (e), strong demo beat where flipping it mid-match re-describes the same moment two ways. Plus Hebrew as a near-free feature (vi) win that would make the LinkedIn post land with his own network.)
- Captured: **Depth selection only. English only.** His reasoning: Hebrew *"would be too much and not really impressive."*
- Good scope discipline and the reasoning holds - a language toggle on an LLM is a one-line trick, and anyone technical reading the repo knows it. Not worth the surface area. **Multi-language is formally out of scope.**
- Personalize stage is therefore covered by the **depth toggle alone**: analyst mode vs casual mode over identical underlying findings.

### Q13 - Stack
- Asked: proposed a stack built toward his demonstrated capability rather than the one that died on the drawing board. Evidence cited: he has shipped **self-contained styled HTML pages real people used** (two World Cup party apps friends played on their phones, the Vol.2 deck emailed to Itai); he has never shipped a React build or a server.
- Captured: **Stack confirmed.** (His reply was cut off mid-sentence after confirming - nothing lost on the decision itself, but he may have had an addition.)

**Stack of record:**
- **Python** throughout for the match engine and agents - the language already in his hands.
- **FastAPI + server-sent events** for the live feed. Smallest real backend that exists; Claude Code carries it.
- **One styled HTML page** consuming the stream. No React, no Vite, no build step, no node_modules.
- **Explicitly not Streamlit** - fastest path but reads as an internal data tool, and "broadcast-grade product" is the impression being sold with 20% of the score on UX/presentation.
- **Microsoft Agent Framework** for the orchestration (from Q10).

**Design decision that solves two scored problems at once:** because the generator is seeded, **pre-bake a full match transcript** (events, findings, pundit lines, verdicts) as a fallback file. If a model call times out or the API is flaky, the system serves the baked line instead of breaking.
1. That *is* the "recover from failures" story the Best Multi-Agent category explicitly judges.
2. It guarantees a judge opening the link at any hour during the Oct 27 - Nov 10 judging window sees a working match, never an error.
3. It de-risks the video recording.
Same work, three wins.

### Q14 - The demo match arc, and Omri's video concept
- Asked: proposed a demo-match arc - pre-kickoff provocation + user take + pundit's own call; ~35' the box-numbers specialist spots bodies arriving in the box from the wrong side and the pundit calls the equaliser coming from a cross *before anything happens* (the moment that sells the product); ~50' it lands; ~70' the pundit's second call **misses, visibly**; full time the ledger (user 1/2, pundit 2/3 with the miss shown). Insisted on the visible miss: 3-for-3 kills the "it can't hedge" hook because nobody believes it.
- Captured: **Arc approved, content stays.** Plus a strong creative addition of his own:
- **Omri's video concept:** two friends talking about the game, then the **AI pundit appears - looking like a person but with an old-style computer monitor (CRT) as a head.** Style: **comedy, light**, less focused on technicalities, more on building a storyline.
- **His explicit framing:** *"That is a big advantage for linkedin, as that's my main goal, I don't think I'll win the competition."* Consistent with Q3 - the LinkedIn artifact is the real deliverable, the prize is not.
- The CRT-head pundit is a genuinely good identity and should be reused as the product's own avatar in the UI (one generated image), so video and product look like the same thing.
- **Problems this creates, to resolve next:**
  1. **Eligibility risk.** Rules §4.3: *"The Project must... function as depicted in the video and/or expressed in the text description"*, and Stage One judging is a pass/fail viability check. A comedy sketch that does not show the product actually working risks failing that gate.
  2. **Resource problem.** He is **solo in Portugal**. "Two friends talking" is not available on camera. No cast, no crew, no CRT prop. Surf-camp people from Oct 25 are a possible but socially and logistically risky cast, and that is after code freeze.

### Q15 - One video or two
- Asked: split into a functional hackathon video (Oct 24, screen recording + voiceover, protects the §4.3 "must function as depicted in the video" eligibility gate) and a separate comedy LinkedIn video (Oct 25-27, fits the 2h/day surf window exactly since the code is frozen by then). Recommended **AI-generating** the comedy piece to solve the no-cast problem - a CRT-headed pundit interrupting two mates on a sofa is close to a best case for late-2026 AI video, is solo-doable, needs no scheduling, and is fitting for an AI-built product. Held him to one condition: comedy gets the clicks but the **post text must carry the substance** (what he built, the architecture, what he learned) or it reads as a funny video with no engineer behind it - same pattern that worked on his Oct 2026 post (narrative hook up front, real credential stated plainly, not hyped).
- Captured: **Agreed, two videos.** Both AI-made: *"The 1st video will be narrated by AI as well. The second video will obviously be created with AI, not planning on filming anything."*
- **Nothing gets filmed. No cast, no crew, no props, no scheduling dependency.** This removes the single biggest execution risk in the LinkedIn plan.
- **Useful synergy spotted:** if video 1 needs an AI voiceover, he is building a TTS pipeline anyway - which makes the in-product pundit voice (the Q7 stretch goal) close to free rather than a separate task. Worth doing the voiceover in a way that is reusable by the app.

### Q16 - Azure slice (+ explainer requested)
- Asked: two Azure services only - **Microsoft Foundry** for inference (highest-value tick: named hero tech, criterion 1, makes him eligible for Best Foundry Use) and **Azure Container Apps** for hosting (named in Best Azure Cloud Native, and he needs a public URL anyway for the "judge can test it" requirement). Deliberately NOT Fabric, Event Hubs, AKS, Functions, Logic Apps, Cosmos - each is a day he does not have and none is visible in the video. Possible free third tick: **Azure AI Speech** for the voiceover he is doing anyway. Insisted on writing model calls behind a **one-function provider interface from hour one** so if Foundry auth fights him on day one he swaps to a direct API in ten minutes and still ships.
- Omri asked for a plain explanation of Azure and each service (he had never used any of it). Explained: Azure = Microsoft's cloud; Foundry = where the models are hosted, your own endpoint + key instead of calling Anthropic/OpenAI directly, i.e. where the pundit's brain lives; Container Apps = hand it a container, get a public https URL, no server to maintain, the simpler cousin of Kubernetes; AI Speech = TTS/STT; **Agent Framework = a free pip-installed open-source library, NOT a cloud service** - successor to AutoGen/Semantic Kernel, runs locally, points at Foundry models, and is where the actual learning goal lives (called non-negotiable). Innovation Studio = the hackathon's own submission platform, not an Azure product.
- Also gave him the honest version: the product would work fine with no Azure at all (call Claude directly, run locally), but criterion 1 would score near zero, he would be ineligible for two of four category prizes, and he would skip the one skill on the list that is on nearly every job spec - deploying something so other people can use it.
- Captured: **"yeah that sits right."** Two-service slice confirmed, Speech as a free third if the voiceover makes it so.
- **Innovation Studio: invite received and he is registered.** URL: https://innovationstudio.microsoft.com/hackathons/insidethegamedeveloperhackathon
- Both previously-blocking open items on Azure/platform are now resolved or reduced: platform access is confirmed; **Azure credits still unchecked** -> Omri to check inside Innovation Studio.

### Q17 - Name and where the code lives
- Asked: flagged the trap that the hackathon requires a **public GitHub repo** while SHMAGS 2 is his private second brain (job search, decision log, client work, D&D, trip finances) - so the code must live in its own standalone public repo, same call he made in June keeping the Economics paper out of SHMAGS 2 rather than exposing everything to Tomer over Live Share. Offered name candidates (The Gaffer, Second Screen, Punditron, On the Record, Hot Take FC) with On the Record as the pick.
- Captured: **Name is "HoTake"** - his words: *"it's trendy and simple."* A compression of "hot take". His call, taken as decided; he has good naming instinct (Through the Gap, Window Winners both deliberate double meanings). Minor note only: slight misspelling/mispronunciation risk, not worth relitigating.
- **Separate public repo accepted.** Follow-up question from him: how to use SHMAGS 2's context and capabilities from inside the new repo.

## Repo architecture (answer to his follow-up)
Established precedent to follow: `c:\עמרי\portfolio` already lives **outside** SHMAGS 2. So: **`c:\עמרי\HoTake`**, its own git repo, public.

- **Primary working directory = HoTake**, with **SHMAGS 2 added as an additional working directory** (he already runs several additional dirs, so the mechanism is proven on this machine). Claude Code's default context is then the code, with the second brain readable when needed.
- **Move genuinely global rules up to user level** (`C:\Users\User\.claude\CLAUDE.md`): the AI Kill List, communication style, and who Omri is are not SHMAGS-2-specific preferences - they should apply in every repo he works in. Same logic for any skill worth having everywhere (`~/.claude/skills/`). This is the real fix and it benefits every future project, not just this one.
- **A `CLAUDE.md` inside HoTake** carrying the build-specific conventions (stack, agent boundaries, the provider-interface rule, the cut order) and pointing at where SHMAGS 2 context lives.
- **Memory is keyed per project path** (`~/.claude/projects/c-------Shmags-2/memory/`), so a new project directory starts with empty memory. Either work with SHMAGS 2 as an additional dir, or copy across the few memories that matter.
- **Hard safety rule, written into HoTake's CLAUDE.md:** this repo is PUBLIC. Never copy content from SHMAGS 2 into it. No personal data, no client names, no trip or job-search detail. Tracker/notes/decision entries for this project stay in SHMAGS 2 (`projects/plms-hackathon/`), never in the public repo.

### Q18 - Completeness backstop
- Asked what had not been touched, with reads on each open item.
- Captured, all four resolved or parked by him:
  - **Azure credits** -> he checks tomorrow (Oct 20) inside Innovation Studio. Still the one blocking unknown.
  - **Club names** -> **fictional clubs confirmed.** Removes the trademark risk entirely at zero cost; the demo does not need real clubs to make sense.
  - **LinkedIn post text** -> explicitly future work, after the project is finished. Correct call - it will be better written against the thing that exists.
  - **Pundit name/personality** -> he wants one now, matching the tone.
- Nothing else nagging. Interview complete on his side.

### Q19 - The pundit's name
- Asked: proposed Clive (deadpan; a robot called Clive is funnier than any clever name, instantly legible as a middle-aged football man, "Ask Clive" reads naturally in the UI), Statto (real football slang for a stats obsessive, but also a real TV character so it carries a mild trademark risk Clive does not), Ceefax (perfect CRT/teletext tie-in but a deep cut), HAL-f Time (comedy-forward but undercuts the credibility the LinkedIn post needs). Recommended Clive.
- Captured: **"yup. clive is right."**
- **Product = HoTake. The pundit = Clive.**

---

# FINAL PLAN OF RECORD

## What it is
**HoTake** - a single-seat AI football pundit named **Clive**, with an old CRT monitor for a head. He watches a synthetic match alongside you, notices tactical shifts before anything obvious happens, provokes you into committing to a take, makes his own falsifiable calls, and then grades both of you against the evidence.

The distinctive claim, and the LinkedIn hook: **most AI products are built so they can never be wrong on the record. Clive keeps score of his own bad takes.**

Why it is not in the crowded lane: every other public entrant repo is building broadcast-grade commentary and recaps for a studio. HoTake is built for the group of friends who argue tactics live. Nobody else is there.

## Architecture
Agents where judgment lives, plain code everywhere else.

| Piece | Agent? |
|---|---|
| Match engine - seeded synthetic events + declared tactical state | No, plain code |
| Stats/context store - running match facts, queryable | No, code + a tool |
| **Set-piece analyst** | Yes |
| **Individual-duels analyst** | Yes |
| **Box-numbers analyst** (attacking/defending bodies in the box) | Yes |
| **Clive** - owns the POV, decides what is worth saying, makes calls | Yes |
| **Adjudicator** - gathers evidence, rules on who was right | Yes |
| Claim ledger - takes, windows, outcomes | No, plain code |
| Supervisor - **event-type routing**, wakes only the relevant specialist | Thin |

Framework: **Microsoft Agent Framework** (named in the Best Multi-Agent category; successor to AutoGen/Semantic Kernel; the skill transfers).

**Failure recovery is a scored requirement, not a nice-to-have.** Every agent gets a timeout + fallback to the pre-baked transcript. Make the degradation visible in the UI.

## Data
Simulate at the **tactical-state level**, not player coordinates. Events carry minute, team, player, zone, outcome; alongside them a small set of declared state variables (pressing intensity, line height, territory share, momentum, shape) tick over the match and drive which events become likely. Schema must emit set-piece events, duel events, and in-box occupancy at shot/cross moments.
- **Seeded** so the demo match is reproducible and the video never depends on a lucky run, while a judge can reseed.
- **Calibrated against real published aggregate stats** so it looks realistic. Never redistribute a real dataset in the public repo; no Opta/Transfermarkt scraping.
- **Fictional clubs and players.**

## Stack
Python throughout · FastAPI + server-sent events · one styled HTML page (no React, no build step) · Microsoft Foundry for inference · Azure Container Apps for hosting · Azure AI Speech if the voiceover makes it free.
**Model calls behind a one-function provider interface from hour one**, so Foundry auth problems cost ten minutes, not a day.

## Personalize stage
Covered by a **depth toggle** alone: "analyst mode" (numbers, percentiles) vs "mate on the sofa" (blunt, numberless) over identical underlying findings. English only. Flipping it mid-match is a demo beat.

## Demo match arc
Pre-kickoff provocation, user take, Clive's own call with a window -> ~35' the box-numbers analyst spots bodies arriving from the wrong side and Clive calls the equaliser coming from a cross *before anything happens* -> ~50' it lands -> ~70' **Clive's second call misses, visibly** -> full time the ledger (user 1/2, Clive 2/3 with the miss shown).
The visible miss is non-negotiable. 3-for-3 and nobody believes the accountability is real.

## Schedule
| When | What |
|---|---|
| Oct 20 | Check Azure credits. Generator (one event family) + ledger + ONE specialist + Clive, in the terminal. No UI. Heavy day. |
| Oct 21 | Other two specialists + adjudicator + supervisor routing |
| Oct 22 | Thin UI, match clock, replay |
| Oct 23 | Azure slice + public deploy + **safety submission** |
| Oct 24 | Demo tuning, record judge video, write pitch. **Code freeze** |
| Oct 25-27 | 2h/day: AI comedy video, LinkedIn post, resubmit if improved |

Cut order, pre-decided: in-product TTS -> 3rd specialist -> adjudicator richness. **Never cut:** Clive's POV, the claim ledger, the judge video.

## Eligibility checklist (these are pass/fail, not polish)
- [ ] Public GitHub repo
- [ ] Demo video **under 2:00**, public URL
- [ ] Written pitch: what it is, which Microsoft/Azure tech, what problem it solves
- [ ] Judge can actually run it (live URL)
- [ ] Project must **function as depicted in the video** (rules §4.3)
- [ ] Submitted via Innovation Studio by **Oct 27 23:59 PT** (= Oct 28 09:59 Israel)

## Repo setup
- Code: **`c:\עמרי\HoTake`**, standalone **public** repo, outside SHMAGS 2 (same pattern as `c:\עמרי\portfolio`).
- Run Claude Code from HoTake with SHMAGS 2 as an additional working directory.
- **Lift global rules to user level** (`C:\Users\User\.claude\CLAUDE.md`): AI Kill List, communication style, who Omri is. They are not SHMAGS-2 facts and every future project should inherit them.
- `CLAUDE.md` in HoTake for build conventions, plus the hard rule: **this repo is public, never copy anything from SHMAGS 2 into it.**
- Tracker and decision entries for this project stay in SHMAGS 2 at `projects/plms-hackathon/`.

## Open flags (pending input)
- **Azure credits** - unknown until he looks inside Innovation Studio -> Omri, Oct 20. If there are none, Foundry inference is out of pocket; the provider interface means falling back costs ten minutes.
- **LinkedIn post text** - deliberately deferred to after the build -> Omri, Oct 25-27.
- **Clive's personality specifics** (voice, verbal tics, how rude he is) - a 10-minute call on build day, better made with the thing in front of him -> Omri.
- **today.md is stale** - still says London through Oct 24; he is already in Portugal -> fix at save-context.
