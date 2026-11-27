# Weekly Review -- 2026-11-27

---

## RECONCILED

- Moved 2 items from "Today's Completed" (dated 2026-11-24) into a new "Recent Work (November 24)" section.
- Cleared "Today's Completed".
- Moved "Recent Work (October 7)" to `archives/today-log-2026.md` (Recent Work now holds November 24, November 13, October 19 -- 3 dates).

---

## PRIORITIES

**Stale section in today.md -- character mismatch:**
- "This Week's Focus (Nov 2 onward)" is 25 days stale. It still lists "Q4 goals -- discuss and set them live (goals.md is still Q2-Q3 2026)" as an open item. Both are done: goals were set on 2026-11-13. The whole section needs a rewrite to reflect current focus (or removal if there is no active weekly focus while traveling).

**HoTake API key -- expired:**
- The `hotake` Anthropic API key expired 2026-11-20 (UTC). Today.md already notes this and says "rotate before the first live-LLM test." No action urgently needed since the project is parked on laptop time, but the note should be treated as confirmed-expired now, not future-tense.

**Possible missing priority:**
- The November 24 session applied to two MoonActive roles and refreshed both portfolios -- a meaningful push that is not reflected anywhere in Current Priority or This Week's Focus beyond the tracker row. If Omri wants to monitor those applications, that belongs in the dashboard, not just the tracker.

---

## DEADLINES

**Past-due (noted, parked):**
- HoTake Anthropic API key `hotake`: expired 2026-11-20. Action needed before first live-LLM test. No urgency while project is parked on laptop time, but it is now definitively expired.

**No other dated deadlines found open:**
- University: degree complete, all submitted.
- EcoTraders: exit closed 2026-11-13.
- Q4 goals: none carry specific dates (career clarity, 36 chess games, HoTake demo are all "when laptop time exists").
- Google Workspace email: nothing breaks before 2027-02-01 (MCP enforcement) or 2027-04-01 (billing). Not flagged as due-soon.

---

## FOLLOW-UPS

Job search is in a one-off exception state (two MoonActive applications submitted 2026-11-24, broader search still paused per `context/current-priorities.md`).

- MoonActive Product Economy Manager -- Applied 2026-11-24 (3 days ago). Not yet 7 days stale. No action yet.
- MoonActive Business Data Analyst -- Applied 2026-11-24 (3 days ago). Not yet 7 days stale. No action yet.

No follow-ups due this week. Flag both applications next review if no status change by 2026-12-01.

---

## CRUFT FLAGGED

**today.md -- "This Week's Focus (Nov 2 onward)":**
- 25 days stale. Lists four focus items, three of which are done or no longer active (chess routine: parked; HoTake as portfolio: parked; Q4 goals discussion: done 2026-11-13). Only the farm volunteering item remains live but is itself vague ("confirm exact start date" -- has that been confirmed?). Recommend rewriting or removing this section.

**scripts/job-tracker.py:**
- Moved from .claude/skills/ to scripts/ in July 2026. No git commits touching it since. The corresponding .claude/skills/job-tracker/ folder contains a separate skill file. The script itself targets a job tracker workflow; the skill's content still targets "junior data analyst roles" per the November 13 decision, which no longer matches the career-direction reframe. Flag: the skill content needs a rewrite before the job search restarts; the .py script may overlap with or be superseded by the skill. Confirm whether scripts/job-tracker.py is still the intended mechanism or whether it can be archived.

**scripts/sync_jobs.py:**
- Noted in the July 2026 decisions log as "future infra, no near-term plan, not hurting anything." No commits touching it since at least July. If the Notion sync it implements has never been used and there is no plan to use it, it is a low-priority archiving candidate. No action without Omri's call.

**archives/moonactive-prep/:**
- A folder was created in archives/ from the November 24 session prep work. If it holds temporary working files from that session rather than a completed project, it may not need to live in archives/ (which is for completed or stale projects) -- could also be removed if the contents are now redundant with the tracker entries and decisions log. Worth a check.

**context/me.md -- outdated role description:**
- Still describes Omri as "Third-year student at Reichman University, working part-time as a policy analyst at EcoTraders." Both are no longer true. Degree is complete; EcoTraders exit closed 2026-11-13. Not a scripts/skills issue but a cruft flag worth noting.
