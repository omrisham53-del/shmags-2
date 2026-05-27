# Folder Reorganization - May 14, 2026

Summary of improvements made to SHMAGS 2 structure.

## Changes Made

### 1. Project Structure (✅ DONE)
- Added `status.md` to each project (energy-program, job-search, university, dnd-campaign)
  - Quick reference for current status
  - Last updated timestamp
  - Key dates and owner info

- Added `next-steps.md` to each project
  - Prioritized action items
  - Checkboxes for tracking progress
  - Notes section

- Added `notes/` folders to: energy-program, job-search, university
  - For meeting notes, ideas, research within each project
  - Keep project-specific context organized

- Added `sessions/` folder to dnd-campaign
  - For individual session planning and post-session notes

### 2. Session Summaries (✅ DONE)
- Created `sessions/` folder at root level
- Moved and renamed session summary:
  - `session-summary-2026-05-14-birthday-playlist.md` → `sessions/2026-05-14_birthday-playlist.md`
- Standardized naming: `YYYY-MM-DD_description.md`
- Added `sessions/README.md` with usage guidelines

### 3. Daily Dashboard (✅ DONE)
- Created `today.md` for quick daily focus
- Includes current priorities, this week's focus, blockers, quick links
- Should be updated at start of each day or when priorities shift

### 4. Date Formatting (✅ DONE)
- Standardized all dates to `YYYY-MM-DD` format
- Updated research/job-market files:
  - `20250513_...` → `2025-05-13_...`
  - `20260514_...` → `2026-05-14_...`
- All new files will use this format going forward

### 5. References Folder (✅ DONE)
- Moved `Brand - assets/` → `references/brand-assets/`
- Added `references/README.md` with organization guidelines
- Ready for future style guides, SOPs, examples

### 6. Memory System Clarification (✅ DONE)
- Created `.claude/MEMORY_SYSTEM.md` explaining:
  - Session memory (repo-based: sessions/, decisions/)
  - Persistent memory (user home: C:\Users\User\.claude\...)
  - When to use each
  - How they work together

### 7. Archives (✅ DONE)
- Added `archives/README.md` with archival strategy
- Ready to receive completed projects and old sessions
- Keeps active workspace clean while preserving history

## New Folder Structure

```
CLAUDE.md (master reference)
today.md (daily dashboard - NEW)
context/
decisions/
sessions/ (NEW - organized session summaries)
projects/
  ├── energy-program/
  │   ├── README.md
  │   ├── status.md (NEW)
  │   ├── next-steps.md (NEW)
  │   └── notes/ (NEW)
  ├── job-search/
  │   ├── README.md
  │   ├── status.md (NEW)
  │   ├── next-steps.md (NEW)
  │   ├── notes/ (NEW)
  │   ├── preferences.md
  │   └── tracker.md
  ├── university/
  │   ├── README.md
  │   ├── status.md (NEW)
  │   ├── next-steps.md (NEW)
  │   └── notes/ (NEW)
  └── dnd-campaign/
      ├── README.md
      ├── status.md (NEW)
      ├── next-steps.md (NEW)
      └── sessions/ (NEW)
references/
  ├── README.md (NEW)
  ├── brand-assets/ (MOVED from root)
  ├── sops/
  └── examples/
research/
  ├── job-market/ (dates standardized)
  ├── academic/
  └── dnd/
archives/ (with README)
.claude/
  ├── MEMORY_SYSTEM.md (NEW)
  ├── agents/
  ├── rules/
  ├── settings.json
  └── skills/
```

## Next Steps

1. ✅ Start using `today.md` as your daily dashboard
2. ✅ Update project `status.md` files as work progresses
3. ✅ Keep `next-steps.md` in sync with actual priorities
4. ✅ Use `notes/` folders for project-specific context
5. ✅ Archive completed projects and old sessions quarterly
6. ✅ Continue using session summaries in `sessions/` folder

## Notes

- No existing project files were deleted
- All changes maintain the CLAUDE.md structure
- Memory system (.claude/MEMORY_SYSTEM.md) clarifies dual-memory approach
- This reorganization file can be archived after reviewing
