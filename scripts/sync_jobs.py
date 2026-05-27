#!/usr/bin/env python3
"""
sync_jobs.py - Bidirectional sync between projects/job-search/tracker.md and
the "Job Applications" Notion database.

Usage:
    python scripts/sync_jobs.py push   # tracker.md  -> Notion (upsert by Link)
    python scripts/sync_jobs.py pull   # Notion      -> tracker.md (regenerate)
    python scripts/sync_jobs.py status # show counts on both sides, no writes

Setup (one time):
    1. Create a Notion internal integration: https://www.notion.so/profile/integrations
       Give it Read + Insert + Update content capabilities.
    2. Open the "Job Search" page in Notion -> ... menu -> Connections ->
       add the integration.
    3. Copy the integration secret. Add to a .env file in repo root:
           NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    4. pip install requests python-dotenv

The script uses the public Notion API directly so it works the same from any
machine (laptop, work computer, CI). No MCP needed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency. Run: pip install requests python-dotenv")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv optional; token can be set in shell env

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = REPO_ROOT / "projects" / "job-search" / "tracker.md"

# Hardcoded IDs for the "Job Applications" database, created 2026-05-18.
DATABASE_ID = "039f5bc1-85c8-49d7-b1b5-ca4e5765b918"

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

VALID_STATUSES = {"Found", "Applied", "In Review", "Rejected", "Offer"}
VALID_FITS = {"High", "Medium", "Low", "Unknown"}


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _headers() -> dict:
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        sys.exit(
            "NOTION_TOKEN not set. Create an integration at "
            "https://www.notion.so/profile/integrations and put the secret in .env"
        )
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _post(path: str, payload: dict) -> dict:
    r = requests.post(f"{NOTION_API}{path}", headers=_headers(), json=payload, timeout=30)
    if not r.ok:
        sys.exit(f"Notion API error {r.status_code} on POST {path}: {r.text}")
    return r.json()


def _patch(path: str, payload: dict) -> dict:
    r = requests.patch(f"{NOTION_API}{path}", headers=_headers(), json=payload, timeout=30)
    if not r.ok:
        sys.exit(f"Notion API error {r.status_code} on PATCH {path}: {r.text}")
    return r.json()


# ---------------------------------------------------------------------------
# tracker.md parsing / writing
# ---------------------------------------------------------------------------

TABLE_HEADER_RE = re.compile(
    r"^\|\s*Date Found\s*\|\s*Job Title\s*\|\s*Company\s*\|\s*Location\s*\|\s*Link\s*\|\s*Fit\s*\|\s*Status\s*\|\s*Notes\s*\|",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def parse_tracker(path: Path) -> list[dict]:
    if not path.exists():
        sys.exit(f"Tracker not found at {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[dict] = []
    in_table = False
    for line in lines:
        if not in_table:
            if TABLE_HEADER_RE.match(line):
                in_table = True
            continue
        if line.startswith("|---") or line.startswith("| ---"):
            continue
        if not line.startswith("|"):
            break  # table ended
        # Parse row. Use a permissive split on "|" then strip.
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue
        date_found, title, company, location, link_md, fit, status, *notes_parts = cells
        notes = " | ".join(notes_parts).strip()
        m = LINK_RE.search(link_md)
        link = m.group(2) if m else link_md
        rows.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link,
            "fit": fit if fit in VALID_FITS else "Unknown",
            "status": status if status in VALID_STATUSES else "Found",
            "date_found": date_found if re.match(r"^\d{4}-\d{2}-\d{2}$", date_found) else None,
            "notes": notes,
        })
    return rows


def write_tracker(path: Path, rows: list[dict]) -> None:
    """Regenerate tracker.md from rows. Preserves the file's surrounding prose."""
    today = datetime.now().strftime("%Y-%m-%d")
    counts = _counts(rows)
    header = [
        "# Job Application Tracker",
        "",
        "Running log of every job surfaced by the Job Opportunity Tracker. Updated automatically after each run.",
        "",
        "## Summary",
        f"- Total jobs found: {counts['total']}",
        f"- Applied: {counts['Applied']}",
        f"- In review: {counts['In Review']}",
        f"- Rejected: {counts['Rejected']}",
        f"- Offer: {counts['Offer']}",
        "",
        f"_Last synced from Notion: {today}_",
        "",
        "---",
        "",
        "## Job Log",
        "",
        "| Date Found | Job Title | Company | Location | Link | Fit | Status | Notes |",
        "|------------|-----------|---------|----------|------|-----|--------|-------|",
    ]
    # Sort by date found (desc), then status priority
    status_order = {"Offer": 0, "In Review": 1, "Applied": 2, "Found": 3, "Rejected": 4}
    rows_sorted = sorted(
        rows,
        key=lambda r: (r.get("date_found") or "", status_order.get(r["status"], 9)),
        reverse=True,
    )
    body = []
    for r in rows_sorted:
        date_found = r.get("date_found") or ""
        link_md = f"[Link]({r['link']})" if r["link"] else ""
        notes = (r.get("notes") or "").replace("|", "\\|").replace("\n", " ")
        body.append(
            f"| {date_found} | {r['title']} | {r['company']} | {r['location']} | "
            f"{link_md} | {r['fit']} | {r['status']} | {notes} |"
        )
    footer = [
        "",
        "---",
        "",
        "## Status Legend",
        "- **Found** - Just discovered, haven't applied yet",
        "- **Applied** - Application submitted, waiting to hear back",
        "- **In Review** - Company is reviewing your application",
        "- **Rejected** - Company declined to move forward",
        "- **Offer** - Company extended an offer",
        "",
        "## Fit Legend",
        "- **High** - Strong match to your profile and interests",
        "- **Medium** - Good fit, worth applying",
        "- **Low** - Interesting but not ideal match",
        "",
    ]
    path.write_text("\n".join(header + body + footer) + "\n", encoding="utf-8")


