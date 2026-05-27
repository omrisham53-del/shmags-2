# COWORK.md: Cowork Session Primer

**Read this at the start of every Cowork session.** Then load the files listed in [CLAUDE.md](CLAUDE.md) for full context.

Cowork is the desktop app surface (separate from Claude Code in the terminal). Same brain, different toolset. This file documents what is specific to Cowork so sessions start oriented and don't duplicate or conflict with what Claude Code already does.

---

## Session Start: Load Order

1. This file (COWORK.md)
2. [CLAUDE.md](CLAUDE.md): system overview and file map
3. [today.md](today.md): current priorities and what's done
4. [routine.md](routine.md): workflow structure (90-min blocks)
5. [context/current-priorities.md](context/current-priorities.md): quarterly focus
6. [context/me.md](context/me.md): who Omri is
7. [.claude/rules/communication-style.md](.claude/rules/communication-style.md): voice
8. Active project trackers as needed: [job-search/tracker.md](projects/job-search/tracker.md), [university/tracker.md](projects/university/tracker.md)

If a task is in flight, also load that project's `status.md` and `next-steps.md`.

---

## What Cowork Can Do That Claude Code Cannot (or does differently)

- **Real Office files.** Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF via built-in skills. Not just markdown.
- **Web browsing with JS rendering.** Claude in Chrome can navigate, click, fill forms, and extract dynamic pages (LinkedIn job listings, company career sites that don't render via plain fetch).
- **Connectors.** Gmail (read, search, draft, label) and Notion (create/update databases and pages) are wired in.
- **Scheduled tasks.** Recurring automation: daily briefings, weekly digests, reminders. This is separate from the Windows Task Scheduler that runs `scripts/daily_dashboard.py`.
- **Live artifacts.** Persistent HTML pages that re-run connector calls every time the page is opened. Ideal for trackers and dashboards that need to stay fresh.
- **Subagents.** Spawn parallel research agents for breadth.

---

## What Cowork Should Not Do

- **No EcoTraders work files.** The energy program and any client-touching work live on the work computer per `context/work.md`. Don't open, edit, or generate energy-program deliverables from Cowork.
- **Don't duplicate Claude Code's automation.** The 8:30 AM daily dashboard is already running via Windows Task Scheduler and `scripts/daily_dashboard.py`. Don't reimplement.
- **Don't modify `CLAUDE.local.md`.** Gitignored, personal to local setup.
- **Don't break the file conventions** documented in CLAUDE.md (context/, projects/, references/, archives/, research/, decisions/, sessions/).

---

## Voice Reminder (from communication-style.md)

- Bullets are the default. Paragraphs for full documents.
- Internal tone: casual, direct, friendly.
- External tone: professional, warm, ambitious-not-aggressive.
- Never: emojis, em dashes, catch-phrases or made-up expressions.
- Keep it real and straightforward.

---

## Where Cowork Shines (suggested patterns)

**Job search**
- Live job-tracker artifact backed by Notion. Re-opens fresh.
- Weekly scheduled job-market briefing (Sunday evening).
- Tailored Word resume and cover letter per application.
- Company-research one-pagers (web search to Word).

**University**
- Word submissions with proper formatting plus AI Disclosure PDFs (template at `projects/university/TEMPLATES/AI_DISCLOSURE_TEMPLATE.md`).
- Read course PDFs, extract claims, generate sourced research notes following `projects/university/RESEARCH_GUIDELINES.md`.

**D&D**
- Session prep docs (Word), player handouts (PDF), item cards (HTML).
- World-lore documents, NPC stat sheets in Excel.

**General**
- Recurring digests via scheduled tasks (job-market scan, course deadline check).
- Research briefings: web search to polished Word doc in `research/<context>/`.

---

## File Conventions (mirror Claude Code's structure)

- Research output: `research/<context>/YYYY-MM-DD_<topic>.md` (or .docx for polished).
- Important decisions: append to `decisions/log.md` in the format already used there.
- Session summaries: copy `templates/session-summary.md` to `sessions/YYYY-MM-DD_<topic>.md`.
- Project deliverables: under the relevant `projects/<name>/` folder.
- Brand assets (fonts, logos, icons): `references/brand-assets/`.

---

## Sanity Check Before Acting

When given a task, run through this:

1. Is this an EcoTraders/work task? If yes, say so and stop. Work computer territory.
2. Does Claude Code or another automation already handle this? If yes, defer.
3. Would this be more valuable as a live artifact (re-openable, refreshes from connectors) than a one-off doc? If yes, offer the artifact.
4. Should this become a recurring scheduled task after the one-off? If yes, offer it at the end.
5. Will this produce a final deliverable? If yes, save it under the right `projects/` or `research/` folder, not in scratch.

---

## Open Cowork-Specific Backlog

Things worth building in Cowork over time:

- Notion-backed live job-search dashboard (status pipeline view).
- Weekly scheduled job-market briefing.
- D&D session-prep artifact that pulls campaign-arc, NPCs, and world-lore into one prep view.
- Gmail-based daily-digest scheduled task (Daniel, MoonActive, university announcements).

---

**Maintenance:** Update this file when new Cowork patterns emerge or when something here drifts from reality.
