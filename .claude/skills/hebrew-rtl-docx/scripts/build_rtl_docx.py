#!/usr/bin/env python3
"""
Hebrew RTL Word Document Builder
---------------------------------
Template for creating Hebrew .docx files that render correctly in Microsoft Word.
Adapt build_document() for your specific content, then run:

    python3 build_rtl_docx.py [output.docx]

The helpers below always emit <w:bidi/> on paragraphs and <w:rtl/> on runs.
These are mandatory at both levels — missing either causes RTL failure in Word.
"""

import zipfile, sys

FONT = "Arial"

# ── Run and paragraph helpers ─────────────────────────────────────────────────

def rPr(sz=22, bold=False, italic=False, color="000000", underline=False):
    """Run properties — always includes <w:rtl/>."""
    parts = [
        f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}" w:eastAsia="{FONT}"/>',
        f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>',
    ]
    if bold:      parts.append('<w:b/><w:bCs/>')
    if italic:    parts.append('<w:i/><w:iCs/>')
    if color != "000000": parts.append(f'<w:color w:val="{color}"/>')
    if underline: parts.append('<w:u w:val="single"/>')
    parts.append('<w:rtl/>')
    return '<w:rPr>' + ''.join(parts) + '</w:rPr>'

def run(text, sz=22, bold=False, italic=False, color="000000"):
    """Single RTL run."""
    text_xml = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    preserve = ' xml:space="preserve"' if text.startswith(' ') or text.endswith(' ') else ''
    return f'<w:r>{rPr(sz, bold, italic, color)}<w:t{preserve}>{text_xml}</w:t></w:r>'

def pPr(align="left", after=100, before=0, line=276, numId=None, border_bottom=False):
    """
    Paragraph properties — always includes <w:bidi/>.

    align="left"   → physical RIGHT (RTL natural start) — use for headings, body
    align="both"   → justified — use for body text
    align="center" → centered
    align="right"  → physical LEFT — NEVER use in RTL paragraphs
    """
    parts = ['<w:bidi/>']
    if numId:
        parts.append(f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{numId}"/></w:numPr>')
    parts.append(f'<w:spacing w:after="{after}" w:before="{before}" w:line="{line}" w:lineRule="auto"/>')
    parts.append(f'<w:jc w:val="{align}"/>')
    if border_bottom:
        parts.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="1F4E79"/></w:pBdr>')
    return '<w:pPr>' + ''.join(parts) + '</w:pPr>'

def para(runs_xml, align="left", after=100, before=0, line=276,
         numId=None, border_bottom=False):
    """Full RTL paragraph."""
    return f'<w:p>{pPr(align, after, before, line, numId, border_bottom)}{runs_xml}</w:p>'

def blank(after=60):
    return para(run(''), after=after)

def heading(text, color="1F4E79", sz=24, after=120, before=180):
    """Section heading — underline border, physically right-aligned."""
    return para(run(text, sz=sz, bold=True, color=color),
                align="left", after=after, before=before, border_bottom=True)

def bullet_para(runs_xml, after=60):
    """Bullet list item — uses numId=1 from NUMBERING below."""
    return para(runs_xml, after=after, numId="1")

# ── Table helpers ─────────────────────────────────────────────────────────────

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
    """Header cell — dark background, white bold text, centered."""
    p = para(run(text, sz=20, bold=True, color="FFFFFF"), align="center", after=0)
    return cell(width, p, fill=bg)

def trow(*cells_xml):
    return '<w:tr>' + ''.join(cells_xml) + '</w:tr>'

def table(col_widths, rows_xml):
    """RTL table — <w:bidiVisual/> makes columns flow right-to-left."""
    total = sum(col_widths)
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in col_widths)
    tblPr = (f'<w:tblPr>'
             f'<w:bidiVisual/>'
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

# ── Required XML strings ──────────────────────────────────────────────────────

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>'''

RELS_PKG = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

RELS_DOCXML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''

STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
</w:styles>'''

NUMBERING = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
</w:numbering>'''

# ── Document content — REPLACE THIS ──────────────────────────────────────────

def build_document():
    """Replace the body_parts list with your document content."""
    body_parts = []

    body_parts.append(heading("כותרת ראשית"))
    body_parts.append(blank())
    body_parts.append(para(run("פסקת גוף לדוגמה עם טקסט בעברית."), align="both"))
    body_parts.append(blank())

    body_parts.append(bullet_para(run("פריט ראשון ברשימה")))
    body_parts.append(bullet_para(run("פריט שני ברשימה")))
    body_parts.append(blank())

    # Table example (widths in twips; 1440 twips = 1 inch)
    col_widths = [3000, 3000, 3000]
    rows = [
        trow(hcell(3000, "עמודה א"), hcell(3000, "עמודה ב"), hcell(3000, "עמודה ג")),
        trow(
            cell(3000, para(run("ערך 1"), align="left", after=0)),
            cell(3000, para(run("ערך 2"), align="left", after=0)),
            cell(3000, para(run("ערך 3"), align="left", after=0)),
        ),
    ]
    body_parts.append(table(col_widths, rows))
    body_parts.append(blank())

    sect_pr = ('<w:sectPr><w:bidi/>'
               '<w:pgSz w:w="11906" w:h="16838"/>'
               '<w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080"'
               ' w:header="709" w:footer="709" w:gutter="0"/>'
               '</w:sectPr>')

    body = ''.join(body_parts) + sect_pr
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
        ' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<w:body>{body}</w:body></w:document>'
    )

# ── Pack and validate ─────────────────────────────────────────────────────────

def pack(out_path):
    files = {
        '[Content_Types].xml': CONTENT_TYPES,
        '_rels/.rels': RELS_PKG,
        'word/_rels/document.xml.rels': RELS_DOCXML,
        'word/document.xml': build_document(),
        'word/styles.xml': STYLES,
        'word/numbering.xml': NUMBERING,
    }
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for name, content in files.items():
            zf.writestr(name, content.encode('utf-8'))
    print(f"Written: {out_path}")

    import re
    with zipfile.ZipFile(out_path) as z:
        doc = z.read('word/document.xml').decode()
        sty = z.read('word/styles.xml').decode()
    p  = len(re.findall(r'<w:pPr\b', doc))
    pb = len(re.findall(r'<w:bidi',  doc))
    r  = len(re.findall(r'<w:rPr\b', doc))
    rb = len(re.findall(r'<w:rtl',   doc))
    print(f"bidi coverage: {pb}/{p} paragraphs")
    print(f"rtl  coverage: {rb}/{r} runs")
    print(f"Normal style: {'styleId=\"Normal\"' in sty}")
    print("Validation: OK" if pb == p and rb == r and 'styleId="Normal"' in sty
          else "Validation: ISSUES FOUND")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'output.docx'
    pack(out)
