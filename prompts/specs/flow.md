# MMW Flow Spec — Workflow, Protocols, and File Schema

This file is the canonical source of truth for how Mark My Words orchestrates its agents. Agent specs reference this file. When the workflow changes, change it here first.

---

## Invocation

This system responds to the following triggers:
- `MMW` — shorthand alias
- `Mark My Words` — full name
- `mmw` — lowercase variant

All three launch Caret as the default entry point.

### Sub-agent shortcuts (bypass Caret, go directly to an agent)

| Shortcut | Agent |
|---|---|
| `MMW:turing` | research |
| `MMW:devil` | critique |
| `MMW:echo` | audience check |
| `MMW:press` | publish prep |
| `MMW:prism` | image prompt generation |
| `MMW:compass` | strategy |
| `MMW:mark` | brand check |
| `MMW:cadence` | editorial calendar |
| `MMW:index` | archive and overlap check |

### Workflow gate
- `MMW:proof [codename]` → human declares draft final, triggers Phase 11 handoff

### Invocation model

Each `MMW:agent` shortcut invokes a **native Claude Code subagent** — an isolated subprocess with its own context window and tool permissions. Agent definition files live in `.claude/agents/` (not `writers-room/agents/`). State is passed exclusively through files in the piece folder — agents cannot share in-memory state across subprocess boundaries.

Caret, as orchestrator, spawns subagents explicitly and coordinates the workflow through the shared file system. When spawning any subagent, Caret must pass the active codename explicitly in the invocation — subagents cannot discover the codename themselves.

Example: "You are working on piece `writers-room-build`. All files are in `writers-room/pieces/writers-room-build/`."

---

## Full Ordered Workflow

```
brief.md written by Caret
   ↓
Phase 0 — Index: overlap gate
   ↓
Phase 1 — Compass: strategic direction
   ↓
Phase 2 — Turing: focused research (reads compass-notes.md first)
   ↓
Phase 3 — Caret: draft-v1.md
           [research.md gate — must exist and be non-empty]
   ↓
Phase 4 — Mark: headlines and hooks (reads draft-v1.md)
   ↓
Phase 5 — Iterative loop: Caret ↔ Mark
           [max 2 iterations, then circuit breaker]
           [co-edit available at every pause]
   ↓
Phase 6+7 — Devil ║ Echo  [run in parallel]
            Devil: accusation audit → critique-vN.md
            Echo:  audience check  → audience-vN.md
   ↓
Phase 8 — User revision window
           [Caret reads both critique-vN.md and audience-vN.md]
           [co-edit available]
   ↓
Phase 9+10 — Press ║ Prism  [run in parallel]
             Press: SEO and Hugo front matter → seo.md
             Prism: image prompt              → image-prompt.txt
   ↓
[MMW:proof [codename] — human declares draft final]
   ↓
Phase 11 — Handoff: final.md → posts/drafts/[slug].md
           Index ║ Cadence  [run in parallel]
           Index:   updates post-index.md
           Cadence: logs in calendar.md
```

---

## Phase 0 — Index Overlap Gate

Index runs before any other agent does real work.

See `specs/agent-index.md` for full startup validation rules and overlap handling (Abandon / Differentiate / Proceed options).

---

## Phase 1 — Compass: Strategic Direction

Compass runs immediately after the Index gate — **before Turing**. Research must be focused within a strategic frame, not done blindly.

Compass reads brief.md and produces compass-notes.md. Turing reads compass-notes.md before starting any research.

See `specs/agent-compass.md` for full compass-notes.md content requirements.

---

## Phase 2 — Turing: Research

Turing reads brief.md and compass-notes.md. Research is scoped to the strategic direction Compass defined.

Turing produces research.md — a thorough grounding document that all subsequent agents read before producing their output. This file is the factual and contextual foundation for the piece.

See `specs/agent-turing.md` for full research requirements and the Deep Dive Pause protocol.

---

## Phase 3 — Caret: First Draft

### Research Gate (CRITICAL — never skip)

Before writing any draft, Caret MUST explicitly verify that research.md exists and is non-empty in the current piece folder.

If research.md does not exist:
- Do NOT proceed to drafting
- Surface this to the user:
  > "research.md is missing. Turing has not completed research for this piece. Run MMW:turing before drafting, or confirm you want to proceed without research."
