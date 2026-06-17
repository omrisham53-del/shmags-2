---
name: hebrew-rtl-docx
description: >
  Use for ANY Word document (.docx) with Hebrew text — building from scratch or fixing
  an existing file. Triggers: Hebrew (עברית), mixed Hebrew-English, RTL layout,
  creating/editing/fixing a Hebrew document. Also use when a docx looks correct in
  LibreOffice but breaks in Microsoft Word: wrong-side bullets, scrambled mixed
  sentences, punctuation drift, left-aligned text. Do NOT use the npm docx library
  for Hebrew — always use Python + zipfile (this skill shows how).
when_to_use: >
  Key phrases: "Hebrew Word document", "RTL document", "עברית", "Hebrew formatting",
  "looks wrong in Word", "bullets on wrong side", "left-aligned in Word",
  "LibreOffice vs Word", "Hebrew docx". Also triggers for Hebrew PPTX (see PPTX section).
allowed-tools: Bash(python3 *)
---

## Where to start

**Building a new Hebrew .docx from scratch?**
Read `${CLAUDE_SKILL_DIR}/scripts/build_rtl_docx.py`, adapt `build_document()` for your content, then run it.

**Fixing an existing .docx that breaks in Word?**
Run: `python3 ${CLAUDE_SKILL_DIR}/scripts/fix_rtl.py <input.docx> <output.docx>`

**Quick reference (alignment rules, symptoms → fix table)?**
See `${CLAUDE_SKILL_DIR}/references/quick-reference.md`

---

## The Two Laws of Hebrew RTL in Word

Every Hebrew document must apply RTL at **two levels simultaneously**:

| Level | XML element | What breaks without it |
|---|---|---|
| Paragraph | `<w:bidi/>` inside `<w:pPr>` | Text left-aligns, bullets land on wrong side |
| Run | `<w:rtl/>` inside `<w:rPr>` | Punctuation drifts, mixed Hebrew-English scrambles |

LibreOffice masks both failures. **Never use LibreOffice as a correctness test.**
Verify by opening in Word, or run the XML validation snippet at the bottom of this file.

---

## The `jc` Reversal Trap

In RTL paragraphs (`<w:bidi/>`), `jc` values are **physically reversed**:

| `w:jc` value | Physical result in RTL paragraph |
|---|---|
| `left` | Right side (natural RTL start) — use for headings/body |
| `both` | Justified — use for body text |
| `center` | Centered |
| `right` | **Left side — NEVER use in RTL** |

---

## Required XML Files

### `word/styles.xml` — Normal style must be defined explicitly

Without this, Word auto-creates Normal as LTR and overrides everything.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault><w:rPr>
      <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/>
      <w:sz w:val="22"/><w:szCs w:val="22"/>
      <w:rtl/>
    </w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr><w:bidi/></w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:pPr><w:bidi/></w:pPr>
    <w:rPr><w:rtl/></w:rPr>
  </w:style>
</w:styles>
```

### `word/numbering.xml` — Bullets must use `lvlJc=left` and `ind w:right`

`lvlJc=left` means physical right in RTL. `ind w:right` indents from the right margin.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="&#x2022;"/>
      <w:lvlJc w:val="left"/>
      <w:pPr>
        <w:bidi/>
        <w:ind w:right="360" w:hanging="360"/>
        <w:jc w:val="left"/>
      </w:pPr>
      <w:rPr>
        <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>
        <w:rtl/>
      </w:rPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>
```

### `word/document.xml` — `sectPr` must include `<w:bidi/>`

```xml
<w:sectPr>
  <w:bidi/>
  <w:pgSz w:w="11906" w:h="16838"/>
  <w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080"
           w:header="709" w:footer="709" w:gutter="0"/>
</w:sectPr>
```

---

## Pack with zipfile

```python
import zipfile

files = {
    '[Content_Types].xml': CONTENT_TYPES,
    '_rels/.rels': RELS_PKG,
    'word/_rels/document.xml.rels': RELS_DOCXML,
    'word/document.xml': build_document(),
    'word/styles.xml': STYLES,
    'word/numbering.xml': NUMBERING,
}
with zipfile.ZipFile('output.docx', 'w', zipfile.ZIP_DEFLATED) as zf:
    for name, content in files.items():
        zf.writestr(name, content.encode('utf-8'))
```

---

## XML Validation

Run after generating any Hebrew docx to confirm RTL coverage before opening in Word:

```python
import re, zipfile
with zipfile.ZipFile('output.docx') as z:
    doc = z.read('word/document.xml').decode()
    styles = z.read('word/styles.xml').decode()
p  = len(re.findall(r'<w:pPr\b', doc))
pb = len(re.findall(r'<w:bidi',  doc))
r  = len(re.findall(r'<w:rPr\b', doc))
rb = len(re.findall(r'<w:rtl',   doc))
print(f"bidi coverage: {pb}/{p} paragraphs")
print(f"rtl  coverage: {rb}/{r} runs")
print(f"Normal style: {'styleId=\"Normal\"' in styles}")
print("OK" if pb==p and rb==r and 'styleId="Normal"' in styles else "ISSUES FOUND")
```

---

## PPTX — Hebrew RTL in PowerPoint

```xml
<!-- Paragraph: both algn and rtl required -->
<a:pPr algn="r" rtl="1"/>

<!-- Table -->
<a:tblPr rtl="1">...</a:tblPr>
```

Pack with `--validate false` (pre-existing duplicate `authorId` in Hebrew decks).
