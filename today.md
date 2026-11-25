# Today - 2026-11-25

**Date:** 2026-11-25
**Updated:** 2026-11-25

---

## Current Priority

**In Portugal, Ericeira surf camp started Oct 25. The hackathon window closed unsubmitted; chess and HoTake are now both no-deadline projects.** Jotunheimen, Alta, Scotland-with-Dad (WHW + Ben Nevis), and the LinkedIn post are all closed out. Ireland dropped.

- **HoTake was not submitted.** No work happened after Oct 21 -- the Oct 22-24 build days, the Oct 23 safety submission, the Oct 24 freeze, the videos and the pitch all passed untouched, and the Oct 27 23:59 PT deadline closed with nothing entered. Confirmed by Omri 2026-11-02. The code that exists (match engine, ledger, 2 specialists, Clive, adjudicator, supervisor, polling web UI, full fallback path) is real and working locally. Per the Oct 19/21 decisions the full version was always framed as a no-deadline follow-on, so this is a reframe, not a loss: it continues as a **portfolio project with no external deadline**. Note: the Anthropic API key `hotake` expires 2026-11-20 (UTC); rotate it in the Console before the first live-LLM test.
- **Chess learning system -- built and waiting on fuel.** M0, M1, M2, M3 and M6 all done. M4 (conversion drills) and M5 (book loop + position-pattern matcher) remain. The blocker is not code: **no rapid games since Sept 13 except one routine run ~Nov 3**, now five consecutive zero-rapid rows in the Rating Log on top of the earlier 6.5-week blackout. Parked until laptop time. HoTake is parked the same way: portfolio project, resumes once Omri has a place to work on the computer. Job search to restart on a light schedule at that point, no pressure while abroad.
- **November is now planned (2026-11-03).** Ericeira camp is over. Omri is going to volunteer on an Israeli-run farm near Lagos, 2 weeks minimum, ideally a month or more. The ~Dec 8 trip end is flexible since there is no job waiting. Paid barista work in the Algarve is being considered as an add-on (see `decisions/log.md` 2026-11-03).
- **EcoTraders exit -- DONE.** Ron's reference letter was received by email (confirmed 2026-11-13). Nothing left open.
- **University: DONE, degree complete.**
- **Through the Gap / Window Winners: killed 2026-09-03.** Not coming back as a suggestion.

---

## Today's Completed

1. **Applied to two MoonActive roles** (Product Economy Manager, Business Data Analyst) -- confirmed submitted. CV fixed via a plain list of text edits against Omri's real Canva-built CV (not a rebuild -- first pass wrongly rebuilt it from scratch and was rejected): Reichmann->Reichman typo, Techincal/willingnes typos, mixed British/American spelling, EcoTraders dates/past tense, distinction-track seminar paper added to the profile and Projects section. `projects/job-search/tracker.md` marked Applied.
2. **Refreshed both of Omri's portfolios** -- portfolio-1.0 (`c:\עמרי\portfolio`, the wrong one at first) and portfolio-2.0 (the real one, a self-hosted Claude Artifact export, discovered only after Omri flagged the mix-up). Both: Student->Graduate, EcoTraders no longer reads as a current job, broken/stale links fixed, current CV swapped in. Portfolio-2.0 additionally: fixed a literal `index.html.html` filename bug that likely meant Vercel had no homepage to serve, added Ron's real signed reference letter (pulled from Gmail) as a download next to the CV, fixed two dead "Read full sheet" project links into in-page expansions, rewrote both project write-ups in plain language after Omri called the first version "gibberish" for anyone but him, and fixed a real factual error (data-center capacity: 100 MW -> 20 MW) plus an inconsistent LinkedIn URL caught proactively.

---

## Recent Work (November 13)

1. **Weekly review run live and sorted** (2026-11-13): Ron's reference letter closed (received by email), HoTake and chess explicitly parked until laptop time, D&D campaign and world-cup-party archived, `current-priorities.md` fully re-derived, Q4 goals set in `context/goals.md` (career clarity, 36 chess games, HoTake demo + LinkedIn posts), grill-me / save-context / job-tracker skills moved into the folder layout so they register, HoTake API key expiry (2026-11-20) recorded, to be rotated at laptop time.

---

## Recent Work (October 19)

1. **Read and analyzed the final posted LinkedIn post** (lnkd.in/p/ej8SauVz, Hebrew, 40 reactions/6 comments) -- confirmed it matches the v4 draft (narrative over stats, grateful/curious tone) plus one real addition Omri wrote in himself: naming the paper's distinction-track selection plainly. Locked in as a durable voice preference (`feedback_linkedin_voice.md`) for future personal-brand posts.

