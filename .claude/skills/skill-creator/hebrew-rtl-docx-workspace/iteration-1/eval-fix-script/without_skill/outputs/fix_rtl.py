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

No external dependencies — uses only Python stdlib (zipfile, re, sys).
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
    # Fix non-empty <w:pPr> blocks
    xml = re.sub(r'<w:pPr\b[^>]*>.*?</w:pPr>', add_bidi, xml, flags=re.DOTALL)
    # Fix self-closing <w:pPr/>
    xml = xml.replace('<w:pPr/>', '<w:pPr><w:bidi/></w:pPr>')
    # Fix <w:rPr> blocks
    xml = re.sub(r'<w:rPr\b.*?</w:rPr>', add_rtl, xml, flags=re.DOTALL)
    return xml


def fix_styles(styles):
    """
    Fix styles.xml:
    - Apply bidi/rtl to all style definitions
    - Fix <w:pPrDefault/> (self-closing default paragraph props)
    - Insert explicit Normal style if missing (prevents Word from auto-creating it as LTR)
    - Fix docDefaults rPrDefault if present but lacks <w:rtl/>
    """
    styles = fix_xml(styles)

    # Fix self-closing pPrDefault
    styles = styles.replace(
        '<w:pPrDefault/>',
        '<w:pPrDefault><w:pPr><w:bidi/></w:pPr></w:pPrDefault>'
    )

    # Insert Normal style if absent
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
    Fix numbering.xml:
    - lvlJc=right means physical LEFT in RTL paragraphs — flip to left (physical right)
    - ind w:left indents from the wrong side — switch to w:right
    - Add <w:bidi/> and <w:rtl/> to each bullet level's pPr/rPr
    """
    # Flip bullet anchor side
    num = num.replace('<w:lvlJc w:val="right"/>', '<w:lvlJc w:val="left"/>')

    # Flip indent side: w:left -> w:right (keep hanging value)
    num = re.sub(
        r'<w:ind w:left="(\d+)" w:hanging="(\d+)"/>',
        lambda m: f'<w:ind w:right="{m.group(1)}" w:hanging="{m.group(2)}"/>',
        num
    )

    def fix_lvl(m):
        lvl = m.group(0)
        # Add <w:bidi/> inside <w:pPr> if not already there
        if '<w:bidi' not in lvl:
            lvl = re.sub(
                r'(</w:pPr>)',
                r'<w:bidi/>\1',
                lvl,
                count=1
            )
        # Add <w:jc w:val="left"/> inside <w:pPr> if not already there
        # (physical right in RTL — where bullets should anchor)
        if '<w:jc' not in lvl:
            lvl = re.sub(
                r'(</w:pPr>)',
                r'<w:jc w:val="left"/>\1',
                lvl,
                count=1
            )
        # Add <w:rPr><w:rtl/></w:rPr> if no rPr block exists in this level
        if '<w:rPr>' not in lvl:
            lvl = re.sub(
                r'(</w:pPr>)',
                r'\1<w:rPr><w:rtl/></w:rPr>',
                lvl,
                count=1
            )
        else:
            # rPr exists — ensure it has <w:rtl/>
            lvl = re.sub(r'<w:rPr\b.*?</w:rPr>', add_rtl, lvl, flags=re.DOTALL)
        return lvl

    num = re.sub(r'<w:lvl\b.*?</w:lvl>', fix_lvl, num, flags=re.DOTALL)
    return num


def fix_sectpr(doc):
    """
    Ensure the section properties (<w:sectPr>) contain <w:bidi/> so the
    overall page layout is right-to-left (paragraph direction default).
    """
    def add_bidi_to_sectpr(m):
        sectpr = m.group(0)
        if '<w:bidi' in sectpr:
            return sectpr
        return sectpr.replace('</w:sectPr>', '<w:bidi/></w:sectPr>', 1)

    return re.sub(r'<w:sectPr\b.*?</w:sectPr>', add_bidi_to_sectpr, doc, flags=re.DOTALL)


def validate(docx_path):
    """Print RTL coverage stats for the output file."""
    with zipfile.ZipFile(docx_path) as z:
        doc = z.read('word/document.xml').decode('utf-8')
        sty = z.read('word/styles.xml').decode('utf-8')

    p  = len(re.findall(r'<w:pPr\b', doc))
    pb = len(re.findall(r'<w:bidi',  doc))
    r  = len(re.findall(r'<w:rPr\b', doc))
    rb = len(re.findall(r'<w:rtl',   doc))

    print(f"  bidi coverage : {pb}/{p} paragraphs")
    print(f"  rtl  coverage : {rb}/{r} runs")
    print(f"  Normal style  : {'styleId=\"Normal\"' in sty}")
    print(f"  sectPr bidi   : {'<w:bidi' in re.search(r'<w:sectPr.*?</w:sectPr>', doc, re.DOTALL).group(0) if re.search(r'<w:sectPr.*?</w:sectPr>', doc, re.DOTALL) else False}")

    ok = (
        pb == p and
        rb == r and
        'styleId="Normal"' in sty
    )
    print("  Validation    : OK" if ok else "  Validation    : ISSUES FOUND — inspect XML manually")
    return ok


def main(input_path, output_path):
    # Read all files from the input ZIP into memory
    with zipfile.ZipFile(input_path, 'r') as zin:
        file_map = {name: zin.read(name) for name in zin.namelist()}

    # Fix document.xml (paragraphs and runs)
    if 'word/document.xml' in file_map:
        xml = file_map['word/document.xml'].decode('utf-8')
        xml = fix_xml(xml)
        xml = fix_sectpr(xml)
        file_map['word/document.xml'] = xml.encode('utf-8')

    # Fix styles.xml (style definitions + Normal style)
    if 'word/styles.xml' in file_map:
        sty = file_map['word/styles.xml'].decode('utf-8')
        file_map['word/styles.xml'] = fix_styles(sty).encode('utf-8')

    # Fix numbering.xml (bullet direction)
    if 'word/numbering.xml' in file_map:
        num = file_map['word/numbering.xml'].decode('utf-8')
        file_map['word/numbering.xml'] = fix_numbering(num).encode('utf-8')

    # Write the corrected .docx
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
