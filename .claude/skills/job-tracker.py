#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Job Opportunity Tracker - Full Automation Implementation
Daily job search, research, and opportunity tracking with tailored application answers.
Runs daily via /loop 24h or manually via python job-tracker.py
"""

import os
import sys
import re
import json
import time
import urllib.parse
import urllib3
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# Fix encoding for Windows terminals
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Suppress SSL warnings (required for this machine's cert intercept)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============================================================================
# FILE I/O FUNCTIONS (existing - reused as-is)
# ============================================================================

def read_file(path: str) -> str:
    """Read a markdown file"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
        exit(1)

def write_file(path: str, content: str):
    """Write content to file"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(path: str, content: str):
    """Append content to file"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)

# ============================================================================
# PARSER FUNCTIONS (existing - keep and enhance)
# ============================================================================

def extract_areas_of_interest(preferences: str) -> List[str]:
    """Extract areas of interest from preferences.md"""
    areas = re.findall(r'### Area \d+: ([^\n]+)', preferences)
    return areas

def extract_companies(preferences: str) -> List[str]:
    """Extract companies of interest from preferences"""
    companies = []
    match = re.search(r'### Gaming Studios(.*?)### Tech & Analytics', preferences, re.DOTALL)
    if match:
        section = match.group(1)
        companies.extend([line.strip('- ').strip() for line in section.split('\n')
                         if line.strip().startswith('-') and line.strip() != '-'])
    match = re.search(r'### Tech & Analytics(.*?)### Government', preferences, re.DOTALL)
    if match:
        section = match.group(1)
        companies.extend([line.strip('- ').strip() for line in section.split('\n')
                         if line.strip().startswith('-') and line.strip() != '-'])
    return companies

# ============================================================================
# NEW HELPER FUNCTIONS
# ============================================================================

def slugify(text: str) -> str:
    """Convert text to URL-safe slug"""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")

def normalize_linkedin_url(url: str) -> str:
    """Get canonical LinkedIn URL for deduplication"""
    match = re.search(r"jobs/view/.*?(\d{10,})", url)
    if match:
        return f"https://www.linkedin.com/jobs/view/{match.group(1)}"
    match2 = re.search(r"currentJobId=(\d+)", url)
    if match2:
        return f"https://www.linkedin.com/jobs/view/{match2.group(1)}"
    return url

def extract_json(text: str) -> dict:
    """Safely extract JSON from LLM response"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{[^{}]+\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        raise

# ============================================================================
# FIXED PARSER FUNCTIONS
# ============================================================================

def extract_target_roles_fixed(preferences: str) -> List[str]:
    """Extract target roles - handles numbered list format (1. Role)"""
    match = re.search(r'### Roles \(ordered by interest\)(.*?)###', preferences, re.DOTALL)
    if match:
        roles_text = match.group(1)
        roles = []
        for line in roles_text.split('\n'):
            line = line.strip()
            # Handle both '- Role' and '1. Role' formats
            m = re.match(r'^(?:\d+\.|[-*])\s+(.+)', line)
            if m:
                roles.append(m.group(1).strip())
        return roles
    return []

def extract_location(preferences: str) -> str:
    """Extract primary search location from preferences"""
    m = re.search(r'- Primary: ([^\n(]+)', preferences)
    return m.group(1).strip() if m else "Israel"

def extract_salary_range(preferences: str) -> str:
    """Extract salary range for answer generation"""
    m = re.search(r'- Acceptable: ([^\n]+)', preferences)
    return m.group(1).strip() if m else "14,000-22,000 ILS/month"

def extract_existing_job_urls(tracker: str) -> set:
    """Extract existing job URLs from tracker to avoid duplicates"""
    urls = set(re.findall(r'\]\((https?[^\)]+)\)', tracker))
    return urls

def count_tracker_jobs(tracker: str) -> int:
    """Fixed: count actual data rows in tracker"""
    lines = tracker.split('\n')
    count = 0
    for line in lines:
        if (line.startswith('| ') and 'Date Found' not in line
                and '---' not in line and len(line.strip()) > 5):
            count += 1
    return count

# ============================================================================
# PROMPT BUILDERS (existing - reused as-is)
# ============================================================================

def prepare_research_prompt(area: str, preferences: str) -> str:
    """Prepare research prompt for market intelligence gathering"""
    return f"""Research the job market for: {area}

