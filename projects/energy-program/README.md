# Energy Efficiency Program Project

**Description:** Excel analysis and documentation for Israel's national energy efficiency program funding and policy recommendations.

**Client:** Ministry of Energy (via EcoTraders)  
**Status:** Active  
**Manager:** Daniel

**Key Dates:**
- **Deadline:** June 30, 2026 (slipped)
- Daniel confirmed 2026-07-26: no new assignments before Omri's Aug 22 last day at EcoTraders — remaining scope on this project is fixed to the 3 items below.

**Incentive-section chapters (Omri owns 3):**
- Grants program chapter — sent to client 2026-07-12 (done)
- Loan fund — position paper (sent to client 2026-07-12) covers the appendix version; the full chapter for the actual national program document still needs to be written
- Tax incentive model, including the market analysis — in progress (see `baseline-technology-data.md` + `tracker.md`)
- Tax incentive chapter for the national program — not yet written (methodology brainstormed, see `brainstorms/2026-07-22_tax-incentive-market-analysis.md`)

**Day-by-day schedule for the remaining work (Jul 27 -- Aug 20):** see `tracker.md`.

**Handoff briefing for the work-account Claude session (loan fund chapter):** see `work-handoff.md` -- paste it as the opening message when starting that work on the company account, since that session can't see this repo. Kept current from this side.

**What's Included:**
- Techno-economic analysis in Excel
- Supporting documents
- Policy recommendations
- Ministry deliverables

---

## Capex Extraction Pipeline

### What it does
Reads the master grant request category table, filters to the relevant technology categories, matches each request ID to its Excel file, extracts equipment cost line items, classifies them by technology, and outputs average CapEx per installation for the tax incentive model.

### Files
- `extract_capex.py` - low-level extractor: reads a single grant Excel file and returns line items
- `capex_pipeline.py` - orchestrator: filter → match → extract → classify → average

### Setup
```bash
git pull
pip install openpyxl
```

### Running
```bash
python capex_pipeline.py <path_to_category_csv> <path_to_round_folder>
```
Point the second argument at a round folder. Each request lives in its own
subfolder whose name contains the request ID (e.g. `אור יהודה 105334\`). The
script walks the tree, so intermediate folders (like `בקשות לבדיקה`) are fine.

### File selection per request
When a request folder has several Excel files, the script picks one in this order:
1. A file marked `בדיקה` (the reviewed/working version)
2. Otherwise the highest numeric version (e.g. `2.0` beats `1.0`)
3. Otherwise the most recently modified
Temp files (`~$...`) and non-grant-form files are skipped automatically. Every
choice is logged in `capex_file_selection.csv` so it can be audited.

### Output (written into the round folder)
| File | What it contains |
|---|---|
| `capex_lineitems.csv` | Every extracted line item, with a *suggested* technology tag and core-equipment flag (both hints only), plus the source file each row came from |

That is the only file produced. Coverage (how many requests matched a file) and
any extraction warnings are printed to the console, not saved.

### Why no averages file
The classifier only guesses, and many extracted rows are irrelevant (piping,
controls, infrastructure). Rather than auto-average and bake in wrong tags, the
pipeline hands you one CSV to review:
1. Open `capex_lineitems.csv` in Excel.
2. Filter/sort on `suggested_technology` and `component`; delete junk rows, fix any wrong tags.
3. Total the survivors with `AVERAGEIF` per technology — those are the model numbers.

### 4 model technologies and their source categories
| Model technology | Category (col F in CSV) |
|---|---|
| משאבות חום | חימום מים |
| צ'ילרים | אקלום מבנים |
| מדחסי VSD | מדחסים |
| מערכות קיטור חשמליות | הסבה (rows tagged "...לחשמל" only) |

### Testing on one round
Point the script at a single round folder (e.g. `...\בקשות לבדיקה` for 2017). The category CSV filter applies regardless of which round.

### First two things to check after running
1. The console "Matched X / unmatched Y" line — a low match rate means the IDs in the table don't line up with the folder names. Unmatched requests from other rounds are expected.
2. The `source_file` column in `capex_lineitems.csv` — spot-check that the file pulled per request is the right one (the latest/reviewed version), not an older draft.

### What this does NOT cover
- `CapEx — ציוד קיים (בסיסי)` (model row 30): grant files only have the efficient equipment cost. Baseline needs Rafi's data.
- OPEX rows (35-42): separate data source needed.
