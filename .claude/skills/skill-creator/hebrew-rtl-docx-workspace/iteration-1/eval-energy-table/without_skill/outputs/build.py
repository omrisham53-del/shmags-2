#!/usr/bin/env python3
"""
Energy Technology Comparison Report - Hebrew RTL Word Document
-------------------------------------------------------------
Builds energy_report.docx: a Hebrew RTL document with a title,
intro paragraph, and a 3-column comparison table.
"""

import zipfile, sys, re

FONT = "Arial"

# ── Run and paragraph helpers ─────────────────────────────────────────────────

def rPr(sz=22, bold=False, italic=False, color="000000"):
    parts = [
        f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}" w:eastAsia="{FONT}"/>',
        f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>',
    ]
    if bold:   parts.append('<w:b/><w:bCs/>')
    if italic: parts.append('<w:i/><w:iCs/>')
    if color != "000000": parts.append(f'<w:color w:val="{color}"/>')
    parts.append('<w:rtl/>')
    return '<w:rPr>' + ''.join(parts) + '</w:rPr>'

def run(text, sz=22, bold=False, italic=False, color="000000"):
    text_xml = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    preserve = ' xml:space="preserve"' if text.startswith(' ') or text.endswith(' ') else ''
    return f'<w:r>{rPr(sz, bold, italic, color)}<w:t{preserve}>{text_xml}</w:t></w:r>'

def pPr(align="left", after=100, before=0, line=276, border_bottom=False):
    """
    align="left"   -> physical right (RTL natural start)
    align="both"   -> justified
    align="center" -> centered
    """
    parts = ['<w:bidi/>']
    parts.append(f'<w:spacing w:after="{after}" w:before="{before}" w:line="{line}" w:lineRule="auto"/>')
    parts.append(f'<w:jc w:val="{align}"/>')
    if border_bottom:
        parts.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="1A5276"/></w:pBdr>')
    return '<w:pPr>' + ''.join(parts) + '</w:pPr>'

def para(runs_xml, align="left", after=100, before=0, line=276, border_bottom=False):
    return f'<w:p>{pPr(align, after, before, line, border_bottom)}{runs_xml}</w:p>'

def blank(after=80):
    return para(run(''), after=after)

def heading(text, color="1A5276", sz=28, after=120, before=200):
    """Main title heading."""
    return para(run(text, sz=sz, bold=True, color=color),
                align="center", after=after, before=before, border_bottom=False)

def section_heading(text, color="1A5276", sz=24, after=100, before=160):
    """Section heading with bottom border."""
    return para(run(text, sz=sz, bold=True, color=color),
                align="left", after=after, before=before, border_bottom=True)

# ── Table helpers ─────────────────────────────────────────────────────────────

BORDER = ('<w:top w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
          '<w:left w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
          '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
          '<w:right w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>')

def cell(width, paragraphs_xml, fill=None):
    shade = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>' if fill else ''
    tcPr = (f'<w:tcPr><w:tcW w:type="dxa" w:w="{width}"/>'
            f'<w:tcBorders>{BORDER}</w:tcBorders>{shade}'
            f'<w:tcMar>'
            f'<w:top w:type="dxa" w:w="80"/><w:left w:type="dxa" w:w="120"/>'
            f'<w:bottom w:type="dxa" w:w="80"/><w:right w:type="dxa" w:w="120"/>'
            f'</w:tcMar>'
            f'<w:vAlign w:val="center"/></w:tcPr>')
    return f'<w:tc>{tcPr}{paragraphs_xml}</w:tc>'

def hcell(width, text, bg="1A5276"):
    """Header cell — dark background, white bold text, centered."""
    p = para(run(text, sz=20, bold=True, color="FFFFFF"), align="center", after=0)
    return cell(width, p, fill=bg)

def dcell(width, text, bg=None, bold=False, align="center"):
    """Data cell."""
    p = para(run(text, sz=20, bold=bold), align=align, after=0)
    return cell(width, p, fill=bg)

def trow(*cells_xml, shading=None):
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
             f'</w:tblBorders>'
             f'<w:tblCellMar>'
             f'<w:top w:type="dxa" w:w="80"/><w:left w:type="dxa" w:w="120"/>'
             f'<w:bottom w:type="dxa" w:w="80"/><w:right w:type="dxa" w:w="120"/>'
             f'</w:tblCellMar>'
             f'</w:tblPr>')
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

