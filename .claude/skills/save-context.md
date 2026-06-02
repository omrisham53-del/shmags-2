---
name: save-context
description: Extract and save context from this session — decisions made, tasks completed, memory updates, and status changes. Trigger proactively when the user signals they're wrapping up ("bye", "done for now", "that's it", "see you", "going to sleep", "logging off", "save context", "save this session"). Also trigger after completing a major task if no new topic follows.
---

# Save Context

Extracts and persists what happened in this session without the user having to explain it again next time.

## What to Extract

Scan the full conversation for:
- **Decisions** — anything meaningful that was chosen, agreed on, or locked in
- **Accomplishments** — tasks completed, files created, things submitted or sent
- **Status changes** — job applications updated, assignments submitted, interviews done
- **New preferences or patterns** — anything worth remembering for future sessions

## Steps

1. **Update `decisions/log.md`** — append new decisions only, format:
   `[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`

2. **Update memory files** in `C:\Users\User\.claude\projects\c-------Shmags-2\memory\` — add or update anything not already captured. Update `MEMORY.md` index if a new file is created.

3. **Update `today.md`** — mark completed tasks as done if not already.

4. **Update project trackers if changed** — e.g., job tracker status, university tracker.

5. **Git sync** — stage and commit all pending changes, then merge to master and push:
   - If on master: `git add -A`, commit, push
   - If on a feature/claude branch: commit any pending changes, then:
     ```
     git checkout master
     git merge --ff-only <branch>
     git push
     git branch -d <branch>
     ```
   - If `--ff-only` fails (diverged history), use `git merge --no-ff <branch>` instead
   - Goal: always end the session with master up to date on the remote

## Report

After saving, show a tight summary:
- DECISIONS: (list or "none")
- ACCOMPLISHMENTS: (list or "none")  
- MEMORY UPDATES: (list or "none")
- FILES UPDATED: (list)
- GIT: branch merged + pushed, or "already on master, pushed"

Skip empty categories.
