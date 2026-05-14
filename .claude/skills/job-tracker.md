# Job Opportunity Tracker Skill

## What This Does

The `/job-tracker` slash command runs a daily automated job search pipeline:

1. **Research** — For each area of interest in `projects/job-search/preferences.md`, run a research pass through the research agent to gather market intelligence (trending companies, valued skills, market signals)
2. **Search** — Use that research to inform targeted searches on LinkedIn and company career pages
3. **Score** — For each job found, generate a fit summary based on Omri's profile and the job's requirements
4. **Generate** — Create tailored application answers for common screening questions, customized to this specific role
5. **Log** — Append all new jobs to the tracker; update statuses based on what Omri applied to
6. **Report** — Save a timestamped report to `research/job-market/` and print a summary

## Usage

### Manual Run
```
/job-tracker
```
Runs once immediately. Useful for testing or running on-demand.

### Automated Daily
```
/loop 24h /job-tracker
```
Runs automatically every 24 hours. Stop with Ctrl+C.

---

## Implementation Notes

### Files Used
- **Read:** 
  - `projects/job-search/preferences.md` (areas of interest, target roles, companies, salary range, skills)
  - `context/me.md` (Omri's profile for fit scoring and answer generation)
  - `projects/job-search/tracker.md` (existing jobs to avoid duplicates)

- **Write:**
  - `research/job-market/YYYYMMDD_job-tracker.md` (main report)
  - `research/job-market/YYYYMMDD_[area].md` (research on each area of interest)
  - `projects/job-search/tracker.md` (update status for new jobs)

### Flow

1. **Read preferences.md** → Extract areas of interest
2. **For each area:**
   - Call research agent (delegated sub-task) to gather market intelligence on this area
   - Save research output to `research/job-market/YYYYMMDD_[area].md`
3. **Synthesize research** → Extract: trending companies, valued keywords, market trends, hiring signals
4. **Search LinkedIn:**
   - For each role in preferences, run WebSearch: `site:linkedin.com/jobs [role] [location] [keywords from research]`
   - Dedup results
5. **Search company pages:**
   - WebFetch targeted company career pages listed in preferences + surfaced by research
6. **Dedup:**
   - Skip any job URL already in `tracker.md` (by exact URL match)
7. **For each new job found:**
   - Extract: title, company, location, posted date, key requirements, link
   - Generate fit summary: score (High/Medium/Low) + 2-3 sentence explanation tied to Omri's profile and research
   - Generate tailored application answers:
     - "Why are you interested in this role?" (use Omri's motivation + job context)
     - "Describe your relevant experience" (use Omri's background + job requirements)
     - "What are your salary expectations?" (use salary range from preferences)
     - Any other common screening questions for this role/industry
8. **Compile report:**
   - Save timestamped report to `research/job-market/YYYYMMDD_job-tracker.md`
   - Format: job title, company, location, link, fit summary, tailored answers
9. **Update tracker:**
   - Append all new jobs to `projects/job-search/tracker.md` with status: "Found"
10. **Ask for feedback:**
    - "Did you apply to any of these? Reply with job numbers (e.g., '1, 3') or 'none'."
    - Parse response
    - Update statuses in tracker to "Applied" for selected jobs
11. **Print summary:**
    - X new jobs found
    - Y total jobs tracked
    - Z applied in this session
    - Top 3 recommendations

---

## Example Output

```
# Job Report — 2026-05-14
**5 new jobs found | 12 total tracked | 2 applied this session**

---

## 1. Data Analyst — Playtika
Location: Herzliya, Israel
Link: https://linkedin.com/jobs/view/12345
Fit: High | Why: Playtika is a top gaming studio hiring analysts (per market research), role emphasizes Python + data visualization which align with your background and growth interests.

**Application answers (tailored to this role):**
- **Why are you interested in this role?** → "I'm interested in Playtika because you're a leading global gaming studio with strong analytical infrastructure. Data analyst roles here offer the chance to directly impact player experience and business metrics at scale — exactly the high-velocity analytics environment I'm looking for to grow my skills."
- **Describe your relevant experience:** → "I've built Excel-based analyses for policy impact assessment at EcoTraders, working with large datasets and translating findings into recommendations for decision-makers. This analytical foundation, combined with my Python knowledge, positions me well to move into data-driven product analytics."
- **What are your salary expectations?** → "For a junior data analyst role, I'm looking at a range of 18,000-22,000 ILS/month, depending on role scope and growth potential."

---

## 2. Business Analyst — Scopely
...

---

Did you apply to any of these? Reply with job numbers (e.g., "1, 3") or "none".
```

---

## Preferences Format

The skill reads `projects/job-search/preferences.md` which is user-editable. Structure:
- **Areas of Interest** — Topics to research; drives both research and search queries
- **Target Roles** — Job titles to search for
- **Industries** — Sectors to focus on
- **Location** — Geographic constraints
- **Skills to highlight** — Used in fit summaries and answer generation
- **Companies of interest** — Specific targets for WebFetch

---

## Error Handling

- If `preferences.md` is missing → Print error and stop
- If research agent fails → Skip that area, continue with others
- If no jobs found in a search → Still print report (0 jobs found section)
- If tracker.md is malformed → Append jobs anyway (don't overwrite)

---

## Rate Limiting

- WebSearch: ~5 searches per run (1 per area of interest + role-based searches)
- WebFetch: ~10 fetches per run (company career pages)
- Research agent calls: 1 per area of interest per run

Space these out to avoid hitting API limits.

---

## Future Enhancements

- Filter jobs by salary range (read from preferences, auto-reject outliers)
- Integration with email: send daily digest to omrisham53@gmail.com
- Resume parsing: auto-extract relevant accomplishments for answer generation
- Application tracking: click-through links that open application form + pre-fill answers
