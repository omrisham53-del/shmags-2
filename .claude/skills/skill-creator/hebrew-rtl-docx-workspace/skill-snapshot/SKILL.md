---
name: hebrew-rtl-docx
description: >
  Use this skill for ANY Word document (.docx) that contains Hebrew text — whether
  building from scratch or editing an existing file. Triggers: user requests a document
  in Hebrew (עברית), mixed Hebrew-English, RTL layout, or any context involving creating,
  editing, improving, or fixing a Hebrew document. Also use when a previously created
  docx looks correct in LibreOffice but breaks in Microsoft Word (wrong-side bullets,
  scrambled mixed sentences, punctuation drift, left-aligned text).
  Apply TOGETHER with the base docx skill — this skill adds the RTL layer on top.
---

# Hebrew RTL Word Documents — Complete Guide

> ⚠️ **CRITICAL: Do NOT use the npm `docx` library for Hebrew documents**
>
> The `docx` npm library produces XML that looks correct in LibreOffice but breaks in
> Microsoft Word because:
> - It does not generate a `Normal` style — Word auto-creates one as LTR
> - Its numbering config ignores RTL settings (bullets always land on the left)
> - LibreOffice masks all these bugs, making the preview useless for validation
>
> **THE ONLY RELIABLE METHOD:** build the docx directly as XML using Python + `zipfile`.
> See the complete Python template below.

---

## Why RTL Breaks in Word — The Two-Level System

Microsoft Word requires RTL to be declared at **TWO levels** simultaneously:

| Level | XML element | Controls |
|---|---|---|
| Paragraph | `<w:bidi/>` inside `<w:pPr>` | Base paragraph direction |
| Run | `<w:rtl/>` inside `<w:rPr>` | Character-level direction |

Missing either level causes: wrong-side bullets, punctuation drift, scrambled mixed sentences.
LibreOffice always hides these bugs. Never use LibreOffice preview as a correctness test.
The only reliable tests are: (a) opening in Word, or (b) inspecting the XML directly.

---

> ⚠️ **CRITICAL: `jc` values are REVERSED in RTL paragraphs**
>
> In OOXML, when a paragraph has `<w:bidi/>`, the `jc` (justification) values mean the **OPPOSITE**
> of what you expect, because they refer to the logical start/end of the text flow:
>
> | `w:jc` value | Physical result in RTL paragraph |
> |---|---|
> | `left` | ✅ Right side (RTL natural start) |
> | `right` | ❌ Left side (RTL logical end) |
> | `both` | ✅ Justified (both sides) |
> | `center` | ✅ Centered |
>
> **Rules:**
> - Body text → use `jc=both` (justified)
> - Headings and label lines → use `jc=left` (= physical right)
> - Centered content → use `jc=center`
> - **NEVER use `jc=right` in RTL paragraphs** — it aligns to the physical LEFT

---

## Building From Scratch — Python XML Template

Always use this pattern. Copy and adapt for every new Hebrew document.

