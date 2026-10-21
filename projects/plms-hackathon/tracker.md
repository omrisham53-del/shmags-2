# HoTake Tracker

**Last Updated:** 2026-10-21
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