Based on this area of interest, gather market intelligence:
- Key companies hiring in this area
- What skills do they value?
- Typical salary ranges
- Market trends - is this area growing?
- Current hiring activity (May 2026)

Context: This is for Omri Shamgar, an economics/policy student transitioning into data analytics. Use Israeli market data where relevant.

Provide findings in a structured format: Key Companies, Skills Valued, Salary Ranges, Market Trends, Current Hiring Activity."""

def prepare_application_answers_prompt(job_title: str, company: str,
                                       job_description: str, profile: str) -> str:
    """Prepare prompt for generating tailored application answers"""
    return f"""Generate tailored application answers for this job posting:

Job: {job_title} at {company}
Key Requirements: {job_description[:300]}

Candidate Profile: {profile[:400]}

Generate answers to these common screening questions (2-3 sentences each, be specific and personalized):
1. "Why are you interested in this role?"
2. "Describe your most relevant experience."
3. "What are your salary expectations?"
4. "What's your timeline to start?"
5. "Experience with our tech stack?" (if applicable)

Make each answer specific to this job and candidate - not generic."""

# ============================================================================
# LLM CLIENT SETUP
# ============================================================================

def setup_llm_client():
    """
    Setup LLM client with Anthropic primary, Groq fallback.
    Both are patched for Windows SSL cert intercept.
    Returns call_llm(prompt, system, max_tokens) -> str or None
    """
    from dotenv import load_dotenv
    load_dotenv()

    import httpx
    _http = httpx.Client(verify=False)  # SSL cert workaround

    anthropic_key = os.getenv('ANTHROPIC_API_KEY', '')
    groq_key = os.getenv('GROQ_API_KEY', '')

    if anthropic_key:
        import anthropic
        client = anthropic.Anthropic(api_key=anthropic_key, http_client=_http)

        def call_llm(prompt: str, system: str = '', max_tokens: int = 800) -> str:
            messages = [{"role": "user", "content": prompt}]
            kwargs = {
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": max_tokens,
                "messages": messages
            }
            if system:
                kwargs["system"] = system
            resp = client.messages.create(**kwargs)
            return resp.content[0].text

        print("[OK] Using Anthropic Claude (claude-haiku-4-5-20251001)")
        return call_llm

    elif groq_key:
        from groq import Groq
        client = Groq(api_key=groq_key, http_client=_http)

        def call_llm(prompt: str, system: str = '', max_tokens: int = 800) -> str:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})
            resp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.3
            )
            return resp.choices[0].message.content

        print("[OK] Using Groq fallback (llama-3.3-70b-versatile)")
        return call_llm

    else:
        print("[WARN] No LLM API key found. Research and fit scoring will be skipped.")
        print("[SETUP] Add to .env: ANTHROPIC_API_KEY=sk-ant-... (from console.anthropic.com)")
        return None

# ============================================================================
# JOB SEARCH FUNCTIONS
# ============================================================================

def search_linkedin_jobs(role: str, location: str = "Israel",
                          days_back: int = 7) -> List[Dict]:
    """
    Scrape LinkedIn job listings for a role+location.
    Returns list of dicts with: title, company, location, url, normalized_url, date_found
    """
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    tpr_map = {1: "r86400", 7: "r604800", 30: "r2592000"}
    params = {
        "keywords": role,
        "location": location,
        "f_TPR": tpr_map.get(days_back, "r604800"),
        "f_E": "2,3",
    }
    url = "https://www.linkedin.com/jobs/search/?" + urllib.parse.urlencode(params)

    try:
        resp = requests.get(url, headers=headers, timeout=15, verify=False)
        resp.raise_for_status()
    except Exception as e:
        print(f"    [WARN] LinkedIn search failed for '{role}': {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    cards = soup.find_all("div", class_="base-card")

    jobs = []
    for card in cards:
        title_el = card.find("h3", class_="base-search-card__title")
        company_el = card.find("h4", class_="base-search-card__subtitle")
        location_el = card.find("span", class_="job-search-card__location")
        link_el = card.find("a", class_="base-card__full-link")
        date_el = card.find("time")

        if not (title_el and link_el):
            continue

        raw_url = link_el.get("href", "")
        jobs.append({
            "title": title_el.text.strip(),
            "company": company_el.text.strip() if company_el else "Unknown",
            "location": location_el.text.strip() if location_el else location,
            "url": raw_url.split("?")[0],
            "normalized_url": normalize_linkedin_url(raw_url),
            "date_found": (date_el.get("datetime", "") if date_el
                          else datetime.now().strftime("%Y-%m-%d")),
        })

    return jobs

def fetch_job_description(job_url: str) -> str:
    """Fetch job description from LinkedIn job detail page"""
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
    }

    try:
        time.sleep(1.5)  # Rate limiting
        resp = requests.get(job_url, headers=headers, timeout=15, verify=False)
        soup = BeautifulSoup(resp.text, "html.parser")
        desc_el = soup.find("div", class_="show-more-less-html__markup")
        if desc_el:
            return desc_el.get_text(separator="\n").strip()[:2000]
        return ""
    except Exception:
        return ""

# ============================================================================
# PIPELINE FUNCTIONS
# ============================================================================

def run_research_phase(areas: List[str], preferences: str, call_llm,
                       research_dir: Path, timestamp: str) -> Dict[str, str]:
    """Run market research for each area of interest"""
    research = {}
    for area in areas:
        print(f"  [*] Researching: {area}...")
        prompt = prepare_research_prompt(area, preferences)
        try:
            text = call_llm(prompt, max_tokens=800)
            research[area] = text
            slug = slugify(area)
            out_path = research_dir / f"{timestamp}_{slug}.md"
            write_file(str(out_path), f"# Market Research: {area}\n\n{text}\n")
            print(f"    [OK] Saved: {out_path.name}")
        except Exception as e:
            print(f"    [WARN] Research failed for '{area}': {e}")
            research[area] = ""
    return research

def score_job_fit(job: Dict, profile: str, call_llm) -> Tuple[str, str]:
    """Score job fit as High/Medium/Low"""
    prompt = f"""Score this job fit. Return ONLY valid JSON, nothing else.