```python
import zipfile, os

FONT = "Arial"

# ── RTL helpers ───────────────────────────────────────────────────────────

def rPr(sz=22, bold=False, italic=False, color="000000", underline=False):
    """Run properties — ALWAYS includes <w:rtl/>"""
    parts = [
        f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}" w:eastAsia="{FONT}"/>',
        f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>',
    ]
    if bold:      parts.append('<w:b/><w:bCs/>')
    if italic:    parts.append('<w:i/><w:iCs/>')
    if color != "000000": parts.append(f'<w:color w:val="{color}"/>')
    if underline: parts.append('<w:u w:val="single"/>')
    parts.append('<w:rtl/>')   # ← MANDATORY on every run
    return '<w:rPr>' + ''.join(parts) + '</w:rPr>'

def run(text, sz=22, bold=False, italic=False, color="000000"):
    """Single RTL run"""
    text_xml = text.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    preserve = ' xml:space="preserve"' if text.startswith(' ') or text.endswith(' ') else ''
    return f'<w:r>{rPr(sz,bold,italic,color)}<w:t{preserve}>{text_xml}</w:t></w:r>'

def pPr(align="left", after=100, before=0, line=276, numId=None, border_bottom=False):
    """
    Paragraph properties — ALWAYS includes <w:bidi/>
    align="left"   → physical RIGHT (RTL natural) ← USE THIS for body/headings
    align="both"   → justified                     ← USE THIS for body text
    align="center" → centered
    align="right"  → physical LEFT ← NEVER USE in RTL
    """
    parts = ['<w:bidi/>']   # ← MANDATORY on every paragraph
    if numId:
        parts.append(f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{numId}"/></w:numPr>')
    parts.append(f'<w:spacing w:after="{after}" w:before="{before}" w:line="{line}" w:lineRule="auto"/>')
    parts.append(f'<w:jc w:val="{align}"/>')
    if border_bottom:
        parts.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="1F4E79"/></w:pBdr>')
    return '<w:pPr>' + ''.join(parts) + '</w:pPr>'

def para(runs_xml, align="left", after=100, before=0, line=276,
         numId=None, border_bottom=False):
    """Full RTL paragraph"""
    pp = pPr(align, after, before, line, numId, border_bottom)
    return f'<w:p>{pp}{runs_xml}</w:p>'

def blank(after=60):
    return para(run(''), after=after)

def heading(text, color="1F4E79", sz=24, after=120, before=180):
    """Section heading with underline border, aligned physical-right"""
    return para(run(text, sz=sz, bold=True, color=color),
                align="left", after=after, before=before, border_bottom=True)

def bullet_para(runs_xml, after=60):
    """Bullet list item — uses numId=1 (defined in numbering.xml below)"""
    return para(runs_xml, after=after, numId="1")

# ── Table helpers ─────────────────────────────────────────────────────────

BORDER = ('<w:top w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
          '<w:left w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
          '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
          '<w:right w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>')

def cell(width, paragraphs_xml, fill=None):
    shade = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>' if fill else ''
    tcPr = (f'<w:tcPr><w:tcW w:type="dxa" w:w="{width}"/>'
            f'<w:tcBorders>{BORDER}</w:tcBorders>{shade}'
            f'<w:tcMar><w:top w:type="dxa" w:w="60"/><w:left w:type="dxa" w:w="100"/>'
            f'<w:bottom w:type="dxa" w:w="60"/><w:right w:type="dxa" w:w="100"/></w:tcMar>'
            f'<w:vAlign w:val="center"/></w:tcPr>')
    return f'<w:tc>{tcPr}{paragraphs_xml}</w:tc>'

def hcell(width, text, bg="1F4E79"):
    """Header cell — dark background, white bold text, centered"""
    # center = jc=center (safe, direction-neutral)
    p = para(run(text, sz=20, bold=True, color="FFFFFF"), align="center", after=0)
    return cell(width, p, fill=bg)

def trow(*cells_xml):
    return '<w:tr>' + ''.join(cells_xml) + '</w:tr>'

def table(col_widths, rows_xml):
    total = sum(col_widths)
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in col_widths)
    tblPr = (f'<w:tblPr>'
             f'<w:bidiVisual/>'          # ← columns flow right-to-left
             f'<w:tblW w:type="dxa" w:w="{total}"/>'
             f'<w:tblBorders>'
             f'<w:top w:val="single" w:sz="4" w:color="BFBFBF"/>'
             f'<w:left w:val="single" w:sz="4" w:color="BFBFBF"/>'
             f'<w:bottom w:val="single" w:sz="4" w:color="BFBFBF"/>'
             f'<w:right w:val="single" w:sz="4" w:color="BFBFBF"/>'
             f'<w:insideH w:val="single" w:sz="4" w:color="BFBFBF"/>'
             f'<w:insideV w:val="single" w:sz="4" w:color="BFBFBF"/>'
             f'</w:tblBorders></w:tblPr>')
    return f'<w:tbl>{tblPr}<w:tblGrid>{grid}</w:tblGrid>{"".join(rows_xml)}</w:tbl>'
```

---

## Required XML files

Every Hebrew docx built from scratch needs these five files:

### `styles.xml` — must define Normal style explicitly with `<w:bidi/>`:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/>
        <w:sz w:val="22"/><w:szCs w:val="22"/>
        <w:rtl/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:bidi/>
        <!-- NO jc here — let paragraph-level jc control alignment -->
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>
  <!-- CRITICAL: Normal style MUST be defined explicitly.
       If absent, Word auto-creates it as LTR and overrides everything. -->
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:pPr><w:bidi/></w:pPr>
    <w:rPr><w:rtl/></w:rPr>
  </w:style>