- Wait for explicit user confirmation before continuing

If research.md exists but appears thin (under 200 words):
- Flag it: "research.md exists but appears brief. Turing may not have completed a full research pass. Proceed anyway or run MMW:turing again?"
- Wait for user confirmation

**Never silently skip this check.**

### Drafting

Caret reads brief.md, compass-notes.md, and research.md before writing draft-v1.md. Caret follows the story arc: **hook → exploration → insight → deeper dive → reflection**.

---

## Phase 4 — Mark: Headlines

Mark reads draft-v1.md and produces headlines.md. The draft is the ground truth — headlines must reflect what the piece is actually about, not just the original brief.

See `specs/agent-mark.md` for scoring criteria and brand rules.

---

## Phase 5 — Iterative Loop: Caret ↔ Mark

This loop runs until one of three exit conditions is met.

### Exit conditions (checked in this order)

1. Mark issues a PASS verdict in brand-notes
2. The draft satisfies the original intent stated in brief.md — Caret explicitly checks the draft against brief.md and declares intent met
3. 2 loop iterations have completed — circuit breaker fires

### Loop pause after every Mark review

After every Mark review and before pausing for user input, Caret must update status.md with the current loop iteration count: `Loop iterations: N of 2`. This ensures the count survives a session boundary and is correct on resume.

After every Mark review, the loop PAUSES. The user receives:

```
Mark has reviewed draft-vN.md → brand-notes-vN.md [REVISE / PASS]

Outstanding issues (if REVISE):
  1. [specific issue Mark flagged]
  2. [specific issue Mark flagged]

Brief intent check: [MET / NOT YET MET]
Loop iteration: N of 2

Your options:
  [C] Co-edit — Caret surfaces the specific lines, you edit the draft
       file directly, Caret reads your edits and produces the next version
  [R] Revise — Caret revises based on brand-notes alone, no user edits
  [S] Stop loop — proceed to Devil/Echo with the current draft as-is
```

### 2-Iteration Circuit Breaker

After 2 full loop iterations without a PASS, Caret stops and presents:

```
The loop has run 2 times without a full PASS from Mark.

Unresolved issues:
  1. [issue]
  2. [issue]

How would you like to proceed?
  [C] Co-edit the current draft together
  [S] Stop and proceed to critique with current draft
  [B] Revisit the brief — the issues may reflect a brief problem,
      not a draft problem
```

---

## Co-Edit Mode — The User's Voice

Co-edit mode is the most important feature in Mark My Words. It is the moment the user's voice enters the draft. It must be treated with more care than any automated agent pass.

Co-edit is available at every loop pause point and after every Devil/Echo review.

### Step 1 — Surface exactly what needs attention

Caret does not summarize vaguely. It identifies and displays the specific lines, sentences, or passages that were flagged. Format:

```
Co-edit — draft-v2.md

The following passages need your attention:

[Line 4]
Current: "Utilizing a multi-agent approach allows us to leverage..."
Issue: Banned words (Utilizing, leverage). Voice drift — sounds corporate.
Your edit here:

[Lines 12-14]
Current: "The system is robust and furthermore provides..."
Issue: Banned words (robust, furthermore). Passive construction.
Your edit here:

[Closing paragraph]
Current: "In conclusion, this approach represents a game-changing..."
Issue: Banned words (game-changing). Weak close — doesn't match brief
intent of honest reflection.
Your edit here:
```

### Step 2 — User edits directly

The user edits the draft file directly — not through Caret. This is intentional. The user owns the keyboard at this moment. Caret waits. No suggestions, no rewrites, no hovering.

Before waiting, Caret writes this state marker to status.md:
`[in-progress] user-edit — awaiting MMW:done`

This ensures the co-edit state survives a session boundary. If the session ends before `MMW:done` is received, Caret will re-surface the co-edit prompt on resume rather than advancing to the next phase.

User signals completion by typing: `MMW:done` as a chat message. Caret listens for this signal in the conversation only — it does not scan file content for it. For posts about MMW itself, `MMW:done` may appear inside the draft file as an example; that does not trigger co-edit completion.

### Step 3 — Caret reads and integrates

Caret reads the user-edited file. It does not rewrite what the user wrote. It integrates the user's edits as the authoritative base and:
- Applies any remaining flagged issues the user did not address
- Checks the result against brief.md intent
- Produces the next versioned draft

