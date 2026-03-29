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
| `MMW:bearings [codename]` | session orientation — recap current state, propose next step, pause |

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
           [user-driven exit — no iteration cap]
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
Phase 8.5 — Mark: brand re-alignment check  [conditional]
             [fires only if draft changed in Phase 8]
             [single pass — option to return to creative mode]
             Mark reads latest draft → writes brand-notes-final.md
             PASS → proceed | REVISE → one fix pass | HOLD → surface to user
   ↓
Phase 9+10 — Press ║ Prism  [run in parallel]
             Press: SEO and Hugo front matter → seo.md
             Prism: image prompt              → image-prompt.md
   ↓
[MMW:proof [codename] — human declares draft final]
   ↑ Caret proposes this exact command (with codename filled in)
     after Press + Prism both complete. Does not advance automatically.
   ↓
Phase 11 — Handoff: final.md → writers-room/published/[slug].md
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

```
research.md is missing — Turing has not run for this piece.

  [T] Run Turing now — start a focused research pass before drafting
  [W] Proceed without research — draft from the brief alone (not recommended)
```

- Wait for user selection before continuing

If research.md exists but appears thin (under 200 words):
- Flag it:

```
research.md exists but appears brief (under 200 words) — Turing may not have completed a full pass.

  [T] Run Turing again — deepen the research before drafting
  [W] Proceed with current research — draft from what's here
```

- Wait for user selection before continuing

**Never silently skip this check.**

### Drafting

Caret reads brief.md, compass-notes.md, and research.md before writing draft-v1.md. Caret follows the story arc: **hook → exploration → insight → deeper dive → reflection**.

---

## Phase 4 — Mark: Headlines

Mark reads draft-v1.md and produces headlines.md. The draft is the ground truth — headlines must reflect what the piece is actually about, not just the original brief.

See `specs/agent-mark.md` for scoring criteria and brand rules.

---

## Phase 5 — Iterative Loop: Caret ↔ Mark

This loop runs until the user decides to move on. There is no iteration cap.

### Exit conditions

1. Mark issues a HOLD verdict — loop exits immediately. HOLD means the issue is structural, not a revision problem. Caret surfaces this to the user:

```
Mark has issued a HOLD — the issue is structural and revising won't resolve it.
[Specific issue from brand-notes]

  [B] Revisit the brief — go back to brief.md and rethink the angle before continuing
  [C] Co-edit — you take the keyboard and address the structural issue directly
  [S] Proceed to critique anyway — send this draft to Devil and Echo as-is
```
2. User selects [N] to move to critique — the only way to exit the loop

### Loop pause after every Mark review

After every Mark review, the loop PAUSES. The user receives:

```
Mark has reviewed draft-vN.md → brand-notes-vN.md [REVISE / PASS]

Outstanding issues (if REVISE):
  1. [specific issue Mark flagged]
  2. [specific issue Mark flagged]

Brief intent check: [MET / NOT YET MET]

Your options:
  [C] Co-edit — Caret surfaces the specific lines, you edit the draft
       file directly, Caret reads your edits and produces the next version
  [R] Revise — Caret revises based on brand-notes alone, no user edits
  [N] Move to critique — send this draft to Devil and Echo for review
```

All three options are available regardless of PASS or REVISE verdict. The user chooses when they are done.

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

Before spawning, Caret writes to status.md: `[partial] Devil → pending, Echo → pending`

Caret spawns Devil and Echo as concurrent subagents. Both receive the same codename and the same explicit draft filename. Neither reads the other's output. As each completes and its output is verified, Caret replaces its `pending` entry with the full completion log entry. Caret waits for both to complete before proceeding to Phase 8. If one fails, the `[partial]` marker persists as a resume signal — on session resume, Caret reads it and knows which agent to re-run.

See `specs/agent-devil.md` and `specs/agent-echo.md` for full audit and review criteria.

---

## Phase 8 — User Revision Window

After Devil and Echo complete, Caret reads critique-vN.md and audience-vN.md, then presents a consolidated feedback summary and pauses:

