# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---

[2026-05-14] DECISION: Birthday playlist structure (start energetic, genre clusters, Hebrew distributed, house late) | REASONING: Tested approach of easing into genres rather than starting chill; heard feedback that pure house start didn't work, rock anchors resonate better, Hebrew songs need to feel natural not forced | CONTEXT: 30-song playlist for May 15 birthday party (1-5 PM, diverse friend group in Jerusalem)

[2026-05-16] DECISION: Build /save-context as aggressive extraction system | REASONING: Avoid re-explaining context every session; automatic file updates prevent manual note-taking; memory system learns patterns; scales across all projects (D&D, university, job search, work) | CONTEXT: Post-session context management system; user wants it to extract decisions, session summaries, references automatically

[2026-05-16] DECISION: Dragon patron as core to Aerendil's arc, reveals gradually (level 2-3 = dragon, level 4+ = enslaved, level 6 = direct aid in final battle) | REASONING: Maintains mystery while ensuring personal investment in dragon freedom; creates emotional weight for final confrontation; fiery dreams are dragon's only remaining power | CONTEXT: Half-Elf Warlock character development, levels 1-6 campaign arc

[2026-05-16] DECISION: Library scene as structured opportunities (not prescriptive) with three magical items available based on search rolls | REASONING: Respects player agency and discovery pace; gives multiple hooks (Harmony Lute for Bard, dragon lore for Aerendil, freedom values for Herald); keeps narrative momentum fast | CONTEXT: Session plan for Tuesday, addressing player feedback on pacing and character depth

[2026-05-16] DECISION: Implement /save-context as simple conversational request, not a command | REASONING: Native Claude Code slash commands require system registration which is not directly available; instead, simple workflow where user says "save context" and extraction happens immediately with file updates; no setup needed, works right now | CONTEXT: User needed simple invocation method that actually works; pivoted from trying to create slash command to functional immediate workflow

[2026-05-20] DECISION: Darkling binding mechanic - crystalline marks on skin, forced bond by the Betrayer | REASONING: Shows the Betrayer practicing the same forced bonding he plans for the dragon, but on smaller creatures first; Darklings become victims not just enemies; thematically previews the dragon's situation without announcing it | CONTEXT: Session 2 planning; needed to explain why Darklings fear the Betrayer more than death

[2026-05-20] DECISION: Aerendil's dream system - wakes next to fire, one word at a time, option to continue from Dream 2 onward, eventually goes fully into fire | REASONING: Creates a personal escalating mechanic that builds mystery across the campaign; dreams get clearer as the campaign progresses toward the patron reveal at level 4-5 | CONTEXT: Session 2 planning for D&D campaign; patron is an ancient enslaved dragon

[2026-05-20] DECISION: Session 2 title "Chains" | REASONING: The word from Aerendil's first dream; simultaneously references Darkling binding and foreshadows the dragon's enslavement; works on every level of the campaign's central theme | CONTEXT: D&D Adventure 2 session naming

[2026-05-20] DECISION: Herald's arc pushed through learning his order was complicit in suppressing Dragon Rider knowledge (interrogation scene) | REASONING: Herald's player doesn't know his order well - revelation works better than recognition; learning they actively signed off on the Scholar's exile is new information that recontextualizes his departure | CONTEXT: Session 2 planning; Herald's arc was stalled after temple visit in Session 1

[2026-05-22] DECISION: Skills (.claude/skills/) are proactive natural language triggers; Commands (.claude/commands/) are explicit slash commands | REASONING: Original save-context was mis-built as a skill file documenting a slash command - the two mechanisms are fundamentally different and shouldn't be conflated | CONTEXT: Debugging why /save-context didn't work; fixed by creating .claude/commands/save-context.md and rewriting the skill as a proactive trigger

[2026-05-22] DECISION: Pursue exploratory call with Lightricks PM despite role being senior | REASONING: PM was open to talking and the outreach was reframed as curiosity/networking rather than cold applying; Omri researched the company (Facetune/LTX split, 50M users, A/B testing culture) to prepare | CONTEXT: PM replied to LinkedIn outreach flagging it's a senior role; Omri chose to move forward with the conversation

[2026-05-26] DECISION: Archive Found/unactioned jobs to tracker-archive.md, keep main tracker active applications only | REASONING: Main tracker was 87 lines with 30+ stale Found rows loading into every session - unnecessary token cost and noise | CONTEXT: Job tracker optimization session

