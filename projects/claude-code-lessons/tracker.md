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

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>Want an "AI kill list" -- specific words, phrases, and structural patterns that read as AI slop, banned from all content/output/conversations, not just a vague "sound natural" instruction</td>
<td>CLAUDE.md rule</td>
<td><strong>Done</strong></td>
<td>Expanded <code>.claude/rules/communication-style.md</code>'s old 4-line "Writing Rules" into a full "AI Kill List" section (buzzwords/filler, structural tics, openers/closers), seeded with common AI-tell patterns Omri can edit/trim/add to. Applies everywhere including academic docs, not just casual register. Living list -- keep adding items as they surface.</td>
</tr>

<tr style="background-color:#eaeaea;">
<td>2026-07-14</td>
<td>Nate (course) keeps his AI kill list + general preferences at the GLOBAL Claude Code level (outside any single project) so they apply across all his projects, not just one. Omri currently only uses Claude Code for SHMAGS 2, so project-level (current setup) is correct for now -- but once a second project starts, the kill list + tone/formatting prefs from <code>.claude/rules/communication-style.md</code> should move/copy to a global config so both projects inherit them.</td>
<td>Folder structure / Settings config</td>
<td><strong>Not Started</strong></td>
<td>Mechanism confirmed: Claude Code supports a user-level <code>CLAUDE.md</code> at <code>C:\Users\User\.claude\CLAUDE.md</code> (does not exist yet -- checked 2026-07-14, only settings.json etc. live there). When actioned: move the tone/formatting/AI-kill-list portions of communication-style.md there (not SHMAGS-2-specific business/EA context, which should stay project-local). Trigger: whenever Omri starts a second Claude Code project.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>Course covers .env files for keeping secrets (API keys, passwords) out of GitHub. Prompted a full audit of SHMAGS 2 for leaked secrets -- don't just assume .gitignore is correct, actually verify.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Audited and confirmed clean: <code>.env</code> (holds ANTHROPIC_API_KEY) is gitignored and was never committed; scanned all 225 tracked files + full git history for API key/AWS key/GitHub token/private-key patterns, zero real hits (one false positive: "AKIA" substring inside base64 binary data in an old eval artifact). Urban Analytics and Economics Final folders aren't git repos at all, so nothing from them is exposed anywhere. Work-PC situation is separate/already handled (Claude Code online-only, anonymized uploads, no local repo involved).</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>Installed the googleworkspace/cli (<code>gws</code>) tool to give Claude Code direct terminal access to Drive/Gmail/Calendar/Sheets/Docs/Slides/Tasks/Chat, on top of the existing Gmail-only MCP connector.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Installed via npm (<code>gws 0.22.5</code>). Installed Google Cloud SDK (winget, <code>Google.CloudSDK</code>) to manage the GCP side. Created new GCP project <code>omri-gws-cli</code>, enabled 44 Workspace APIs. Learned OAuth client creation is NEVER automatable via gcloud, even with the SDK installed -- always requires manual clicks in Cloud Console (consent screen + Desktop OAuth client), regardless of which setup path is chosen. Downloaded <code>client_secret.json</code> to <code>C:\Users\User\.config\gws\client_secret.json</code>, logged in as omrisham53@gmail.com (had to add self as a Test User under Audience since the consent screen defaults to Testing mode -- even the project owner isn't auto-whitelisted). Verified working with a live Drive files list call. gws is now usable from Bash/PowerShell directly.</td>
</tr>

<tr style="background-color:#fff3cd;">
<td>2026-07-14</td>
<td>gws OAuth consent screen is in Testing mode, which caps refresh tokens at 7 days -- re-login (<code>gws auth login</code>) will be needed roughly weekly until/unless the app is published to Production.</td>
<td>Habit-workflow</td>
<td><strong>In Progress</strong></td>
<td>Flagging now, not yet decided: live with the weekly re-login (simple, no extra setup), or go through Google's app verification process to move to Production (removes the 7-day cap but is a heavier one-time process, may not be worth it for personal-only use). No action taken yet -- revisit if the weekly re-login gets annoying.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>VS Code has useful default-behavior settings worth tuning: whether new Claude Code sessions open as terminal vs. panel view, and whether .md files default to rendered Preview vs. raw source editor.</td>
<td>Settings config</td>
<td><strong>Done</strong></td>
<td>Added <code>claudeCode.useTerminal</code> and <code>workbench.editorAssociations</code> (<code>"*.md": "vscode.markdown.preview.editor"</code>) to the global VS Code <code>settings.json</code> (<code>%APPDATA%\Code\User\settings.json</code>). Omri doesn't edit markdown by hand, so applied globally rather than scoped to one file; to edit a file when needed, right-click tab -&gt; Reopen Editor With -&gt; Text Editor.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>gws can build a full, styled Google Slides deck (diagrams, icons, charts, terminal mockups, custom color system) directly from a plain-English brief -- not just read/write data in existing files.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Built a 9-slide visual deck for Itai entirely through <code>gws slides presentations batchUpdate</code> (native shapes/lines/text boxes, no manual Slides editing). Gotcha: object IDs in createShape/createLine/createSlide requests must be 5+ characters or the whole batchUpdate call fails validation. Workflow: generate batch JSON with a small Python helper script, apply via gws, pull thumbnails back via <code>getThumbnail</code> to visually verify and catch layout collisions before calling it done. Reusable pattern for any future deck request.</td>
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
