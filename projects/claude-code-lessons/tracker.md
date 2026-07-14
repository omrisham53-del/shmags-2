# Claude Code Lessons Tracker

**Last Updated:** July 14, 2026

Backlog of lessons/ideas from the 6-hour Claude Code manual, plus meta-lessons that surface organically during regular work sessions (auto-fed by `/save-context`). Add new rows as lessons come up; work them in any order across sessions.

Row colors are HTML, so they only render as color in **VS Code Markdown Preview** (Ctrl+Shift+V) -- viewed as raw text or on GitHub it still reads fine, just without the background tint.

---

## Backlog

<table>
<thead>
<tr>
<th>Date Added</th>
<th>Lesson / Idea</th>
<th>Implies</th>
<th>Status</th>
<th>Notes</th>
</tr>
</thead>
<tbody>

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>save-context should also capture Claude Code meta-lessons (not just project decisions) and feed them here automatically at the end of every session</td>
<td>Skill/Command edit</td>
<td><strong>Done</strong></td>
<td>Added a "Claude Code meta-lessons" extraction category + a tracker-append step to both <code>.claude/skills/save-context.md</code> and <code>.claude/commands/save-context.md</code></td>
</tr>

</tbody>
</table>

---

## Status Legend

<table>
<tbody>
<tr style="background-color:#eaeaea;"><td><strong>Not Started</strong></td><td>captured, not yet worked -- this is what to scan for first</td></tr>
<tr style="background-color:#fff3cd;"><td><strong>In Progress</strong></td><td>actively being implemented this session</td></tr>
<tr style="background-color:#d4f4dd;"><td><strong>Done</strong></td><td>implemented and verified</td></tr>
<tr style="background-color:#e0e0e0;"><td><strong><em>Skipped</em></strong></td><td>considered, decided not to apply here (reason in Notes)</td></tr>
</tbody>
</table>

## Categories (for the "Implies" column)
Skill (new or edit) / Command / CLAUDE.md rule / Settings config / Folder structure / Habit-workflow / Other

---

## Row Template (copy-paste, pick the color matching Status)

```html
<tr style="background-color:#eaeaea;"> <!-- Not Started -->
<td>YYYY-MM-DD</td>
<td>Lesson text</td>
<td>Category</td>
<td><strong>Not Started</strong></td>
<td>Notes</td>
</tr>

<tr style="background-color:#fff3cd;"> <!-- In Progress -->
<td>YYYY-MM-DD</td>
<td>Lesson text</td>
<td>Category</td>
<td><strong>In Progress</strong></td>
<td>Notes</td>
</tr>

<tr style="background-color:#d4f4dd;"> <!-- Done -->
<td>YYYY-MM-DD</td>
<td>Lesson text</td>
<td>Category</td>
<td><strong>Done</strong></td>
<td>Notes</td>
</tr>

<tr style="background-color:#e0e0e0;"> <!-- Skipped -->
<td>YYYY-MM-DD</td>
<td>Lesson text</td>
<td>Category</td>
<td><strong><em>Skipped</em></strong></td>
<td>Notes</td>
</tr>
```
