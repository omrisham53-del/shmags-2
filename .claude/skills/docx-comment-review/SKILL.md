---
name: docx-comment-review
description: Work through reviewer comments on a Word (.docx) chapter for EcoTraders' national energy-efficiency program and apply the agreed fixes as tracked changes. Use this whenever Omri has a chapter that came back with comments from Daniel (or anyone) and needs to address them - "Daniel sent back the grants chapter with comments", "go through the review comments", "address the comments on this docx", "I got the file back from review", "apply the review fixes", "/review-comments", or any time he points at a commented .docx and wants to resolve it. Use it even if he doesn't say the word "comment" - if a reviewed chapter needs its feedback worked through and a new version produced, this is the skill. NOT for writing a chapter from scratch (that is a separate chapter-writing flow) and NOT for the academic assignment writer.
---

# DOCX Comment Review

Daniel reviews every chapter Omri writes for the national energy-efficiency program. The review comes back as a `.docx` full of Word comment bubbles. This skill is the loop that turns those bubbles into an agreed, tracked-changes revision saved under the next version number.

The point is not to blast through the comments automatically. Daniel's comments carry real analytical content (a number is wrong, a framing is off, a link to the tax mechanism is missing), and Omri owns the chapter, so each fix should be his call. Your job is to make that fast: pull every comment with the exact text it points at, propose a concrete fix for each, let Omri accept/edit/skip, then apply the accepted ones cleanly as tracked changes so Daniel can see on his next pass exactly what changed.

This runs on Omri's **work PC**, against real client files. The skill itself is just instructions and lives in the repo; it syncs to the work machine via git. Never upload a real chapter (company names, tax IDs) anywhere.

## The two scripts

Both are in `scripts/`. They handle the docx XML so you don't have to reason about Word's comment and revision markup by hand.

- **`read_comments.py <file.docx>`** - extracts every comment bubble paired with the exact document text it is anchored to. Add `--json` for machine-readable output. The anchored text matters: it is what the reviewer is pointing at, and what a replacement has to act on.
- **`apply_revisions.py <file.docx> <corrections.json> [--author "Omri"]`** - applies approved corrections as tracked changes (a tracked deletion of the old anchored text plus a tracked insertion of the new), leaves the comment bubbles in place, and saves under the bumped version number. `corrections.json` is a list of `{"id": "<comment id>", "new_text": "<replacement>"}`.

## Workflow

### 1. Read the comments

Run `read_comments.py` on the file. Show Omri the full list: for each comment, the reviewer, the anchored text, and the comment itself. This orients both of you on the whole review before touching anything.

### 2. Propose a fix per comment, one batch

For each comment, work out what addressing it actually means and draft the concrete `new_text`. Comments come in a few shapes, and the right `new_text` differs:

- **Replace** ("this number is wrong", "tighten this phrasing") - `new_text` is the corrected version of the anchored text.
- **Add** ("add a sentence linking this to the tax mechanism") - `new_text` is the anchored text *plus* the new content, since the script replaces the anchored span. Don't send a bare addition - send the whole resulting sentence.
- **Judgement / question** ("are you sure this holds after 2027?", "consider reframing") - there may be no single right edit. Surface it to Omri, propose an option, but expect discussion. Some of these resolve to "no change, I'll reply to Daniel instead."

Use what you know about this program (the grants chapter framing, Decision 1261, the ₪500M/2025-2027 budget, the carrot-vs-stick framing, the decisions log) to make the proposed fixes real, not generic. A weak proposal wastes Omri's time; a sharp one he can just approve.

Present them together as a numbered list - anchored text, Daniel's comment, your proposed `new_text` - so Omri can go down the list quickly and say "1 yes, 2 use this instead, 3 skip".

### 3. Lock the corrections with Omri

Take his accept/edit/skip on each. Skipped comments simply don't go in `corrections.json` (the bubble stays, unaddressed, for him to handle or reply to). Build `corrections.json` from the approved set.

### 4. Apply as tracked changes

Run `apply_revisions.py`. It writes the next version (e.g. `... 0.2.docx` -> `... 0.3.docx`), never overwriting the input. Report what was applied and what was skipped, and why.

Then tell Omri to open the new file in Word and eyeball the tracked changes before anything goes further - the script is solid on single-paragraph comment ranges but you both want eyes on a real client document. Comments that span multiple paragraphs are skipped by the script with a warning; handle those by hand in Word.

## Version numbering (EcoTraders scheme)

Files carry a version in the filename. The scheme:

- `0.x` = pre-client internal drafts. Each work or review pass bumps the minor: `0.1` (first draft) -> `0.2` (after a review) -> `0.3` (next pass).
- A whole number = a client release. The first client-ready version is `1`, then `2`, then `3`.
- After a client release, internal revisions add a minor again: `1` -> `1.1` -> `1.2`, until the next client release `2`.

`apply_revisions.py` encodes this: it bumps the minor by one (`0.2` -> `0.3`, `1` -> `1.1`, `2.4` -> `2.5`). Promotion to a client version (e.g. `0.4` -> `1`) is a deliberate human decision, not something this skill does. If Omri says "this one's going to the client," rename to the next whole number by hand.

## Notes

- Chapters are **Hebrew, RTL**. The scripts are encoding-safe (UTF-8, no terminal box-drawing). When you draft `new_text`, write natural Hebrew that matches the chapter's register.
- The reviewer author defaults to "Omri" on the tracked changes (it's Omri making the edits in response to Daniel). Pass `--author` if that should differ.
- Keep the comment bubbles. Omri was explicit: he does not want a clean file with the comments stripped - he and Daniel both need to see the comment sitting next to the revision that answers it.

## Known limits (v1 - revisit after the first real chapter)

Built and tested against synthetic, single-sentence comments. A real Daniel review will likely stress these, so when it does, that's the signal to update the skill rather than force it:

- **Multi-paragraph comment ranges** are skipped, not applied. If Daniel routinely comments across whole sections, `apply_revisions.py` needs to handle ranges that span paragraphs.
- **Run-level formatting inside the anchored text** (bold, a footnote, a citation in the middle of the commented span) is collapsed - the replacement is inserted as one clean run carrying the first run's formatting. Fine for plain prose, lossy if the anchored text is richly formatted.
- **Footnotes / tracked footnote edits** aren't handled at all. The program's chapters lean on footnotes heavily (the citation scheme), so editing text that lives in a footnote, or a comment attached to one, is out of scope for v1.
- **Comments that aren't text edits** - "let's discuss", "check with Rafi", a question - have no `new_text`. The skill should leave these for Omri to reply to Daniel directly; don't invent an edit to make the bubble go away.
- **Tracked-changes rendering across Word versions** - validated structurally, not visually in Word. First real run, confirm Word shows them as expected before trusting it on a client deliverable.
