# Academic Style Guide

Extracted from real past assignments. Apply this whenever drafting university coursework.

---

## Writing Voice

- Analytical and direct. State the conclusion first, then support it.
- No filler phrases or padding. Every sentence carries information.
- Formal but not stiff - avoid bureaucratic language.
- Policy/recommendations sections are always concrete and actionable.
- Limitations section is always included and honest.
- English technical terms stay in English even in Hebrew assignments (NPV, CapEx, WTP, GDP, etc.).

---

## Document Structure (both languages)

Every assignment follows this skeleton (adapt to assignment type):

1. Cover page
2. Abstract / Introduction
3. Background / Literature review (if required)
4. Methodology
5. Results / Analysis
6. Discussion
7. Conclusions and Recommendations
8. Limitations
9. Bibliography
10. Appendices (if needed)

Section headers are always bold and clearly distinguished from body text.

---

## Hebrew Mode

### Cover Page (RTL, centered)
```
[Assignment Title - bold, large]

[Subtitle or research question - smaller, centered]

[Your name - ID number]
[Partner name - ID number] (if group)

[Track/Program name]
[Course name]
[Instructor name with title]
[Submission date - DD/MM/YY]
```

### Headers
- Section headers: **bold + underlined**, right-aligned
- Sub-headers: **bold only**, right-aligned
- Body text: justified (מיושר משני הצדדים)

### Paragraph style
- Dense, structured paragraphs
- Footnotes for inline citations (not parenthetical)
- Bullets (•) for lists and breakdowns within sections

### Inline citations
Use footnotes numbered sequentially. Bibliography at the end.

### Mixed Hebrew/English
- English technical terms appear naturally mid-sentence: NPV, CapEx, PUE, SCC, WTP, HPM, CVM
- English model names stay in English: Model 1, survreg, log-level
- Code blocks are LTR even in Hebrew documents
- R code, equations, and formulas are always LTR

### Word Setup for Hebrew (RTL fix checklist)
To avoid RTL/LTR mixing issues in Word:
1. Set document language: Hebrew (Israel) - applies to whole document
2. Set paragraph direction: Right-to-Left for all Hebrew paragraphs
3. For English terms mid-sentence: type normally, Word handles inline direction
4. For code/equation blocks: set paragraph direction to Left-to-Right explicitly
5. Page direction: Right-to-Left (File > Options > Advanced > Show document content)
6. Footnotes: bottom of page, Hebrew formatting, auto-numbered
7. Never mix RTL and LTR paragraph direction in the same text block

### Bibliography (Hebrew documents)
Split into two labeled sections:
- **מקורות בעברית:** - bullet list, Hebrew citation format
- **English Sources:** - bullet list, APA format with DOI links

Hebrew citation format:
`Author (Year). Title. Publisher/Journal.`

English citation format (APA):
`Author, A., & Author, B. (Year). Title of article. *Journal Name*, volume(issue), pages. https://doi.org/...`

---

## English Mode

### Cover Page
Omit unless assignment explicitly requires one. Start with the title as a heading.

### Header format
```
# Assignment Title or Deliverable Name

## Section Heading

### Sub-section
```

Title style: "Deliverable X - Description" or the assignment name, bold heading.

### Paragraph style
- Short, punchy paragraphs
- Heavy use of bullet points for synthesis, analysis, and pain points
- Prose paragraphs for reflections, proposals, and argumentation
- Tables for side-by-side comparisons

### Inline citations
Parenthetical: (Author, Year) or (Author et al., Year)

### Bibliography (English documents)
Single list, APA format:
`Author, A. (Year). Title. *Journal*, volume(issue). https://doi.org/...`

---

## Charts and Tables

- Always inline with the text, not in an appendix (unless very large)
- Chart titles in the document language (Hebrew titles for Hebrew papers)
- Axis labels can be in English for technical charts
- Tables: clean borders, bold headers
- Source footnote below each chart if data is external

---

## Citation Style

Default: **APA 7th edition** for both Hebrew and English assignments.

Key patterns from past work:
- Journal articles: Author (Year). Title. *Journal*, volume, pages. DOI
- Government reports: Agency (Year). Report title. Publisher.
- Online sources: Organization (Year, Month Day). Title. URL
- Multiple authors: up to 5 listed, then "et al."

---

## What Not to Do

- No em dashes in English text
- No filler transitions ("It is important to note that...", "As can be seen...")
- No bullet points in abstract or introduction - use prose there
- Do not translate English technical terms into Hebrew
- Do not mix footnote and parenthetical citations in the same document
- Do not put code in the main body - always in appendix
