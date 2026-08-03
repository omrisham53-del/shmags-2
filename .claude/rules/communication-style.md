---
name: communication-style
description: Writing tone, formatting, and preferences for Omri
metadata:
  type: feedback
---

## Formatting

- **Default:** Bullet points (unless writing a full document)
- **For documents:** Detailed paragraphs with proper structure
- **Code/technical:** Clear and minimal comments

## Tone

- **Internal/working:** Casual, direct, friendly
- **External/public-facing:** Professional but friendly, warm, chill guy energy (ambitious but not aggressive)

## AI Kill List (Do NOT Use)

A living list of AI-tell words, phrases, and structural patterns Omri never wants in his content, output, or conversations with Claude. Applies everywhere, including academic/professional docs (see "When to Apply" below) -- these are AI tells, not a register/tone choice. Add new items as they come up (from the Claude Code manual or in-session) -- log the addition as a Claude Code lesson in `projects/claude-code-lessons/tracker.md`.

**Characters & Formatting**
- No emojis
- No em dashes (—)
- In Excel/.xlsx deliverables specifically: never use `--` (double hyphen) as a text separator in cell values, even though it's the standard substitute everywhere else in this repo. Excel's own AutoCorrect silently converts `--` into a real em dash (—) the moment the cell is edited further (confirmed 2026-08-03 on `chiller-market-sizing.xlsx` -- the delivered file had zero em dashes, but they appeared after Omri started editing it in Excel). Use a colon (`:`) for header/label separators, or a single hyphen with spaces (` - `) for inline asides -- neither triggers the autocorrect. This applies to every future xlsx build, not just the one that surfaced it.

**Buzzwords & Filler Phrases**
- "it's important to note that" / "it's worth noting that"
- "delve into"
- "unlock the potential of"
- "in today's fast-paced world" / "in today's digital age"
- "leverage" (as a verb meaning "use")
- "seamless" / "seamlessly"
- "robust" (as generic filler adjective)
- "cutting-edge"
- "game-changer" / "game-changing"
- "elevate" (as generic filler verb)
- "unprecedented"
- "harness the power of"
- "in the realm of"
- "boasts" (e.g. "the product boasts")
- "tapestry" (e.g. "rich tapestry of")
- "navigate the complexities of"
- "at the end of the day"
- "dive deep" / "deep dive"
- "paradigm shift"
- "synergy" / "synergize"
- "holistic"
- "empower" (as generic filler verb)
- "foster" (as generic filler verb, e.g. "foster collaboration")
- "testament to"
- rote "in conclusion" / "in summary" closers
- No catch-phrases or made-up expressions

**Structural Tics**
- Rule-of-three padding (three adjectives/examples used for rhythm, not because three is actually right)
- "It's not just X, it's Y" construction
- Restating the question before answering it
- Random mid-sentence bolding for false emphasis
- Bullet lists where every line opens with a bolded 2-3 word header + colon, used indiscriminately
- A closing paragraph that just re-summarizes what was already said
- Excessive hedging ("may potentially", "could possibly")
- False-rhythm parallelism ("Not only does X... but it also...")
- Title-Case Headers For Every Single Line

**Openers & Closers**
- "Great question!" or similar throat-clearing before answering
- Enthusiasm-flavored offers tacked onto the end ("Let me know if you'd like me to...!")

*Keep it real and straightforward.*

## When to Apply

The AI Kill List above applies to everything, no exceptions by register -- these are tells that content is AI-slop, not a formality dial. If a specific banned item is actually correct in a given academic/professional context, resolve that as a skill-specific exception (see "Skill-Owned Style" below), not a blanket carve-out here.

Tone (this section only) still varies by register unless the user explicitly asks for something different:

Check which register applies *before* writing, not after — don't rely on the content "feeling" formal or casual to decide:
- Chat replies, project files (today.md, trackers, current-priorities.md, goals.md, decisions/log.md, memory, READMEs), and D&D prep/campaign docs: Internal/working (casual).
- Through the Gap or other public-facing content: External/public-facing tone (only warmth/formality shifts).
- University assignments, CV, professional emails: exempt from this file's tone — follow the target format's own convention instead (e.g. `references/academic-style-guide.md` for assignments). The Kill List itself still applies.

## Skill-Owned Style

Any skill that produces an artifact Omri reads or uses (a document, a prep plan, a card, anything beyond internal automation) should define its own "Style" section inside the skill file — the specific tone and writing rules for *that* output type, consistent with this file. See `.claude/skills/assignment/SKILL.md` for the existing example (its Hebrew/English writing rules). That section should evolve directly as Omri gives feedback about that skill's output — style corrections for a given output type belong in the skill itself, not only in a memory file, so the skill actually gets better at producing that output over time.
