"""Diagnostic: show exactly what Python sees under a round folder.
Usage: py diag_walk.py "<round_folder_path>"
"""
import sys
import os

root = sys.argv[1]
print("root exists:", os.path.isdir(root))

try:
    top = os.listdir(root)
except Exception as e:
    print("listdir(root) FAILED:", e)
    sys.exit(1)

print("top-level entries:", len(top))
for name in top[:5]:
    p = os.path.join(root, name)
    print(f"  {name!r}")
    print(f"     isdir={os.path.isdir(p)} islink={os.path.islink(p)}")
    try:
        inner = os.listdir(p)
        print(f"     inner entries: {len(inner)} -> {inner[:5]}")
    except Exception as e:
        print(f"     listdir(sub) FAILED: {e}")

nd = nf = nx = 0
for dp, dirs, files in os.walk(root, followlinks=True):
    nd += 1
    for f in files:
        nf += 1
        if f.lower().endswith(".xlsx"):
            nx += 1
print(f"\nwalk totals: dirs={nd}  files={nf}  xlsx={nx}")
