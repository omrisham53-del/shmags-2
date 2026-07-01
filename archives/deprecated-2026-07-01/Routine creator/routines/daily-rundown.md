# Daily Morning Rundown

## What it does
Every morning at 8:30 AM, Claude scans all project folders under `C:\עמרי\Shmags 2\projects\` for open/pending tasks, picks a single top priority for the day, and refreshes the `daily-rundown` Cowork artifact. Omri opens the artifact in the sidebar to see his full task picture for the day.

> Telegram notifications were removed on 2026-05-22 — artifact-only output.

## Schedule
`30 8 * * *` — 8:30 AM daily, local time
Scheduled task ID: `daily-rundown`

## Data sources
- `C:\עמרי\Shmags 2\projects\` — scans all subdirectories
- Per project: `tracker.md`, `next-steps.md`, `status.md`, and any `todo.md` / `actions.md` files found
- Job search specifically: rows in `tracker.md` where Status is not "Rejected" or "Offer accepted"

## Artifact
- ID: `daily-rundown`
- Shows: date, daily focus card (top 1 priority), task list grouped by project
- Updated by the scheduled task each run via `mcp__cowork__update_artifact`

## Logic
1. List all project folders under `projects/`
2. For each folder, read any task-bearing files (tracker.md, next-steps.md, status.md, etc.)
3. Extract open/pending items with their status and any implied action from notes
4. Pick one daily focus: prefer time-sensitive or actionable items over passive ones
5. Build the full HTML artifact (self-contained, light mode)
6. Write HTML to outputs folder, call `update_artifact` with id `daily-rundown`

## Edge cases & known issues
- If SHMAGS 2 is inaccessible, artifact shows an error notice instead of crashing
- If a project folder has no open tasks, it is omitted from the artifact
- Tool approvals needed on first run — click "Run now" once in the Scheduled section to pre-approve

## Last updated
2026-05-20