```
Devil and Echo have reviewed [draft-vN.md].

Key findings:
  Devil: [1–3 bullet summary of the sharpest accusations from critique-vN.md]
  Echo:  [1–3 bullet summary of the top audience concerns from audience-vN.md]

What would you like to do?

  [C] Co-edit — Caret surfaces the flagged passages, you edit the draft directly
  [R] Revise — Caret rewrites the flagged sections based on Devil and Echo's feedback
  [P] Proceed to publish prep — move to Press and Prism with the current draft as-is
```

If [C] or [R]: Caret produces a new versioned draft before handing off to Press.

If [P]: Press reads the existing latest draft — no new version is created. Caret does not increment the draft version without a reason.

---

## Phase 8.5 — Mark: Brand Re-Alignment Check [conditional]

### When it fires

After Phase 8 completes, Caret compares the draft filename passed to Devil/Echo at Phase 6+7 against the highest-numbered draft in the piece folder. If a new draft version was produced during Phase 8, Phase 8.5 fires. If no new draft exists (the user chose to proceed as-is), Phase 8.5 is skipped entirely. Caret logs the outcome in status.md:

- Skipped: `[skip] Phase 8.5 — no draft change in Phase 8`
- Fired: Caret spawns Mark as a subagent, passing the latest draft filename explicitly

### What Mark reads

- latest draft-vN.md (passed explicitly by Caret)
- brief.md

Mark does not read critique-vN.md or audience-vN.md. The scope is brand alignment only — what may have drifted since Phase 5.

### What Mark writes

`brand-notes-final.md` — same PASS/REVISE/HOLD format as Phase 5 brand-notes-vN.md, focused on drift since Phase 5. Mark does not relitigate issues already resolved in the Phase 5 loop.

### Verdict handling

**PASS** — Caret logs the result to status.md and asks:

```
Mark: PASS on brand alignment.

  [L] Back to creative mode — keep working with Mark before publishing
  [P] Move to publish prep — run Press and Prism on the current draft
```

**HOLD** — same as Phase 5 HOLD handling. Caret surfaces:

```
Mark has issued a HOLD on the final draft — the issue is structural and revising won't resolve it.
[Specific issue from brand-notes-final.md]

  [B] Revisit the brief — go back to brief.md and rethink the angle before continuing
  [C] Co-edit — you take the keyboard and address the structural issue directly
  [S] Proceed to Press anyway — skip the brand fix and move to publish prep
```

**REVISE** — Caret presents the issues and offers one fix pass. No loop:

```
Mark flagged issues in brand-notes-final.md:
  1. [specific issue]
  2. [specific issue]

  [C] Co-edit — Caret surfaces the specific lines, you edit directly
  [A] Apply — Caret applies Mark's feedback from brand-notes-final.md directly
  [S] Proceed anyway — go to Press with the current draft
```

If [C] or [A]: Caret produces a new versioned draft, then asks:

```
Draft updated → draft-vN.md

  [L] Back to creative mode — keep working with Mark before publishing
  [P] Move to publish prep — run Press and Prism on the current draft
```

If [L]: Caret logs `[loop restart] creative mode re-entry from brand check` in status.md and re-enters Phase 5 on the latest draft. On exit ([N] Move to critique), flow continues through Devil/Echo → revision window → brand check as normal (brand check fires again only if the revision window produces a new draft).

If [P] (after PASS or after [C]/[A]): Caret proceeds to Phase 9+10.

If [S]: Caret logs `[user override] brand re-alignment: skipped by user` in status.md and proceeds to Phase 9+10.

### What does NOT happen here

- No second Mark review after a [C] or [A] fix within this phase — [L] re-enters the full creative loop, it does not re-run Mark here
- No re-running of Devil or Echo from within this phase — they run again naturally after the creative loop exits
- Co-edit follows the same rules as Co-edit Mode — user voice is never overridden

---

## Phase 9+10 — Press + Prism [parallel]

Before spawning, Caret resolves the current latest draft filename once (highest-numbered draft-vN.md in the piece folder) and passes it explicitly to both subagents in the invocation. Agents must use the filename Caret passes — they do not scan for the latest draft themselves.

