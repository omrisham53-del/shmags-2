"""Diagnostic: show what Python sees, how many xlsx match selected IDs, and the
sheet structure of a few matched 2017 files.
Usage: py diag_walk.py "<round_folder>" "<category_csv>"
"""
import sys
import os
import re
import csv
import warnings

root = sys.argv[1]
csv_path = sys.argv[2] if len(sys.argv) > 2 else None

# --- load selected request IDs from the category CSV (cp862) ---
RELEVANT = {
    "אקלום מבנים", "חימום מים", "מדחסים", "כללי/אחר/משולב",
    "פרויקטים המשלבים מס' טכנולוגיות",
}
selected = set()
if csv_path:
    with open(csv_path, encoding="cp862") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            if len(row) <= 5:
                continue
            g = row[5].strip()
            d = row[4].strip()
            if g in RELEVANT or (g == "הסבה" and "לחשמל" in d):
                selected.add(row[0].strip())
print("selected IDs from CSV:", len(selected))

# --- walk and collect xlsx, group by matched selected ID ---
matched_files = []
all_xlsx = 0
for dp, dirs, files in os.walk(root, followlinks=True):
    for fn in files:
        if not fn.lower().endswith(".xlsx") or fn.startswith("~$"):
            continue
        all_xlsx += 1
        hay = dp + os.sep + fn
        ids = set(re.findall(r"\d{5,7}", hay))
        if selected and (selected & ids):
            matched_files.append(os.path.join(dp, fn))

print(f"total xlsx: {all_xlsx}")
print(f"xlsx whose path contains a selected ID: {len(matched_files)}")

# --- dump sheet names of the first few matched files ---
try:
    import openpyxl
except ImportError:
    print("openpyxl not installed")
    sys.exit(0)

print("\n--- sheet structure of first 5 matched files ---")
for fp in matched_files[:5]:
    print(f"\n{os.path.basename(fp)}")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            wb = openpyxl.load_workbook(fp, read_only=True, data_only=True)
        print("  sheets:", wb.sheetnames)
        wb.close()
    except Exception as e:
        print("  FAILED to open:", e)