Job: {job['title']} at {job['company']} ({job['location']})
Description: {job.get('description', '')[:400]}

Candidate: {profile[:500]}

JSON format: {{"fit": "High", "reason": "2 sentence explanation"}}
fit must be exactly one of: High, Medium, Low"""

    try:
        text = call_llm(prompt, max_tokens=250)
        data = extract_json(text)
        return data.get("fit", "Unknown"), data.get("reason", "")
    except Exception as e:
        print(f"    [WARN] Fit scoring failed: {e}")
        return "Unknown", ""

def generate_answers(job: Dict, profile: str, call_llm) -> str:
    """Generate 5 tailored application answers"""
    prompt = prepare_application_answers_prompt(
        job["title"], job["company"],
        job.get("description", "Not available"), profile
    )
    try:
        return call_llm(prompt, max_tokens=1000)
    except Exception as e:
        print(f"    [WARN] Answer generation failed: {e}")
        return "(Answer generation failed)"

def append_jobs_to_tracker(tracker_path: Path, new_jobs: List[Dict], today: str) -> str:
    """Append new job rows to tracker.md"""
    tracker = read_file(str(tracker_path))
    lines = tracker.split("\n")

    # Find last data row
    last_row = -1
    for i, line in enumerate(lines):
        if (line.startswith("| ") and "Date Found" not in line
                and "---" not in line and len(line) > 5):
            last_row = i

    insert_at = last_row + 1 if last_row >= 0 else len(lines)

    # Add new rows
    new_rows = []
    for job in new_jobs:
        notes = job.get("fit_reason", "").replace("|", "-")[:80]
        row = (f"| {today} | {job['title']} | {job['company']} | "
               f"{job['location']} | [LinkedIn]({job['url']}) | "
               f"{job.get('fit', 'Unknown')} | Found | {notes} |")
        new_rows.append(row)

    for i, row in enumerate(new_rows):
        lines.insert(insert_at + i, row)

    # Update summary counts
    total = count_tracker_jobs("\n".join(lines))
    result = "\n".join(lines)
    result = re.sub(r"(- Total jobs found: )\d+", rf"\g<1>{total}", result)
    write_file(str(tracker_path), result)
    return result

def update_applied_statuses(tracker_path: Path, applied_jobs: List[Dict]):
    """Update status from Found to Applied for selected jobs"""
    tracker = read_file(str(tracker_path))
    lines = tracker.split("\n")

    for job in applied_jobs:
        url = job["url"]
        for i, line in enumerate(lines):
            if url in line and "| Found |" in line:
                lines[i] = line.replace("| Found |", "| Applied |")

    result = "\n".join(lines)
    applied_count = sum(1 for l in lines if "| Applied |" in l)
    result = re.sub(r"(- Applied: )\d+", rf"\g<1>{applied_count}", result)
    write_file(str(tracker_path), result)

def generate_report(new_jobs: List[Dict], total_tracked: int, applied_count: int,
                   research: Dict[str, str], report_path: Path, today: str):
    """Save timestamped job tracker report"""
    lines = [
        f"# Job Tracker Report - {today}",
        f"**{len(new_jobs)} new jobs found | {total_tracked} total tracked | {applied_count} applied**",
        "", "---", "",
    ]

    if research:
        lines.append("## Market Research Summaries\n")
        for area, text in research.items():
            lines.append(f"### {area}\n{text[:600]}\n")
        lines.append("---\n")

    lines.append("## New Jobs Found\n")
    for i, job in enumerate(new_jobs, 1):
        lines += [
            f"## {i}. {job['title']} - {job['company']}",
            f"Location: {job['location']}",
            f"Link: [View on LinkedIn]({job['url']})",
            f"Date Posted: {job.get('date_found', 'Unknown')}",
            f"Fit: {job.get('fit', 'Unknown')} - {job.get('fit_reason', '')}",
            "",
            "**Application Answers:**",
            job.get("answers", "(Not generated)"),
            "", "---", "",
        ]

    write_file(str(report_path), "\n".join(lines))
    print(f"  [OK] Report saved: {report_path.name}")

def parse_apply_response(response: str, total_jobs: int) -> List[int]:
    """Parse user response to extract applied job numbers"""
    response = response.strip().lower()

    if response == "none" or response == "":
        return []

    indices = []
    for part in response.split(','):
        try:
            num = int(part.strip())
            if 1 <= num <= total_jobs:
                indices.append(num - 1)  # Convert to 0-indexed
        except ValueError:
            pass

    return indices

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Full job tracker workflow"""

    # Paths
    project_root = Path(__file__).parent.parent.parent
    prefs_path   = project_root / "projects" / "job-search" / "preferences.md"
    tracker_path = project_root / "projects" / "job-search" / "tracker.md"
    me_path      = project_root / "context" / "me.md"
    research_dir = project_root / "research" / "job-market"
    os.makedirs(research_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d")
    today = datetime.now().strftime("%Y-%m-%d")

    print("\n" + "=" * 70)
    print(" JOB OPPORTUNITY TRACKER")
    print("=" * 70)

    # STEP 1: Read files
    print("\n[1/7] Reading configuration files...")
    preferences = read_file(str(prefs_path))
    tracker = read_file(str(tracker_path))
    profile = read_file(str(me_path))

    areas = extract_areas_of_interest(preferences)
    roles = extract_target_roles_fixed(preferences)
    companies = extract_companies(preferences)
    existing_urls = extract_existing_job_urls(tracker)
    existing_normalized = {normalize_linkedin_url(u) for u in existing_urls}
    initial_count = count_tracker_jobs(tracker)
    location = extract_location(preferences)

    print(f"  [OK] {len(areas)} areas | {len(roles)} roles | "
          f"{len(companies)} companies | {initial_count} jobs tracked")

    # STEP 2: LLM setup
    print("\n[2/7] Setting up LLM client...")
    call_llm = setup_llm_client()

    # STEP 3: Research
    print("\n[3/7] Running market research...")
    research = {}
    if call_llm:
        research = run_research_phase(areas, preferences, call_llm, research_dir, timestamp)
    else:
        print("  [SKIP] No LLM available")

    # STEP 4: Job search
    print("\n[4/7] Searching LinkedIn for new jobs...")
    all_found: List[Dict] = []
    seen_normalized = set(existing_normalized)

    for role in roles:
        print(f"  [*] Searching: {role} in {location}...")
        time.sleep(1.5)
        results = search_linkedin_jobs(role, location="Israel", days_back=7)
        new_count = 0

        for job in results:
            if job["normalized_url"] not in seen_normalized:
                seen_normalized.add(job["normalized_url"])
                all_found.append(job)
                new_count += 1

        print(f"    [OK] Found {len(results)} results, {new_count} new")

    print(f"\n  Total new jobs (pre-description fetch): {len(all_found)}")

    # Cap at 10 jobs per run
    all_found = all_found[:10]

    # STEP 5: Fetch descriptions + score + generate answers
    print("\n[5/7] Fetching descriptions and scoring fit...")
    for i, job in enumerate(all_found, 1):
        print(f"  [{i}/{len(all_found)}] {job['title']} at {job['company']}")

        description = fetch_job_description(job["url"])
        job["description"] = description

        if call_llm:
            fit, reason = score_job_fit(job, profile, call_llm)
            job["fit"] = fit
            job["fit_reason"] = reason
            print(f"    Fit: {fit}")

            if fit in ("High", "Medium", "Unknown"):
                answers = generate_answers(job, profile, call_llm)
                job["answers"] = answers
            else:
                job["answers"] = "(Low fit - answers skipped)"
        else:
            job["fit"] = "Unknown"
            job["fit_reason"] = ""
            job["answers"] = "(No LLM available)"

    # STEP 6: Save report
    print("\n[6/7] Saving report...")
    report_path = research_dir / f"{timestamp}_job-tracker.md"
    generate_report(all_found, initial_count + len(all_found), 0, research, report_path, today)

    # STEP 7: Update tracker
    print("\n[7/7] Updating tracker...")
    if all_found:
        tracker = append_jobs_to_tracker(tracker_path, all_found, today)
        print(f"  [OK] Added {len(all_found)} jobs to tracker.md")
    else:
        print("  [OK] No new jobs found - tracker unchanged")

    # Print summary
    print("\n" + "=" * 70)
    print(f" NEW JOBS FOUND: {len(all_found)}")
    print("=" * 70)

    for i, job in enumerate(all_found, 1):
        fit_str = f"[{job.get('fit', '?')}]"
        print(f"  {i}. {fit_str:10} {job['title']} - {job['company']}")
        print(f"           {job['url'][:70]}")

    # Interactive apply prompt
    if all_found:
        print("\n" + "-" * 70)
        print("Did you apply to any of these? Enter job numbers (e.g. 1,3) or 'none':")
        try:
            response = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            response = "none"

        applied_indices = parse_apply_response(response, len(all_found))
        applied_jobs = [all_found[i] for i in applied_indices]

        if applied_jobs:
            update_applied_statuses(tracker_path, applied_jobs)
            print(f"  [OK] Marked {len(applied_jobs)} job(s) as Applied")
    else:
        applied_jobs = []

    # Final summary
    final_count = count_tracker_jobs(read_file(str(tracker_path)))
    print("\n" + "=" * 70)
    print(" SUMMARY")
    print("=" * 70)
    print(f"  New jobs found:    {len(all_found)}")
    print(f"  Total tracked:     {final_count}")
    print(f"  Applied (session): {len(applied_jobs)}")
    print(f"  Report saved:      research/job-market/{report_path.name}")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