If invoked directly via `MMW:press` or `MMW:prism`, they resolve independently by scanning for the highest-numbered draft-vN.md.

Before spawning, Caret writes to status.md: `[partial] Press → pending, Prism → pending`

Caret spawns Press and Prism as concurrent subagents. Both receive the same codename and the same explicit draft filename. Press writes seo.md. Prism writes image-prompt.md. Neither reads the other's output. As each completes, Caret replaces its `pending` entry with the full completion log entry. Caret waits for both before the MMW:proof gate is valid. If one fails, the `[partial]` marker persists as a resume signal.

See `specs/agent-press.md` and `specs/agent-prism.md` for full output requirements.

---

## Phase 11 — Handoff

See `specs/agent-caret.md` for the full pre-flight check, handoff steps, and parallel Index ║ Cadence spawn.

When Index updates `post-index.md` at Phase 11, it pulls the plain-English description from the `> [one line]` field in `status.md` — not the title from seo.md. This description is what Compass and Index use in future pieces to identify thematic adjacency.

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
├── brand-notes-final.md  ← Mark's re-alignment check (Phase 8.5, conditional)
├── critique-v2.md        ← Devil's audit — version matches draft reviewed
├── audience-v2.md        ← Echo's review — version matches draft reviewed
├── seo.md                ← Press Hugo front matter + SEO notes (slug also written to status.md)
├── image-prompt.md       ← Prism's image prompt for Gemini Image Pro (one focused paragraph)
└── final.md              ← publish-ready
```

Draft versioning rule: **never overwrite a previous draft — always increment version numbers.**

---

## post-index.md Schema

`writers-room/index/post-index.md` is a markdown table maintained by Index. Each row represents one published piece:

| Title | Slug | Date | Tags | Description |
|---|---|---|---|---|
| click-hook title | url-slug | YYYY-MM-DD | tag1, tag2 | plain-English description of what the piece actually covers — from status.md |

- **Title**: the published headline (click-hook — not reliable for content scanning)
- **Slug**: URL slug from seo.md
- **Date**: publish date
- **Tags**: from Hugo front matter
- **Description**: the `> [one line]` field from status.md — source of truth for what the piece covers. This is what Compass and Index use to identify thematic adjacency without reading every published file.

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
- Slug: (written by Press)
- Next step: Awaiting user direction

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
- [ ] Awaiting user direction ([N] Move to critique)
- [ ] Devil → critique-v1.md
- [ ] Echo → audience-v1.md
- [ ] [skip] Phase 8.5 — no draft change in Phase 8
  (or: [x] Mark → brand-notes-final.md (PASS))
  (or: [x] Mark → brand-notes-final.md (REVISE) → Caret produced draft-vN.md)
  (or: [x] Mark → brand-notes-final.md (REVISE) → user proceeded as-is)
- [ ] Press → seo.md
- [ ] Prism → image-prompt.md
- [ ] final.md
```

The `- Slug: (written by Press)` line is an exact-string placeholder. Press locates it by literal match and replaces it with `- Slug: [slug-value]`. Do not add comments or extra text to this line — any variation will cause Press's slug sync to fail silently. Press is solely responsible for keeping the slug in status.md in sync with seo.md.

After Press and Prism both complete, Caret writes `Next step: Ready for MMW:proof [codename]` to status.md. This is the exact string Caret scans for when `MMW:proof` is called without a codename.

---

## Constraints

- All agent system prompts in plain markdown — no code, no JSON
- Stateless file-based architecture — agents read from and write to files
- Never overwrite a previous draft — always increment version numbers
- Press outputs valid Hugo YAML front matter matching the schema exactly
- image-prompt.md: one focused paragraph — no headers, no bullets, no code fences
- Caret/Mark loop has no iteration cap — the user exits explicitly with [N]
- Index runs before any other agent as an overlap gate, and always validates post-index.md before doing anything else
- Compass runs before Turing — research must be focused, not blind
- Caret never skips the research gate silently
- Co-edit: Caret never rewrites the user's edits without flagging
- Do not over-engineer — this is a writing tool first

---

*Success criteria live in `prompts/mmw-build-prompt.md` § Validation — build-time only, not needed at runtime.*
