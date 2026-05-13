---
name: research
description: Research assistant that calls GPT-4.5 with context-appropriate system prompts for job market, academic, or D&D queries. Returns structured bullet-point summaries with key findings, sources, and next steps.
---

## When to Use This Skill

Invoke this skill whenever the user asks a research question that falls into one of these three categories:

**Job market** -- anything about companies, roles, salaries, required skills, hiring trends, career positioning, or job search strategy. Examples:
- "What companies in Israel hire data analysts for gaming?"
- "What skills should I build for a product analyst role?"
- "What is the typical salary range for a junior analyst at a startup in Tel Aviv?"

**Academic** -- anything about course content, research concepts, methodologies, academic arguments, technical definitions, or study help. Examples:
- "Explain Functional Unit in LCA methodology"
- "What are the main schools of thought in energy economics?"
- "Help me structure an argument about carbon pricing"

**D&D** -- anything about game mechanics, encounter design, NPC creation, world-building, campaign planning, rules questions, or creative content for the weekly D&D campaign. Examples:
- "Give me 5 plot hooks for a low-fantasy campaign"
- "How do I balance a 4-player party encounter at level 5?"
- "What are interesting personality quirks for a dwarven merchant NPC?"

## How to Detect Context

Read the user's message and classify it into one of: `job`, `academic`, or `dnd`.

Rules:
- If the message mentions companies, roles, hiring, salaries, job market, career, LinkedIn, interviews, or skills-for-employment -> `job`
- If the message mentions course content, research papers, methodology, academic concepts, theories, university assignments, LCA, energy policy, economic models, or study help -> `academic`
- If the message mentions D&D, dungeons, dragons, campaign, encounter, NPC, player characters, spells, monsters, world-building, session planning, or any tabletop RPG topic -> `dnd`
- If genuinely ambiguous between academic and job, prefer `academic`
- If none of the above applies, ask the user to clarify before running the script

## How to Run

Once you have determined the context, run this exact command (substitute `<context>` and `<query>`):

```
python "c:\עמרי\Shmags 2\.claude\skills\research\research.py" --context <context> --query "<the user's full question>"
```

Pass the user's complete original question as the `--query` value, enclosed in double quotes. Do not paraphrase or shorten it.

## How to Present Output

The script prints structured Markdown to stdout. Present it to the user exactly as-is, without wrapping it in another layer of bullets or commentary. You may add a brief one-sentence intro like "Here is what I found:" but keep it minimal. If the script exits with an error (any output to stderr or non-zero exit), report the error message clearly and do not invent a fallback answer.
