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
    - Fixes sectPr: adds <w:bidi/> to section properties for page-level RTL
    - Fixes docDefaults: ensures default paragraph and run properties are RTL

No external dependencies — uses only Python standard library (zipfile, re, sys).
"""

import re, sys, zipfile


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
    """Apply bidi + rtl fixes to any OOXML string (document.xml or styles.xml)."""
    # Fix full <w:pPr>...</w:pPr> blocks
    xml = re.sub(r'<w:pPr\b[^>]*>.*?</w:pPr>', add_bidi, xml, flags=re.DOTALL)
    # Fix self-closing <w:pPr/>
    xml = xml.replace('<w:pPr/>', '<w:pPr><w:bidi/></w:pPr>')
    # Fix full <w:rPr>...</w:rPr> blocks
    xml = re.sub(r'<w:rPr\b.*?</w:rPr>', add_rtl, xml, flags=re.DOTALL)
    return xml


def fix_sect_pr(xml):
    """Add <w:bidi/> to <w:sectPr> if missing (page-level RTL direction)."""
    def add_sect_bidi(m):
        sect = m.group(0)
        if '<w:bidi' in sect:
            return sect
        open_tag = re.match(r'<w:sectPr[^>]*>', sect).group(0)
        return open_tag + '<w:bidi/>' + sect[len(open_tag):]
    return re.sub(r'<w:sectPr\b[^>]*>.*?</w:sectPr>', add_sect_bidi, xml, flags=re.DOTALL)


def fix_styles(styles):
    """
    Fix styles.xml:
    - Apply bidi/rtl to all existing style definitions
    - Fix docDefaults to include RTL defaults
    - Ensure Normal style is explicitly defined as RTL
    """
    styles = fix_xml(styles)

    # Fix self-closing <w:pPrDefault/>
    styles = styles.replace('<w:pPrDefault/>',
        '<w:pPrDefault><w:pPr><w:bidi/></w:pPr></w:pPrDefault>')

    # Fix self-closing <w:rPrDefault/>
    styles = styles.replace('<w:rPrDefault/>',
        '<w:rPrDefault><w:rPr><w:rtl/></w:rPr></w:rPrDefault>')

    # Ensure Normal style exists explicitly — if Word doesn't find it, it
    # auto-generates Normal as LTR and that overrides everything else.
    if 'styleId="Normal"' not in styles:
        normal = (
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
            '<w:name w:val="Normal"/>'
            '<w:pPr><w:bidi/></w:pPr>'
            '<w:rPr><w:rtl/></w:rPr>'
            '</w:style>'
        )
        # Insert right after </w:docDefaults>
        styles = styles.replace('</w:docDefaults>', '</w:docDefaults>' + normal, 1)

    return styles


def fix_numbering(num):
    """
    Fix numbering.xml for RTL bullet lists.

    In RTL paragraphs, jc values are physically reversed:
    - lvlJc=left means the physical right side (natural RTL start) — correct
    - lvlJc=right means the physical left side — wrong for RTL bullets

    Indentation must also flip:
    - ind w:right indents from the right margin — correct for RTL
    - ind w:left indents from the left margin — wrong for RTL
    """
    # lvlJc=right is physical left in RTL — flip to left (physical right)
    num = num.replace('<w:lvlJc w:val="right"/>', '<w:lvlJc w:val="left"/>')

    # ind w:left indents from the wrong side — switch to w:right
    num = re.sub(
        r'<w:ind w:left="(\d+)" w:hanging="(\d+)"/>',
        lambda m: f'<w:ind w:right="{m.group(1)}" w:hanging="{m.group(2)}"/>',
        num
    )

    # Also handle ind with only w:left (no hanging)
    num = re.sub(
        r'<w:ind w:left="(\d+)"/>',
        lambda m: f'<w:ind w:right="{m.group(1)}"/>',
        num
    )

    def fix_lvl(m):
        """Add bidi/rtl to each bullet level definition."""
        lvl = m.group(0)
        # Add <w:bidi/> inside the level's <w:pPr> if missing
        if '<w:pPr>' in lvl or '<w:pPr ' in lvl:
            if '<w:bidi' not in lvl:
                lvl = re.sub(r'</w:pPr>', '<w:bidi/></w:pPr>', lvl, count=1)
        else:
            # No pPr at all — insert one with bidi before </w:lvl>
            lvl = lvl.replace('</w:lvl>', '<w:pPr><w:bidi/></w:pPr></w:lvl>')

        # Add <w:rtl/> inside the level's <w:rPr> if missing
        if '<w:rPr>' in lvl or '<w:rPr ' in lvl:
            if '<w:rtl' not in lvl:
                lvl = re.sub(r'</w:rPr>', '<w:rtl/></w:rPr>', lvl, count=1)
        else:
            # No rPr at all — insert one with rtl after </w:pPr>
            lvl = lvl.replace('</w:pPr>', '</w:pPr><w:rPr><w:rtl/></w:rPr>', 1)

        return lvl

    return re.sub(r'<w:lvl\b.*?</w:lvl>', fix_lvl, num, flags=re.DOTALL)


def validate(docx_path):
    """
    Print RTL coverage stats and a pass/fail verdict.
    Run after fixing to confirm correctness before opening in Word.
    """
    with zipfile.ZipFile(docx_path) as z:
        doc = z.read('word/document.xml').decode()
        sty = z.read('word/styles.xml').decode()

    p  = len(re.findall(r'<w:pPr\b', doc))
    pb = len(re.findall(r'<w:bidi',  doc))
    r  = len(re.findall(r'<w:rPr\b', doc))
    rb = len(re.findall(r'<w:rtl',   doc))

    normal_defined = 'styleId="Normal"' in sty
    sect_bidi      = '<w:bidi/>' in doc  # at minimum one bidi present at section level

    print(f"  bidi coverage : {pb}/{p} paragraphs")
    print(f"  rtl  coverage : {rb}/{r} runs")
    print(f"  Normal style  : {'defined' if normal_defined else 'MISSING'}")

    ok = (pb == p and rb == r and normal_defined)
    print("  Validation    : OK" if ok else "  Validation    : ISSUES FOUND -- inspect XML manually")
    return ok


def main(input_path, output_path):
    # Read every file in the zip into memory
    with zipfile.ZipFile(input_path, 'r') as zin:
        file_map = {name: zin.read(name) for name in zin.namelist()}

    # Fix document.xml (paragraphs, runs, section properties)
    if 'word/document.xml' in file_map:
        xml = file_map['word/document.xml'].decode('utf-8')
        xml = fix_xml(xml)
        xml = fix_sect_pr(xml)
        file_map['word/document.xml'] = xml.encode('utf-8')

    # Fix styles.xml (Normal style, docDefaults, all style definitions)
    if 'word/styles.xml' in file_map:
        sty = file_map['word/styles.xml'].decode('utf-8')
        file_map['word/styles.xml'] = fix_styles(sty).encode('utf-8')

    # Fix numbering.xml (bullet direction and indentation)
    if 'word/numbering.xml' in file_map:
        num = file_map['word/numbering.xml'].decode('utf-8')
        file_map['word/numbering.xml'] = fix_numbering(num).encode('utf-8')

    # Repack all files into the output docx
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
