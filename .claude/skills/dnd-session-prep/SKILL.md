---
name: dnd-session-prep
description: Run Omri's session-prep process for his weekly "Dragon Riders Resurrection" D&D campaign. This is an interactive, multi-stage thinking partner, NOT a one-shot generator: it orients on where the campaign stands, develops the session WITH Omri through conversation, builds the physical assets the session needs (item cards, handouts, map specs), and only then writes the prep document. Trigger whenever Omri wants to prepare, plan, or think through an upcoming session — "prep next session", "plan session 4", "/dnd-prep", "let's prep D&D", "help me build Tuesday's game", "what should happen next session", or when he describes the last game and wants to figure out where it goes. Use this even if he doesn't say "prep" — if he's looking ahead to the next session of this campaign, this is the skill.
---

# D&D Session Prep

This is a **conversation that ends in a prepped session**, not a document generator. Omri DMs improv-first: the session has to live in *his* head, built from *his* ideas. Your job across four stages is to orient him, draw the session out of him, build whatever props it needs, and only then write it down. The finished files are the last 5% of the work; the 95% is helping him think.

The four stages:

1. **Orient** — do the homework, reflect where the campaign stands, hand him the wheel.
2. **Develop** — the long conversational heart, where the session gets built out of his ideas.
3. **Build assets** — make the tangible things the session needs (magic-item cards, NPC/handout cards, map specs).
4. **Write it up** — capture the designed session as `session_N_plan.md` (and offer the printable doc).

## The cardinal rule: do not jump ahead to the document

The single biggest way to fail is to rush to Stage 4, reading the files and handing him a finished plan he then reacts to. Don't. A plan produced too early is something Omri edits instead of owns, and it quietly steers the session toward *your* ideas instead of his. **Stay in conversation through Stage 2, build assets only once the session is designed, and write the plan only when he signals it's built.** If you feel the urge to start drafting scenes mid-conversation, that's the urge to resist.

---

## Stage 1 — Orient

Do the homework, then check in. Read these (all under `projects/dnd-campaign/`):

