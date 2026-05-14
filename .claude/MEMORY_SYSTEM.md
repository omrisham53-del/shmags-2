# Memory System Clarification

Two complementary memory systems work together:

## 1. Session Memory (in repo)
**Location:** `sessions/` folder + `decisions/log.md`

**Purpose:** Document work sessions and decisions made
**Content:**
- Session summaries (what got done, decisions, next steps)
- Decision log (important decisions with reasoning and context)

**Frequency:** After each major work session
**Retention:** Current quarter in active sessions/, older items archived

## 2. Persistent Memory (user home directory)
**Location:** `C:\Users\User\.claude\projects\c-------Shmags-2\memory\`

**Purpose:** Remember preferences, patterns, and learnings across conversations
**Content:**
- Music curation preferences
- D&D font palette preferences
- Job tracker skill development progress
- Any other repeating patterns or preferences

**Frequency:** As patterns emerge, not after every session
**Retention:** Persistent across all conversations

## When to Use Each

**Session Memory** when:
- Documenting what you accomplished in a work session
- Making an important decision that shapes future work
- Capturing context that will be useful for 30 days

**Persistent Memory** when:
- Learning a repeating preference ("I always prefer X")
- Discovering a pattern that applies across projects
- Finding something non-obvious that will inform future similar tasks
- User explicitly asks to remember something

## How They Work Together

1. Session captures the work + immediate next steps
2. Persistent memory captures the lessons that apply to future work
3. Both are indexed and easily accessible
4. Together they let Claude Code understand both what you're doing and how you like to work
