# Final Day Prompt -- paste this into the company account

**Use:** copy everything below the line into the company/work-computer Claude account as the
opening message. It replaces the two older per-deliverable handoff files for today's purposes
(`work-handoff.md` = grants model doc, `loan-fund-work-handoff.md` = loan fund trim), which
stay in the repo as the detailed backup versions.

---

Today is my last working day at EcoTraders. I have two deliverables left to close out, and I
want to finish both today. You can't see my personal notes repo, so here's the full context.

## Project context

EcoTraders is writing the incentive-section chapters of a national energy efficiency program
document for Israel's Ministry of Energy. There are 3 such chapters: grants program, tax
incentive, and loan fund. I own all 3, plus 2 model-documentation files my manager Daniel added
on 2026-08-16 (one per model: grants and tax).

Already finished, do not redo:
- Grants program chapter: sent to the Ministry client 2026-07-12.
- Loan fund position paper: sent to the Ministry client 2026-07-12.
- Tax incentive model and chapter: submitted to Daniel 2026-08-17.
- Tax model documentation file: done 2026-08-17 (`tax-model-documentation.docx`).

## Deliverable 1 (priority): trim the loan fund chapter from 6 pages to 3

This is an edit, not a drafting task. The appendix version of the loan fund chapter (built
2026-08-03) is essentially the position paper with a few minor tweaks, and every required
section already exists in it. It currently runs about 6 pages. It needs to be about 3.

Open the appendix version and trim it. Work in this order, because cutting whole low-value
chunks reads better than shaving sentences evenly across a document:

1. Redundant explanation. Anything this chapter re-explains that the grants or tax chapter
   already established for the reader (shared policy background, Government Decision 1261
   framing) becomes a one-line reference instead of a repeat.
2. Non-load-bearing examples. If there's a worked example or an extended narrative of how a
   firm would use the fund, keep the numbers and cut the walk-through.
3. Any international comparison: compress it into a table if it isn't one already. Prose
   comparisons run long; a table with the same parameters is far denser per page.
4. Background and context prose. A position paper is written to stand alone and persuade a
   reader with no other context. As the third of three sibling chapters, most of that
   scene-setting is dead weight. Cut it, keep the mechanism and the numbers.
5. Only as a last resort, cut detail from the mechanism and methodology sections. That's where
   the chapter's actual substance lives.

Do not cut: the core mechanism explanation (terms, eligibility, how the fund actually works),
any real number or result, or the brief framing of where this instrument sits among the three
(grants = direct cash outlay, tax incentive = timing benefit through depreciation, loan fund =
access to financing).

Process notes:
- Check the page count after each pass rather than planning all cuts up front, and stop as soon
  as you hit 3 pages. Don't over-cut past the target.
- Confirm the page-format convention (font, size, spacing, margins) against the grants and tax
  chapters first, so "3 pages" means the same thing here as it does there.
- Read the trimmed version straight through at the end. It has to read as a complete chapter,
  not as the fragments that survived.
- If any cut costs a real number or a substantive claim the position paper made, tell me
  explicitly so I can flag it to Daniel rather than dropping it silently.

Relevant precedent: the tax chapter hit this exact problem (6 pages against a 4-page ceiling,
flagged 2026-08-16) and the trim kept getting deferred. Don't let that happen on this one.

## Deliverable 2: grants model documentation file (confirm status first)

My notes still show this as in progress on this computer. Check whether it's actually finished
before doing anything. If it's done, say so and move on.

If it isn't done: it's a standalone file listing every assumption, calculation method, and
source data file the grants model actually uses, so that someone who never built the model can
audit it. Use `tax-model-documentation.docx` as the exact structure and style template. Same
section order, same table format, same tone, just filled with grants-model content instead:

1. Model structure overview (how many sheets, what each section covers)
2. General and shared assumptions actually used (discount rates, tariffs, conversion factors,
   whatever the grants model actually references)
3. Technology-specific assumption tables (parameter / value / source, one table per technology)
4. Calculation methodology, step by step, in prose
5. Source data files list (which real files and standards backed each number)
6. Open items and unresolved flags, stated plainly rather than glossed over

Read the grants model workbook itself before writing anything. Don't reinvent the document
shape, just fill the existing one.

## Files to open

For the trim: the loan fund appendix version (the file to edit directly), plus the grants
program chapter and the final tax incentive chapter
(`tax-chapter-draft-with-results.docx`) as the page-format and tone references.

For the documentation file: the grants model Excel workbook, plus
`tax-model-documentation.docx` as the structure template.

## Writing rules

The chapters are in Hebrew. Match the register and conventions already used in the grants and
tax chapters rather than introducing a new voice.

Hard formatting rules, these apply to everything you write:
- No em dashes. Use a colon, or a single hyphen with spaces around it.
- No emojis.
- No AI filler: no "it's important to note", "delve into", "leverage" meaning "use",
  "seamless", "robust" as a generic adjective, "cutting-edge", "harness the power of",
  "testament to", or rote "in conclusion" closers.
- No rule-of-three padding, no "it's not just X, it's Y", no closing paragraph that just
  restates what was already said, no random mid-sentence bolding.

## What done looks like

Both deliverables sent to Daniel. That closes the entire Energy Program scope for my time here.

Start with the loan fund trim. Before you begin cutting, tell me the current real page count
and where you plan to take the pages from, so I can redirect you before the work is done rather
than after.
