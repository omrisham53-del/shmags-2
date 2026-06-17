# Hebrew .docx RTL: Root Causes and Fix

## Why it looks fine in LibreOffice but breaks in Word

LibreOffice applies RTL rendering heuristically — it detects Hebrew characters and renders them right-aligned regardless of what the XML actually says. Microsoft Word is strict: it only applies RTL layout when the XML explicitly declares it. So a document that was never given proper RTL markup "works" in LibreOffice and fails in Word.

---

## The Two Root Causes

Every Hebrew Word document requires RTL markers at **two independent levels**. Missing either one causes a different class of symptoms.

### Root Cause 1: Missing `<w:bidi/>` in paragraph properties

`<w:bidi/>` inside `<w:pPr>` tells Word to treat the paragraph as a right-to-left paragraph. Without it:

- Text aligns to the left margin instead of the right
- Bullet points appear on the left side of the paragraph
- The paragraph's logical start/end are reversed

This element must appear in every `<w:pPr>` block in `word/document.xml`, in `word/styles.xml` (including the Normal style and docDefaults), and in each bullet level's `<w:pPr>` inside `word/numbering.xml`.

### Root Cause 2: Missing `<w:rtl/>` in run properties

`<w:rtl/>` inside `<w:rPr>` tells Word that the text run is RTL at the character level. Without it:

- Punctuation drifts to the wrong side (period or comma appears at the start of a line instead of the end)
- Mixed Hebrew-English sentences are rendered in the wrong visual order
- Parentheses and quotation marks face the wrong direction

This element must appear in every `<w:rPr>` block.

### Root Cause 3: Normal style auto-created by Word as LTR

If `word/styles.xml` does not contain an explicit definition for the `Normal` style, Word silently auto-generates one as LTR when the file is opened. This overrides any RTL settings you applied to individual paragraphs. The Normal style must be defined explicitly with both `<w:bidi/>` and `<w:rtl/>`.

### Root Cause 4: Numbering (bullet) direction wrong in `word/numbering.xml`

Bullet levels use `<w:lvlJc>` to control the side the bullet sits on. In RTL paragraphs, the `jc` axis is **reversed** — `val="left"` means physical right (correct for RTL), and `val="right"` means physical left (wrong). Similarly, paragraph indentation uses `w:left` and `w:right` attributes that must be on the correct side. LibreOffice handles this transparently; Word does not.

---

## The `jc` Reversal Trap

Inside any `<w:bidi/>` paragraph, alignment values map to the **opposite physical side**:

| `w:jc` value | Physical result in RTL paragraph |
|---|---|
| `left` | Right side (the natural RTL start) — use this for body/headings |
| `both` | Justified |
| `center` | Centered |
| `right` | **Left side — never use this in Hebrew paragraphs** |

---

## Symptom-to-Cause Table

| Symptom in Word | Root cause |
|---|---|
| All text left-aligned | Missing `<w:bidi/>` in paragraphs OR Normal style auto-created as LTR |
| Bullet points on the left | `lvlJc=right` or `ind w:left` in numbering.xml |
| Period/comma on wrong side | Missing `<w:rtl/>` in run properties |
| Mixed Hebrew-English scrambled | Paragraph has `<w:bidi/>` but run lacks `<w:rtl/>` |
| New text typed in Word reverts to LTR | docDefaults or Normal style not fixed in styles.xml |
| Table columns in wrong order | Missing `<w:bidiVisual/>` in `<w:tblPr>` |
| Looks fine in LibreOffice | LibreOffice is not a valid RTL correctness test — always verify in Word |

---

## The Fix Script

`fix_rtl.py` in this directory repairs all four root causes on any existing `.docx` without unpacking it manually. It uses Python's built-in `zipfile` module — no dependencies needed.

```
python3 fix_rtl.py input.docx output.docx
```

What it does:
1. Reads every file inside the .docx ZIP
2. In `word/document.xml`: adds `<w:bidi/>` to every `<w:pPr>`, adds `<w:rtl/>` to every `<w:rPr>`
3. In `word/styles.xml`: same fixes plus inserts an explicit `Normal` style if absent, fixes `<w:pPrDefault/>`
4. In `word/numbering.xml`: flips `lvlJc=right` to `lvlJc=left`, switches `ind w:left` to `ind w:right`, adds `<w:bidi/>` and `<w:rtl/>` to each bullet level
5. Writes the corrected .docx and prints a validation summary

The output file can be opened directly in Microsoft Word.