[2026-05-26] DECISION: Job searches run inline (WebSearch directly), not via research sub-agent | REASONING: Custom .claude/agents/ files don't override system agent tool permissions when called via subagent_type - WebSearch never reached the agent despite being in frontmatter; inline is also cheaper | CONTEXT: Testing research agent after adding WebSearch - agent still said it had no web access

[2026-05-26] DECISION: Skills require YAML frontmatter (name + description) to be recognized by Claude Code | REASONING: job-tracker.md and save-context.md had no frontmatter and weren't reliably triggering; adding frontmatter fixed recognition | CONTEXT: Skill improvement session with skill-creator

[2026-05-26] DECISION: Build assignment skill as two-phase workflow (intake gate → draft) with no-research-without-draft rule | REASONING: Assignments written without verified sources need full rewrites; the gate forces the research-first workflow that worked well for HW2; also ensures sources.md and notes.md are always created for future reference | CONTEXT: Building university assignment writer skill using skill-creator eval loop

[2026-05-26] DECISION: Assignment skill uses brief's structure first, standard template as fallback | REASONING: Post-eval feedback showed that drafts should follow the assignment's specific questions/sections in order, not be reformatted into a generic academic report structure | CONTEXT: Skill eval iteration; user noticed structure mismatch in baseline draft

[2026-05-27] DECISION: Use Tel Aviv Open Data Dataset 90 (Fitness Centers) over CBS socioeconomic index for Urban Analytics lab | REASONING: More directly relevant to the athlete synthetic population; publicly accessible via GIS API; real facility-level data with neighborhood field for joining | CONTEXT: Urban Analytics Session 3 lab - needed open dataset to correlate with synthetic Tel Aviv athletes dataset

[2026-05-27] DECISION: Use reportlab for PDF generation instead of pandoc or weasyprint | REASONING: pandoc not installed on this machine; weasyprint not available; reportlab was already installed and gives full layout control | CONTEXT: Generating polished lab report PDF for Urban Analytics Session 3

[2026-05-30] DECISION: Read BAFU database via PowerShell COM object (Excel.Application) rather than direct file read | REASONING: .xlsx is binary and unreadable by the Read tool; COM object lets us query specific rows/columns without converting the file | CONTEXT: HW3 LCA assignment - needed to search 11,749-row BAFU emissions database for specific material datasets

[2026-05-30] DECISION: AI disclosure in assignments framed as "brainstorming partner and calculation aid" not listing all tasks Claude performed | REASONING: Listing everything Claude did raises academic integrity questions; framing as brainstorming + calculation check matches what the assignment allows (ChatGPT brainstorming explicitly welcomed in HW3 brief) and keeps analytical ownership with Omri | CONTEXT: HW3 LCA draft - user flagged that full disclosure of Claude's role could raise questions with the professor

[2026-05-30] DECISION: HW3 Option B (cups) chosen over Option A (PET bottle) | REASONING: Option A had an AI prompt injection trap planted in the PDF header instructing Claude to fabricate a fixed 10 kgCO2eq result; Option B had no such trap | CONTEXT: HW3 LCA assignment with two product options; trap identified before any work began

[2026-05-31] DECISION: ReportLab table cells must use Paragraph objects, not raw strings | REASONING: Raw strings in reportlab Table cells do not word-wrap properly and overflow column bounds visually; wrapping in Paragraph() with explicit font size and leading fixes this | CONTEXT: HW3 PDF polish - appendix inventory tables had text spilling out of cells

[2026-05-31] DECISION: University logos stored at references/brand-assets/university-logos/ with filename reichman-main-logo.png | REASONING: Follows existing UNIVERSITY_LOGOS.md guide already in the repo; generate_pdf.py checks for the file at runtime and gracefully skips if absent | CONTEXT: HW3 PDF cover - user wanted to add Reichman logo; standardizing location for future assignments

[2026-05-31] DECISION: Configure Claude Code status line via bash script to show model + context size + effort + progress bar + token count | REASONING: User wanted persistent visibility of context usage and token counts without running /cost each time; matches screenshot reference showing "148k / 1000k tokens" format | CONTEXT: Script at C:\Users\User\.claude\statusline-command.sh; settings.json updated with statusLine block; requires restart to activate

