#!/usr/bin/env python3
"""Apply approved corrections to a reviewed .docx as Word tracked changes,
leaving the reviewer's comment bubbles in place, and save under the next
version number.

Why tracked changes and not a clean edit: Daniel is going to look at this again.
He needs to *see* that each comment was addressed and how, not receive a clean
file where the text silently moved. So every correction becomes a tracked
deletion of the old anchored text plus a tracked insertion of the new text
(w:del + w:ins). The comment that prompted it stays attached, so on his next
pass each bubble sits right next to the revision that answers it.

Input: the reviewed docx + a JSON list of approved corrections, each
    {"id": "<comment id>", "new_text": "<replacement for the anchored text>"}
Comment ids come from read_comments.py. A correction whose new_text equals the
anchored text (or is omitted) is treated as "no change" and skipped.

Usage:
    python apply_revisions.py reviewed.docx corrections.json [--author "Omri"]

Version bump: the next minor version. 0.2 -> 0.3, 1 -> 1.1, 2.4 -> 2.5. The
output file is written next to the input with the bumped number; the input is
never overwritten. See bump_version().

Scope note: this handles the common case where a comment is anchored within a
single paragraph (a word, phrase, or sentence). If a comment range spans
multiple paragraphs the script skips it and warns, so you can handle that one by
hand rather than risk mangling structure.
"""
import sys
import json
import re
import os
import datetime
from lxml import etree
from docx import Document

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def q(tag):
    return f"{{{W}}}{tag}"


def bump_version(filename):
    """Return filename with the trailing version number's minor part +1.

    Versions look like '...0.2.docx', '...1.docx', '...2.4.docx'. The scheme:
    X.Y where X is the client-release number (0 = pre-first-client) and Y is the
    internal revision. Addressing a review is an internal revision, so we bump Y.
    A whole-number client version like '1' becomes '1.1'.
    """
    base, ext = os.path.splitext(filename)
    m = re.search(r"(\d+)(?:\.(\d+))?\s*$", base)
    if not m:
        raise ValueError(
            f"No version number found at the end of '{base}'. "
            "Expected something ending in e.g. ' 0.2' or ' 1'."
        )
    major = int(m.group(1))
    minor = int(m.group(2)) if m.group(2) is not None else 0
    new_ver = f"{major}.{minor + 1}"
    new_base = base[:m.start()] + new_ver
    return new_base + ext


def _next_rev_id(root):
    ids = [int(e.get(q("id"))) for e in root.iter()
           if e.tag in (q("ins"), q("del")) and (e.get(q("id")) or "").isdigit()]
    return max(ids, default=1000) + 1


def _make_run(text, rpr, kind):
    """Build a <w:r> with the given text. kind 'del' uses w:delText, 'ins' w:t."""
    run = etree.Element(q("r"))
    if rpr is not None:
        run.append(etree.fromstring(etree.tostring(rpr)))
    t = etree.SubElement(run, q("delText") if kind == "del" else q("t"))
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return run


def apply_corrections(docx_path, corrections, author, out_path):
    doc = Document(docx_path)
    root = doc.element  # the w:document element
    body = root.find(q("body"))
    date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    rev = _next_rev_id(root)

    by_id = {str(c["id"]): c for c in corrections
             if c.get("new_text") is not None}

    applied, skipped = [], []
    for cid, corr in by_id.items():
        new_text = corr["new_text"]
        starts = [e for e in root.iter(q("commentRangeStart")) if e.get(q("id")) == cid]
        ends = [e for e in root.iter(q("commentRangeEnd")) if e.get(q("id")) == cid]
        if not starts or not ends:
            skipped.append((cid, "comment range not found"))
            continue
        start, end = starts[0], ends[0]
        para = start.getparent()
        if end.getparent() is not para:
            skipped.append((cid, "comment spans multiple paragraphs - apply by hand"))
            continue

        children = list(para)
        si, ei = children.index(start), children.index(end)
        old_runs = [c for c in children[si + 1:ei] if c.tag == q("r")]
        old_text = "".join(
            "".join(t.text or "" for t in r.iter(q("t"))) for r in old_runs
        )
        if not new_text.strip():
            # Empty replacement is almost never intended (a comment like "add a
            # sentence here" needs new_text = old text + the addition, not a
            # blank). Skip rather than silently delete the anchored text.
            skipped.append((cid, "empty new_text - skipped (to delete text, do it by hand)"))
            continue
        if not old_text.strip() or new_text.strip() == old_text.strip():
            skipped.append((cid, "no change vs anchored text"))
            continue

        rpr = old_runs[0].find(q("rPr")) if old_runs else None
        del_el = etree.Element(q("del"))
        del_el.set(q("id"), str(rev)); rev += 1
        del_el.set(q("author"), author); del_el.set(q("date"), date)
        del_el.append(_make_run(old_text, rpr, "del"))

        ins_el = etree.Element(q("ins"))
        ins_el.set(q("id"), str(rev)); rev += 1
        ins_el.set(q("author"), author); ins_el.set(q("date"), date)
        ins_el.append(_make_run(new_text, rpr, "ins"))

        insert_at = si + 1
        for r in old_runs:
            para.remove(r)
        para.insert(insert_at, ins_el)
        para.insert(insert_at, del_el)
        applied.append((cid, old_text, new_text))

    doc.save(out_path)
    return applied, skipped


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    author = "Omri"
    if "--author" in sys.argv:
        author = sys.argv[sys.argv.index("--author") + 1]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    docx_path, corrections_path = args[0], args[1]
    with open(corrections_path, encoding="utf-8") as f:
        corrections = json.load(f)
    out_path = bump_version(docx_path)
    applied, skipped = apply_corrections(docx_path, corrections, author, out_path)
    print(f"Saved: {out_path}")
    print(f"Applied {len(applied)} tracked change(s):")
    for cid, old, new in applied:
        print(f"  [{cid}] '{old}' -> '{new}'")
    if skipped:
        print(f"Skipped {len(skipped)}:")
        for cid, why in skipped:
            print(f"  [{cid}] {why}")


if __name__ == "__main__":
    main()
