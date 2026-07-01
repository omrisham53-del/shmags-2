#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Dashboard Generator
Writes dashboard to dashboard.md and commits to GitHub
"""

import os
import sys
import re
import subprocess
from datetime import datetime

# Fix encoding for Windows PowerShell
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configuration
REPO_DIR = r"c:\עמרי\Shmags 2"
DASHBOARD_FILE = os.path.join(REPO_DIR, "dashboard.md")


def read_file(filepath):
    """Read a file safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def parse_today_md():
    """Extract priorities and info from today.md"""
    today_path = os.path.join(REPO_DIR, "today.md")
    content = read_file(today_path)

    # Find "Today's Remaining Blocks" section
    blocks = []
    if "Today's Remaining Blocks" in content:
        section = content.split("Today's Remaining Blocks")[1]
        # Find all unchecked and checked blocks
        lines = section.split('\n')
        for line in lines:
            if line.strip().startswith('- ['):
                blocks.append(line.strip())

    return blocks


def parse_tracker():
    """Extract deadlines from tracker files"""
    deadlines = []

    # University tracker
    uni_tracker = os.path.join(REPO_DIR, "projects/university/tracker.md")
    content = read_file(uni_tracker)

    # Find Key Dates & Deadlines section
    if "Key Dates & Deadlines" in content:
        section = content.split("Key Dates & Deadlines")[1]
        lines = section.split('\n')
        for line in lines:
            if '|' in line and any(x in line for x in ['5/', '6/', '7/', '8/', '9/', '10/', '11/', '12/']):
                deadlines.append(line.strip())

    return deadlines


def parse_priorities():
    """Extract priorities from current-priorities.md"""
    priorities_path = os.path.join(REPO_DIR, "context/current-priorities.md")
    content = read_file(priorities_path)

    priorities = []
    if "Priority 1:" in content:
        lines = content.split('\n')
        count = 0
        for i, line in enumerate(lines):
            if line.startswith("## Priority"):
                count += 1
                if count <= 3:
                    # Get the priority title and description
                    title = line.replace("## ", "").strip()
                    desc = ""
                    if i + 1 < len(lines):
                        desc = lines[i + 1].strip()
                    priorities.append(f"{title}: {desc}")

    return priorities


def get_first_focus_block(blocks):
    """Extract the first unchecked block"""
    for block in blocks:
        if '[ ]' in block:
            return block.replace('- [ ]', '').replace('**', '').strip()
    return "No blocks scheduled"


def generate_dashboard():
    """Generate the dashboard content"""
    today = datetime.now()
    date_str = today.strftime("%A, %B %d, %Y")

    blocks = parse_today_md()
    priorities = parse_priorities()
    deadlines = parse_tracker()
    first_block = get_first_focus_block(blocks)

    # Build the dashboard
    dashboard = {
        "date": date_str,
        "priorities": priorities[:3] if priorities else ["No priorities set"],
        "first_block": first_block,
        "deadlines": deadlines[:3] if deadlines else ["No deadlines this week"]
    }

    return dashboard


def git_commit_and_push():
    """Commit dashboard to git and push to GitHub"""
    try:
        os.chdir(REPO_DIR)

        # Stage the dashboard file
        subprocess.run(["git", "add", "dashboard.md"], check=True, capture_output=True)

        # Commit
        today = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(
            ["git", "commit", "-m", f"Update daily dashboard - {today}"],
            check=True,
            capture_output=True
        )

        # Push
        subprocess.run(["git", "push"], check=True, capture_output=True)

        print("[OK] Committed and pushed to GitHub")
        return True

    except subprocess.CalledProcessError as e:
        if "nothing to commit" in str(e.stderr):
            print("[INFO] No changes to commit")
            return True
        print(f"[ERROR] Git error: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error committing to GitHub: {e}")
        return False


def write_dashboard_file(dashboard):
    """Write dashboard to markdown file"""
    try:
        content = f"""# Daily Dashboard — {dashboard['date']}

## Top 3 Priorities

"""
        for i, priority in enumerate(dashboard['priorities'], 1):
            content += f"{i}. {priority}\n"

        content += f"""
## This Week's Deadlines

"""
        for deadline in dashboard['deadlines']:
            content += f"- {deadline}\n"

        content += f"""
## First Focus Block

{dashboard['first_block']}

---

*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Check this file on GitHub mobile app for updates*
"""

        with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Dashboard written to {DASHBOARD_FILE}")
        return True

    except Exception as e:
        print(f"[ERROR] Error writing dashboard file: {e}")
        return False


def main():
    """Main function"""
    print("=" * 50)
    print("Daily Dashboard Generator")
    print("=" * 50)

    print("\n[*] Reading files...")
    dashboard = generate_dashboard()

    print(f"\n[Date] {dashboard['date']}")
    print(f"\n[Priorities]")
    for p in dashboard['priorities']:
        print(f"   - {p}")

    print(f"\n[First Block] {dashboard['first_block']}")

    print(f"\n[Deadlines]")
    for d in dashboard['deadlines']:
        print(f"   - {d}")

    print("\n[*] Writing dashboard to file...")
    write_success = write_dashboard_file(dashboard)

    if write_success:
        print("\n[*] Committing to GitHub...")
        git_success = git_commit_and_push()
        if git_success:
            print("\n[OK] All done! Check your GitHub repo on mobile.")
        else:
            print("\n[WARNING] File written but git push failed.")
    else:
        print("\n[ERROR] Failed to write dashboard file.")

    print("=" * 50)


if __name__ == "__main__":
    main()