### Step 4 — Caret reports what it changed

After producing the new draft, Caret reports exactly what it touched beyond the user's edits:

```
draft-v3.md produced.

Your edits: preserved exactly as written.
Caret also addressed:
  - Removed "additionally" from paragraph 3 (banned word not in your edit)
  - Tightened transition between paragraph 5 and 6 per brand-notes

Nothing else was changed. Your voice is intact.
```

### Co-edit rules Caret must never break

- NEVER rewrite a passage the user just wrote without flagging it first
- NEVER silently change the user's phrasing in the name of brand compliance
- If a user's edit contains a banned word, flag it — do not delete it:
  > "You used 'leverage' in paragraph 2. This is a banned word per brand guidelines. Keep it, or would you like an alternative?"
- The user's voice overrides Mark's preferences when there is a conflict
- Caret's job in co-edit is to be the user's assistant, not their editor
- User edits are always recorded in status.md: `[user-edit] draft-v2.md → basis for draft-v3.md`

---

## Phase 6+7 — Devil + Echo [parallel]

Before spawning, Caret resolves the current latest draft filename once (highest-numbered draft-vN.md in the piece folder) and passes it explicitly to both subagents in the invocation. Agents must use the filename Caret passes — they do not scan for the latest draft themselves.

If invoked directly via `MMW:devil` or `MMW:echo`, they resolve independently by scanning for the highest-numbered draft-vN.md.

Caret spawns Devil and Echo as concurrent subagents. Both receive the same codename and the same explicit draft filename. Neither reads the other's output. Caret waits for both to complete before proceeding to Phase 8.

See `specs/agent-devil.md` and `specs/agent-echo.md` for full audit and review criteria.

---

## Phase 8 — User Revision Window

After Devil and Echo complete, Caret reads critique-vN.md and audience-vN.md, then presents a consolidated feedback summary and pauses. The user may:
- Edit the draft directly (co-edit mode available)
- Ask Caret to revise based on Devil/Echo feedback
- Proceed to publish prep with the current draft as-is

If changes are made: Caret produces a new versioned draft before handing off to Press.

If no changes: Press reads the existing latest draft — no new version is created. Caret does not increment the draft version without a reason.

---

## Phase 9+10 — Press + Prism [parallel]

Before spawning, Caret resolves the current latest draft filename once (highest-numbered draft-vN.md in the piece folder) and passes it explicitly to both subagents in the invocation. Agents must use the filename Caret passes — they do not scan for the latest draft themselves.

If invoked directly via `MMW:press` or `MMW:prism`, they resolve independently by scanning for the highest-numbered draft-vN.md.

Caret spawns Press and Prism as concurrent subagents. Both receive the same codename and the same explicit draft filename. Press writes seo.md. Prism writes image-prompt.txt. Neither reads the other's output. Caret waits for both before the MMW:proof gate is valid.

See `specs/agent-press.md` and `specs/agent-prism.md` for full output requirements.

---

## Phase 11 — Handoff

See `specs/agent-caret.md` for the full pre-flight check, handoff steps, and parallel Index ║ Cadence spawn.

---

## File Schema

Every piece folder contains exactly these files, created in order:

```
writers-room/pieces/[codename]/
├── brief.md              ← user intent — source of truth for the piece
├── status.md             ← codename, description, draft version, agent log
├── compass-notes.md      ← Compass strategic direction (before Turing)
├── research.md           ← Turing's grounding document
├── headlines.md          ← Mark's hook and headline options
├── draft-v1.md           ← Caret's first draft
├── draft-v2.md           ← after first Caret/Mark loop
├── draft-v3.md           ← after second loop or user edits
├── brand-notes-v1.md     ← Mark's review of draft-v1
├── brand-notes-v2.md     ← Mark's review of draft-v2
├── critique-v2.md        ← Devil's audit — version matches draft reviewed
├── audience-v2.md        ← Echo's review — version matches draft reviewed
├── seo.md                ← Press Hugo front matter + SEO notes (slug also written to status.md)
├── image-prompt.txt      ← Prism's plain-text prompt for Gemini Image Pro
└── final.md              ← publish-ready
```

Draft versioning rule: **never overwrite a previous draft — always increment version numbers.**

