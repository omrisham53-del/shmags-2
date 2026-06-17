#!/usr/bin/env python3
"""
Hebrew RTL Word Document Builder — Assignment Summary
------------------------------------------------------
Generates assignment_summary.docx with:
  - Title: סיכום עבודה סמינריונית
  - Intro paragraph (Hebrew, 2-3 sentences)
  - Section heading: ממצאים עיקריים
  - 3 Hebrew bullet points
  - Closing paragraph

Uses the zipfile-based approach (NOT python-docx) to guarantee correct
RTL rendering in Microsoft Word (not just LibreOffice).

Two Laws enforced on every element:
  1. <w:bidi/> in <w:pPr> — paragraph-level RTL
  2. <w:rtl/>  in <w:rPr> — run-level RTL
"""

import zipfile, re, sys, os

FONT = "Arial"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "assignment_summary.docx")

# ── Run and paragraph helpers ──────────────────────────────────────────────────

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

    align="left"   -> physical RIGHT (RTL natural start) — use for headings, body
    align="both"   -> justified — use for body text
    align="center" -> centered
    align="right"  -> physical LEFT — NEVER use in RTL paragraphs
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

def title(text, color="1F3864", sz=32, after=200, before=240):
    """Document title — large, centered, bold."""
    return para(run(text, sz=sz, bold=True, color=color),
                align="center", after=after, before=before)

def bullet_para(runs_xml, after=60):
    """Bullet list item — uses numId=1 from NUMBERING."""
    return para(runs_xml, after=after, numId="1")

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
    body_parts.append(title("סיכום עבודה סמינריונית"))
    body_parts.append(blank(after=80))

    # Intro paragraph (2-3 sentences)
    intro_text = (
        "עבודה זו בוחנת את הכדאיות הכלכלית של מקורות אנרגיה שונים להפעלת מרכז נתונים "
        "בגוש דן, תוך שימוש בניתוח עלות-תועלת מקיף. "
        "המחקר השווה בין חיבור לרשת החשמל הלאומית, פתרון היברידי המשלב אנרגיה סולרית, "
        "וייצור עצמאי מלא. "
        "הממצאים מראים כי הפתרון ההיברידי מציע את האיזון האופטימלי בין עלויות הון לעלויות תפעול לאורך מחזור חיים של עשרים שנה."
    )
    body_parts.append(para(run(intro_text), align="both", after=140, line=310))
    body_parts.append(blank(after=80))

    # Section heading
    body_parts.append(heading("ממצאים עיקריים"))
    body_parts.append(blank(after=40))

    # 3 Hebrew bullet points
    body_parts.append(bullet_para(run(
        "הפתרון ההיברידי מפחית את עלות האנרגיה הכוללת ב-23% לעומת חיבור ישיר לרשת, "
        "עם תקופת החזר השקעה של שבע שנים."
    )))
    body_parts.append(bullet_para(run(
        "עלויות הפחתת פחמן דו-חמצני בתרחיש הסולרי נמוכות ב-40% מהממוצע הענפי הישראלי, "
        "מה שמחזק את הצדקת ההשקעה גם מהיבט חיצוניות חברתיות."
    )))
    body_parts.append(bullet_para(run(
        "ניתוח רגישות ל-PUE מצביע על כך שגם בתרחיש שמרני של יעילות נמוכה, "
        "הכדאיות הכלכלית של הפתרון ההיברידי נשמרת לאורך כל טווח ההשקעה."
    )))
    body_parts.append(blank(after=80))

    # Closing paragraph
    closing_text = (
        "לסיכום, ניתוח עלות-תועלת זה מספק בסיס מוצק לקבלת החלטות מדיניות בתחום תשתיות "
        "הדיגיטל בישראל. "
        "מומלץ לאמץ את מודל האנרגיה ההיברידי כברירת מחדל לפרויקטים עתידיים בקנה מידה דומה, "
        "תוך עדכון שוטף של הנחות הדגם בהתאם לשינויים בתמחור אנרגיה ולטכנולוגיות מתפתחות."
    )
    body_parts.append(para(run(closing_text), align="both", after=140, line=310))

    # Section properties — <w:bidi/> is mandatory for document-level RTL
    sect_pr = (
        '<w:sectPr><w:bidi/>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080"'
        ' w:header="709" w:footer="709" w:gutter="0"/>'
        '</w:sectPr>'
    )

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

    # XML validation — confirm RTL coverage before opening in Word
    with zipfile.ZipFile(out_path) as z:
        doc = z.read('word/document.xml').decode()
        sty = z.read('word/styles.xml').decode()
        num = z.read('word/numbering.xml').decode()

    p  = len(re.findall(r'<w:pPr\b', doc))
    r_count  = len(re.findall(r'<w:rPr\b', doc))
    rb       = len(re.findall(r'<w:rtl',   doc))

    # Count bidi only in paragraph properties (exclude the sectPr bidi)
    # Strip the sectPr out of the document first, then count
    doc_body_only = re.sub(r'<w:sectPr>.*?</w:sectPr>', '', doc, flags=re.DOTALL)
    doc_bidi = len(re.findall(r'<w:bidi', doc_body_only))

    has_normal    = 'styleId="Normal"' in sty
    has_sect_bidi = bool(re.search(r'<w:sectPr>.*?<w:bidi', doc, re.DOTALL))
    has_num_bidi  = '<w:bidi/>' in num
    has_num_rtl   = '<w:rtl/>'  in num

    print()
    print("=== RTL Validation Report ===")
    print(f"  bidi in paragraphs:  {doc_bidi}/{p} (need {p}/{p})")
    print(f"  rtl  in runs:        {rb}/{r_count} (need {r_count}/{r_count})")
    print(f"  Normal style defined: {has_normal}")
    print(f"  sectPr bidi:          {has_sect_bidi}")
    print(f"  numbering bidi:       {has_num_bidi}")
    print(f"  numbering rtl:        {has_num_rtl}")

    ok = (doc_bidi == p and rb == r_count and has_normal
          and has_sect_bidi and has_num_bidi and has_num_rtl)
    print()
    print("Result: OK -- safe to open in Microsoft Word" if ok
          else "Result: ISSUES FOUND -- review XML before opening in Word")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    pack(out)
