Run Omri's weekly review. This is the cleanup + reconcile ritual that keeps the second brain from accumulating stale weight. Do it in order and keep the final report tight.

## 1. Reconcile today.md

- Read `today.md`. Move any items in "Today's Completed" that are from a past date into a dated "Recent Work" section, and clear "Today's Completed".
- If "Recent Work" has grown beyond the last ~3 dates, move the oldest blocks into `archives/today-log-YYYY.md` (append, create if missing). today.md should stay a live dashboard, not a journal.
- Verify "Current Priority", "This Week's Focus", and "Active Applications" still reflect reality based on the conversation and trackers. Flag anything that looks stale but do NOT rewrite priorities without confirming.

## 2. Deadline radar

- Read `projects/university/tracker.md`, `projects/job-search/tracker.md`, `context/goals.md`, and today.md.
- List every dated deadline. Flag: (a) anything past-due still marked open, (b) anything due within 7 days, (c) any goal milestone whose date has slipped.
- Convert relative dates to absolute against today's date.

## 3. Job-search hygiene

- In `projects/job-search/tracker.md`, find every application in "Applied" or "In Review" status.
- Flag any with no status change in 7+ days as a follow-up candidate. List them with how many days stale.
- Do not draft or send anything. Just surface the list.

## 4. Stale-automation sweep (the anti-cruft check)

This is the step that prevents the mess this ritual was built to fix.

- Check `scripts/`, `.claude/skills/`, `.claude/commands/`, and `.claude/agents/` against how they're actually described/used.
- Flag anything that looks abandoned: a script that hasn't run (check git log for its last real commit vs "chore" noise), a skill with no recent invocation, duplicate artifacts (e.g. a `.py` and a `.md` doing the same job), empty folders.
- Cross-check the memory index `C:\Users\User\.claude\projects\c-------Shmags-2\memory\MEMORY.md`: flag any memory that describes a system that no longer exists.
- Report flags as a checklist. Do NOT archive anything without confirming with Omri first (except obvious no-brainers like clearing a completed today.md item).

## 5. Report

Output a tight review, skipping empty sections:

- **RECONCILED:** what changed in today.md
- **DEADLINES:** past-due / due-soon / slipping (each with a date)
- **FOLLOW-UPS:** stale applications worth a nudge
- **CRUFT FLAGGED:** anything to archive, with a one-line why each (ask before acting)
- **PRIORITY CHECK:** anything in the priority files that no longer matches reality

Then ask which flagged cruft to archive, and stop.

## Style

- No emojis, no em dashes, bullets over prose (per communication-style.md).
- Make the safe fixes automatically (today.md reconcile). Everything destructive or judgment-heavy gets confirmed first.
