# mmw Flow Spec — Workflow, Protocols, and File Schema

This file is the canonical source of truth for how mmw orchestrates its agents. Agent specs reference this file. When the workflow changes, change it here first.

---

## Invocation

This system responds to a single trigger: `mmw`

`mmw` launches Caret as the default entry point.

### Modes

- `mmw [topic | file path | bullet brainstorm]` — manual mode (default). Caret pauses after each phase and proposes the next step. The user decides when to advance.
- `mmw --auto [topic | file path | bullets]` — auto mode. Caret runs the full pipeline without pausing between phases. Stops at the proof gate (`mmw:proof`), which is always a human step.
- `mmw --auto --quick [topic | file path | bullets]` — auto-quick mode. Reduced-agent fast path for short posts or cheap first drafts. See Auto Quick Flow below.

**Input types**: After stripping flags, the remaining input may be:
- A topic string — current behavior
- A file path — Caret reads the file as the brief foundation, derives codename from content
- Bullet brainstorm items — Caret structures them into brief.md, then generates the codename

Caret strips `--auto` and `--quick` from the input before processing. If `--auto` is present, Caret writes `- Mode: auto` in `## Current State` of `status.md`. If `--auto --quick` are both present, Caret writes `- Mode: auto-quick`. Absence of both = manual mode.

On session resume, Caret reads `Mode:` from `## Current State` in `status.md`. The mode applies for all remaining phases and survives session boundaries.

### Sub-agent shortcuts (bypass Caret, go directly to an agent)

| Shortcut | Agent |
|---|---|
| `mmw:turing` | research |
| `mmw:devil` | critique |
| `mmw:echo` | audience check |
| `mmw:press` | publish prep |
| `mmw:prism` | image prompt generation |
| `mmw:compass` | strategy |
| `mmw:mark` | brand check |
| `mmw:cadence` | editorial calendar |
| `mmw:index` | archive and overlap check |
| `mmw:bearings [codename]` | session orientation — recap current state, propose next step, pause |

### Workflow gate
- `mmw:proof [codename]` → human declares draft final, triggers Phase 11 handoff

### Invocation model