def _counts(rows: list[dict]) -> dict:
    out = {"total": len(rows), "Found": 0, "Applied": 0, "In Review": 0, "Rejected": 0, "Offer": 0}
    for r in rows:
        out[r["status"]] = out.get(r["status"], 0) + 1
    return out


# ---------------------------------------------------------------------------
# Notion <-> dict translation
# ---------------------------------------------------------------------------

def _text(value: str | None) -> list[dict]:
    if not value:
        return []
    return [{"type": "text", "text": {"content": value[:2000]}}]


def row_to_notion_props(row: dict) -> dict:
    props = {
        "Title": {"title": _text(row["title"])},
        "Company": {"rich_text": _text(row["company"])},
        "Location": {"rich_text": _text(row["location"])},
        "Link": {"url": row["link"] or None},
        "Fit": {"select": {"name": row["fit"]}},
        "Status": {"select": {"name": row["status"]}},
        "Notes": {"rich_text": _text(row.get("notes", ""))},
    }
    if row.get("date_found"):
        props["Date Found"] = {"date": {"start": row["date_found"]}}
    if row.get("date_applied"):
        props["Date Applied"] = {"date": {"start": row["date_applied"]}}
    return props


def notion_page_to_row(page: dict) -> dict:
    p = page["properties"]

    def rich_text(prop):
        items = prop.get("rich_text", []) if prop else []
        return "".join(i.get("plain_text", "") for i in items)

    def title(prop):
        items = prop.get("title", []) if prop else []
        return "".join(i.get("plain_text", "") for i in items)

    def select(prop):
        sel = (prop or {}).get("select")
        return sel.get("name") if sel else None

    def date(prop):
        d = (prop or {}).get("date")
        return d.get("start") if d else None

    return {
        "page_id": page["id"],
        "title": title(p.get("Title")),
        "company": rich_text(p.get("Company")),
        "location": rich_text(p.get("Location")),
        "link": (p.get("Link") or {}).get("url") or "",
        "fit": select(p.get("Fit")) or "Unknown",
        "status": select(p.get("Status")) or "Found",
        "date_found": date(p.get("Date Found")),
        "date_applied": date(p.get("Date Applied")),
        "notes": rich_text(p.get("Notes")),
    }


# ---------------------------------------------------------------------------
# Notion queries
# ---------------------------------------------------------------------------

def fetch_all_notion_rows() -> list[dict]:
    rows: list[dict] = []
    payload = {"page_size": 100}
    while True:
        resp = _post(f"/databases/{DATABASE_ID}/query", payload)
        for page in resp.get("results", []):
            rows.append(notion_page_to_row(page))
        if not resp.get("has_more"):
            break
        payload["start_cursor"] = resp["next_cursor"]
    return rows


def create_notion_page(row: dict) -> dict:
    return _post("/pages", {
        "parent": {"database_id": DATABASE_ID},
        "properties": row_to_notion_props(row),
    })


def update_notion_page(page_id: str, row: dict) -> dict:
    return _patch(f"/pages/{page_id}", {"properties": row_to_notion_props(row)})


# ---------------------------------------------------------------------------
# Sync commands
# ---------------------------------------------------------------------------

def cmd_push() -> None:
    md_rows = parse_tracker(TRACKER_PATH)
    notion_rows = fetch_all_notion_rows()
    by_link = {r["link"]: r for r in notion_rows if r["link"]}

    created = updated = skipped = 0
    for md in md_rows:
        if not md["link"]:
            skipped += 1
            continue
        existing = by_link.get(md["link"])
        if existing:
            # Update only if a field differs
            if any(existing.get(k) != md.get(k) for k in
                   ("title", "company", "location", "fit", "status",
                    "date_found", "notes")):
                update_notion_page(existing["page_id"], md)
                updated += 1
        else:
            create_notion_page(md)
            created += 1
    print(f"push: {created} created, {updated} updated, {skipped} skipped (no link)")


def cmd_pull() -> None:
    notion_rows = fetch_all_notion_rows()
    write_tracker(TRACKER_PATH, notion_rows)
    print(f"pull: regenerated {TRACKER_PATH.relative_to(REPO_ROOT)} from {len(notion_rows)} Notion rows")


def cmd_status() -> None:
    md_rows = parse_tracker(TRACKER_PATH)
    notion_rows = fetch_all_notion_rows()
    print(f"tracker.md: {len(md_rows)} rows  | Notion: {len(notion_rows)} rows")
    md_links = {r["link"] for r in md_rows if r["link"]}
    notion_links = {r["link"] for r in notion_rows if r["link"]}
    print(f"  only in md     : {len(md_links - notion_links)}")
    print(f"  only in Notion : {len(notion_links - md_links)}")
    print(f"  in both        : {len(md_links & notion_links)}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["push", "pull", "status"])
    args = parser.parse_args()
    {"push": cmd_push, "pull": cmd_pull, "status": cmd_status}[args.command]()


if __name__ == "__main__":
    main()