</w:styles>
```

### `numbering.xml` — bullets must use `lvlJc=left` (= physical right) and `ind w:right`:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="&#x2022;"/>
      <w:lvlJc w:val="left"/>   <!-- left = physical right in RTL -->
      <w:pPr>
        <w:bidi/>
        <w:ind w:right="360" w:hanging="360"/>  <!-- right-side indent for RTL -->
        <w:jc w:val="left"/>
      </w:pPr>
      <w:rPr>
        <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>
        <w:rtl/>
      </w:rPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1">
    <w:abstractNumId w:val="0"/>
  </w:num>
</w:numbering>
```

### `document.xml` — `sectPr` must include `<w:bidi/>`:

```xml
<w:sectPr>
  <w:bidi/>   <!-- ← MANDATORY: sets page direction to RTL -->
  <w:headerReference w:type="default" r:id="rId3"/>
  <w:footerReference w:type="default" r:id="rId4"/>
  <w:pgSz w:w="11906" w:h="16838"/>
  <w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080"
           w:header="709" w:footer="709" w:gutter="0"/>
</w:sectPr>
```

### Pack with `zipfile` (no npm, no external tools):

```python
files = {
    '[Content_Types].xml': CONTENT_TYPES,
    '_rels/.rels': RELS_PKG,
    'word/_rels/document.xml.rels': RELS_DOCXML,
    'word/document.xml': build_document(),
    'word/styles.xml': STYLES,
    'word/numbering.xml': NUMBERING,
    'word/header1.xml': HEADER,
    'word/footer1.xml': FOOTER,
}
with zipfile.ZipFile('output.docx', 'w', zipfile.ZIP_DEFLATED) as zf:
    for name, content in files.items():
        zf.writestr(name, content.encode('utf-8'))
```

---

## Editing Existing Files (XML Direct Edit)

When the user uploads an existing docx, apply a sweep BEFORE content changes.

### Step 0: Diagnosis

```bash
python scripts/office/unpack.py doc.docx unpacked/
python3 - << 'EOF'
import re
xml = open('unpacked/word/document.xml').read()
p  = len(re.findall(r'<w:pPr\b', xml))
pb = len(re.findall(r'<w:bidi',  xml))
r  = len(re.findall(r'<w:rPr\b', xml))
rb = len(re.findall(r'<w:rtl',   xml))
print(f"pPr: {p}  bidi: {pb}  missing: {p-pb}")
print(f"rPr: {r}  rtl:  {rb}  missing: {r-rb}")
# Also check Normal style
styles = open('unpacked/word/styles.xml').read()
print(f"Normal style defined: {'styleId=\"Normal\"' in styles}")
EOF
```

### Step 1: Inject `bidi` + `rtl`

```python
# fix_rtl.py
import re, shutil

path = 'unpacked/word/document.xml'
shutil.copy(path, path + '.bak')
xml = open(path, encoding='utf-8').read()

def add_bidi(m):
    ppr = m.group(0)
    if '<w:bidi' in ppr: return ppr
    open_tag = re.match(r'<w:pPr[^>]*>', ppr).group(0)
    rest = ppr[len(open_tag):]
    style_m = re.match(r'(\s*<w:pStyle[^/]*/>\s*)', rest)
    if style_m:
        return open_tag + style_m.group(1) + '<w:bidi/>' + rest[len(style_m.group(1)):]
    return open_tag + '<w:bidi/>' + rest

def add_rtl(m):
    rpr = m.group(0)
    if '<w:rtl' in rpr: return rpr
    return rpr.replace('</w:rPr>', '<w:rtl/></w:rPr>')

xml = re.sub(r'<w:pPr\b[^>]*>.*?</w:pPr>', add_bidi, xml, flags=re.DOTALL)
xml = xml.replace('<w:pPr/>', '<w:pPr><w:bidi/></w:pPr>')
xml = re.sub(r'<w:rPr\b.*?</w:rPr>', add_rtl, xml, flags=re.DOTALL)
open(path, 'w', encoding='utf-8').write(xml)

# Fix styles.xml
styles_path = 'unpacked/word/styles.xml'
styles = open(styles_path, encoding='utf-8').read()
# Apply same fixes to styles
styles = re.sub(r'<w:pPr\b[^>]*>.*?</w:pPr>', add_bidi, styles, flags=re.DOTALL)
styles = re.sub(r'<w:rPr\b.*?</w:rPr>', add_rtl, styles, flags=re.DOTALL)
# Fix pPrDefault if self-closing
styles = styles.replace('<w:pPrDefault/>',
    '<w:pPrDefault><w:pPr><w:bidi/></w:pPr></w:pPrDefault>')
# Add Normal style if missing
if 'styleId="Normal"' not in styles:
    normal = '''<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
  <w:name w:val="Normal"/>
  <w:pPr><w:bidi/></w:pPr>
  <w:rPr><w:rtl/></w:rPr>
</w:style>'''
    styles = styles.replace('</w:docDefaults>', '</w:docDefaults>' + normal, 1)
open(styles_path, 'w', encoding='utf-8').write(styles)
print("Done.")
```

