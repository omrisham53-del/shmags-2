# HoTake - Microsoft x Premier League Hackathon

**What it is:** Omri's solo entry to the Microsoft x Premier League "Inside the Game" Developer Hackathon (Sep 29 - Oct 27, 2026).

**The product:** **HoTake** - a single-seat AI football pundit named **Clive**, with an old CRT monitor for a head. He watches a synthetic match alongside you, notices tactical shifts before anything obvious happens, provokes you into committing to a take, makes his own falsifiable calls, and then grades both of you against the evidence.

**The distinctive claim:** most AI products are built so they can never be wrong on the record. Clive keeps score of his own bad takes.

**Why this and not something else:** every other public entrant is building broadcast-grade commentary and recaps for a studio. HoTake is built for the group of friends who argue tactics live. That lane is empty.

---

## Goals, in Omri's own ranking

1. **A portfolio piece with a public link** - something to show off on LinkedIn
2. **Real skill development** - specifically multi-agent orchestration
3. **Genuine interest** - football tactics and prediction arguments with friends

Winning is explicitly **not** a goal. His words: *"I was never expecting to win the competition, but more to develop skills and show them off."* Target is the **Best Multi-Agent category prize**, not the Grand Prize.

This ranking drives everything: if it cannot be seen in 120 seconds it is near-worthless; Azure is a box to tick cheaply, not a thing to go deep on; hours go into the agent layer, not the frontend.

---

## Where things live

| Thing | Where |
|---|---|
| **Code** | `c:\עמרי\HoTake` - standalone **public** GitHub repo, outside SHMAGS 2 |
| Discovery capture | `brainstorms/2026-10-19_plms-hackathon-project.md` (19 questions + consolidated plan of record) |
| Status, deadlines, open items | `tracker.md` in this folder |
| Decisions | `decisions/log.md` (four entries, 2026-10-19) |
| Submission platform | https://innovationstudio.microsoft.com/hackathons/insidethegamedeveloperhackathon |
| Official rules | https://github.com/microsoft/insidethegamehackathon |

**Hard rule:** the code repo is public. Nothing from SHMAGS 2 ever goes into it - no personal data, no client names, no trip or job-search detail. Tracker and decision entries stay here.

---

## Architecture in one table

Agents only where judgment lives, plain code everywhere else.

| Piece | Agent? |
|---|---|
| Match engine (seeded synthetic events + declared tactical state) | No, plain code |
| Stats/context store | No, code + a tool |
| Set-piece analyst | Yes |
| Individual-duels analyst | Yes |
| Box-numbers analyst (attacking/defending bodies in the box) | Yes |
| **Clive** (owns the POV, decides what is worth saying, makes calls) | Yes |
| Adjudicator (gathers evidence, rules on who was right) | Yes |
| Claim ledger | No, plain code |
| Supervisor (event-type routing, wakes only the relevant specialist) | Thin |

Framework: **Microsoft Agent Framework**. Stack: Python, FastAPI + server-sent events, one styled HTML page. Azure: Foundry for inference, Container Apps for hosting.

Full detail, including the data abstraction and the failure-recovery design, is in the brainstorm capture.