# ── Document content ──────────────────────────────────────────────────────────

def build_document():
    body_parts = []

    # Main title
    body_parts.append(heading("השוואת טכנולוגיות אנרגיה מתחדשת"))
    body_parts.append(blank(after=60))

    # Introductory paragraph
    intro = (
        "דוח זה מציג השוואה בין טכנולוגיות ייצור אנרגיה מתחדשת הפועלות בישראל, "
        "תוך התמקדות בעלות הממוצעת להתקנה ובמדד היעילות האנרגטית של כל טכנולוגיה. "
        "הנתונים מבוססים על ממוצע עלויות עגול 2022 מתוך מאגר הנתונים של תכנית המענקים הלאומית "
        "לייעול אנרגטי, ומיועדים לשמש כבסיס לניתוח עלות-תועלת חברתי."
    )
    body_parts.append(para(run(intro), align="both", after=120, before=0))
    body_parts.append(blank(after=80))

    # Section heading
    body_parts.append(section_heading("טבלת השוואה: עלות ויעילות לפי טכנולוגיה"))
    body_parts.append(blank(after=60))

    # Column widths in twips (total ~7200 for a standard page with 1080 margins)
    # Right column (first in RTL): טכנולוגיה (technology name) - widest
    # Middle column: עלות ממוצעת (average cost)
    # Left column: יעילות (efficiency)
    COL_TECH  = 3200
    COL_COST  = 2200
    COL_EFF   = 1800

    # Alternating row shading
    ROW_LIGHT = "EBF5FB"
    ROW_WHITE = "FFFFFF"

    rows = [
        # Header row
        trow(
            hcell(COL_TECH, "טכנולוגיה"),
            hcell(COL_COST, "עלות ממוצעת"),
            hcell(COL_EFF,  "יעילות"),
        ),
        # Data rows
        trow(
            dcell(COL_TECH, "משאבות חום תעשייתיות", bg=ROW_LIGHT, bold=True, align="left"),
            dcell(COL_COST, "850,000 ₪",             bg=ROW_LIGHT),
            dcell(COL_EFF,  "300% (COP)",             bg=ROW_LIGHT),
        ),
        trow(
            dcell(COL_TECH, "צ'ילרים אבסורפציה",      bg=ROW_WHITE, bold=True, align="left"),
            dcell(COL_COST, "620,000 ₪",              bg=ROW_WHITE),
            dcell(COL_EFF,  "70% (COP 0.7)",           bg=ROW_WHITE),
        ),
        trow(
            dcell(COL_TECH, "מדחסים עם כונן מהירות (VSD)", bg=ROW_LIGHT, bold=True, align="left"),
            dcell(COL_COST, "410,000 ₪",              bg=ROW_LIGHT),
            dcell(COL_EFF,  "חיסכון 35%",             bg=ROW_LIGHT),
        ),
        trow(
            dcell(COL_TECH, "קולטי קיטור חשמליים",   bg=ROW_WHITE, bold=True, align="left"),
            dcell(COL_COST, "1,100,000 ₪",            bg=ROW_WHITE),
            dcell(COL_EFF,  "98% (חשמלי)",             bg=ROW_WHITE),
        ),
    ]

    body_parts.append(table([COL_TECH, COL_COST, COL_EFF], rows))
    body_parts.append(blank(after=100))

    # Footer note
    note = "* עלויות הינן ממוצע משוקלל להשקעה לפי נתוני עיגול 2022 מתוך capex_all_rounds.csv."
    body_parts.append(para(run(note, sz=18, italic=True, color="595959"), align="left", after=0))

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

    with zipfile.ZipFile(out_path) as z:
        doc = z.read('word/document.xml').decode()
        sty = z.read('word/styles.xml').decode()

    p  = len(re.findall(r'<w:pPr\b', doc))
    pb = len(re.findall(r'<w:bidi',  doc))
    r  = len(re.findall(r'<w:rPr\b', doc))
    rb = len(re.findall(r'<w:rtl',   doc))
    print(f"bidi coverage: {pb}/{p} paragraphs")
    print(f"rtl  coverage: {rb}/{r} runs")
    has_normal = 'styleId="Normal"' in sty
    print(f"Normal style: {has_normal}")
    print("Validation: OK" if pb == p and rb == r and has_normal
          else "Validation: ISSUES FOUND")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'energy_report.docx'
    pack(out)
