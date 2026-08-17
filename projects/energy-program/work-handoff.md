# Work-Account Handoff -- Loan Fund Chapter + Grants Model Documentation File

**Purpose:** Paste this whole file as the opening message on the EcoTraders/company Claude
account when starting this work. It's the context that account has no way to see on its own --
this file lives in Omri's personal second-brain repo, not on the work computer.

**Keep this file scoped to these two deliverables only.** Don't fold in personal, non-EcoTraders
content when updating it -- that's a hard boundary, not a style preference.

---

## Project context

EcoTraders (Omri's employer, part-time policy analyst role) is writing the incentive-section
chapters of a national energy efficiency program document for Israel's Ministry of Energy.
There are 3 such chapters total: grants program, tax incentive, and loan fund. Omri owns all 3,
plus a 4th deliverable Daniel added on 2026-08-16: a documentation file per model (assumptions,
calculation methods, source data) for the grants model and the tax model.

**Scope lock (Daniel, EcoTraders manager, confirmed 2026-07-26):** Omri's last day is
August 22, 2026 (real last working day: Thursday Aug 20), and no new assignments will land
before then beyond what's described here.

**Status of the other pieces, for context:**
- Grants program chapter -- finished, sent to the Ministry client 2026-07-12.
- Tax incentive chapter and model -- **finished and submitted to Daniel today (2026-08-17)**.
- Tax model documentation file -- **already built on the personal account**, attached alongside
  this handoff (`tax-model-documentation.docx`). Use it as the exact structure/style template
  for the grants model documentation file below -- same section order, same table format, same
  tone. Don't reinvent the shape, just fill it with grants-model content.

## The two remaining deliverables

### 1. Loan fund chapter -- due tomorrow (2026-08-18)

Two parts:
- **Appendix version** -- reuses the loan fund **position paper** that was already written
  and sent to the Ministry client on 2026-07-12. Light adaptation work (reformatting/trimming
  to fit an appendix slot), not a rewrite.
- **Full chapter** -- a genuinely new, complete write-up for the body of the actual national
  program document. Real writing work, not adaptation.

**Structure convention to match:** mirror the grants program chapter (finished -- locate and
read it as the actual template for tone and section layout). Broadly: background/policy context
for the loan fund instrument, how the mechanism works, methodology (how impact/cost-effectiveness
is measured), results. The tax incentive chapter (also finished now, attached) is a second
reference point for section layout and tone, since all 3 chapters should read as one coherent
document -- particularly its structure: 1) background/policy, 2) how the mechanism works,
3) international review, 4) methodology, 5) results, 6) summary/conclusions. The loan fund
mechanism differs enough from a tax deduction that the methodology section will look different
in substance, but the shape (background -> mechanism -> methodology -> results -> conclusions)
should carry over.

### 2. Grants model documentation file

Same purpose as `tax-model-documentation.docx` (attached): a standalone file listing every
assumption, calculation method, and source data file the grants model actually uses, so someone
who never built the model can audit it. Structure to copy from the attached tax version:
1. Model structure overview (how many sheets, what each section covers)
2. General/shared assumptions actually used (discount rates, tariffs, conversion factors --
   whatever the grants model actually references from the shared "נתונים והנחות - כללי" sheet,
   if it uses the same national-program format)
3. Technology-specific assumption tables (parameter / value / source, one table per technology)
4. Calculation methodology, step by step, in prose
5. Source data files list (which real files/standards backed each number)
6. Open items / unresolved flags, stated plainly rather than glossed over

## What's NOT known from this side (needs the actual work files)

The grants model's actual structure, the grants chapter's finished prose, the loan fund position
paper, and the national program document's own template/formatting requirements all live on the
work computer, not here. **Upload these before starting:**
- Loan fund position paper (sent to the Ministry 2026-07-12)
- Grants program chapter (finished doc)
- Grants model (Excel workbook)
- Tax incentive chapter (final, attached from this handoff) and `tax-model-documentation.docx`
  (attached) -- for structure/tone reference, not re-editing

Read all of those before writing anything.

---

*Last updated: 2026-08-17. Update this file (from Omri's personal account, not the company
one) whenever these two deliverables' scope, status, or the sibling chapters' progress
materially changes -- so the next work-account session pastes in something current, not stale.*
