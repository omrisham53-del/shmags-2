# Job Tracker Skill

## How to Use

### Run the Job Tracker Framework

The Python script validates your setup and shows what would happen:

```bash
python "./.claude/skills/job-tracker.py"
```

**Output:**
- Confirms all config files exist
- Lists areas of interest to research
- Shows the full 5-phase workflow
- Displays example output format
- Validates paths

---

## Full Automation (Next Phase)

The current framework (`job-tracker.py`) needs the following to be fully automated:

### Phase 1: Research Integration
Add code to call the research agent for each area of interest:
```python
# For each area in preferences:
#   Call research agent → gather market intelligence
#   Save to research/job-market/[area].md
```

### Phase 2: Job Search
Integrate web search for LinkedIn job listings:
```python
# For each role + industry combination:
#   WebSearch: site:linkedin.com/jobs [role] [location]
#   Parse results, extract job URLs, titles, requirements
```

### Phase 3: Fit Scoring & Answer Generation
Call Claude API to generate tailored content:
```python
# For each job found:
#   Generate fit summary (use Omri's profile + job requirements)
#   Generate 5 tailored application answers (customized to this job)
```

### Phase 4: Tracker Updates
Update the application log:
```python
# Append new jobs to projects/job-search/tracker.md
# Update statuses based on user feedback
```

### Phase 5: Report Generation
Save the complete report:
```python
# Save to research/job-market/YYYYMMDD_job-tracker.md
# Print terminal summary
```

---

## Current Test Results

**What Works:**
- Configuration file validation
- Area of interest extraction (3 areas identified)
- Company list parsing (10 companies)
- File path verification
- Workflow mapping

**Test Output Location:**
- Test report: `research/job-market/20260513_job-tracker-test.md`
- Research sample: `research/job-market/20260513_israeli-gaming-data-analyst-market.md`
- Tracker log: `projects/job-search/tracker.md`

---

## Dependencies

To complete Phase 1-5, you'll need:

1. **Anthropic SDK** (for Claude API calls)
   ```bash
   pip install anthropic
   ```

2. **Web Scraping** (for LinkedIn parsing)
   - Option A: Use WebSearch through Claude's interface
   - Option B: BeautifulSoup + requests library

3. **API Key Management**
   - Add `ANTHROPIC_API_KEY` to environment variables
   - Or store in `.env` file (gitignored)

---

## How the Loop Skill Would Work

Once fully implemented:

```bash
/loop 24h /job-tracker
```

This would:
- Run the script every 24 hours
- Research your areas of interest
- Search for new job postings
- Generate a report with tailored answers
- Ask: "Which jobs did you apply to?"
- Update your tracker automatically

---

## Files & Locations

| File | Purpose |
|------|---------|
| `.claude/skills/job-tracker.py` | Main automation script |
| `projects/job-search/preferences.md` | Your config (areas, roles, companies, skills) |
| `projects/job-search/tracker.md` | Application log (auto-updated) |
| `research/job-market/` | Output reports (timestamped) |
| `context/me.md` | Your profile (used for fit scoring) |

---

## Next Steps

1. Review the current script output
2. Review test reports in `research/job-market/`
3. Refine preferences.md if needed
4. Once Phase 1-5 are implemented, the skill will be fully autonomous

---

## Manual Workflow (Until Fully Automated)

For now, you can manually run the research + job search pipeline:

1. **Run research manually:**
   - Ask the research agent to investigate your areas of interest
   - Save findings to `research/job-market/`

2. **Search LinkedIn manually:**
   - Use LinkedIn job search for your roles + companies
   - Copy job links into a document

3. **Generate answers manually:**
   - Use Claude to tailor answers for each job
   - Copy tailored answers into a template

4. **Update tracker manually:**
   - Add new jobs to `tracker.md`
   - Update status column as you apply

See test report for example output format.
