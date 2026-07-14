# Claude Code Lessons

**Description:** Backlog of lessons and ideas from watching a 6-hour Claude Code manual/tutorial, to be worked into SHMAGS 2's structure, skills, CLAUDE.md rules, and settings over multiple sessions.

**Status:** Active
**Source:** 6-hour Claude Code manual (video), watched in chunks starting 2026-07-14

---

## What This Is

Omri is watching a long-form Claude Code training video and picking up things worth changing in this repo -- new skills, CLAUDE.md rule tweaks, settings.json config, folder structure adjustments, workflow habits. Not every lesson gets actioned immediately; some sit in the backlog until a session is dedicated to working through them.

## Workflow

1. **Capture** -- as a lesson comes up (mid-video or after), add it to `tracker.md` as a new row with status `Not Started`.
2. **Work sessions** -- pick items off the backlog (any order, doesn't have to be sequential), implement the change, update status to `Done` (or `Skipped` with a one-line reason if it turns out not to apply here).
3. **No forced graduation** -- unlike `brainstorms/`, there's no separate raw-capture file that needs to "graduate" -- the tracker IS the live backlog, from capture through completion.

## Where Changes Land

Depending on what the lesson is about, the actual change happens in the real file, not here:
- New/modified skill -> `.claude/skills/`
- New/modified slash command -> `.claude/commands/`
- Rule or convention change -> `CLAUDE.md`, `.claude/rules/`
- Settings/permissions/hooks -> `.claude/settings.json` (use the `update-config` skill)
- Folder structure change -> update the folder map in `CLAUDE.md` to match

This project just tracks *that* the change is planned/done -- it's not where the change itself lives long-term.
