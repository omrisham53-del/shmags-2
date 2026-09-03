# Today - 2026-09-04

**Date:** 2026-09-04
**Updated:** 2026-09-04

---

## Current Priority

**Four days to departure (Sept 8).** Everything below is either "close it before the flight" or "decide it before the flight."

- **Norway leg -- both Jotunheimen and Breheimen now reversed and routed around dead bus seasons.** **Confirmed: Memurubu closes Sept 13**, breaking the original Jotunheimen Day 5 night -- fixed by reversing the whole 6-day loop, landing every hut inside its season. Then confirmed the bigger problem: **every seasonal mountain bus connecting Jotunheimen to Breheimen (Lom-Gjendesheim, Lom-Sogndal, Bismo-Sota Sæter) stops running by Aug 16-30**, weeks before this trip. Fixed the same way -- Breheimen reversed too, entered by taxi from Gjendesheim via Sota Sæter/Slæom, exiting at Høyheimsvik on the fjord where real year-round transport exists. Full confirmed route (83km, 7 waymarked sections pulled directly from DNT's own map data) in `projects/travel/tracker.md`. **What's still open is the weather call on Sept 5-6** -- hold until the forecast actually reaches the Sept 10-21 window, DNT conversation in Oslo Sept 9 as a second input, keep the gate reversible since DNT comes after it. DNT now also has three real questions queued from the Breheimen rebuild (see below).

- **EcoTraders exit -- one item left.** The job is finished (last working day 2026-08-19, every deliverable shipped) and the exit is closed except for one thing. Confirmed 2026-09-03: the closing email to Daniel went out with the final two deliverables, the pension release letter was unnecessary, and the vacation payout was already settled. What remains is the **reference letter from Ron**: draft written for him to react to rather than write from scratch, at `projects/energy-program/reference-letter-draft.md`. Send it before the flight.

- **LinkedIn post on the economics seminar presentation -- write before Sept 8.** The stray "LinkedIn post" line that had been drifting through this file for weeks turned out to be about the distinction-track economics seminar presentation with Tomer (data-center energy CBA, presented July 30), not EcoTraders. Confirmed plan: write and post it this week.

- **University: DONE, degree complete.** Final Sustainability Project submitted 2026-08-12, both channels confirmed. All grades pending, nothing further to produce.

- **Through the Gap / Window Winners: killed 2026-09-03.** No work and no future work planned. Folder archived, calendar blocks deleted. Not coming back as a suggestion.

---

## Today's Completed

1. **Discovered and fixed a second, bigger transport problem: the whole Jotunheimen-Breheimen bus corridor is dead by September.** Checked Omri's plan to bus from Gjendesheim via Lom/Sognefjellsvegen to the Breheimen trailhead against innlandstrafikk.no directly (not trip aggregators, which gave conflicting answers) -- every relevant seasonal mountain route (Lom-Gjendesheim, Lom-Sogndal, Bismo-Sota Sæter) stops running by Aug 16-30, 2026, weeks before the Sept 9/16/21 dates that depend on them. This breaks getting to Gjendesheim, the Jotunheimen-Breheimen transition, and the planned Breheimen exit shuttle, all three.

2. **Fixed by reversing Breheimen the same way Jotunheimen was reversed.** Entered from the mountain side by taxi (Gjendesheim → Lom → Sota Sæter, real road confirmed, ~$16-24 for the Lom leg alone), exit at the fjord side (Høyheimsvik), which has a genuine year-round Norled express boat to Bergen. Found two real local taxi numbers (Taxi 03650 Lom, Schøss Taxi Otta) and confirmed Gjendesheim's own staff can arrange the booking, since Omri has no Norwegian number.

3. **Confirmed Sota Sæter itself is closed by these dates** (staffed season ends Sept 6, no self-service option at all -- checked directly against dnt.no) and that the real first night is at Slæom, a genuine self-service hut, via a DNT-confirmed 5-hour walk. Omri independently found this by checking the hut schedule himself.

4. **Built the full Slæom-to-Høyheimsvik route from real DNT map data**, not aggregator guesses -- Omri pulled the route IDs and distances directly from ut.no via a browser extension after my own attempts (WebFetch, then a headless-Chrome screenshot) both failed to read the interactive map. 83.0km across 7 waymarked sections, saved as `projects/travel/slaeomtohoyheimsvikroute.json`. Flagged two things this uncovers rather than just handing over the numbers: it's a materially longer, harder route than the one originally scoped (83km + a 5h approach walk vs. the original 61km), and the endpoint (Luster Fjordhytter) is a private cabin, not a DNT hut, so it likely needs advance booking unlike everything else on this trip.

5. **Full Norway route section of the tracker rebuilt** around both reversals, old plans marked superseded rather than deleted, and three concrete DNT questions queued (Day 1/5 real difficulty, Fivla's actual status, Luster Fjordhytter booking) for Sept 9 or an earlier email.

---

## Recent Work (September 3)

1. **Pulled ~105 commits of work from remote** (Aug 5 to Sept 2) after a long gap. Local `today.md` change was a stale duplicate of a date bump remote had already made, so it was discarded; the uncommitted `Travel_Budget_Tracker.xlsx` edits were untouched by the merge and preserved.

2. **Window Winners removed completely.** Project folder moved to `archives/through-the-gap/` (newsletter articles kept with it), both recurring Google Calendar build blocks deleted (Tue 19:00-21:00 and Fri 10:00-12:00, which had been set to run indefinitely and would have fired all through the trip), and every live reference cleared out of `today.md` and `context/current-priorities.md`.

3. **Full priorities re-derivation.** The file still described the trip as "under 7 weeks out" and carried EcoTraders and University as active delivery priorities. Rewritten around what is actually live: trip and departure at #1, exit logistics at #2, career exploration at #3, LinkedIn as an explicit decide-or-defer item.

4. **Reference letter draft written for Ron** -- English, all-round emphasis, at `projects/energy-program/reference-letter-draft.md`. Draft revised to drop the pension/vacation mention once Omri confirmed both were already handled.

5. **EcoTraders exit closed to one item.** Omri confirmed the closing email to Daniel was sent with the final two deliverables, the pension release letter is unnecessary, and the vacation payout was already settled. Tracker, priorities and today.md all updated -- the reference letter is now the only open item.

6. **Jotunheimen route reversed and verified.** Omri confirmed Memurubu (the private lodge, not a DNT cabin) closes Sept 13 -- the same date as the DNT staffed network -- which breaks the original plan's Day 5 night there outright, not just as a risk. Checked the two other borderline huts directly against dnt.no and spiterstulen.no rather than assume: Glitterheim's self-service quarter runs Feb 15-Oct 15 (closed only while staffed, so a Sept 14 night is fine), Spiterstulen runs to ~Oct 15. Built the reversed 6-day itinerary (same legs, same total distance, opposite direction) -- every hut now lands inside its season. Flagged the real cost of reversing rather than presenting it as free: Besseggen swaps from its easier climbing direction (Memurubu to Gjendesheim) to its harder descending direction (Gjendesheim to Memurubu) on Day 1, with no acclimatization day beforehand, and the single longest day (21km) moves from first to last.

7. **LinkedIn post source identified.** Omri's best guess: it was always about the economics seminar presentation with Tomer, not EcoTraders -- the wording had just drifted over several today.md rewrites. Confirmed plan: write and post before the flight.

---

## Recent Work (August 19)

1. **EcoTraders closed out -- last working day.** All deliverables shipped. The final one, the full loan fund chapter, turned out to be a trim rather than a drafting job: the appendix version already had every section, so the work was cutting ~6 pages toward ~3. Planned it in two phases with a decision gate, lossless cuts (redundant explanation, narrative around examples, prose-to-table compression, background tightening) made first, and anything that would cost real substance escalated as a ranked list for Omri to decide rather than cut on the model's own judgment.

2. **Status swept across the whole project.** The tracker had ~30 unchecked boxes that would have read as outstanding work to anyone opening it later; restructured into a final status table plus an honest "Unresolved at handoff" section (Rafi data that never arrived, the heat pump COP tension, cohort-discounting convention, sensitivity tables never rebuilt, market sizing paused not solved). README, current-priorities, goals and today.md all updated to match.

3. **Status confirmed across every open item.** Model bugs all fixed, sensitivity tables rebuilt, lifespans equalized, all five flagged tax-chapter content issues closed. The tax chapter shipped as a ~10-page appendix version rather than being trimmed to the 4-page in-body ceiling. Loan fund landed at ~4 pages on the lossless pass alone. Yaniv's import data never came, Rafi never responded further, PRTR turned out not to be relevant, so market sizing stays a documented placeholder. Only genuinely open item: the cohort-discounting convention, now low-stakes since the cross-chapter cost-effectiveness comparison was dropped.

*(August 8 and August 5 blocks moved to `archives/today-log-2026.md`.)*

---

## This Week's Focus (Sept 4-8, pre-departure)

1. **Send Ron the reference letter draft.** The last open EcoTraders item. Fill the three placeholders first (Ron's title, start date, whether to name the Ministry).
2. **Write and post the LinkedIn piece on the economics seminar presentation.**
3. **Sept 5-6: the Jotunheimen weather call** -- forecast finally reaches the front half of the trek window then. Route itself is already fixed (reversed loop); this is purely the go/no-go on the trek as a whole. Keep it reversible; the DNT conversation is Sept 9, after the gate.
4. **Consider emailing DNT before Sept 9** on the Breheimen questions specifically (Day 1/5 real difficulty, Fivla's status, Luster Fjordhytter booking) -- this route is now load-bearing enough that finding out something's wrong in person on Sept 9 leaves little room to adjust.
5. **Sept 9 in Oslo:** raise the Jotunheimen trade-off (Besseggen's harder direction, no warm-up day) and the Breheimen questions with DNT, collect the DNT key, gas canister, confirm membership, book the Gjendesheim→Sota Sæter taxi through the lodge staff.
6. **Final gear sweep** -- everything except the DNT key and gas canister has to be sourced before boarding. `projects/travel/equipment-list.md`.

---

## Quick Links

**Work Projects:**
- [Energy Program](projects/energy-program/)
- [Travel](projects/travel/)
- [Job Search](projects/job-search/)
- [University](projects/university/)
- [Chess](projects/chess/)
- [Claude Code Lessons](projects/claude-code-lessons/)

**Workflows & References:**
- [Trip Planning](projects/travel/tracker.md)
- [Equipment List](projects/travel/equipment-list.md)
- [Daily Routine](routine.md)
- [Current Priorities](context/current-priorities.md)
- [Job Tracker](projects/job-search/tracker.md)
