# Energy Efficiency Program Project

**Description:** Excel analysis and documentation for Israel's national energy efficiency program funding and policy recommendations.

**Client:** Ministry of Energy (via EcoTraders)  
**Status:** COMPLETE: closed out 2026-08-19, Omri's last working day  
**Manager:** Daniel

**Key Dates:**
- **Original deadline:** June 30, 2026 (slipped)
- Daniel confirmed 2026-07-26: no new assignments before Omri's Aug 22 last day at EcoTraders: scope fixed to the items below, later amended with 2 model documentation files (2026-08-16).
- **All deliverables shipped by 2026-08-19.** See `tracker.md` for the final status table and the list of limitations left unresolved at handoff.

**Deliverables (all complete):**
- Grants program chapter: sent to client 2026-07-12
- Loan fund position paper: sent to client 2026-07-12; appendix version done 2026-08-03
- Loan fund chapter (full): trimmed from ~6 pages toward ~3 and finished 2026-08-19
- Tax incentive model, including the market analysis: submitted to Daniel 2026-08-17
- Tax incentive chapter for the national program: submitted to Daniel 2026-08-17
- Tax model documentation: `tax-model-documentation.docx`, 2026-08-17
- Grants model documentation: built on the company account, confirmed 2026-08-19

**Final status table and unresolved limitations:** see `tracker.md`.

**Historical handoff briefings** (both deliverables now done, kept for the record): `work-handoff.md` (grants model documentation), `loan-fund-work-handoff.md` and `2026-08-19-final-day-prompt.md` (loan fund chapter trim). These were pasted into the company-account Claude session, which couldn't see this repo.

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
3. Total the survivors with `AVERAGEIF` per technology: those are the model numbers.

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
1. The console "Matched X / unmatched Y" line: a low match rate means the IDs in the table don't line up with the folder names. Unmatched requests from other rounds are expected.
2. The `source_file` column in `capex_lineitems.csv`: spot-check that the file pulled per request is the right one (the latest/reviewed version), not an older draft.

### What this does NOT cover
- The baseline-CapEx row in the model, `CapEx` / `ציוד קיים (בסיסי)` (row 30): grant files only have the efficient equipment cost. Baseline needs Rafi's data.
- OPEX rows (35-42): separate data source needed.
