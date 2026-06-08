"""
Generate a printable magic-item card in Omri's established parchment/gold style.

Usage:
    python make_item_card.py path/to/item_spec.json [output.html]

The JSON spec looks like:
{
  "name": "Ring of Warmth",
  "subtitle": "Ring",                      // the small italic type line
  "rarity": "Uncommon",                    // shown in the gold badge
  "footer": "Warmth's Embrace",            // italic flavor line at the bottom
  "attunement": true,                      // adds the attunement checkbox section
  "sections": [
    {"title": "Description", "content": "Plain prose for this section."},
    {"title": "Magical Effects", "abilities": [
        "<strong>Cold Resistance:</strong> Reduce cold damage by 2d8",
        "Unharmed by temperatures 0°F or lower"
    ]}
  ]
}

Each section has either "content" (a paragraph) or "abilities" (a bulleted list).
Writes a self-contained .html file (one card per file) ready to print. This
replaces hand-building the ~250-line card HTML per item; only the spec changes.
"""

import html
import json
import re
import sys
from pathlib import Path

CSS = """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Georgia', serif; background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); padding: 40px 20px; min-height: 100vh; }
        .container { max-width: 1200px; margin: 0 auto; text-align: center; }
        .card { width: 400px; height: 560px; background: linear-gradient(135deg, #f4e8d0 0%, #ede2c5 100%); border: 3px solid #8b6f47; border-radius: 8px; box-shadow: 0 10px 40px rgba(0,0,0,0.5), inset 0 0 20px rgba(255,255,255,0.3); padding: 30px; margin: 20px auto; position: relative; overflow: hidden; page-break-inside: avoid; display: inline-block; vertical-align: top; }
        .card::before, .card::after { content: '\\2726'; position: absolute; font-size: 24px; color: #8b6f47; opacity: 0.6; }
        .card::before { top: 10px; left: 10px; }
        .card::after { bottom: 10px; right: 10px; }
        .corner-tl, .corner-tr, .corner-bl, .corner-br { position: absolute; font-size: 20px; color: #8b6f47; opacity: 0.4; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; }
        .corner-tl { top: 8px; left: 8px; } .corner-tr { top: 8px; right: 8px; } .corner-bl { bottom: 8px; left: 8px; } .corner-br { bottom: 8px; right: 8px; }
        .card-content { position: relative; z-index: 1; height: 100%; display: flex; flex-direction: column; }
        .card-header { text-align: center; border-bottom: 2px solid #8b6f47; padding-bottom: 15px; margin-bottom: 15px; }
        .item-name { font-size: 22px; font-weight: bold; color: #5a4a3a; letter-spacing: 1px; margin-bottom: 5px; }
        .item-subtitle { font-size: 12px; color: #8b6f47; font-style: italic; text-transform: uppercase; letter-spacing: 2px; }
        .rarity-badge { display: inline-block; background: linear-gradient(135deg, #d4af37 0%, #c9a227 100%); color: white; padding: 4px 12px; border-radius: 20px; font-size: 10px; font-weight: bold; margin-top: 8px; text-transform: uppercase; box-shadow: 0 2px 8px rgba(212,175,55,0.4); letter-spacing: 1px; }
        .card-divider { border-top: 1px dashed #8b6f47; margin: 12px 0; opacity: 0.5; }
        .card-section { margin-bottom: 12px; }
        .section-title { font-size: 11px; font-weight: bold; color: #8b6f47; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; display: flex; align-items: center; }
        .section-title::before { content: '\\2756'; margin-right: 6px; color: #d4af37; }
        .section-content { font-size: 12px; color: #3a3a3a; line-height: 1.5; text-align: justify; }
        .ability-list { list-style: none; padding: 0; margin: 0; }
        .ability-list li { font-size: 11px; color: #3a3a3a; margin-bottom: 6px; line-height: 1.4; }
        .ability-list li::before { content: '\\25C6 '; color: #d4af37; font-weight: bold; margin-right: 4px; }
        .card-footer { margin-top: auto; padding-top: 12px; border-top: 1px dashed #8b6f47; font-size: 9px; color: #8b6f47; text-align: center; font-style: italic; }
        @media print { body { background: white; padding: 0; } .card { page-break-inside: avoid; margin: 0.5in; box-shadow: none; } }
"""


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def render_section(section: dict) -> str:
    title = html.escape(section.get("title", ""))
    block = ['<div class="card-section">', f'  <div class="section-title">{title}</div>']
    if "abilities" in section:
        block.append('  <ul class="ability-list">')
        for ability in section["abilities"]:
            # Abilities may include intentional <strong> tags, so don't escape them.
            block.append(f"    <li>{ability}</li>")
        block.append("  </ul>")
    else:
        block.append(f'  <div class="section-content">{section.get("content", "")}</div>')
    block.append("</div>")
    return "\n".join(block)


def build_html(spec: dict) -> str:
    name = html.escape(spec.get("name", "Unnamed Item"))
    subtitle = html.escape(spec.get("subtitle", ""))
    rarity = html.escape(spec.get("rarity", ""))
    footer = html.escape(spec.get("footer", name))

    sections = []
    for i, section in enumerate(spec.get("sections", [])):
        if i > 0:
            sections.append('<div class="card-divider"></div>')
        sections.append(render_section(section))

    if spec.get("attunement"):
        sections.append('<div class="card-divider"></div>')
        sections.append(
            '<div class="card-section">\n'
            '  <div class="section-title">Attuned</div>\n'
            '  <div class="section-content" style="text-align:center;font-size:11px;">'
            '□ Not Attuned &nbsp;&nbsp;&nbsp;&nbsp; □ Attuned</div>\n'
            "</div>"
        )

    sections_html = "\n".join(sections)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
  <div class="card">
    <div class="corner-tl">❦</div>
    <div class="corner-tr">❦</div>
    <div class="corner-bl">❦</div>
    <div class="corner-br">❦</div>
    <div class="card-content">
      <div class="card-header">
        <div class="item-name">{name}</div>
        <div class="item-subtitle">{subtitle}</div>
        <div class="rarity-badge">{rarity}</div>
      </div>
{sections_html}
      <div class="card-footer">✦ {footer} ✦</div>
    </div>
  </div>
</div>
</body>
</html>
"""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else spec_path.with_name(slugify(spec["name"]) + ".html")
    out_path.write_text(build_html(spec), encoding="utf-8")
    print(f"Card created: {out_path}")


if __name__ == "__main__":
    main()
