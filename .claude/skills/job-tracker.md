---
name: job-tracker
description: Run a job search pipeline for Omri's data analyst job search. Trigger when the user says /job-tracker, "run job tracker", "find new jobs", "search for jobs", or "run a job search". Searches LinkedIn and company career pages, filters for junior roles only, scores fit, and updates the tracker.
---

# Job Tracker

Runs a targeted job search pipeline and updates the tracker with new findings.

## Files

- **Read:** `projects/job-search/preferences.md` — all search criteria, target companies, exclusions
- **Read:** `projects/job-search/tracker.md` — active applications (avoid duplicates)
- **Read:** `projects/job-search/tracker-archive.md` — previously found jobs (avoid duplicates)
- **Write:** `projects/job-search/tracker-archive.md` — append new Found jobs here
- **Write:** `research/job-market/YYYYMMDD_job-tracker.md` — full timestamped report

## Flow

### 1. Read preferences
Load `preferences.md`. Extract: target roles, sectors, locations, excluded companies, companies of interest.

### 2. Search for jobs
Run WebSearch queries targeting LinkedIn and company career pages directly. Do not delegate to a sub-agent — run searches inline.

Good search patterns:
- `site:il.linkedin.com/jobs "junior" OR "entry level" [role] [company or sector] Israel`
- `site:il.linkedin.com/jobs "[company name]" analyst`
- `[company] careers data analyst Tel Aviv 2026`

Search the high-priority companies list directly. Run 6-8 searches covering different sectors.

### 3. Filter hard
Before scoring anything, drop any job that:
- Requires 3+ years experience
- Is located in an excluded city (Petah Tikva, Beer Sheva, Haifa, etc.)
- Is at an excluded company (Playtika, Wix, monday.com, MoonActive)
- Is senior, lead, or staff level
- Is part-time or freelance only
- Is in an excluded sector (FinTech, HealthTech, Defense, B2G)

### 4. Deduplicate
Skip any job whose URL already appears in `tracker.md` or `tracker-archive.md`.

### 5. Score each job
For each job that passes filtering, generate:
- **Fit:** High / Medium / Low
- **Reason:** 1-2 sentences tied to Omri's profile (economics student, policy analyst background, analytical skills, target sector)

### 6. Update tracker-archive.md
Append new jobs as Found rows. Do NOT add to the main `tracker.md` — that's only for jobs Omri actively pursues.

Format:
```
| [date] | [title] | [company] | [location] | [link] | [fit] | [1-line reason] |
```

### 7. Print summary
Show a clean list of new jobs found:
- Title, Company, Location, Link, Fit score, Reason
- Group by sector

Then ask: "Did you apply to any of these, or want to move any to the active tracker?"

### 8. Save report
Write full results to `research/job-market/YYYYMMDD_job-tracker.md`.

---

## Quality bar

- Every job must have a direct link (LinkedIn URL or careers page URL)
- Junior/entry-level only — when in doubt, skip it
- If a role doesn't have a clear link, note it but don't add it to the tracker
