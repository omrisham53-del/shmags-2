# Hebrew RTL Quick Reference

## Alignment Rules

In RTL paragraphs (`<w:bidi/>`), `jc` values refer to the logical start/end of text flow,
so they map to the **opposite** physical side from what you'd expect in LTR.

| Content type | `align=` in helpers | `w:jc` in XML | Physical result |
|---|---|---|---|
| Body text | `"both"` | `both` | Justified |
| Headings | `"left"` | `left` | Right side (RTL natural start) |
| Label lines | `"left"` | `left` | Right side |
| Centered content | `"center"` | `center` | Center |
| Table header cells | `"center"` | `center` | Center |
| Table data cells | `"left"` | `left` | Right side |
| **NEVER USE** | `"right"` | `right` | **Left side** |

---

## Common Symptoms, Root Causes, and Fixes

| Symptom | Root cause | Fix |
|---|---|---|
| All text aligns left | Normal style missing — Word auto-creates it as LTR | Add Normal style explicitly in styles.xml |
| Bullets on left side | `lvlJc=right` or `ind w:left` in numbering.xml | Change to `lvlJc=left`, `ind w:right` |
| Comma/period on wrong side | Run missing `<w:rtl/>` | Add `<w:rtl/>` to every `<w:rPr>` |
| Mixed Hebrew-English scrambled | Paragraph has `<w:bidi/>` but run lacks `<w:rtl/>` | Both levels required |
| Looks fine in LibreOffice, broken in Word | Any of the above | LibreOffice is not a valid RTL test |
| npm docx library output broken in Word | Library doesn't generate Normal style | Switch to Python + zipfile method |
| Table columns in wrong order | Missing `<w:bidiVisual/>` in `<w:tblPr>` | Add `<w:bidiVisual/>` to table properties |
| Cell content left-aligned | Cell paragraph uses `jc=right` (physical left) | Change to `jc=left` |
| New text typed in Word reverts to LTR | styles.xml docDefaults not fixed | Fix docDefaults + Normal style |
| Validation errors on pack | Pre-existing `w:hint="cs"` warnings | Use `--validate false` when repacking |
