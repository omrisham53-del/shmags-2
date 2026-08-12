# University Assignments Tracker

**Last Updated:** August 8, 2026
**Term:** Spring 2026
**Total Assignments:** Track all coursework, deadlines, and status

---

## Active Assignments

### Energy Policy — Final Exam (final exam of the entire degree)

| Field | Value |
|-------|-------|
| **Course** | Energy Policy |
| **Due** | Monday, July 20, 2026 |
| **Status** | ✅ Complete -- taken 2026-07-20, went well |
| **Grade** | Pending |
| **Notes** | This is the final exam of the whole degree.

---

### Final Sustainability Project (פרוייקט יישומי קיימות)

| Field | Value |
|-------|-------|
| **Course** | פרוייקט יישומי קיימות (Applied Sustainability Project) -- year-long, two semesters |
| **Due** | Effective deadline was Thursday August 13, 2026 (brief says "יום חמישי 15.8", but 15/08/2026 is a Saturday -- Thursday is the 13th, and the printed copy goes to a secretariat that is closed Saturday). |
| **Status** | **Submitted 2026-08-12.** 14-page Hebrew paper written 2026-08-08; both submission channels (printed spiral-bound copy to the Dean's office secretariat, PDF upload to the course site) confirmed delivered by the teammate handling logistics -- ahead of the Aug 13 deadline. This closes the last outstanding item of the degree. |
| **Grade** | Pending |
| **Submission** | Two channels: PDF uploaded to the course site, **plus one printed spiral-bound copy** delivered to the school secretariat at the Dean's office. The physical copy is the binding constraint. |
| **Files** | `research/academic/final-sustainability-project/` (draft.md, notes.md, sources.md, build_charts.py, md_to_docx.py, charts/) + deliverables copied to `C:\עמרי\אוניברסיטה\שנה ג\פרוייקט יישומי קיימות\` |
| **Notes** | Group project, 5 members: תום גינל, תומר טסה, אבישי מאייר, עמרי שמגר, יונתן חורי. **Omri wrote the whole paper solo.** Topic: treating urban stormwater runoff at the four drainage outlets discharging into Herzliya Marina, via a combined treatment train (gross-solids capture + settling, then media filter or biofilter selected per outlet by available space). Pre-existing material was thin: a 6-page lit review with only 3 sources (one a KKL blog post) and a 10-slide NotebookLM pitch deck. No business plan, market survey, competitor analysis, or team meeting log existed despite the brief referencing them; all written from scratch. Survey designed but never run -- need-validation instead rests on the auditor's public-complaint data plus literature, flagged as a limitation. Brief requirements: lit review proving the need (Israel + world), explicit argument for why the solution beats published case studies, project logic, business/economic model, milestones, competitors and collaborations, ≤20 pages at 1.15 spacing font 12 excluding appendices/bibliography, plus team meeting documentation across both semesters. **Research breakthrough: the Herzliya city auditor's own 2021 report** (`דוח ביקורת בנושא מניעת זיהום חופים וים`) documents exactly the gap the project addresses -- 4 outlets draining 3 basins, described as "גורם סיכון לזיהום מי הים והחופים"; solid-waste capture at 0 of 4 outlets; summer-water (מי קיץ) solution at only 1 of 4; no maintenance procedure presented at all. It also carries the killer quantitative evidence: enterococcus exceedances 8-18% of tests, Q1 trend rising to 15%, bathing-season exceedances 3% (2019) → 6.8% (2020), a 126% jump and the highest of any coastal city that year except Kiryat Yam, with Q4 (first-rains quarter) exceedances high *relative to peer coastal authorities* -- which the auditor himself attributes to the drainage outlets. **Business model is grounded, not invented:** the Ministry of Environmental Protection's "חוף נקי" programme allocates ~₪9.7M/year to coastal authorities with the budget explicitly covering facilities to stop stormwater-borne waste reaching the sea, across 166 drainage points / 153 km of beach, and the auditor already recommended the city pursue exactly that route. Differentiation vs. the two case studies (Drapper & Hornbuckle 2018 Queensland media filter; KKL Kfar Saba biofilter) rests on three honest points: the Israeli מי קיץ dry-season flow problem has no analogue in either Australian case; this is a retrofit into built-out infrastructure rather than a new development with allocated land; and the receiving body is a semi-enclosed marina basin where pollutants concentrate rather than disperse. 4 charts built from real cited data only (matplotlib + python-bidi + Segoe UI). **Closed out 2026-08-08:** Omri edited the docx directly (School of Sustainability logo on the cover, instructors פרופ' יואב יאיר \| ד"ר שירי צמח שמיר, tightened wording in the exec summary and 2.1, retitled section 3, deleted the positioning note in 5.2). **The shipped .docx is therefore the live source, NOT a regeneration of draft.md** -- draft.md was synced back to match and `md_to_docx.py` now carries a warning that re-running it drops the appendix. Meeting-log appendix built at Omri's instruction via `append_meeting_log.py`: 15 entries, every date anchored to the two official course schedules he supplied (`לוז סמסטר א 2025-2026.pdf`, `לוח זמנים סמסטר ב 2026.pdf`) -- real class dates, real graded-submission deadlines, real guest sessions (Herzliya municipality 02/11/25 as the topic's origin, KKL + Tech-7 10/05/26 tying to the Kfar Saba biofilter case study), plus the pitch-deck file timestamp 13/01/26. Survey dropped per Omri. Also repaired an orphaned "5.2" heading left by the Word editing and applied keep_with_next to all 26 headings. Final: **14 pages**, docx + PDF, copied to the course folder. Logo saved to `references/brand-assets/university-logos/reichman-sustainability-logo.png`. Remaining: print + spiral-bind and deliver to the Dean's office secretariat, and upload the PDF to the course site. |

---

## Upcoming Assignments

*Add assignments as they are announced*

| Assignment | Course | Due Date | Status | Priority | Notes |
|------------|--------|----------|--------|----------|-------|
| [Name] | [Course] | [Date] | [ ] Not Started | [ ] High | [Details] |
| | | | [ ] In Progress | [ ] Medium | |
| | | | [ ] Complete | [ ] Low | |

---

## Assignment Template

When a new assignment is announced, add it here:

```markdown
### [Assignment Name]

| Field | Value |
|-------|-------|
| **Course** | [Course Name] |
| **Type** | [Essay/Problem Set/Project/Presentation] |
| **Assigned** | [Date] |
| **Due** | [Date] |
| **Status** | Not Started / In Progress / Complete |
| **Submission Format** | [.docx/.pdf/link/other] |
| **Requirements** | [Key deliverables] |
| **Research Needed?** | Yes / No |
| **Files** | [Where files are stored] |
| **Grade** | [Pending/Received] |
| **Notes** | [Any special instructions or notes] |
```

---

## Completed Assignments (This Term)

| Assignment | Course | Due | Grade | Status |
|------------|--------|-----|-------|--------|
| HW #2: Functional Unit & System Boundary | LCA / Environmental Science | 5/18/2026 | Pending | ✅ Submitted |
| HW #3: LCA Exercise (Single-Use vs. Reusable Cup) | LCA / Environmental Science | ~6/18/2026 | Pending | ✅ Submitted (confirmed 2026-07-10) |
| Economics Final Paper: CBA – Data Center Energy Sourcing (with Tomer) | Economics (final paper) | ~7/2026 | Pending | ✅ Submitted (confirmed 2026-07-10) |
| Economics Seminar Poster + Distinction Presentation (with Tomer) | Economics seminar | Presented 7/30/2026 | Pending | ✅ Presented -- went great |
| Final LCA Assignment: Comparative EPD (ready-mix concrete) | Industrial Ecology and LCA | 8/1/2026 | Pending | ✅ Submitted -- confirmed 2026-08-03. Full build detail in `research/academic/final-lca-assignment/` |
| Final Sustainability Project: Herzliya Marina stormwater treatment (group of 5, written solo) | פרוייקט יישומי קיימות | 8/13/2026 | Pending | ✅ Written 2026-08-08, submitted 2026-08-12 -- **last assignment of the degree, degree fully complete**. Build detail in `research/academic/final-sustainability-project/` |

---

## By Course

### [Course Name 1]
- [ ] HW #2 (Due 5/18) - Complete
- [ ] [Next assignment]
- [ ] [Future assignment]

### [Course Name 2]
- [ ] [Assignment]
- [ ] [Assignment]

---

## Timeline View (This Month)

**May 16-18:** 
- [ ] HW #2 due 5/18 → SUBMITTED

**May 19-25:**
- [ ] [Upcoming assignments]

**May 26-31:**
- [ ] [End of month assignments]

---

## Key Dates & Deadlines

| Date | What | Course | Priority |
|------|------|--------|----------|
| 5/18 | HW #2 Due | [Course] | HIGH ✅ DONE |
| [Date] | [Exam/Project] | [Course] | MEDIUM |
| [Date] | [Assignment] | [Course] | HIGH |

---

## Research Organization

For assignments requiring research:
- See: `research/academic/[assignment-name]/` folder
- Use: `RESEARCH_GUIDELINES.md` workflow
- Template: `research/academic/hw2-lca-milk-production/` (example)

**Current research projects:**
- HW #2 (LCA milk production) - Complete

---

## Workflow for New Assignments

1. **Announcement** → Add to this tracker immediately
2. **Read instructions** → Note requirements and deadline
3. **Plan research** → If needed, create folder in `research/academic/`
4. **Use RESEARCH_GUIDELINES.md** → Follow the workflow
5. **Create AI disclosure** → If using Claude (use template)
6. **Before submitting** → Update status to "Complete" and add submission details
7. **After submitting** → Move to "Completed Assignments" section

---

## Notes

- Update this tracker immediately when assignments are announced
- Link assignments to daily priorities in `today.md`
- Use consistent file naming: `project/type/YYYY-MM-DD_name`
- Always research before finalizing (verify claims against peer-reviewed sources)
- Include AI disclosure PDF if you used Claude
- Archive completed assignments to `archives/` at end of term
