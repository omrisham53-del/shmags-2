# Routine Creator — Project Instructions

## Purpose

This project serves two roles:

1. **Hub** — The single source of truth for every automation and scheduled routine that runs across the SHMAGS 2 workspace. Every active routine is registered here.
2. **Builder** — The workspace used to design, test, and deploy new automations.

When you open a session in this project, your default working folder is `projects/Routine creator/` inside SHMAGS 2.

---

## SHMAGS 2 Folder Context

The parent workspace is `C:\עמרי\Shmags 2\`. It contains multiple active projects under `projects/`:

| Folder | Description |
|--------|-------------|
| `projects/job-search/` | Job application tracker. Source of truth: `tracker.md`. Syncs daily to Notion. |
| `projects/Routine creator/` | This project — automation hub and builder. |
| *(other projects)* | Add rows here as new projects are created. |

When building automations for any project, read the relevant project files first before designing logic.

---

## Active Automations Registry

Each automation should have an entry in the table below. Keep this up to date.

| Name | Schedule | Trigger | What it does | Source file | Status |
|------|----------|---------|--------------|-------------|--------|
| Daily Job Tracker Sync | Daily, 10:00 AM (Asia/Jerusalem) | Scheduled task (Claude) | Reads `projects/job-search/tracker.md`, compares against Notion DB, pushes new rows, refreshes the job-tracker artifact | *(inline prompt in scheduled task)* | ✅ Active |
| Daily Morning Rundown | Daily, 8:30 AM (local) | Scheduled task (Claude) | Scans all SHMAGS 2 project files for open tasks, picks a daily focus, refreshes the `daily-rundown` Cowork artifact | `routines/daily-rundown.md` | ✅ Active |

> When you add a new routine, add a row here AND document it in its own section below.

---

## Integrations Available

This project can use the following integrations. Confirm they are connected in Cowork before building an automation that depends on them.

### Notion
- Used for: reading/writing databases and pages across projects.
- Job search DB lives at the Notion workspace connected via the Notion MCP.
- When syncing from a markdown file to Notion: always dedup by a stable unique field (e.g. job application URL) before pushing new rows — never push blindly.

### Gmail
- Used for: searching, reading, and drafting emails.
- Useful for automations that monitor inboxes, send reminders, or draft replies.
- Always draft first, never send automatically without explicit user confirmation.

### Files (SHMAGS 2)
- The primary data source for most automations.
- Source-of-truth files (like `tracker.md`) live in `projects/<project-name>/`.
- Automations should read from these files, not from Notion, when the two diverge — the markdown file wins.

### Scheduled Tasks
- Claude can run on a cron schedule via `mcp__scheduled-tasks__create_scheduled_task`.
- Use `cronExpression` for repeating tasks (e.g. `"0 10 * * *"` = 10:00 AM daily).
- Use `fireAt` for one-off future runs.
- Always record the schedule in the Active Automations Registry above.
- To update an existing task's schedule or prompt, use `mcp__scheduled-tasks__update_scheduled_task`. List current tasks first with `mcp__scheduled-tasks__list_scheduled_tasks`.

---

## How to Build a New Routine

Follow this process whenever creating a new automation:

1. **Define the trigger** — Is it time-based (cron), event-based (user asks), or reactive (something changes in a file)?
2. **Define the source** — Where does the input data come from? (markdown file, Notion, Gmail, etc.)
3. **Define the output** — What should happen? (update Notion, send email draft, refresh artifact, write a file)
4. **Test manually first** — Run the logic once in a session and verify the output before scheduling.
5. **Schedule it** — Use `create_scheduled_task` with a clear prompt that includes: what to read, what to compare, what to write/push, and how to handle errors.
6. **Register it** — Add a row to the Active Automations Registry in this file.
7. **Save context** — If the routine is complex, create a `routines/<routine-name>.md` file documenting its logic, edge cases, and known issues.

---

## Routine Documentation Files

Store detailed documentation for individual routines under `projects/Routine creator/routines/`. Naming convention: `routines/<routine-name>.md`.

Example structure for a routine doc:

```
# <Routine Name>

## What it does
<One paragraph summary>

## Schedule
<Cron expression and timezone>

## Data sources
- Source 1: <path or integration>
- Source 2: <path or integration>

## Logic
<Step-by-step description>

## Edge cases & known issues
- ...

## Last updated
<Date>
```

---

## Conventions & Rules

- **Markdown files are the source of truth.** If Notion and a `.md` file disagree, trust the `.md` file and update Notion to match.
- **Never send emails automatically.** Always draft and confirm with the user first.
- **Dedup before pushing to Notion.** Use a stable unique field (URL, ID, etc.). Never push duplicate rows.
- **Artifacts need manual refresh.** Cowork artifacts are static snapshots. After a sync, always call `update_artifact` to rebuild the view from fresh data.
- **Always test before scheduling.** Run the routine's logic once in a session before setting up a cron task.
- **One cron task per routine.** Don't create duplicate scheduled tasks. Check `list_scheduled_tasks` before creating a new one.
- **Log issues inline.** If a routine fails or produces unexpected output, note it in the routine's `.md` doc under "Edge cases & known issues."

---

## Session Startup Checklist

When opening a session in this project:

1. Read this file (`CLAUDE.md`) if you haven't already.
2. Check `mcp__scheduled-tasks__list_scheduled_tasks` to see what's currently running.
3. If the user asks to build something new, follow the "How to Build a New Routine" process above.
4. If the user asks to fix or update an existing routine, find it in the Active Automations Registry and read its routine doc (if one exists) before making changes.