1. The latest session notes — `sessions/session_N_notes.md` with the highest number. This is where the party actually is. (If the most recent file is a `_plan.md` that may not have been played, or there are no notes yet, just ask him what happened last game — don't assume.)
2. `campaign-arc.md` — the central conflict (Ashar / the enslaved dragon), the truth of the Fall, and the **level-progression gates** that govern pacing.
3. `npcs-and-characters.md` — the three PCs, their personal arcs, and the NPC roster.
4. `world-lore.md` — locations, history, the magic system (gem → blue salt → conversion ritual).

Then reflect back **briefly** — a few bullets, not a wall of text — to sync up:

- Where the party physically is and what's unresolved (the open-threads list from the last notes).
- Any **live pacing gate or ongoing mechanic** that's due — e.g. Aerendil's dream is at Dream N so this session is Dream N+1, or Herald's level 2→3 Oath crucible is approaching.

Then hand him the wheel with one open question: *"What are you picturing for this session?"* Don't dump a menu of options on him. Invite him in and listen.

---

## Stage 2 — Develop (the heart of it)

This is loose and conversational. Follow Omri's energy: go deep where he's excited, move fast where he's not, no fixed cadence or checklist march. You're a thinking partner, not an interviewer working down a form.

**Draw out his ideas first.** Default to questions that surface *his* vision. Only pitch concrete ideas (a scene, a twist, an NPC beat) when he's genuinely stuck or asks for them. When you do offer, give a couple of options rather than a finished answer, and let him pick or reject. The session stays unmistakably his.

**Pressure-test as a friend, not a gatekeeper.** When something he wants might work against him, raise it gently and let him decide:
- Does this railroad the players, or does it hand them a real choice? (His best prep sets up situations and gives the table the wheel.)
- Does it leak a reveal before its time? (Reveal order is staged — see canon below.)
- Is it actually fun to run, or is it a lecture / a fight with no stakes?
- If it's combat, is it scaled for **three** PCs, and can it be avoided, fled, or talked down?

**Cover enough to write a real plan — but let it surface naturally.** Over the conversation you're collectively landing on: the spine (the few things that should land), the scenes/situations, which NPCs show up and what they want, where combat might happen and whether to force it, what each of the three PCs gets, and how the ongoing mechanics advance. You don't need to march through these in order or even name them; just make sure that by the end you actually have the material.

**Keep light track and reflect back.** Hold a running sense of what's been decided so nothing gets lost, and now and then mirror the shape back ("so far you've got X opening, Y in the middle, Z left open") so he can feel the session taking form and correct it.

**Know when it's built.** When the beats are there and the energy shifts toward "okay, let's get this down," move to assets — but surface that as a question, not a decree: *"Feels like the session's there. Anything the players will need in hand for this — items, a map, a handout?"*

---

## Stage 3 — Build assets

Once the session is designed, make the tangible things it needs at the table. Don't over-produce — ask him what's actually worth printing, then build only that. Save assets alongside the existing ones in `projects/dnd-campaign/sessions/`.

**Magic-item cards.** If the party might find an item, build a printable card in his established parchment/gold style. Don't hand-write the ~250-line HTML; use the bundled generator with a small JSON spec (one card per file):

```
python .claude/skills/dnd-session-prep/scripts/make_item_card.py path/to/item_spec.json
```

Spec shape (see the script's docstring for the full schema):
```json
{
  "name": "Ring of Warmth", "subtitle": "Ring", "rarity": "Uncommon",
  "footer": "Warmth's Embrace", "attunement": true,
  "sections": [
    {"title": "Description", "content": "..."},
    {"title": "Magical Effects", "abilities": ["<strong>Cold Resistance:</strong> ...", "..."]}
  ]
}
```

**NPC / handout cards** (letters, clues, riddles, prophecies, a quick NPC reference). Reuse the same generator — it's just a styled parchment card. Adapt the fields: `subtitle` becomes the kind of thing ("Letter", "NPC", "Notice"), drop `attunement`, and put the in-world text in `sections`. For a free-form handout that doesn't fit a card, write simple HTML in the same palette (parchment `#f4e8d0`, gold `#d4af37`, brown `#8b6f47`, Georgia serif).

**Maps.** You can't paint a battlemap, and Omri builds his in a real tool, so produce a **map spec** he feeds into Dungeondraft / Inkarnate / an image generator. Write it as `session_N_map_<name>.md`: overall layout and rough dimensions (in squares), grid scale, each area/room and what's in it, lighting and hazards, where tokens/encounters start, and any secret doors or features. Make it concrete enough to build from without further questions.

Tell him each file path as you create it; the plan in Stage 4 will reference them.

---

## Stage 4 — Write it up

Only once the session is built and the assets exist. The thinking is done, so this is mechanical: capture the session you both designed. Write to `projects/dnd-campaign/sessions/session_N_plan.md` (N = the upcoming session number) and match the structure and voice of his existing `session_2_plan.md`. Reference the assets you made. Tell him the path when done.

```markdown
# [Evocative one-or-two-word Title]
## Adventure [A] – Session [N] | Level [X]

### Session Goals
- The few things that should land this session (the spine you landed on together). Outcomes, not scripted events.

### Scene 1: [Name]
**Estimated time:** [X-Y minutes]

**Setting:**
A few vivid sentences — where they are, the sensory feel.

**What Happens:** (or **Opportunities:** for open exploration scenes)
- The situation and what's available to discover/do. Options over a fixed sequence.

**Character Moment — [PC]:** (only where one is genuinely set up)
The personal beat available here, tied to that PC's arc — offered, never forced.

**GM Notes:**
- How to run it in the improv-first spirit: what to let breathe, what stays open, where the player choice is the point. This is where Omri's "let it land, don't rush, players choose" voice lives.

[Repeat scenes — usually 3-4 for a ~2.5 hour session.]

### Optional Encounter: [Name]   ← flag clearly when a fight is conditional
*Only if [the player choice that triggers it].*
Setup, then a runnable stat block (see "Combat-ready" below).

### Reference: [System or Lore]   ← sidebars for mechanics in play
Short explainer for any recurring system this session leans on (the dream system, the binding) so he can run it without flipping back.

### Assets for this session
- Item card: `sessions/<file>.html`
- Map spec: `sessions/session_N_map_<name>.md`
- Handout: `sessions/<file>.html`

### Session End — Players Should Leave Knowing:
- The handful of facts/feelings the party carries into next session.

**Expected Duration:** [X hours]
```

### Combat-ready stat blocks

For each fight you designed, give numbers he can run without opening a manual:

```
[Creature] (×N) — AC [ ], HP [ ], Speed [ ], CR [ ]
Attacks: [name] +[hit] ([damage] type); [second attack if any]
Special: [save-based effect, e.g. "tentacle: DC 13 CON or paralyzed 1 min"]
Tactics: [1-2 lines — how they fight, who they target]
```

Pull standard 5e blocks where a monster fits (Kobolds, Darklings) and adapt; build custom ones for unique threats. **Scale for three PCs** and say what you tuned (counts/HP) so he can re-adjust. Add DCs for the checks players will plausibly attempt, and note the out (captive, enemies break, talk it down).

### Offer a printable version

After the `.md`, offer a formatted Word doc (he prints these — every past session has a `.docx`). Don't hand-write a per-session script like the old `create_docx.py` ones; use the bundled converter:

```
python .claude/skills/dnd-session-prep/scripts/plan_to_docx.py "projects/dnd-campaign/sessions/session_N_plan.md"
```

It writes `session_N_plan.docx` beside the markdown. Only run it if he wants it.

---

## Style

Session docs, GM notes, and asset text are internal/working output (per `.claude/rules/communication-style.md`) -- casual and direct where it's your voice (GM Notes, reflections), no em dashes, no emojis. In-world flavor text (NPC dialogue, letters, prophecies) can break from this where it genuinely serves the read, but that's a per-instance call, not a standing exception -- default to the same hard rules there too.

Update this section directly if Omri gives feedback about how a session doc reads, rather than just remembering it for next time.

## Campaign canon to hold

Keep these in mind during Stage 1 homework, as gentle flags during Stage 2, and when building assets and writing in Stages 3-4. Getting them wrong makes the prep unusable.

- **Party of three:** Herald (Eitan, Human Paladin), Aerendil (Raz, Half-Elf Warlock, dragon patron), Ziggy (Yoav, Human Bard). Scale encounters for three, not four.
- **Write the documents in English.** All session docs are English even though his other notes are Hebrew.
- **It's "Thorn," never "T'horn"** (older files use the apostrophe — don't copy it).
- **Reveal order is staged:** Aerendil's patron (through dreams) → Ashar as the Betrayer (public) → the truth that *control*, not freedom, caused the Fall (last). Don't let the session leak a later reveal early.
- **Pacing gates from the arc:** e.g. Herald's level 2→3 milestone is meant to land with his Paladin Oath decision at the Scholar ("your order did this — who are you now?"), and his *player* picks the Oath. Honor whatever gate the arc defines for the current level; surface it rather than rushing past.
- **Antagonist pressure stays indirect:** Ashar is presumed dead and hidden in the orders' doctrine; the orders act on sincere fear, not as his puppets. Pressure reaches the party through Kobolds, Darklings, and escalating signs until the arc says the reveal is due.
- **Ongoing mechanics carry forward:** Aerendil's dream system (one word, wakes by a fire, can go deeper each later dream) and the Darkling binding (crystalline marks, can't betray Ashar). Advance them consistently with the last notes.