### Step 2: Fix `numbering.xml` (if bullets are present)

```python
import re
num_path = 'unpacked/word/numbering.xml'
if os.path.exists(num_path):
    num = open(num_path, encoding='utf-8').read()
    num = num.replace('<w:lvlJc w:val="right"/>', '<w:lvlJc w:val="left"/>')  # right→left (physical right in RTL)
    # Fix indent direction
    num = re.sub(r'<w:ind w:left="(\d+)" w:hanging="(\d+)"/>',
                 lambda m: f'<w:ind w:right="{m.group(1)}" w:hanging="{m.group(2)}"/>',
                 num)
    # Add bidi + rtl to each level
    def fix_lvl(m):
        lvl = m.group(0)
        if '<w:bidi' not in lvl:
            lvl = lvl.replace('</w:pPr>', '<w:bidi/></w:pPr>')
        if '<w:rPr>' not in lvl:
            lvl = lvl.replace('</w:pPr>', '</w:pPr><w:rPr><w:rtl/></w:rPr>')
        return lvl
    num = re.sub(r'<w:lvl\b.*?</w:lvl>', fix_lvl, num, flags=re.DOTALL)
    open(num_path, 'w', encoding='utf-8').write(num)
```

### Step 3: Repack

```bash
python scripts/office/pack.py unpacked/ fixed.docx --original original.docx --validate false
# --validate false: Hebrew Word files often have pre-existing w:hint="cs" warnings
```

---

## RTL Alignment Quick Reference

| Content type | `align=` value | `jc` in XML | Physical result |
|---|---|---|---|
| Body text | `"both"` | `both` | Justified ✅ |
| Headings | `"left"` | `left` | Right side ✅ |
| Label lines | `"left"` | `left` | Right side ✅ |
| Centered | `"center"` | `center` | Center ✅ |
| Table cells (data) | `"left"` | `left` | Right side ✅ |
| Table cells (number) | `"center"` | `center` | Center ✅ |
| **NEVER USE** | `"right"` | `right` | Left side ❌ |

---

## Common Symptoms → Root Cause → Fix

| Symptom | Root cause | Fix |
|---|---|---|
| All text aligns left | Normal style missing → Word creates LTR default | Add Normal style explicitly in styles.xml |
| Bullets on left | `lvlJc=right` or `ind w:left` in numbering | Change to `lvlJc=left`, `ind w:right` |
| Comma/period on wrong side | Run missing `<w:rtl/>` | Add `<w:rtl/>` to every `<w:rPr>` |
| Mixed Hebrew-English scrambled | Paragraph has `<w:bidi/>` but run lacks `<w:rtl/>` | Both levels required |
| Looks fine in LibreOffice, broken in Word | Any of the above | LibreOffice is not a valid test |
| npm library output broken in Word | npm library doesn't generate Normal style | Switch to Python XML method |
| Validation errors on pack | Pre-existing `w:hint="cs"` | Use `--validate false` |
| Table columns wrong order | Missing `<w:bidiVisual/>` in tblPr | Add to table properties |
| Cell content left-aligned | Cell paragraph uses `jc=right` (physical left) | Change to `jc=left` |
| New text typed in Word reverts LTR | styles.xml not updated | Fix docDefaults + Normal style |

---

## Visual Validation Checklist

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.docx
pdftoppm -jpeg -r 130 output.pdf page
# Then view page-1.jpg etc.
```

> **BUT:** LibreOffice preview is unreliable for RTL. It will show correct alignment even when
> the XML is wrong. Always verify by opening in Microsoft Word or by XML inspection.

### XML inspection (most reliable):

```bash
python3 - << 'EOF'
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
print("✅ OK" if pb==p and rb==r and 'styleId="Normal"' in styles else "⚠️ ISSUES FOUND")
EOF
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
