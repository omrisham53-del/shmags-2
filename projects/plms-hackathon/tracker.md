# HoTake Tracker

**Last Updated:** 2026-11-19
**Status:** Lost all of Oct 20 to travel (surf-camp transit took far longer than planned). Scope cut to a smaller v1 to fit Oct 24; the cut full version becomes a no-deadline side project after submission. Terminal pipeline AND polling web UI both working end to end as of Oct 21 -- effectively 2 of the 4 remaining build days done in one session. Not yet tested with a live LLM key; all verification so far is on the fallback path.

---

## The deadline that matters

| Date | What |
|---|---|
| **Oct 24** | **Code freeze.** This is the real deadline. |
| Oct 27, 23:59 PT | Official submission close (= **Oct 28, 09:59 Israel**) |
| Oct 27 - Nov 10 | Judging |
| by Nov 20 | Winners announced |

**Why Oct 24 and not Oct 27:** the Ericeira surf camp starts Oct 25 and drops available time to about 2h/day. That is enough to record a video and write a post. It is not enough to debug a broken agent pipeline.

---

## Build schedule

| When | What | Done |
|---|---|---|
| **Oct 20** | Lost to travel. | [x] (skipped) |
| **Oct 21** | Compressed Oct 20+21: repo set up at `c:\עמרי\HoTake`, match generator (tactical-state driven, seeded demo match scripted for the arc below), claim ledger, LLM provider seam with timeout+fallback, 2 specialists (set-piece, box-numbers), Clive, adjudicator, supervisor routing -- all running end to end in the terminal, verified both with and without a live API key. **Third specialist (duels) cut per the standing cut order**, now a post-submission addition. | [x] |
| **Oct 22** | Thin polling-based web UI (scoreboard, live feed, ledger panel, take box). No SSE -- swapped for 1s polling to fit the timeline; cut from scope, not from the eventual full version. Done same session as Oct 21 (full 90-minute match verified end to end over real HTTP, no crashes). | [x] |
| **Oct 23** | Azure Foundry + Container Apps + public deploy + **safety submission** | [ ] |
| **Oct 24** | Demo match tuning, record judge video, write pitch. **Code freeze** | [ ] |
| **Oct 25-27** | 2h/day: AI comedy video, LinkedIn post, resubmit if improved | [ ] |

Editing a submission during the submission period is permitted (rules section 5 only restricts changes after it closes), so the Oct 23 safety submission is free insurance.

---

## Smaller-v1 scope cut (2026-10-21, after losing Oct 20 to travel)

To fit the remaining 3 build days, v1 additionally drops (beyond the
pre-planned cut order below): SSE streaming (polling instead), replay/match
history, multi-match support. These come back after submission -- no
deadline on that follow-on work.

## Cut order, decided in advance

So the call does not have to be made while tired:

