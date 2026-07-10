Run Omri's weekly review. This is the cleanup + reconcile ritual that keeps the second brain from accumulating stale weight. Do it in order and keep the final report tight.

## 1. Reconcile today.md

- Read `today.md`. Move any items in "Today's Completed" that are from a past date into a dated "Recent Work" section, and clear "Today's Completed".
- If "Recent Work" has grown beyond the last ~3 dates, move the oldest blocks into `archives/today-log-YYYY.md` (append, create if missing). today.md should stay a live dashboard, not a journal.

## 2. Priorities re-derivation (not a status patch)

This replaces a simple "does this still look right" skim. The failure mode this guards against: patching status text inside the same old buckets while a priority quietly dies, changes character entirely, or a new one never gets added at all (see `decisions/log.md` 2026-07-10 for the concrete example that prompted this).

- Read `context/current-priorities.md`, `context/goals.md`, `decisions/log.md` (entries since the last review), and today.md's "Recent Work" sections since the last review.
- For each priority currently listed: look for supporting evidence in that window (decision log entries, today.md work items, relevant tracker/project activity, git log commits touching that project's folder). No evidence in ~3+ weeks -> flag as **possibly stalled/dead**, not just "check on this."
- Scan the decisions log and today.md for recurring projects/themes that AREN'T in `current-priorities.md` at all -> flag as a **possible missing priority**.
- Watch for a priority whose stated framing contradicts what recent decisions/today.md entries actually say (e.g. file still says "paused for logistics" but decisions show it's actually a full direction change) -> flag as a **character mismatch**, not just "stale."
- This step only flags. The cloud run is non-interactive and cannot ask Omri which way to resolve a mismatch — never rewrite `current-priorities.md` or `goals.md` unattended. Full re-derivation happens live with Omri; this step's job is making sure he doesn't go long without knowing it's needed.

## 3. Deadline radar

- Read `projects/university/tracker.md`, `projects/job-search/tracker.md`, `context/goals.md`, and today.md.
- List every dated deadline. Flag: (a) anything past-due still marked open, (b) anything due within 7 days, (c) any goal milestone whose date has slipped.
- Convert relative dates to absolute against today's date.

## 4. Job-search hygiene

- In `projects/job-search/tracker.md`, find every application in "Applied" or "In Review" status.
- Flag any with no status change in 7+ days as a follow-up candidate. List them with how many days stale.
- If the tracker/current-priorities.md indicates the search is paused/deprioritized (e.g. for travel), skip nudging entirely and just note the pause is still in effect — don't manufacture urgency around a deliberately paused search.
- Do not draft or send anything. Just surface the list.

## 5. Stale-automation sweep (the anti-cruft check)

This is the step that prevents the mess this ritual was built to fix.

- Check `scripts/`, `.claude/skills/`, `.claude/commands/`, and `.claude/agents/` against how they're actually described/used.
- Flag anything that looks abandoned: a script that hasn't run (check git log for its last real commit vs "chore" noise), a skill with no recent invocation, duplicate artifacts (e.g. a `.py` and a `.md` doing the same job), empty folders.
- Cross-check the memory index `C:\Users\User\.claude\projects\c-------Shmags-2\memory\MEMORY.md`: flag any memory that describes a system that no longer exists.
- Report flags as a checklist. Do NOT archive anything without confirming with Omri first (except obvious no-brainers like clearing a completed today.md item).

## 6. Report

Output a tight review, skipping empty sections:

- **RECONCILED:** what changed in today.md
- **PRIORITIES:** stalled/dead priorities, possible missing priorities, character mismatches (see step 2) -- this is a standing flag list, not a rewrite
- **DEADLINES:** past-due / due-soon / slipping (each with a date)
- **FOLLOW-UPS:** stale applications worth a nudge (skip if search is paused)
- **CRUFT FLAGGED:** anything to archive, with a one-line why each (ask before acting)

Then ask which flagged cruft to archive, and stop.

## Style

- No emojis, no em dashes, bullets over prose (per communication-style.md).
- Make the safe fixes automatically (today.md reconcile). Everything destructive or judgment-heavy gets confirmed first.