2. **Chess goal set at 1600 rapid and a full learning system designed** via a 9-question grill-me session (`brainstorms/2026-10-19_chess-learning-routine.md`). The session reframed the problem three times rather than building what was asked for: the five-week rapid stall turned out to be an access problem (no laptop time, won't play rapid on a phone), "more puzzles" is the wrong main lever since Tactics 1871 means vision isn't the bottleneck, and "improve my endgames" is the same problem as blowing leads slowly, not a third item. Omri's own objection about hint-dependency became four hard design rules. Build plan at `projects/chess/learning-system-plan.md`, 7 milestones, clock analyzer first because it can invalidate the endgame workstream before it's built.

3. **Audited the two chess cloud routines** before deciding their fate, at Omri's insistence. Found two things that mattered more than the consolidation: the Rating Log tracks ratings but never games played, so eight rows of "Rapid unchanged" hid a five-week rapid blackout that a games-played column would have caught in mid-September; and the routine prompts exist only in the claude.ai UI, nowhere in the repo, so they can't be audited or recovered. Both logged, the second as a Claude Code lesson affecting every routine including the weekly review.

4. **Travel tracker reconciled.** It still had Omri in London through Oct 24 and the Worldpackers placement as "pending confirmation" -- both wrong. Fixed, and the three fully-historical Norway sections (Oslo DNT questions, Weather Watch, the Odda/Hardangervidda planning block) marked historical so they stop reading as live open items in every future session.

5. **HoTake specified end to end** via a 19-question grill-me session (`brainstorms/2026-10-19_plms-hackathon-project.md`) for the Microsoft x Premier League hackathon. Researched the event first (rules, judging weights, entrant repos) rather than asking blind, which surfaced that the crowded lane is broadcast commentary and that two explicitly-judged items were missing from the design: "recover from failures" in the Multi-Agent criteria, and Personalize as a named pipeline stage. Omri improved on the concept twice himself: the pundit framing (neither analysis companion nor prediction referee, but a stat-based pundit that creates conversations), and splitting the analyst into three narrow specialists for control over what gets assessed. The real deadline was reset from Oct 27 to **Oct 24** once the surf camp's 2h/day was priced in honestly, and the videos split into two (functional for judges, AI-generated comedy for LinkedIn) because one video cannot serve both without risking the eligibility gate.

---

## Recent Work (October 7)

1. **Caught up on ~5 weeks of trip history** after a gap in sessions (last here Sept 4) -- git pull, reconciled today.md and the energy-program exit-logistics table against what actually happened: Jotunheimen, Alta, Breheimen dropped, Scotland-with-Dad moved earlier, West Highland Way + Ben Nevis completed Oct 6.
2. **Confirmed Ron's reference letter was actually sent** (2026-09-09, found via Gmail search) and sent a reminder (2026-10-07) -- both self-written by Omri, closing out a "status unknown" flag the weekly review had been carrying for weeks.
3. **LinkedIn post written and posted**, four drafts -- pivoted from a stats-heavy paper recap to a grateful/curious reflection built around the IDCA Annual Summit, the trip's purpose, and connecting with nature. Full iteration logged in `decisions/log.md`.
4. **Ireland dropped, Portugal re-anchored** around a signed-up Ericeira surf camp (Oct 25) and a submitted Worldpackers candidacy in Sagres (Nov 3) -- decided in a separate online session that never synced to this repo; flagged as a cross-session gap worth fixing (`projects/claude-code-lessons/tracker.md`).

---

## This Week's Focus (Nov 2 onward)

1. **Chess: run the full session routine for the first time.** Everything built is waiting on rapid games. Play -> self-review -> engine pass -> drill -> book, per `projects/chess/learning-system-plan.md`.
2. **HoTake as a portfolio project.** No deadline. Decide what "done" means now that the judging criteria are gone.
3. **Farm volunteering near Lagos.** Confirm exact start date, length and what the farm covers (bed, meals). Decide whether to add paid barista work after.
4. **Q4 goals.** Discuss and set them live (goals.md is still Q2-Q3 2026).

---

## Quick Links

**Work Projects:**
- [Energy Program](projects/energy-program/)
- [Travel](projects/travel/)
- [Job Search](projects/job-search/)
- [University](projects/university/)
- [Chess](projects/chess/)
- [HoTake / PLMS Hackathon](projects/plms-hackathon/)
- [Claude Code Lessons](projects/claude-code-lessons/)

**Workflows & References:**
- [Trip Planning](projects/travel/tracker.md)
- [Equipment List](projects/travel/equipment-list.md)
- [Daily Routine](routine.md)
- [Current Priorities](context/current-priorities.md)
- [Job Tracker](projects/job-search/tracker.md)