1. In-product TTS (the pundit's spoken voice)
2. The third specialist - two specialists is still a multi-agent system
3. The adjudicator's richness - a plain verdict beats a clever one

**Never cut:** Clive's point of view, the claim ledger, the judge video.

If Oct 20 slips, cut the third specialist immediately rather than compressing the UI and deploy days. An undeployed project is a non-submission.

---

## Eligibility checklist (pass/fail, not polish)

More hackathon entries die here than on code quality.

- [ ] Public GitHub repo
- [ ] Demo video **under 2:00**, public URL (YouTube/Vimeo)
- [ ] Written pitch: what it is, which Microsoft/Azure tech, what problem it solves
- [ ] Judge can actually run it (live public URL)
- [ ] Project **functions as depicted in the video** (rules section 4.3)
- [ ] Submitted via Innovation Studio by Oct 27 23:59 PT

---

## Demo match arc

The 2-minute video rests entirely on this, so the match is designed, not random.

| Minute | What happens |
|---|---|
| Pre-kickoff | Clive provokes. User commits to a take. Clive makes his own call with a window. |
| ~35' | Box-numbers analyst spots bodies arriving from the wrong side. Clive calls the equaliser coming from a cross, **before anything has happened**. This is the moment that sells the product. |
| ~50' | It lands. Clive collects. |
| ~70' | **Clive's second call misses, visibly.** |
| Full time | The ledger. User 1/2. Clive 2/3, with the miss shown. |

**The visible miss is non-negotiable.** 3-for-3 and nobody believes the accountability is real, which kills the whole hook.

---

## Open items

| Item | Owner | Status |
|---|---|---|
| Check Azure credits inside Innovation Studio | Omri | **Blocking-ish, Oct 20.** If none, Foundry inference is out of pocket; the provider interface makes falling back a 10-minute job |
| Clive's personality specifics (voice, verbal tics, how rude) | Omri | 10-minute call on build day, better made with the thing in front of him |
| LinkedIn post text | Omri | Deliberately deferred to Oct 25-27, after the build |
| Lift global rules (AI Kill List, comms style, identity) to user-level CLAUDE.md | Omri + Claude | Not started. Logged in `projects/claude-code-lessons/tracker.md` |
| Anthropic API key `hotake` expires **2026-11-20 (UTC)** | Omri | Confirmed from the Console email 2026-11-13. After expiry every request with that key gets an authentication error. Fix: create a new key in the Anthropic Console, update HoTake's local env var, delete the old key. Only the live-LLM path is affected, the fallback path needs no key. Not urgent while HoTake is parked, but rotate before the first live test. |

---

## Decided and closed

- Solo entry, no team (registration closed Oct 20, so irreversible)
- Target Best Multi-Agent category only, not the Grand Prize
- Skill target is multi-agent orchestration; frontend deliberately demoted
- Synthetic data simulated at tactical-state level, not player coordinates; seeded for a reproducible demo; calibrated against real published aggregate stats
- Fictional clubs and players (removes the trademark risk at zero cost)
- Personalize stage covered by a depth toggle alone (analyst mode vs mate-on-the-sofa). **English only** - multi-language cut as "too much and not really impressive"
- Clive's *predictions* are gated to user request + pre-kickoff + half-time. Live tactical observations still fire automatically
- Two videos, neither filmed: functional screen recording for judges, AI-generated comedy for LinkedIn
- Failure recovery (timeout + fallback to a pre-baked transcript) is in scope because the Best Multi-Agent criteria explicitly judge it
- Not using: Fabric, Event Hubs, AKS, Functions, Logic Apps, Cosmos, auto-eventing from video

---

## Post-hackathon: the six winners vs HoTake (2026-11-19)

Winners announced Nov 19 at Ignite (source: Microsoft Tech Community post, pasted by Omri). HoTake was not submitted. All six repos are public.

| Prize | Project | Builder | Core idea |
|---|---|---|---|
| Grand Prize, 1st | Pitch Ledger | Philippines | Deterministic engine computes every stat, 5 agents write stories, an Auditor recalculates each figure and blocks anything beyond the evidence. Ledger with audit trail. Match Lab plants known scenarios in ~125k events per match. ~$0.07 model cost per match. |
| Grand Prize, 2nd | Footballytics | Pakistan | Personal Director agent follows your club and fantasy squad across 10 matches. Verifier rejects inflated stats live in the UI. Template fallback if models go down. 7 languages. |
| Best Foundry | Matchcut | Nigeria | Per-fan voiced highlight films, 7 languages, audio description, QA agent that watches the output. 42 films in ~3 min at ~2 cents each. |
| Best Enterprise | Absolute Scenes | India | AI pundit that draws on the pitch as it speaks. Every number links to a tool call. Tactician plus simulator replays alternatives. Producer approval console. |
| Best Multi-Agent | MatchCast | India | Broadcast crew with a separate Verifier that recounts from the raw log. Failures route back to the responsible agent. Up to 5 parallel specialists, A2A, audit chain, Content Safety, 10 languages. |
| Best Azure Cloud Native | Talkback | Poland | Editorial gallery: Spotter ranks moments, Lab agent replays a moment 120 times to test causal wording, clears lines per territory. |

Shared pattern: facts computed in code, language models only write, an independent verifier sits before the audience, multilingual and accessible personalization treated as core, production-style Azure (Event Hubs, Container Apps, keyless managed identities).

**Matched:** facts in code and judgment in agents, claim ledger, adjudicator, timeout plus fallback, declared tactical-state generator with a scripted demo arc.

**Thinner:** no independent check of the numbers Clive quotes (adjudicator grades predictions, not stats); 2 specialists with event-type routing vs MatchCast's typed graph; depth toggle vs 7 to 18 variants; no production framing; never deployed, never run on a live LLM, no measured numbers.

**Different (the lane to keep):** no winner built a take-versus-take game where the pundit is graded in the same ledger as the user. Closest is Absolute Scenes, but it is broadcaster-facing and never scored against the viewer.

**Carry-forwards for the portfolio version:**
1. Add a verifier for Clive's quoted numbers (the ledger already exists).
2. Add a visible "plant a false stat, watch it get caught" demo.
3. Report measured cost per match and latency per call.
4. Keep the accountable-pundit game as the differentiator.
5. Read the Pitch Ledger and MatchCast repos (links need to come from the post page itself).
