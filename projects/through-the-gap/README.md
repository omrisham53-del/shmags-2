# Through the Gap

Football economics newsletter on Substack. Skill 6 project: a passion-first revenue stream that runs through the September trip and beyond.

**Status note (2026-07-10):** Actively reconsidering the format. Omri wants to elevate this beyond a newsletter into a tool/app that generates revenue, is genuinely useful to him and people around him, hones his AI/product/creativity skills, and doubles as a portfolio piece for his next career step. Subject matter and passion-first premise stay; format is the open question. The workflow below is still valid if the newsletter format continues in some form -- don't build more newsletter-specific infrastructure without checking in on direction first.

**Concept:** The economics and politics of English football, for fans who want to understand why the game looks the way it does. Visual data journalism, not newspaper articles. Charts, graphics, and (later) interactive features carry the story; text stays tight.

**Editorial spine:** Inequality in English football. The gap between the giants and everyone else, how the rules create and protect it, and what it means for fans of the other clubs.

**Audience:** Football fans interested in tactics, data-driven insights, and the business side of the game. Broader than typical newsletter readers because the format is visual-first.

**Name logic:** "Through the Gap" is a football phrase (a pass threaded through a tight space) and the subject matter (the gap between clubs) in one.

**Platform:** Substack (throughthegap.substack.com or nearest available). Free tier only at launch; flip on paid after 2-3 published pieces and early readers.

**Revenue targets:** €100/month makes it a success in year one (~15-20 paid subs at €7/month). Long-term: ~€1,000/month within 5 years (~150 paid subs or subs + small sponsorships).

**Related, not yet started:** a passive football data tool to build during trip downtime. Newsletter comes first.

---

## Article Workflow

The repeatable pipeline (built with the first piece, July 2026):

1. **Idea + hook** - Start from a live story football fans already care about (a transfer, a vote, a collapse). Omri brings the idea.
2. **Saturation check** - Web search: who has already covered it, from what angle? If the mainstream angle is saturated, find the untold economic/structural angle. Kill ideas with no gap to fill.
3. **Research sprint** - Targeted searches on the specifics: the money, the rules, the votes, the incentives. Collect real numbers with sources. Push past the surface (e.g. not just "who voted" but "why would a small club vote for this?").
4. **Narrative lock** - Agree on the bottom line in one sentence before writing anything. What should the reader walk away believing? Omri sets this, not the research.
5. **Structure + charts** - Section-by-section skeleton where every section has one job and (usually) one chart. Charts are specified BEFORE the text is written; the text exists to connect the visuals.
6. **Draft** - 900-1,200 words. Visual-first, tight text, no filler. Chart placeholders inline. British football vocabulary. No em dashes, no emojis.
7. **Fact check pass** - Every number in the draft gets verified against a source before publish. Keep a "verify before publish" list in the draft file.
8. **Build charts** - Python/matplotlib (or interactive later). Consistent visual identity across articles.
9. **Publish + distribute** - Substack post + Twitter/X thread version (charts as images, thread tells the compressed story, links to the full piece).

## Files

- `articles/` - One markdown file per article: `YYYY-MM-DD_slug.md`. Draft, chart specs, and verify-list live together in the file.
- `tracker.md` - Article pipeline status, subscriber/revenue milestones.