Each `mmw:agent` shortcut invokes a **native Claude Code subagent** — an isolated subprocess with its own context window and tool permissions. Agent definition files live in `.claude/agents/` (not `writers-room/agents/`). State is passed exclusively through files in the piece folder — agents cannot share in-memory state across subprocess boundaries.

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
           Compass reads brief.md + post-index.md + calendar.md
           → compass-notes.md (includes ## Cadence Context)
           Caret surfaces one-line angle notice → Turing starts
           [S] Skip research — draft from compass-notes.md alone
   ↓
Phase 2 — Turing: focused research (reads compass-notes.md first)
           [auto: deep dive skipped | manual: deep dive pause offered]
   ↓
Phase 3 — Caret: draft-v1.md
           [research.md gate — must exist and be non-empty]
   ↓
Phase 3.5 — Echo: audience signal  [manual only, non-blocking]
             quick structural fit check → audience-signal.md
             result surfaced as advisory sidebar at Phase 4
   ↓
Phase 4 — Mark: headlines and hooks (reads draft-v1.md)
   ↓
Phase 5 — Iterative loop: Caret ↔ Mark
           [manual: user-driven exit — no iteration cap | co-edit available]
           [auto: 1 Mark pass only — REVISE applied directly, HOLD logged and exits]
   ↓
Phase 6+7 — Devil ║ Echo  [run in parallel]
            Devil: accusation audit → critique-vN.md
            Echo:  audience check  → audience-vN.md
   ↓
Phase 8 — User revision window
           [manual: Caret reads both critique-vN.md and audience-vN.md, pauses for user]
           [auto: Caret reads feedback, applies directly, produces new draft, logs summary]
           [T] Re-research — Turing gap-fill → re-enter Phase 5 loop → Phase 6+7 again
   ↓
Phase 8.5 — Mark: brand re-alignment check  [conditional — manual only]
             [skipped entirely in auto mode]
             [fires only if draft changed in Phase 8]
             [single pass — option to return to creative mode]
             Mark reads latest draft → writes brand-notes-final.md
             PASS → proceed | REVISE → one fix pass | HOLD → surface to user
   ↓
Phase 9+10 — Press ║ Prism  [run in parallel]
             Press: SEO and Hugo front matter → seo.md
             Prism: image prompt              → image-prompt.md
   ↓
[mmw:proof [codename] — human declares draft final]
   ↑ Caret proposes this exact command (with codename filled in)
     after Press + Prism both complete. Does not advance automatically.
   ↓
Phase 11 — Handoff: final.md → writers-room/published/[slug].md
                    image-prompt.md → writers-room/published/[slug]-image-prompt.md
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

Compass reads brief.md, `writers-room/index/post-index.md` (if exists), and `writers-room/cadence/calendar.md` (if exists). Compass produces compass-notes.md, which includes a `## Cadence Context` section derived from calendar.md. Turing reads compass-notes.md before starting any research.

See `specs/agent-compass.md` for full compass-notes.md content requirements.

---

## Phase 2 Transition — Angle Notice

After Compass completes and compass-notes.md is verified, Caret surfaces a one-line angle notice and immediately proceeds to Turing:

```
Compass has set the direction: [one-sentence angle from compass-notes.md]
Starting Turing — [S] to skip research.
```

**[S] Skip research**: If the user types [S] before Turing completes, Caret aborts the Turing spawn (or skips it if not yet started), logs `[skip] Phase 2 — user skipped research` in status.md, and proceeds to Phase 3. The research gate at Phase 3 will fire; the user must select [W] to draft from brief alone.

No acknowledgment required before Turing starts. To adjust the angle after Compass has run, use `mmw:compass [codename]` directly.

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

If research.md exists but is thin — measured by raw word count (all content including headers and bullets; no markdown stripping):
- **Manual mode**: thin = under 200 words
- **Auto / auto-quick mode**: thin = under 100 words (intentionally shallower research is expected)

Flag it:

```
research.md exists but appears brief ([N] words) — Turing may not have completed a full pass.

  [T] Run Turing again — deepen the research before drafting
  [W] Proceed with current research — draft from what's here
```

- Wait for user selection before continuing

**Never silently skip this check.**

### Drafting

Caret reads brief.md, compass-notes.md, and research.md before writing draft-v1.md. Caret follows the story arc: **hook → exploration → insight → deeper dive → reflection**.

### Phase 3.5 — Audience Signal [manual mode only]

After draft-v1.md is written and before Phase 4, Caret invokes Echo in quick mode:

```
mmw:echo [codename] --quick
```

Echo in `--quick` mode reads only brief.md and draft-v1.md. It writes `audience-signal.md` — a single paragraph answering one question: **does the structural shape of this draft match what the intended audience needs?** PASS or FLAG verdict only. No persona breakdown, no full audience review.

Caret does **not** surface the result at Phase 3.5. Echo runs silently. The result is held and surfaced as an advisory note at the start of Phase 4 — it does not block the writer from proceeding.

**Auto mode and auto-quick**: Phase 3.5 is skipped. Caret logs `[skip] Phase 3.5 — auto mode` in status.md.

---

## Phase 4 — Mark: Headlines

Mark reads draft-v1.md and produces headlines.md. The draft is the ground truth — headlines must reflect what the piece is actually about, not just the original brief.

If audience-signal.md exists (i.e., Phase 3.5 ran), Caret surfaces the Echo quick result as a sidebar before presenting Mark's headlines — no action required:

```
Audience signal (advisory): [PASS / FLAG — one sentence]
```

The writer can note it and continue. The signal is informational only at this point.

See `specs/agent-mark.md` for scoring criteria and brand rules.

---

## Phase 5 — Iterative Loop: Caret ↔ Mark

### Manual mode

This loop runs until the user decides to move on. There is no iteration cap.

### Auto mode

Caret runs exactly 1 Mark pass, then exits the loop:
- **REVISE**: Caret applies Mark's feedback directly (no pause), exits loop
- **PASS**: exit immediately, proceed to Devil and Echo
- **HOLD**: Caret pauses and surfaces the HOLD to the user:

```
[auto] Mark has issued a HOLD — structural issue that revision won't resolve.
[Specific issue from brand-notes]

  [C] Co-edit — address the structural issue directly
  [S] Skip — proceed to critique and audience review (HOLD logged in status.md)
```

Co-edit is not available in auto mode.

### Exit conditions (manual)

1. Mark issues a HOLD verdict — loop exits immediately. HOLD means the issue is structural, not a revision problem. Caret surfaces this to the user:

```
Mark has issued a HOLD — the issue is structural and revising won't resolve it.
[Specific issue from brand-notes]

  [B] Revisit brief — re-examine the premise (the angle is the problem, not the lines)
  [C] Co-edit — you take the keyboard and address the structural issue directly
  [M] Move to critique — proceed to Devil and Echo with current draft as-is
```
2. User selects [M] to move to critique — the only way to exit the loop without a HOLD

### Loop pause after every Mark review

After every Mark review, the loop PAUSES. The writer receives the pass label first, then options:

Pass 1 (desk mode):
```
Mark reviewed the draft.
Voice check — is this piece distinctly yours?
[verdict and specific findings from brand-notes]

  [C] Co-edit — Caret surfaces the specific lines, you edit the draft
       file directly, Caret reads your edits and produces the next version
  [R] Revise — Caret revises based on brand-notes alone, no user edits
  [M] Move to critique — send this draft to Devil and Echo for review
```

Pass 2+ (copy mode):
```
Mark reviewed the draft.
Polish pass — banned words, rhythm, pronouns
[verdict and specific findings from brand-notes]

  [C] Co-edit — Caret surfaces the specific lines, you edit the draft
       file directly, Caret reads your edits and produces the next version
  [R] Revise — Caret revises based on brand-notes alone, no user edits
  [M] Move to critique — send this draft to Devil and Echo for review
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

Before waiting, Caret writes two fields to status.md:
- `[in-progress] user-edit — awaiting mmw:done` (log entry via `status_log`)
- `co_edit_draft: [current draft filename]` (field via `status_write`, e.g. `{"co_edit_draft": "draft-v2.md"}`)

This ensures the co-edit state survives a session boundary. If the session ends before `mmw:done` is received, Caret will re-surface the co-edit prompt on resume rather than advancing to the next phase.

User signals completion by typing: `mmw:done` as a chat message. Caret listens for this signal in the conversation only — it does not scan file content for it. For posts about mmw itself, `mmw:done` may appear inside the draft file as an example; that does not trigger co-edit completion.

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

### Step 5 — Selective accept/reject

After Caret reports its changes in Step 4, the user may selectively reject individual items. Step 5 is a conversation-only exchange — the writer does not edit the draft file during this step.

```
draft-v3.md produced.

Your edits: preserved exactly as written.
Caret also addressed:
  1. Removed "additionally" from paragraph 3 (banned word not in your edit)
  2. Tightened transition between paragraph 5 and 6 per brand-notes

  [K] Keep all — accept Caret's changes and proceed
  [X] Reject one — specify item number to revert
```

**[X] Reject one**: Caret reverts only the named item, restoring the user's original text for that passage. Caret re-presents the list with the rejected item struck through. The loop continues until [K] or no remaining items. The final accepted state is written as the next versioned draft.

If the user wants to make further direct edits, they select [K] first to close Step 5, then begin a new co-edit round.

### Co-edit rules Caret must never break

- NEVER rewrite a passage the user just wrote without flagging it first
- NEVER silently change the user's phrasing in the name of brand compliance
- If a user's edit contains a banned word, flag it — do not delete it:
  > "You used 'leverage' in paragraph 2. This is a banned word per brand guidelines. Keep it, or would you like an alternative?"
- The user's voice overrides Mark's preferences when there is a conflict
- Caret's job in co-edit is to be the user's assistant, not their editor
- User edits are always recorded in status.md: `[user-edit] draft-v2.md → basis for draft-v3.md`
- Caret never re-argues a change the user rejected in Step 5; flags once if a banned word is kept, then moves on
- Caret does not edit the draft file during Step 2 (writer's turn) or between receiving `mmw:done` and completing Step 4

---

## Phase 6+7 — Devil + Echo [parallel]

Before spawning, Caret resolves the current latest draft filename once (highest-numbered draft-vN.md in the piece folder) and passes it explicitly to both subagents in the invocation. Agents must use the filename Caret passes — they do not scan for the latest draft themselves.

If invoked directly via `mmw:devil` or `mmw:echo`, they resolve independently by scanning for the highest-numbered draft-vN.md.

Before spawning, Caret writes to status.md: `[partial] Devil → pending, Echo → pending`

Caret spawns Devil and Echo as concurrent subagents. Both receive the same codename and the same explicit draft filename. Neither reads the other's output. As each completes and its output is verified, Caret replaces its `pending` entry with the full completion log entry. Caret waits for both to complete before proceeding to Phase 8. If one fails, the `[partial]` marker persists as a resume signal — on session resume, Caret reads it and knows which agent to re-run.

See `specs/agent-devil.md` and `specs/agent-echo.md` for full audit and review criteria.

---

## Phase 8 — User Revision Window

### Auto mode

Caret reads critique-vN.md and audience-vN.md, applies the feedback directly (no pause), produces a new versioned draft, and logs a one-line summary in status.md: `[auto] Phase 8 revision applied → draft-vN.md`. Phase 8.5 does not run in auto mode. Caret proceeds directly to Phase 9+10.

### Manual mode

After Devil and Echo complete, Caret pauses and surfaces the feedback files directly:

```
Devil and Echo have reviewed [draft-vN.md].

Feedback files:
  critique-vN.md (Devil)
  audience-vN.md (Echo)

  [C] Co-edit — Caret surfaces the flagged passages, you edit the draft directly
  [R] Revise — Caret revises using Devil and Echo's feedback
  [T] Re-research — Turing runs a targeted gap-fill, then re-enter the draft loop
  [F] Fact-check — Turing checks draft claims against research.md  ← only shown if Devil flagged credibility concerns
  [P] Proceed to Press and Prism
  [X] Prioritize — Caret synthesizes Must / Worth / Already Working Well
```

**[X] Prioritize**: On request, Caret synthesizes critique-vN.md and audience-vN.md into a structured triage before the writer chooses an action:
- **Must address before publishing**: Devil's REVISE items + Echo persona bounce points
- **Worth addressing if time allows**: Devil's Challenge Questions + minor Echo notes
- **Already working well**: Devil's positive Persona Reactions + Echo passing assessments

**[F] Fact-check** is shown only if Devil flagged credibility concerns in critique-vN.md. See flow.md § Turing Fact-Check Sub-mode.

**[T] Re-research**: Caret invokes Turing with a targeted gap-fill prompt. The prompt is derived from Devil's and Echo's flags when triggered via menu, or from the writer's own prompt when the writer types it directly (e.g., "I need more on [specific topic] before revising"). Turing appends new findings to research.md — it does not overwrite it. Caret logs `[loop] re-research → Turing gap-fill` in status.md. After Turing completes, Caret re-enters the Phase 5 loop on the latest draft. On [M] exit, flow continues through Phase 6+7 again (Devil and Echo re-run on the new draft).

If [C] or [R]: Caret produces a new versioned draft using Devil + Echo feedback (+ fact-check-vN.md if it exists). Caret reports what it addressed from each feedback file, then asks:

```
Draft updated → draft-vN.md

  [B] Brand check — run Mark on the updated draft
  [L] Back to draft — re-enter the Mark loop for more drafting passes
  [P] Proceed to Press and Prism
```

If [P] without producing a new draft: Press reads the existing latest draft. Caret does not increment the draft version without a reason. Before proceeding, Caret offers:

```
  [B] Brand check first — run Mark, then proceed to Press and Prism
  [P] Proceed to Press and Prism
```

---

## Phase 8.5 — Mark: Brand Re-Alignment Check [user-initiated — manual only]

**Auto mode**: Phase 8.5 does not run. Caret logs `[skip] Phase 8.5 — auto mode` in status.md and proceeds directly to Press and Prism.

### When it fires (manual mode only)

Phase 8.5 fires when the user selects `[B] Brand check` from the Phase 8 menu (available after a [C] or [R] revision produces a new draft, and also as a pre-proceed option before [P]). Caret does not trigger Phase 8.5 automatically — no filename comparison, no heuristic.

Caret logs `[user] Phase 8.5 — brand check requested` in status.md and spawns Mark as a subagent, passing the latest draft filename explicitly.

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

  [L] Back to draft — re-enter the Phase 5 loop for more drafting passes
  [P] Proceed to Press and Prism
```

**HOLD** — same as Phase 5 HOLD handling. Caret surfaces:

```
Mark has issued a HOLD on the final draft — the issue is structural and revising won't resolve it.
[Specific issue from brand-notes-final.md]

  [B] Revisit brief — re-examine the premise (the angle is the problem)
  [C] Co-edit — you take the keyboard and address the structural issue directly
  [P] Proceed to Press and Prism — skip the fix
```

**REVISE** — Caret presents the issues and offers one fix pass. No loop:

```
Mark flagged issues in brand-notes-final.md:
  1. [specific issue]
  2. [specific issue]

  [C] Co-edit — Caret surfaces the specific lines, you edit directly
  [R] Revise — Caret applies Mark's feedback from brand-notes-final.md directly
  [P] Proceed to Press and Prism — skip the fix
```

If [C] or [R]: Caret produces a new versioned draft, then asks:

```
Draft updated → draft-vN.md

  [L] Back to draft — re-enter the Phase 5 loop for more drafting passes
  [P] Proceed to Press and Prism
```

If [L]: Caret logs `[loop restart] draft re-entry from brand check` in status.md and re-enters Phase 5 on the latest draft. On exit ([M] Move to critique), flow continues through Devil/Echo → revision window → brand check as normal (brand check fires again only if the revision window produces a new draft).

If [P] (after PASS or after [C]/[R]): Caret proceeds to Phase 9+10.

If [P] from HOLD or REVISE (skip the fix): Caret logs `[user override] brand re-alignment: skipped by user` in status.md and proceeds to Phase 9+10.

### What does NOT happen here

- No second Mark review after a [C] or [R] fix within this phase — [L] re-enters the full draft loop, it does not re-run Mark here
- No re-running of Devil or Echo from within this phase — they run again naturally after the draft loop exits
- Co-edit follows the same rules as Co-edit Mode — user voice is never overridden

---

## Turing Fact-Check Sub-mode [manual only, opt-in from Phase 8]

Triggered when the user selects [F] at the Phase 8 triage. Only offered if Devil flagged credibility concerns in critique-vN.md.

```
[User selects [F] at Phase 8]
    ↓
mmw:turing [codename] --fact-check
    ↓
Turing reads research.md + latest draft-vN.md
    ↓
→ fact-check-vN.md (version matches draft reviewed)
    ┌─ ## Confirmed
    │    [claim] — supported by [source in research.md]
    ├─ ## Ungrounded
    │    [claim] — not in research.md; needs citation or removal
    │    → user can run: mmw:turing [codename] --find-citation "[claim text]"
    │      Turing searches, appends result to fact-check-vN.md
    │      If found: moves claim to Confirmed. If not: notes inconclusive.
    └─ ## Inaccurate
         [claim] — contradicts/oversimplifies research.md: [what research says]
    ↓
Caret reads fact-check-vN.md alongside critique-vN.md + audience-vN.md
Addresses all three in one combined revision pass when producing next draft
Caret reports what it addressed from each feedback file
    ↓
[C] Co-edit or [R] Revise continues with all feedback available
```

**Auto mode**: Does not run.

---

## Auto Mode — Full Flow

```
mmw --auto [topic | file | bullets]
    ↓
[Phase 0] Index — overlap gate (same as manual)
    ↓
[Phase 1] Compass — reads brief.md + post-index.md + calendar.md → compass-notes.md
    ↓
[Phase 2] Turing — research → research.md (deep dive: SKIPPED)
    ↓
[Phase 3] Caret — first draft → draft-v1.md
    [Phase 3.5 audience signal: SKIPPED — logs [skip] Phase 3.5 — auto mode]
    ↓
[Phase 4] Mark — headlines → headlines.md
    ↓
[Phase 5] Mark — 1 pass, copy mode (polish: banned words, rhythm, pronouns)
    REVISE → Caret revises directly, no pause, exits loop
    PASS   → exit immediately
    HOLD   → surface to user: [C] Co-edit or [S] Skip (HOLD logged if skipped)
    ↓
[Phase 6+7] Devil ║ Echo — parallel
    Devil → critique-vN.md
    Echo  → audience-vN.md (The Executive + The Builder)
    ↓
[Phase 8] Auto revision
    Caret reads critique-vN.md + audience-vN.md
    Revises directly, no pause → new draft-vN.md
    Logs [auto] Phase 8 revision applied → draft-vN.md
    [No fact-check]
    [Phase 8.5 SKIPPED — logs [skip] Phase 8.5 — auto mode]
    ↓
[Phase 9+10] Press ║ Prism — parallel
    ↓
[mmw:proof [codename]] — human gate
    ↓
[Phase 11] (same as manual, including image-prompt copy)
    ↓
  Done
```

---

## Auto Quick Flow (`mmw --auto --quick`)

```
mmw --auto --quick [topic | file | bullets]
    ↓
[Phase 0] Index — overlap gate (always runs)
    [Phase 1 Compass: SKIPPED — logs [skip] Phase 1 — auto-quick mode]
    ↓
[Phase 2] Turing — single focused search only (no deep dive)
    → research.md
    ↓
[Phase 3] Caret — first draft → draft-v1.md
    (drafts from brief + research; no compass-notes.md)
    ↓
[Phase 3.5] Echo --quick → audience-signal.md
    PASS → log [auto-quick] Echo PASS — continue, proceed silently
    FLAG → surface to user:
      [auto-quick] Echo FLAG: [one sentence]
        [C] Revise opening — Caret addresses the flag, produces draft-v2.md
        [S] Skip — proceed to Press and Prism with flag noted in status.md
    [Phase 4 Mark headlines: SKIPPED — logs [skip] Phase 4 — auto-quick mode]
    [Phase 5 Mark loop: SKIPPED — logs [skip] Phase 5 — auto-quick mode]
    [Phase 6+7 Devil+Echo: SKIPPED — logs [skip] Phase 6+7 — auto-quick mode]
    [Phase 8 revision window: SKIPPED — logs [skip] Phase 8 — auto-quick mode]
    [Phase 8.5: SKIPPED — logs [skip] Phase 8.5 — auto-quick mode]
    ↓
[Phase 9+10] Press ║ Prism — parallel
    ↓
[mmw:proof [codename]] — human gate
    ↓
[Phase 11] (same as manual)
    ↓
  Done
```

status.md writes `- Mode: auto-quick` at initialization.

**Draft elaborator use case**: Run `mmw --auto --quick [topic]` to produce a cheap complete draft. Then `mmw [codename]` to continue in manual mode — the full pipeline picks up from the existing draft-v1.md. Use this when starting from a blank page feels slow or when you need a concrete artifact to react to before committing to a full run.

**Deadline-constrained auto**: If `calendar.md` contains a target publish date for this piece and it is <3 days away, auto mode activates the quick path automatically. Caret logs: `[auto] Publish deadline in N days — fast path activated` in status.md and proceeds as auto-quick. This only applies when the piece has a calendar entry with a target date; if no entry exists, auto mode runs at full depth.

At auto mode startup (before Phase 0), Caret reads `writers-room/cadence/calendar.md`. If the codename appears with a target date and that date is <3 days from today: auto-quick is activated regardless of whether `--quick` was passed. If >3 days (or no calendar entry): full auto mode runs as normal.

---

## Phase 9+10 — Press + Prism [parallel]

Before spawning, Caret resolves the current latest draft filename once (highest-numbered draft-vN.md in the piece folder) and passes it explicitly to both subagents in the invocation. Agents must use the filename Caret passes — they do not scan for the latest draft themselves.

If invoked directly via `mmw:press` or `mmw:prism`, they resolve independently by scanning for the highest-numbered draft-vN.md.

Before spawning, Caret writes to status.md: `[partial] Press → pending, Prism → pending`

Caret spawns Press and Prism as concurrent subagents. Both receive the same codename and the same explicit draft filename. Press writes seo.md. Prism writes image-prompt.md. Neither reads the other's output. As each completes, Caret replaces its `pending` entry with the full completion log entry. Caret waits for both before the mmw:proof gate is valid. If one fails, the `[partial]` marker persists as a resume signal.

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
├── compass-notes.md      ← Compass strategic direction (before Turing); includes ## Cadence Context
├── research.md           ← Turing's grounding document
├── headlines.md          ← Mark's hook and headline options
├── draft-v1.md           ← Caret's first draft
├── audience-signal.md    ← Echo's structural fit check (Phase 3.5, manual only; not versioned)
├── draft-v2.md           ← after first Caret/Mark loop
├── draft-v3.md           ← after second loop or user edits
├── brand-notes-v1.md     ← Mark's review of draft-v1
├── brand-notes-v2.md     ← Mark's review of draft-v2
├── brand-notes-final.md  ← Mark's re-alignment check (Phase 8.5, conditional)
├── critique-v2.md        ← Devil's audit — version matches draft reviewed
├── audience-v2.md        ← Echo's review — version matches draft reviewed
├── fact-check-vN.md      ← Turing's fact-check (opt-in, manual only, version matches draft reviewed)
├── seo.md                ← Press Hugo front matter + SEO notes (slug also written to status.md)
├── image-prompt.md       ← Prism's image prompt for Gemini Image Pro (one focused paragraph)
└── final.md              ← publish-ready
```

```
writers-room/published/
├── [slug].md             ← clean copy of final.md
└── [slug]-image-prompt.md ← copy of image-prompt.md (written at Phase 11)
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
- Phase: 3 — Caret first draft
- Mode: auto    ← only present in auto mode; absent = manual
- Current draft: draft-v1.md
- co_edit_draft: draft-v1.md  ← transient; set only while awaiting mmw:done; cleared on resume
- Slug: (written by Press)
- Next step: Awaiting user direction

## Agent Run Log
- [x] Index → overlap check (no conflicts found)
- [x] Compass → compass-notes.md
- [x] Turing → research.md
- [x] Caret → draft-v1.md [research gate: PASSED]
```

The Agent Run Log contains only completed entries, written as each phase finishes. Pending phases are implied by absence — do not pre-populate future entries.

The `- Slug: (written by Press)` line is an exact-string placeholder. Press locates it by literal match and replaces it with `- Slug: [slug-value]`. Do not add comments or extra text to this line — any variation will cause Press's slug sync to fail silently. Press is solely responsible for keeping the slug in status.md in sync with seo.md.

After Press and Prism both complete, Caret writes `Next step: Ready for mmw:proof [codename]` to status.md. This is the exact string Caret scans for when `mmw:proof` is called without a codename.

---

## Manual Mode: Next-Step Prompts

In manual mode, Caret always surfaces a concrete proposed next step after each phase completes. It never goes silent after a completion. Format:

```
[Phase N complete] [what was produced]

Proposed next step: [specific action]
  [C] Continue — [what C does]
  [S] Stop and review — pause here

  → [pre-filled command to continue, e.g. "mmw:devil writers-room-build"]
```

The pre-filled command is always shown so the user can copy it to a new session if needed.

---

## Constraints

- All agent system prompts in plain markdown — no code, no JSON
- Stateless file-based architecture — agents read from and write to files
- Never overwrite a previous draft — always increment version numbers
- Press outputs valid Hugo YAML front matter matching the schema exactly
- image-prompt.md: one focused paragraph — no headers, no bullets, no code fences
- Caret/Mark loop has no iteration cap in manual mode — the user exits explicitly with [M] Move to critique
- Auto mode: Phase 5 loop cap = 1 pass; Phase 8.5 skipped; Phase 8 applied without pause
- Index runs before any other agent as an overlap gate, and always validates post-index.md before doing anything else
- Compass runs before Turing — research must be focused, not blind
- Caret never skips the research gate silently
- Co-edit: Caret never rewrites the user's edits without flagging; co-edit not available in auto mode
- Do not over-engineer — this is a writing tool first

---

*Success criteria live in `prompts/mmw-build-prompt.md` § Validation — build-time only, not needed at runtime.*