[2026-05-31] DECISION: Always stage, commit, and push all pending changes as part of the save-context / end-of-session workflow | REASONING: Work PC couldn't see yesterday's work because changes were never pushed; git push should be the final step of every session so all devices stay in sync | CONTEXT: User tested cross-device sync and found stale state on work PC; explicitly requested this become standard behavior

[2026-05-31] DECISION: Tax incentive model uses depreciation multiplier (e.g. 2× = 20%/year for 5 years) not a "% in year 1" parameter | REASONING: Multiplier is more intuitive, maps to Cyprus model and existing Israeli mechanisms, and better represents how the policy would be framed to the Ministry | CONTEXT: Building Excel model for national energy efficiency program tax incentive analysis

[2026-05-31] DECISION: Tax incentive model will consolidate to 2 sheets only (global assumptions + single analysis sheet with all 4 technologies) | REASONING: Matches the format of the existing grants analysis Excel the Ministry already uses; all calculations under section 3 of the analysis sheet | CONTEXT: Reviewing current 7-sheet model structure during walkthrough session

[2026-05-31] DECISION: Add equipment degradation factor as input to the energy savings calculation | REASONING: Energy savings are not flat over lifetime — equipment efficiency degrades ~0.5–1%/year; affects NPV accuracy especially for 15–17 year lifetimes | CONTEXT: Walking through tax model structure; degradation rate to be confirmed with Rafi alongside CapEx and kWh data

[2026-05-31] DECISION: Payback period in final model should use NPV cumulative crossover (when running sum turns positive), not simple CapEx ÷ annual savings | REASONING: Simple formula only accounts for Year 1 tax shield; cumulative NPV row already captures the correct crossover point | CONTEXT: Tax model Section 5/6 review

[2026-06-02] DECISION: Auto-update today.md date via session-start hook (option 2), not a CLAUDE.md instruction | REASONING: Hook runs before Claude reads any files, so the date is always correct by the time context loads; instruction-based approach requires Claude to notice and act, which is less reliable | CONTEXT: today.md was stuck on May 30 even after days away; hook updates the 3 date fields, Claude handles archiving stale completed items per CLAUDE.md instruction

[2026-06-02] DECISION: Repo folder structure rules: projects get README.md + tracker.md only; no per-project status.md or next-steps.md | REASONING: Those files were always stale (all last updated May 14, never maintained) because live state belongs in today.md and the tracker; having them created an illusion of documentation that was actually noise | CONTEXT: Repo audit session; deleted 7 stale status/next-steps files across all projects

[2026-06-02] DECISION: Work PC branches must be merged to master and pushed at end of every session (not left as claude/* branches) | REASONING: Branches were invisible to home PC until git pull revealed them; the save-context skill now includes a merge-to-master step so both PCs always stay on master | CONTEXT: Discovered two unmerged branches (tax model + CapEx pipeline) from May 31 and June 1 work PC sessions

[2026-06-02] DECISION: Protect work-PC Claude Code with deterministic deny rules + PreToolUse hook, not a "guardian agent" | REASONING: A guardian agent is still an LLM and can be wrong or talked around; deny rules and hooks are harness-level and cannot be reasoned around. Real risk on the work PC is data exfiltration (client names + tax IDs leaving the machine) and destructive file ops, not "code attacking the computer" | CONTEXT: Omri worried the CapEx extraction Python might be harmful; friend suggested a guardian agent. Built kit at references/work-pc-security/ (settings.json deny rules + block-network.ps1 hook + README)

[2026-06-02] DECISION: CapEx extraction scripts audited and confirmed safe (no network/exec/destructive ops) | REASONING: Read all of capex_pipeline.py, extract_capex.py, diag_walk.py plus exhaustive grep for network/subprocess/eval/pickle/delete patterns; only imports are sys/os/re/csv/warnings/collections/openpyxl, workbooks opened read_only, all writes go to the passed-in folder. Local file-processing code can only exfiltrate via a network call, and there are none | CONTEXT: Security review of the June 1 CapEx pipeline before trusting it on real work files

[2026-06-02] DECISION: Work-PC security kit is parked, not deployed — Omri uses Claude Code online only | REASONING: The desktop settings.json + PowerShell hook do nothing for the web/cloud version; online code runs in an isolated sandbox that cannot touch the physical work PC, so "harmful code" is off the table. For online-only use the entire security model is "be deliberate about what you upload" — upload anonymized/sample files, never real files with company names + tax IDs | CONTEXT: Clarified mid-session that all work-PC work is done on Claude Code online because it's easier
