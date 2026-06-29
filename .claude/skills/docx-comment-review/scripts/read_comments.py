#!/usr/bin/env python3
"""Extract reviewer comment bubbles from a .docx, each paired with the exact
document text it is anchored to.

Word stores comments in word/comments.xml, and marks where each one attaches
in word/document.xml using <w:commentRangeStart>/<w:commentRangeEnd> pairs that
share the comment id. This script walks the document body in order, tracks which
comment ranges are open at each run, and collects the anchored text per id. That
anchored text is what the reviewer is actually pointing at, so it is the thing a
correction has to act on.

Usage:
    python read_comments.py path/to/file.docx [--json]

Default output is human-readable. --json emits a list of
{id, author, date, comment, anchor_text} for downstream tooling.
"""
import sys
import json
import zipfile
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def _q(tag):
    return f"{{{W}}}{tag}"


def _text_of_paragraphish(elem):
    """Concatenate all <w:t> descendants of an element (a comment is paragraphs)."""
    return "".join(t.text or "" for t in elem.iter(_q("t")))


def read_comments(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        if "word/comments.xml" not in names:
            return []
        comments_xml = z.read("word/comments.xml")
        document_xml = z.read("word/document.xml")

    # 1. comment id -> {author, date, text}
    comments = {}
    croot = ET.fromstring(comments_xml)
    for c in croot.findall(_q("comment")):
        cid = c.get(_q("id"))
        comments[cid] = {
            "id": cid,
            "author": c.get(_q("author")) or "",
            "date": c.get(_q("date")) or "",
            "comment": _text_of_paragraphish(c).strip(),
            "anchor_text": "",
        }

    # 2. walk the document body in document order, accumulating anchored text
    droot = ET.fromstring(document_xml)
    open_ids = set()
    # iterate over every element; when we hit a range start/end toggle the id,
    # and append any <w:t> we encounter to every currently-open comment.
    for elem in droot.iter():
        tag = elem.tag
        if tag == _q("commentRangeStart"):
            open_ids.add(elem.get(_q("id")))
        elif tag == _q("commentRangeEnd"):
            open_ids.discard(elem.get(_q("id")))
        elif tag == _q("t") and open_ids:
            for cid in open_ids:
                if cid in comments:
                    comments[cid]["anchor_text"] += elem.text or ""

    # preserve the order comments appear in comments.xml
    ordered = [comments[c.get(_q("id"))] for c in croot.findall(_q("comment"))
               if c.get(_q("id")) in comments]
    for c in ordered:
        c["anchor_text"] = c["anchor_text"].strip()
    return ordered


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    comments = read_comments(args[0])
    if as_json:
        print(json.dumps(comments, ensure_ascii=False, indent=2))
        return
    if not comments:
        print("No comments found in this document.")
        return
    print(f"{len(comments)} comment(s) found:\n")
    for c in comments:
        print(f"[{c['id']}] {c['author']} ({c['date']})")
        print(f"  Anchored to: {c['anchor_text'] or '(no text range / whole paragraph)'}")
        print(f"  Comment: {c['comment']}")
        print()


if __name__ == "__main__":
    main()
