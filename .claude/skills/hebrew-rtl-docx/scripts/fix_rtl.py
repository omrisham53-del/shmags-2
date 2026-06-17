#!/usr/bin/env python3
"""
Hebrew RTL Fixer for existing .docx files
------------------------------------------
Fixes Hebrew Word documents that render correctly in LibreOffice but break
in Microsoft Word (left-aligned text, wrong-side bullets, scrambled mixed content).

Usage:
    python3 fix_rtl.py input.docx output.docx

What it fixes:
    - Adds <w:bidi/> to every paragraph that lacks it (word/document.xml + styles.xml)
    - Adds <w:rtl/> to every run that lacks it
    - Ensures Normal style is defined explicitly as RTL (prevents Word from auto-creating LTR)
    - Fixes numbering.xml: lvlJc direction, indent direction, bidi/rtl in bullet levels
"""

import re, sys, zipfile, tempfile, os

def add_bidi(m):
    """Add <w:bidi/> to a <w:pPr> block, after <w:pStyle> if present."""
    ppr = m.group(0)
    if '<w:bidi' in ppr:
        return ppr
    open_tag = re.match(r'<w:pPr[^>]*>', ppr).group(0)
    rest = ppr[len(open_tag):]
    style_m = re.match(r'(\s*<w:pStyle[^/]*/>\s*)', rest)
    if style_m:
        return open_tag + style_m.group(1) + '<w:bidi/>' + rest[len(style_m.group(1)):]
    return open_tag + '<w:bidi/>' + rest

def add_rtl(m):
    """Add <w:rtl/> to a <w:rPr> block."""
    rpr = m.group(0)
    if '<w:rtl' in rpr:
        return rpr
    return rpr.replace('</w:rPr>', '<w:rtl/></w:rPr>')

def fix_xml(xml):
    """Apply bidi + rtl fixes to any OOXML string."""
    xml = re.sub(r'<w:pPr\b[^>]*>.*?</w:pPr>', add_bidi, xml, flags=re.DOTALL)
    xml = xml.replace('<w:pPr/>', '<w:pPr><w:bidi/></w:pPr>')
    xml = re.sub(r'<w:rPr\b.*?</w:rPr>', add_rtl, xml, flags=re.DOTALL)
    return xml

def fix_styles(styles):
    """Fix styles.xml: apply bidi/rtl to all styles, ensure Normal style exists."""
    styles = fix_xml(styles)
    styles = styles.replace('<w:pPrDefault/>',
        '<w:pPrDefault><w:pPr><w:bidi/></w:pPr></w:pPrDefault>')
    if 'styleId="Normal"' not in styles:
        normal = ('<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
                  '<w:name w:val="Normal"/>'
                  '<w:pPr><w:bidi/></w:pPr>'
                  '<w:rPr><w:rtl/></w:rPr>'
                  '</w:style>')
        styles = styles.replace('</w:docDefaults>', '</w:docDefaults>' + normal, 1)
    return styles

def fix_numbering(num):
    """Fix numbering.xml: correct lvlJc direction, indent direction, add bidi/rtl."""
    # lvlJc=right means physical left in RTL — change to left (physical right)
    num = num.replace('<w:lvlJc w:val="right"/>', '<w:lvlJc w:val="left"/>')
    # ind w:left indents from wrong side — switch to w:right
    num = re.sub(
        r'<w:ind w:left="(\d+)" w:hanging="(\d+)"/>',
        lambda m: f'<w:ind w:right="{m.group(1)}" w:hanging="{m.group(2)}"/>',
        num
    )
    def fix_lvl(m):
        lvl = m.group(0)
        if '<w:bidi' not in lvl:
            lvl = lvl.replace('</w:pPr>', '<w:bidi/></w:pPr>')
        if '<w:rPr>' not in lvl:
            lvl = lvl.replace('</w:pPr>', '</w:pPr><w:rPr><w:rtl/></w:rPr>')
        return lvl
    return re.sub(r'<w:lvl\b.*?</w:lvl>', fix_lvl, num, flags=re.DOTALL)

def validate(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        doc = z.read('word/document.xml').decode()
        sty = z.read('word/styles.xml').decode()
    p  = len(re.findall(r'<w:pPr\b', doc))
    pb = len(re.findall(r'<w:bidi',  doc))
    r  = len(re.findall(r'<w:rPr\b', doc))
    rb = len(re.findall(r'<w:rtl',   doc))
    print(f"bidi coverage: {pb}/{p} paragraphs")
    print(f"rtl  coverage: {rb}/{r} runs")
    print(f"Normal style defined: {'styleId=\"Normal\"' in sty}")
    if pb == p and rb == r and 'styleId="Normal"' in sty:
        print("Validation: OK")
    else:
        print("Validation: ISSUES FOUND — inspect XML manually")

def main(input_path, output_path):
    with zipfile.ZipFile(input_path, 'r') as zin:
        file_map = {name: zin.read(name) for name in zin.namelist()}

    if 'word/document.xml' in file_map:
        xml = file_map['word/document.xml'].decode('utf-8')
        file_map['word/document.xml'] = fix_xml(xml).encode('utf-8')

    if 'word/styles.xml' in file_map:
        sty = file_map['word/styles.xml'].decode('utf-8')
        file_map['word/styles.xml'] = fix_styles(sty).encode('utf-8')

    if 'word/numbering.xml' in file_map:
        num = file_map['word/numbering.xml'].decode('utf-8')
        file_map['word/numbering.xml'] = fix_numbering(num).encode('utf-8')

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, content in file_map.items():
            zout.writestr(name, content)

    print(f"Written: {output_path}")
    validate(output_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 fix_rtl.py input.docx output.docx")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
