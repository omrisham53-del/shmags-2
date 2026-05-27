---
name: assignment
description: Write university assignments from research notes. Trigger whenever the user says "write assignment", "draft my assignment", "/assignment", "start writing", "let's write the assignment", or anything indicating they want to produce a university deliverable. Also trigger proactively when the user says research is ready or asks to move from research to writing phase. Use this skill even if the user doesn't say the word "assignment" explicitly — if they have research notes and want a structured academic document, this is the skill to use.
---

# Assignment Writer

Produces a complete, submission-ready university assignment draft from existing research notes. Follows Omri's documented style conventions and handles both Hebrew (RTL) and English assignments.

---

## Phase 1: Intake

Before writing anything, collect these four pieces of information. If any are missing, ask for them directly (one question, not four):

1. **Assignment name** — used to locate the research folder at `research/academic/[assignment-name]/`
2. **Language** — Hebrew or English (if not stated, ask; this determines the entire document format)
3. **Brief/requirements** — the assignment prompt or a summary of what needs to be covered
4. **Due date** — for the tracker update

Once you have these, check whether a research folder exists:

```
research/academic/[assignment-name]/
```

**If no research folder exists:**
- Create the folder: `research/academic/[assignment-name]/`
- Create empty `notes.md` and `sources.md` files inside it
- Tell the user: "Research folder created at research/academic/[assignment-name]/. Add your notes and sources there, then come back and I'll write the draft."
- **Stop here.** Do not attempt to draft without research notes. The quality of the draft depends entirely on verified, sourced research.

**If the research folder exists:**
- Read `research/academic/[assignment-name]/notes.md`
- Read `research/academic/[assignment-name]/sources.md`
- Read `references/academic-style-guide.md`
- Proceed to Phase 2.

---

## Phase 2: Draft

### Structure Priority

Before writing a single line, read the assignment brief carefully. **The brief's structure always wins.**

If the brief specifies questions to answer (e.g., "Question 1: Define the functional unit... Question 2: Define system boundaries..."), numbered sections, or a required section list, use that structure exactly — don't convert it into a generic academic report. Answer Q1 as Q1, Q2 as Q2, in the order given.

The default templates below (Introduction → Body → Conclusions → Limitations → References) are only fallbacks when the brief provides no structural guidance.

---

### Language Detection

Everything that follows branches on language. Determine it from what the user told you in intake, or from the language of the research notes if ambiguous.

---

### Hebrew Assignments

Read the **Hebrew Mode** section of `references/academic-style-guide.md` before writing a single line.

**Document structure (follow brief first; if no structure specified, use this order):**
1. Cover page (see template below)
2. תקציר / מבוא (prose, no bullets)
3. Sections as required by the brief — bold+underlined headers, right-aligned
4. סיכום ומסקנות
5. מגבלות
6. ביבליוגרפיה (split: Hebrew sources first, English sources second)

**Cover page template** (centered, RTL):
```
[כותרת המטלה — bold, large]

[שאלת המחקר או כותרת משנה — smaller, centered]

[שם מלא — מספר ת.ז.]

[שם המסלול / התוכנית]
[שם הקורס]
[שם המרצה עם תואר]
[תאריך הגשה — DD/MM/YY]
```

**Writing rules for Hebrew drafts:**
- Analytical, direct — state the conclusion first, then support it
- Dense structured paragraphs, footnotes for inline citations (not parenthetical)
- English technical terms stay in English naturally mid-sentence (NPV, CapEx, WTP, GDP, SCC, PUE, CVM, etc.) — do not translate them
- R code, equations, and formulas are LTR even in an RTL document
- No filler transitions, no em dashes, no unsupported claims

**Bibliography format (Hebrew documents):**

```
מקורות בעברית:
• Author (Year). Title. Publisher/Journal.

English Sources:
• Author, A., & Author, B. (Year). Title of article. *Journal Name*, volume(issue), pages. https://doi.org/...
```

**After the draft, output a Word RTL Setup Checklist:**

```
## Word RTL Setup Checklist
Before submitting, apply these settings in Word:
1. Document language → Hebrew (Israel) — apply to whole document
2. All Hebrew paragraphs → paragraph direction Right-to-Left
3. Code/equation blocks → paragraph direction Left-to-Right explicitly
4. Page direction → Right-to-Left (File > Options > Advanced > Show document content)
5. Footnotes → bottom of page, Hebrew formatting, auto-numbered
6. Verify no RTL and LTR paragraph directions are mixed in the same text block
```

---

### English Assignments

Read the **English Mode** section of `references/academic-style-guide.md` before writing.

**Document structure (follow brief first; if no structure specified, use this order):**
1. Title as a heading (no cover page unless explicitly required)
2. Introduction (prose, no bullets)
3. Sections as specified by the brief — `##` headers. If the brief has numbered questions, answer them in order under those headers.
4. Conclusions and Recommendations
5. Limitations
6. References (single APA list)

**Writing rules for English drafts:**
- Short, punchy paragraphs
- Heavy bullets for synthesis, analysis, pain points
- Prose for reflections, proposals, arguments
- Tables for side-by-side comparisons
- Parenthetical citations: (Author, Year) — not footnotes
- No em dashes, no filler transitions ("It is important to note that...", "As can be seen...")

**Bibliography format (English documents):**
```
Author, A. (Year). Title. *Journal*, volume(issue). https://doi.org/...
```

---

### Citations

Build citations directly from `sources.md`. For every factual claim, data point, or number in the draft, cite the source inline. Do not leave any claim unsourced.

If a claim in the notes has no corresponding source in `sources.md`, flag it with `[SOURCE NEEDED]` in the draft — do not silently omit or fabricate a citation.

---

### After the Draft

1. **AI Disclosure summary** — briefly list what Claude assisted with (structure, phrasing, citations, synthesis) vs. what was Omri's original work (analysis, decisions, research judgment). Check if `projects/university/TEMPLATES/AI_DISCLOSURE_TEMPLATE.md` exists and reference it.

2. **Update the university tracker** — open `projects/university/tracker.md` and add or update the assignment entry:
   - Status: In Progress (or Complete if the draft is final)
   - Files: the draft location
   - Notes: brief summary

3. **Tell the user what to review:**
   - Any `[SOURCE NEEDED]` flags in the draft
   - Whether the structure matches the assignment brief
   - RTL Word checklist (Hebrew only)
   - Whether the AI disclosure needs to be submitted alongside the assignment

---

## What NOT to Do

- Never draft without research notes — a guess-based draft will require complete rewriting
- Never translate English technical terms into Hebrew
- Never mix footnote and parenthetical citations in the same document
- Never put code in the main body — always appendix
- Never add bullet points to the abstract or introduction — use prose there
- Never add filler padding or em dashes
