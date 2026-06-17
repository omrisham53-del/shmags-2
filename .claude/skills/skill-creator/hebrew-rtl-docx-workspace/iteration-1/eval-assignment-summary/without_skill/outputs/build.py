#!/usr/bin/env python3
"""
Assignment Summary Hebrew RTL Word Document
--------------------------------------------
Generates assignment_summary.docx with correct Hebrew RTL rendering in Microsoft Word.

Uses zipfile (not python-docx) to write raw XML, applying:
  - <w:bidi/> on every paragraph pPr
  - <w:rtl/> on every run rPr
  - Normal style defined as RTL in styles.xml
  - Bullet numbering with lvlJc=left and ind w:right (RTL-correct)
  - sectPr with <w:bidi/> for RTL page direction
"""

import zipfile, sys, re, os

FONT = "Arial"

# ── Run and paragraph helpers ─────────────────────────────────────────────────

def rPr(sz=22, bold=False, italic=False, color="000000"):
    """Run properties — always includes <w:rtl/>."""
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
    """Single RTL run."""
    text_xml = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    preserve = ' xml:space="preserve"' if text.startswith(' ') or text.endswith(' ') else ''
    return f'<w:r>{rPr(sz, bold, italic, color)}<w:t{preserve}>{text_xml}</w:t></w:r>'

def pPr(align="left", after=100, before=0, line=276, numId=None, border_bottom=False):
    """
    Paragraph properties — always includes <w:bidi/>.

    align="left"   -> physical RIGHT (RTL natural start) — use for headings, body
    align="both"   -> justified — use for body text
    align="center" -> centered
    NOTE: align="right" means physical LEFT in RTL — never use it
    """
    parts = ['<w:bidi/>']
    if numId:
        parts.append(f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{numId}"/></w:numPr>')
    parts.append(f'<w:spacing w:after="{after}" w:before="{before}" w:line="{line}" w:lineRule="auto"/>')
    parts.append(f'<w:jc w:val="{align}"/>')
    if border_bottom:
        parts.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="1F4E79"/></w:pBdr>')
    return '<w:pPr>' + ''.join(parts) + '</w:pPr>'

def para(runs_xml, align="left", after=100, before=0, line=276, numId=None, border_bottom=False):
    """Full RTL paragraph."""
    return f'<w:p>{pPr(align, after, before, line, numId, border_bottom)}{runs_xml}</w:p>'

def blank(after=60):
    return para(run(''), after=after)

def heading_main(text):
    """Document title — large, bold, centered, dark blue."""
    return para(run(text, sz=32, bold=True, color="1F4E79"),
                align="center", after=240, before=240)

def heading_section(text):
    """Section heading — bold, right-aligned (physical), underline border."""
    return para(run(text, sz=26, bold=True, color="1F4E79"),
                align="left", after=120, before=180, border_bottom=True)

def body_para(text, after=100):
    """Body text paragraph — justified."""
    return para(run(text, sz=22), align="both", after=after)

def bullet_para(text, after=60):
    """Bullet list item — uses numId=1 from NUMBERING."""
    return para(run(text, sz=22), after=after, numId="1")

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

    # Title
    body_parts.append(heading_main("סיכום עבודה סמינריונית"))
    body_parts.append(blank(after=60))

    # Intro paragraph
    body_parts.append(body_para(
        "עבודה זו עוסקת בניתוח עלות-תועלת של מקורות אנרגיה לצורכי מרכז נתונים בגוש דן. "
        "המחקר בוחן שלוש חלופות עיקריות: חיבור לרשת החשמל הלאומית, מערכת היברידית, "
        "ומערכת עצמאית המבוססת על אנרגיה מתחדשת."
    ))
    body_parts.append(body_para(
        "הניתוח מתבסס על מודל כלכלי מקיף הכולל עלויות הון, עלויות תפעול, ועלויות סביבתיות "
        "על פני אופק תכנון של עשרים שנה. המסקנות נועדו לסייע לקובעי מדיניות ולגורמים "
        "עסקיים בקבלת החלטות מושכלות בתחום אספקת האנרגיה."
    ))
    body_parts.append(blank(after=80))

    # Section heading
    body_parts.append(heading_section("ממצאים עיקריים"))
    body_parts.append(blank(after=40))

    # 3 bullet points
    body_parts.append(bullet_para(
        "החלופה ההיברידית מציגה את היחס הטוב ביותר בין עלות לתועלת על פני כל אופק הזמן הנבחן."
    ))
    body_parts.append(bullet_para(
        "עלויות הפחמן מהוות גורם מכריע בהשוואה בין החלופות, במיוחד בתרחישים של מחיר פחמן גבוה."
    ))
    body_parts.append(bullet_para(
        "השקעה בתשתיות מתחדשות מקטינה את תלות המרכז ברשת הלאומית ומייצרת יתרון תחרותי לטווח הארוך."
    ))
    body_parts.append(blank(after=80))

    # Closing paragraph
    body_parts.append(body_para(
        "לסיכום, ממצאי המחקר מצביעים על כך שמעבר לאנרגיה היברידית מהווה את הבחירה האסטרטגית "
        "המיטבית עבור מרכז נתונים בהיקף של עשרים מגה-וואט. מומלץ להמשיך ולעדכן את המודל "
        "ככל שנתוני עלויות חדשים יתקבלו, ולשקול את ההשלכות הרגולטוריות של כל חלופה לפני "
        "קבלת החלטה סופית."
    ))

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

    # XML validation
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
    ok = (pb == p and rb == r and has_normal)
    print("Validation: OK" if ok else "Validation: ISSUES FOUND")
    return ok

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, 'assignment_summary.docx')
    pack(out)