---

## status.md Schema

```markdown
# [codename]
> [plain English description of the piece — one line, used by Index
>  to identify this piece without opening other files]

## Current State
- Current draft: draft-v2.md
- Last agent: Mark (brand-notes-v2.md) [REVISE]
- Brief intent: NOT YET MET
- Loop iterations: 2 of 2
- Slug: (written by Press — must match seo.md)
- Next step: Awaiting user direction (circuit breaker reached)

## Agent Run Log
- [x] Index → overlap check (no conflicts found)
- [x] Compass → compass-notes.md
- [x] Turing → research.md
- [x] Caret → draft-v1.md [research gate: PASSED]
- [x] Mark → headlines.md
- [x] Mark → brand-notes-v1.md (REVISE)
- [x] [user-edit] draft-v1.md → basis for draft-v2.md
- [x] Caret → draft-v2.md
- [x] Mark → brand-notes-v2.md (REVISE)
- [ ] Awaiting user direction (circuit breaker reached)
- [ ] Devil → critique-v1.md
- [ ] Echo → audience-v1.md
- [ ] Press → seo.md
- [ ] Prism → image-prompt.txt
- [ ] final.md
```

---

## Constraints

- All agent system prompts in plain markdown — no code, no JSON
- Stateless file-based architecture — agents read from and write to files
- Never overwrite a previous draft — always increment version numbers
- Press outputs valid Hugo YAML front matter matching the schema exactly
- image-prompt.txt: one plain paragraph, zero markdown formatting, consumed directly by GitHub Actions without parsing. After Prism writes image-prompt.txt, verify the file contains none of the characters: `#`, `*`, `` ` ``, `_`, `|`. If any are found, surface a warning before `MMW:proof` is accepted as valid.
- Caret/Mark loop maximum 2 iterations before surfacing to user
- Index runs before any other agent as an overlap gate, and always validates post-index.md before doing anything else
- Compass runs before Turing — research must be focused, not blind
- Caret never skips the research gate silently
- Co-edit: Caret never rewrites the user's edits without flagging
- Do not over-engineer — this is a writing tool first

---

## Success Criteria

When done, the following session must work end to end:

1. User types: `MMW write a post about building this writer's room`
2. Index validates post-index.md — reports N entries found
3. Index checks brief against post-index.md — no overlap found
4. Caret generates codename `writers-room-build`, creates folder, writes brief.md and status.md with plain English description
5. Compass reads brief.md → produces compass-notes.md with strategic direction and research priorities for Turing
6. Turing reads compass-notes.md → produces focused research.md
7. Turing surfaces 3 deep-dive candidates — user picks one (or steers with a prompt) → Turing appends deeper findings to research.md
8. Caret checks: research.md exists and is non-empty [GATE PASSED]
9. Caret reads brief.md, compass-notes.md, research.md → produces draft-v1.md
10. Mark reads draft-v1.md → produces headlines.md
11. Mark reviews draft-v1.md → brand-notes-v1.md [REVISE]
12. Loop pauses — user sees outstanding issues and options
13. User chooses [C] co-edit
14. Caret surfaces the exact flagged lines with current text and issue
15. User edits draft-v1.md directly
16. User types: MMW:done
17. Caret reads user-edited file → produces draft-v2.md
18. Caret reports exactly what it changed beyond the user's edits
19. Mark reviews draft-v2.md → brand-notes-v2.md [PASS]
20. Loop exits — brief intent met
21. Devil ║ Echo run in parallel:
    - Devil reads brief.md, research.md, draft-v2.md → critique-v2.md
    - Echo reads brief.md, draft-v2.md → audience-v2.md
22. User revision window — user edits or proceeds
23. Press ║ Prism run in parallel:
    - Press reads latest draft-vN.md → seo.md with valid Hugo YAML front matter + writes slug to status.md
    - Prism reads latest draft-vN.md → image-prompt.txt as one plain paragraph, zero markdown
24. User types: `MMW:proof writers-room-build`
25. Pre-flight check passes — draft, seo.md, slug, image-prompt.txt all present
26. final.md written and copied to `posts/drafts/writers-room-build.md`
27. Index ║ Cadence run in parallel:
    - Index updates post-index.md with new entry
    - Cadence logs codename, description, and target publish date in calendar.md
