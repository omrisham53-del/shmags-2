#!/usr/bin/env python3
"""
Research skill for Omri's second brain.
Usage: python research.py --context <job|academic|dnd> --query "<query string>"
"""

import argparse
import os
import sys
from pathlib import Path

# Load .env from the project root (three levels up from this file:
# skills/research/ -> skills/ -> .claude/ -> project root)
try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv is not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# Resolve root .env relative to this script's location
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_ENV = SCRIPT_DIR.parent.parent.parent / ".env"
load_dotenv(dotenv_path=ROOT_ENV)

try:
    from openai import OpenAI, OpenAIError
except ImportError:
    print("ERROR: openai package is not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# --- System prompts per context ---

SYSTEM_PROMPTS = {
    "job": """You are a specialized job market research assistant for an Israeli analyst \
early in their career (economics/data/policy background, targeting data analyst or \
product analyst roles, graduating 2026).

When given a research query, respond in structured Markdown with exactly these sections:
## Key Findings
- Bullet list of the most actionable insights (companies, roles, salary ranges, required skills, hiring trends)

## Sources / References
- Named sources, reports, or platforms where this data originates. If none are available, write "No specific sources identified."

## Suggested Next Steps
- Concrete, prioritized actions the user should take based on the findings

Keep the tone direct, practical, and specific to the Israeli market unless the query \
specifies otherwise. Avoid vague career advice.""",

    "academic": """You are a specialized academic research assistant supporting a third-year \
economics/policy student in Israel.

When given a research query, respond in structured Markdown with exactly these sections:
## Key Findings
- Core concepts, main schools of thought, methodological frameworks, or factual answers

## Sources / References
- Seminal papers, textbooks, authors, or academic institutions associated with this topic. \
If none are available, write "No specific sources identified."

## Suggested Next Steps
- How to deepen understanding: related sub-topics to explore, angles to take for an essay \
or presentation, technical terms to define

Keep explanations rigorous but accessible. Prefer concrete examples over abstract definitions.""",

    "dnd": """You are a specialized D&D 5e assistant and creative game design collaborator, \
supporting an experienced DM who runs a weekly campaign.

When given a research query, respond in structured Markdown with exactly these sections:
## Key Findings
- Direct answers, mechanics, rulings, world-building ideas, NPC concepts, or encounter \
designs addressing the query

## Sources / References
- Relevant rulebooks (PHB, DMG, MM, Xanathar's, etc.), page numbers if known, or \
sourcebooks where this content appears. If none are applicable, write "No specific sources identified."

## Suggested Next Steps
- Follow-up ideas, variations, hooks, or ways to adapt this to the user's specific campaign

Be creative, specific, and DM-friendly. Prefer usable content over theory."""
}

CONTEXT_ALIASES = {
    "job": "job",
    "jobmarket": "job",
    "job_market": "job",
    "academic": "academic",
    "academia": "academic",
    "study": "academic",
    "dnd": "dnd",
    "d&d": "dnd",
    "dungeonsanddragons": "dnd",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Research skill powered by GPT-4.5")
    parser.add_argument(
        "--context",
        required=True,
        help="Research context: job, academic, or dnd",
    )
    parser.add_argument(
        "--query",
        required=True,
        help="The research question or topic to investigate",
    )
    parser.add_argument(
        "--model",
        default="gpt-4.5-preview",
        help="OpenAI model to use (default: gpt-4.5-preview)",
    )
    return parser.parse_args()


def resolve_context(raw: str) -> str:
    normalized = raw.lower().replace(" ", "").replace("-", "")
    resolved = CONTEXT_ALIASES.get(normalized)
    if resolved is None:
        print(
            f"ERROR: Unknown context '{raw}'. Valid values: job, academic, dnd",
            file=sys.stderr,
        )
        sys.exit(1)
    return resolved


def main():
    args = parse_args()
    context = resolve_context(args.context)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your-openai-key-here":
        print(
            "ERROR: OPENAI_API_KEY is missing or not set. "
            f"Edit {ROOT_ENV} and add your key.",
            file=sys.stderr,
        )
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    system_prompt = SYSTEM_PROMPTS[context]

    try:
        response = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": args.query},
            ],
            temperature=0.4,  # Factual but not robotic
        )
    except OpenAIError as e:
        print(f"ERROR: OpenAI API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    result = response.choices[0].message.content
    print(result)


if __name__ == "__main__":
    main()
