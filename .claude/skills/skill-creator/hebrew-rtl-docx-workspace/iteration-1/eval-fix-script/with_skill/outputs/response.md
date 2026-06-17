# Why Hebrew .docx Looks Fine in LibreOffice but Breaks in Microsoft Word

## Root Causes

There are three distinct failures, all invisible to LibreOffice but fatal in Word.

**1. Missing `<w:bidi/>` at the paragraph level**

Every Hebrew paragraph needs `<w:bidi/>` inside its `<w:pPr>` block. Without it, Word renders the paragraph left-to-right. This is the direct cause of left-aligned text and bullets appearing on the left side. LibreOffice applies RTL heuristically based on character detection and doesn't require this flag, so it masks the bug entirely.

**2. Missing `<w:rtl/>` at the run level**

Every text run needs `<w:rtl/>` inside its `<w:rPr>` block. Without it, punctuation drifts to the wrong side and mixed Hebrew-English sentences come out scrambled. A paragraph can have `<w:bidi/>` set correctly and still fail this second requirement — both levels must be present simultaneously.

**3. Normal style not defined explicitly in styles.xml**

If `styles.xml` does not include an explicit Normal paragraph style marked as RTL, Word auto-generates one as LTR on open and it overrides everything else. This single root cause can undo all other fixes. The Normal style must appear in `styles.xml` with `<w:bidi/>` in its `<w:pPr>` and `<w:rtl/>` in its `<w:rPr>`.

**Bonus: Numbering (bullets) direction errors**

Bullet lists have their own RTL requirements in `numbering.xml`. The physical alignment of bullet levels uses `<w:lvlJc w:val="left"/>` (not `right`) because in RTL paragraphs the `jc` values are physically reversed: `left` means the natural RTL start (right edge of the page). Indentation must use `w:right` (not `w:left`) to indent from the right margin.

## The jc Reversal Rule

In any paragraph that has `<w:bidi/>`, all `jc` (justification) values are physically reversed:

| `w:jc` value | Physical result in RTL paragraph |
|---|---|
| `left` | Right side (natural RTL start) — correct for headings and body |
| `both` | Justified |
| `center` | Centered |
| `right` | Left side — never use this in RTL |

## Why LibreOffice Masks All of This

LibreOffice detects Hebrew characters and applies RTL rendering automatically, regardless of whether the underlying XML flags are present. It is not a valid correctness test for Word compatibility. Always verify RTL documents by opening in Microsoft Word, or by running the XML validation script included in `fix_rtl.py`.

## Quick Symptom-to-Cause Table

| Symptom in Word | Root cause |
|---|---|
| All text aligns left | Normal style missing from styles.xml |
| Bullets appear on left side | `lvlJc=right` or `ind w:left` in numbering.xml |
| Punctuation on wrong side | Run missing `<w:rtl/>` |
| Mixed Hebrew-English scrambled | Paragraph has `<w:bidi/>` but run lacks `<w:rtl/>` |
| New text typed in Word reverts to LTR | docDefaults in styles.xml not fixed |
| Table columns in wrong order | Missing `<w:bidiVisual/>` in table properties |
