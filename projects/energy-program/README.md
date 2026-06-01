# Energy Efficiency Program Project

**Description:** Excel analysis and documentation for Israel's national energy efficiency program funding and policy recommendations.

**Client:** Ministry of Energy (via EcoTraders)  
**Status:** Active  
**Manager:** Daniel

**Key Dates:**
- **Deadline:** June 30, 2026

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

### Outputs (written into the round folder)
| File | What it contains |
|---|---|
| `capex_lineitems.csv` | Every line item, with technology tag and core/support flag |
| `capex_by_request.csv` | Per request per technology: core equipment cost + full site total |
| `capex_averages.csv` | Average, median, min, max per technology — feeds the model |
| `capex_file_selection.csv` | Which file was chosen per request, and the rejected candidates |
| `capex_coverage.txt` | ID match coverage and sum-validation warnings |

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
1. `capex_coverage.txt` — how many request IDs matched a file. A low match rate means the IDs in the table don't line up with the folder names.
2. `capex_file_selection.csv` — spot-check that the chosen file per request is the right one (the latest/reviewed version), not an older draft.

### What this does NOT cover
- `CapEx — ציוד קיים (בסיסי)` (model row 30): grant files only have the efficient equipment cost. Baseline needs Rafi's data.
- OPEX rows (35-42): separate data source needed.
