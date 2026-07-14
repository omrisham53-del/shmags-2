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
- **Claude Code meta-lessons** — anything learned about using Claude Code itself, as distinct from project work: a new feature or setting discovered, a workflow habit worth adopting, a skill/config pattern that worked or failed, a harness quirk or gotcha. This is about the tool, not the project the tool was used on.

## Steps

1. **Update `decisions/log.md`** — append new decisions only, format:
   `[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`

2. **Update memory files** in `C:\Users\User\.claude\projects\c-------Shmags-2\memory\` — add or update anything not already captured. Update `MEMORY.md` index if a new file is created.

3. **Update `today.md`** — mark completed tasks as done if not already.

4. **Update project trackers if changed** — e.g., job tracker status, university tracker.

5. **Update `projects/claude-code-lessons/tracker.md`** — for each Claude Code meta-lesson found, append an HTML `<tr>` row inside the Backlog table (it's an HTML table, not a markdown one, so rows can carry a background color — copy the matching block from the "Row Template" section at the bottom of that file). Status is `Done` (green, `#d4f4dd`) if the change was actually implemented this session (note what changed and where), or `Not Started` (gray, `#eaeaea`) if it's just an idea/observation not yet acted on. Skip this step entirely if no meta-lessons came up — most sessions won't have any.

6. **Git sync** — stage and commit all pending changes, then merge to master and push:
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
- CLAUDE CODE LESSONS: (list or "none")
- FILES UPDATED: (list)
- GIT: branch merged + pushed, or "already on master, pushed"

Skip empty categories.
