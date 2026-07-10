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

## Writing Rules (Do NOT Do)

- No emojis
- No em dashes (—)
- No catch-phrases or made-up expressions
- Keep it real and straightforward

## When to Apply

These rules apply to all outputs unless the user explicitly asks for something different (e.g., a formal document for external delivery where more polish is needed).

Check which register applies *before* writing, not after — don't rely on the content "feeling" formal or casual to decide:
- Chat replies, project files (today.md, trackers, current-priorities.md, goals.md, decisions/log.md, memory, READMEs), and D&D prep/campaign docs: Internal/working (casual), hard rules apply.
- Through the Gap or other public-facing content: External/public-facing tone, hard rules still apply (only warmth/formality shifts).
- University assignments, CV, professional emails: exempt from this file's tone — follow the target format's own convention instead (e.g. `references/academic-style-guide.md` for assignments).

## Skill-Owned Style

Any skill that produces an artifact Omri reads or uses (a document, a prep plan, a card, anything beyond internal automation) should define its own "Style" section inside the skill file — the specific tone and writing rules for *that* output type, consistent with this file. See `.claude/skills/assignment/SKILL.md` for the existing example (its Hebrew/English writing rules). That section should evolve directly as Omri gives feedback about that skill's output — style corrections for a given output type belong in the skill itself, not only in a memory file, so the skill actually gets better at producing that output over time.
