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
python capex_pipeline.py <path_to_category_csv> <path_to_grant_files_folder>
```

### Outputs (written into the grant files folder)
| File | What it contains |
|---|---|
| `capex_lineitems.csv` | Every line item, with technology tag and core/support flag |
| `capex_by_request.csv` | Per request per technology: core equipment cost + full site total |
| `capex_averages.csv` | Average, median, min, max per technology — feeds the model |
| `capex_coverage.txt` | ID match coverage and sum-validation warnings |

### 4 model technologies and their source categories
| Model technology | Category (col F in CSV) |
|---|---|
| משאבות חום | חימום מים |
| צ'ילרים | אקלום מבנים |
| מדחסי VSD | מדחסים |
| מערכות קיטור חשמליות | הסבה (rows tagged "...לחשמל" only) |

### Testing on one round
Point the script at a subfolder containing only that round's files. The category CSV filter applies regardless.

### First thing to check after running
Open `capex_coverage.txt`. If many IDs are unmatched, the request ID may not appear in the filename — let Claude know and we'll switch to matching on ח.פ (read from inside each file).

### What this does NOT cover
- `CapEx — ציוד קיים (בסיסי)` (model row 30): grant files only have the efficient equipment cost. Baseline needs Rafi's data.
- OPEX rows (35-42): separate data source needed.
