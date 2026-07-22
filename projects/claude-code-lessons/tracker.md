# Claude Code Lessons Tracker

**Last Updated:** July 21, 2026

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

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>gws OAuth consent screen is in Testing mode, which caps refresh tokens at 7 days -- re-login (<code>gws auth login</code>) will be needed roughly weekly until/unless the app is published to Production.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Fixed 2026-07-17: no full Google verification needed for personal single-user use -- just clicked <strong>Publish App</strong> in Cloud Console (OAuth consent screen -> moves Testing -> In Production), which lifts the 7-day cap since the app owner/sole user just clicks through the one-time "unverified app" warning. Re-ran <code>gws auth login</code> after publishing (old token still carried the 7-day expiry, had to get a fresh one). Verified live with <code>gws gmail users getProfile</code>. No more weekly re-login needed.</td>
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

<tr style="background-color:#d4f4dd;">
<td>2026-07-14</td>
<td>General principle: OS-level installs and credential storage are portable across AI tools; anything scoped to one tool's own session is not. Checked whether switching from Claude Code to a different tool (e.g. Codex) would mean reconnecting gws from scratch.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Confirmed gws's OAuth credentials live at <code>C:\Users\User\.config\gws\</code> (encrypted file + OS keyring), and both <code>gws</code> (npm) and <code>gcloud</code> (winget) are registered on the permanent Windows user-level PATH (verified straight from the registry, not just the current shell). None of that state lives inside Claude Code or this repo's <code>.env</code> -- any new tool that can run shell commands opens a fresh process, reads the same PATH, and finds gws already authenticated. The only session-scoped thing was manually exporting the Cloud SDK path inside already-running Bash calls, which a brand-new terminal never hits. Takeaway for future tool setups: prefer real OS-level installs + OS-level credential storage over anything sandboxed to one tool's session, so switching tools later never requires redoing auth.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-17</td>
<td>Portal-gated document sites (e.g. environdec.com's EPD/PCR library) often expose a direct file-download API endpoint discoverable via WebFetch on the library page, even when the site's own UI walks you through account registration first.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Used this to source real EPD + PCR PDFs for the LCA final assignment directly via <code>curl</code> against <code>api.prod.environdec.com/.../Documents</code> -- skipped the manual portal signup the assignment brief walked through entirely. Reusable pattern for future academic research on similar registries.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-17</td>
<td>The Read tool's PDF extraction pulls the underlying embedded text, not a rendered image -- so hidden white-on-white or off-page prompt-injection text (the AI-trap pattern from HW3 in May) would surface in the extracted content exactly like visible text.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Confirmed this is a reliable way to scan a document for that specific trap type, not just a formality -- reading a PDF with Read IS the trap check, no separate step needed. Used to clear 4 LCA source PDFs this session.</td>
</tr>

<tr style="background-color:#eaeaea;">
<td>2026-07-17</td>
<td>The Bash tool's sandboxed shell can report the wrong timezone for "what time is it" (returned JST instead of Israel time this session) -- don't trust the sandbox system clock for the user's local time, ask directly instead.</td>
<td>Habit-workflow</td>
<td><strong>Not Started</strong></td>
<td>Worked around it this session by just asking Omri directly. No fix needed, just a standing habit to remember.</td>
</tr>

<tr style="background-color:#eaeaea;">
<td>2026-07-17</td>
<td>gcloud CLI (installed 2026-07-14 per that session's decision log entry, confirmed on the permanent Windows PATH) was not found in this session's Bash or PowerShell when trying to check the gws OAuth consent screen's publishing status.</td>
<td>Habit-workflow</td>
<td><strong>Not Started</strong></td>
<td>Worked around it by just doing the fix manually in Cloud Console instead (which was needed anyway, per the standing "OAuth changes require manual clicks" lesson). Open question whether this is a one-off session quirk or a real PATH-persistence gap worth investigating if it recurs.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>Editing a .docx with python-docx fails with a <code>PermissionError</code> if the file is currently open in Word -- the <code>~$filename.docx</code> companion file is the tell.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Hit this mid-session writing script edits into an open <code>script.docx</code>. Fix: check for the <code>~$</code> lock file (or just try the write and catch the <code>PermissionError</code>) and ask the user to close the file rather than forcing it. Retried successfully once Omri closed Word -- no data lost.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>gws gmail +send's <code>-a</code>/<code>--attach</code> rejects any file path that resolves outside the current working directory, even a legitimate absolute path to a real file.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Had to <code>cp</code> the target file (from an unrelated folder outside the repo) into the repo's cwd before attaching, then <code>rm</code> it right after sending so it doesn't linger as an untracked file. Reusable pattern: always stage external attachments into cwd first when using <code>gws gmail +send</code>.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>Edge headless (<code>--headless=new</code>) was unreliable in this sandboxed Bash environment for capturing a real webpage screenshot -- silent failures and profile-lock collisions across repeated calls even with a fresh <code>--user-data-dir</code>; switching to Chrome headless with a fresh <code>--user-data-dir</code> per call worked reliably on the first try.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Also: screenshot output height caps around ~1200-1250px regardless of a taller <code>--window-size</code> request, so capturing a full article requires cropping the region of interest with PIL afterward rather than one tall screenshot. Used to capture the real Calcalist article headline for a presentation deck instead of a mockup.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>python-pptx can build a fully custom deck locally, and gws can convert it to a native (editable) Google Slides file on upload by setting the target mimeType in <code>--json</code> metadata alongside <code>--upload</code>/<code>--upload-content-type</code> set to the source PPTX mimetype.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td><code>gws drive files create --upload deck.pptx --upload-content-type application/vnd.openxmlformats-officedocument.presentationml.presentation --json '{"mimeType":"application/vnd.google-apps.presentation",...}'</code> triggers Drive's real conversion, not just an uploaded static file. To iterate, <code>gws drive files update --upload</code> on the same fileId overwrites content in place, keeping the same shareable link. Complements the 2026-07-14 batchUpdate-based deck lesson -- this path is better when layouts need pixel-precise custom positioning (color-coded cards, big stat callouts, embedded real images/charts) that's easier to lay out in python-pptx than via repeated batchUpdate calls. Verified rendering via <code>getThumbnail</code> per slide before delivering, same as the 07-14 pattern.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>Building a submission-ready .docx from a markdown draft is reliable via a custom python-docx script tailored to the doc's own structure, but the conversion should be visually verified, not just trusted from the generation code.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Verification pipeline: render the .docx to PDF via Word COM automation (<code>win32com.client.Dispatch('Word.Application')</code>, <code>doc.SaveAs(pdf_path, FileFormat=17)</code>), then rasterize pages with PyMuPDF (<code>fitz</code>) since poppler/pdftoppm isn't installed in this environment and the Read tool's built-in PDF-page rendering depends on it. This caught a real leftover em dash on the cover page that reviewing the conversion script alone would have missed. Used for the Final LCA assignment; script at <code>research/academic/final-lca-assignment/md_to_docx.py</code>.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>The dataviz skill is framed around interactive HTML/web charts, but its core method (pick the form by job, fixed categorical hue order per role and never cycled, one-axis rule, legend placement, no rainbow) applies directly to static matplotlib charts embedded in an academic Word/PDF document too.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Used the skill's reference palette for the LCA assignment's charts: a fixed blue/green categorical pair for Interbeton/JSW across every comparison chart, and a highlight-vs-context two-color scheme (orange vs. muted gray) for the market-cap charts.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-21</td>
<td>Matplotlib pie-chart leader-line labels need explicit anti-overlap placement for small/adjacent wedges: assign each label an evenly spaced target position (top-to-bottom per left/right side) rather than placing it proportional to the wedge's own angle.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Without this, labels for thin slices sitting close together in angle (e.g. two companies each under 3% of the total) visually collide. Fixed overlapping company-name labels in two market-cap pie charts for the LCA assignment this way.</td>
</tr>

<tr style="background-color:#d4f4dd;">
<td>2026-07-22</td>
<td>Before drafting a status/data-request message about a living artifact (a model, a spreadsheet), open the actual file and read its own status markers rather than trusting the project notes. Reading the tax model's cell fill colors via openpyxl (yellow = awaiting data, orange = to verify, green/peach = settled) revealed the notes had drifted: electric steam was dropped and fuel prices were already sourced. The live file is the source of truth; notes go stale.</td>
<td>Habit-workflow</td>
<td><strong>Done</strong></td>
<td>Caught two would-be errors in the Rafi email (asking for data we already had / for a technology no longer in the model). openpyxl exposes both cell values and fill fgColor.rgb, so a color-coded legend in a workbook is machine-readable, not just visual.</td>
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
