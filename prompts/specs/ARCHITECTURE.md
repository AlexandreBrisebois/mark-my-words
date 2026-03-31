# Mark My Words — System Architecture

Mark My Words (mmw) is a multi-agent writing system built on Claude Code. Caret orchestrates a set of specialized subagents that run in isolated subprocesses, communicating exclusively through files in the piece folder. There is no in-memory state passing between agents — the file system is the memory.

---

## Agents

| Agent | Role | Model |
|---|---|---|
| **Caret** | Orchestrator + Writer | claude-sonnet-4-6 |
| **Compass** | Strategist — editorial direction | claude-sonnet-4-6 |
| **Turing** | Researcher | claude-opus-4-6 |
| **Mark** | Brand + Voice Guardian | claude-sonnet-4-6 |
| **Devil** | Adversarial Auditor | claude-sonnet-4-6 |
| **Echo** | Audience Evaluator | claude-sonnet-4-6 |
| **Press** | Publisher (Hugo/SEO) | claude-haiku-4-5-20251001 |
| **Prism** | Visual Brand Agent | claude-sonnet-4-6 |
| **Index** | Archivist + Overlap Gate | claude-sonnet-4-6 |
| **Cadence** | Scheduler | claude-haiku-4-5-20251001 |

Agent definition files live in `.claude/agents/`. Each file contains YAML frontmatter with `name`, `description`, `model`, and `tools` fields. Claude Code reads these files to register agents and enforce tool scoping.

---

## Invocation Model

`mmw` is the only recognized trigger. `MMW` and `Mark My Words` are not triggers.

When the user types `mmw [input]`, Caret starts as the entry point. Caret strips flags, determines the input type, generates a codename, and routes the piece through the pipeline.

Caret spawns subagents using the Agent tool. Each subagent is an isolated subprocess with its own context window. Caret passes the codename explicitly in every spawn — subagents cannot discover the codename themselves.

Slash commands (registered as Skills in `.claude/skills/`) provide guaranteed routing to specific agents. Plain-text `mmw:agent` variants work as fallbacks when skills are not loaded.

---

## Invocation Modes

### Manual Mode (default)

```
mmw [topic | file path | bullet brainstorm]
```

Caret pauses after each phase and proposes the next step. The user decides when to advance. Co-edit mode is fully available. No iteration cap on the Mark loop.

### Auto Mode

```
mmw --auto [topic | file path | bullets]
```

Caret runs the full pipeline without pausing between phases. Key differences from manual:
- Phase 3.5 (audience signal): skipped — logs `[skip] Phase 3.5 — auto mode`
- Phase 5 loop cap: 1 Mark pass only. REVISE → applied directly, no pause. PASS → exit immediately. HOLD → surfaces to user (co-edit not available except at HOLD)
- Phase 8: Caret reads critique and audience feedback, applies directly without pause, produces new draft, logs `[auto] Phase 8 revision applied → draft-vN.md`
- Phase 8.5: skipped — logs `[skip] Phase 8.5 — auto mode`
- `mmw:proof` is always a human gate — auto mode stops and waits

A Mark HOLD verdict is logged in status.md but does not pause the workflow if the user skips. Auto mode may produce drafts with unresolved structural flags. Use manual mode for complex or high-stakes pieces.

### Auto-Quick Mode

```
mmw --auto --quick [topic | file path | bullets]
```

Reduced-agent fast path for short posts or cheap first drafts. Status.md writes `- Mode: auto-quick`.

Phases run:
- Phase 0 (Index) — always runs
- Phase 2 (Turing) — single focused search only, no deep dive
- Phase 3 (Caret) — drafts from brief + research only; no compass-notes.md
- Phase 3.5 (Echo --quick) — audience signal; FLAG surfaces a one-time revise/skip choice
- Phase 9+10 (Press ║ Prism) — parallel
- `mmw:proof` — human gate
- Phase 11 — handoff

Phases skipped (each logged in status.md):
- `[skip] Phase 1 — auto-quick mode` (Compass)
- `[skip] Phase 4 — auto-quick mode` (Mark headlines)
- `[skip] Phase 5 — auto-quick mode` (Mark loop)
- `[skip] Phase 6+7 — auto-quick mode` (Devil + Echo)
- `[skip] Phase 8 — auto-quick mode` (revision window)
- `[skip] Phase 8.5 — auto-quick mode`

**Draft elaborator use case**: Run `mmw --auto --quick [topic]` to produce a cheap complete draft. Then `mmw [codename]` to continue in manual mode — the full pipeline picks up from the existing draft.

### Deadline-Constrained Auto Upgrade

In auto mode only (not already auto-quick), before Phase 0, Caret reads `writers-room/cadence/calendar.md`. If the codename appears with a target date <3 days from today, Caret upgrades mode to auto-quick and logs `[auto] Publish deadline in N days — fast path activated` in status.md. If no calendar entry exists, auto runs at full depth.

This check runs at startup only — not on session resume.

### Discovery Mode

```
mmw --discovery [topic | file path | bullets]
mmw --discovery --auto [...]
```

Discovery runs before Phase 0. Caret generates three distinct briefs (`brief-discovery-1.md`, `brief-discovery-2.md`, `brief-discovery-3.md`), spawns Compass once across all three, and presents a selection menu. The user picks one angle before the pipeline proceeds.

Incompatible with `--quick` — Caret rejects `mmw --discovery --quick`.

---

## Full Ordered Workflow

```
brief.md written by Caret
   ↓
Phase 0 — Index: overlap gate
   ↓
Phase 1 — Compass: strategic direction [SKIPPED in auto-quick]
           compass-notes.md (includes ## Cadence Context from calendar.md)
           → Caret surfaces one-line angle notice → Turing starts
           [S] Skip research — draft from compass-notes.md alone
   ↓
Phase 2 — Turing: research
           [auto: deep dive skipped]
           [auto-quick: single focused search only]
           [manual: deep dive pause offered if warranted]
   ↓
Phase 3 — Caret: draft-v1.md
           [research.md gate — must exist and be non-empty before drafting]
   ↓
Phase 3.5 — Echo --quick: audience signal [manual only; SKIPPED in auto/auto-quick]
             → audience-signal.md (PASS / FLAG)
             result surfaced as advisory sidebar at Phase 4 — does not block
             [auto-quick: runs; FLAG surfaces revise/skip choice]
   ↓
Phase 4 — Mark: headlines.md [SKIPPED in auto-quick]
   ↓
Phase 5 — Iterative loop: Caret ↔ Mark [SKIPPED in auto-quick]
           [manual: user-driven exit — no iteration cap; co-edit available]
           [auto: 1 Mark pass only — copy mode; REVISE applied directly; HOLD surfaced]
           Loop pause format: "Voice check — is this piece distinctly yours?" (pass 1)
                              "Polish pass — banned words, rhythm, pronouns" (pass 2+)
   ↓
Phase 6+7 — Devil ║ Echo [parallel] [SKIPPED in auto-quick]
            critique-vN.md (Devil: accusation audit — 4 sections)
            audience-vN.md (Echo: 5 questions × 2 personas + cross-persona)
   ↓
Phase 8 — User revision window [SKIPPED in auto-quick]
           [manual: Caret surfaces feedback, pauses; [F] fact-check if credibility concerns]
           [auto: feedback applied directly, new draft, no pause]
           [T] Re-research → Turing gap-fill → re-enter Phase 5 loop → Phase 6+7 again
   ↓
Phase 8.5 — Mark brand re-alignment check [manual only; user-initiated; SKIPPED in auto/auto-quick]
             conditional: fires only when user selects [B] Brand check from Phase 8 menu
             → brand-notes-final.md
   ↓
Phase 9+10 — Press ║ Prism [parallel]
             Press → seo.md (Hugo YAML front matter + SEO recommendations)
                   → Slug written to status.md via Edit-tool exact-string replace
             Prism → image-prompt.md (one focused paragraph, no markdown)
   ↓
[mmw:proof [codename] — human gate — always deliberate in all modes]
   Caret proposes this exact command (with codename) after Phase 9+10 completes.
   Does not advance automatically.
   ↓
Phase 11 — Handoff
            mmw_tools.py publish <codename> atomically writes:
              → final.md (clean copy of latest draft)
              → writers-room/published/[slug].md
              → writers-room/published/[slug]-image-prompt.md
            Index ║ Cadence [parallel]
              Index:   updates post-index.md
              Cadence: logs in calendar.md
```

---

## Parallel Execution Pairs

Three phases run parallel subagent pairs. Both Agent tool calls must be issued in the same response turn for genuine concurrency.

| Phase | Pair | Output files |
|---|---|---|
| 6+7 | Devil ║ Echo | critique-vN.md ║ audience-vN.md |
| 9+10 | Press ║ Prism | seo.md ║ image-prompt.md |
| 11 handoff | Index ║ Cadence | post-index.md ║ calendar.md |

Before spawning any parallel pair, Caret writes a partial marker to status.md:
`[partial] Devil → pending, Echo → pending`

As each completes, Caret replaces its entry. If one fails, the `[partial]` marker persists as a resume signal.

**Recovery**: If you return to a session and status.md shows `[partial]` with no recent activity, the agent likely timed out. Use the relevant `mmw:agent` shortcut to retry. Example: `[partial] Echo → pending` means run `mmw:echo [codename]`.

---

## Caret ↔ Mark Loop

The iterative loop runs after the first draft is written. Caret generates a draft, Mark reviews it, Caret revises, repeat until exit condition is met.

**Exit conditions (manual mode):**
- Mark issues HOLD — loop exits immediately (structural issue, not a revision problem)
- User selects [M] Move to critique

**Circuit breaker (manual mode):** After 2 consecutive REVISE verdicts in the Caret ↔ Mark Refinement Loop (Phase 5), Caret surfaces a Choice Gate: [C] Co-edit / [R] One more revision / [S] Proceed to Devil and Echo. The loop iterations reset if [C] or [R] is selected. This allows human intervention without creating a hard stop.

**Co-edit mode:** The user's voice is the point. Everything else serves that. At any loop pause, the user can select [C] to take the keyboard. Caret surfaces the exact flagged lines, waits while the user edits the file directly, then integrates remaining issues and produces the next draft. See CLAUDE.md § Co-Edit Mode for the full flow.

---

## Index Overlap Gate

Index always runs first (Phase 0) — before Compass, before any research, before any drafting.

Index validates `post-index.md` exists and is readable before doing anything else. It reports the archive state, then checks brief.md against `post-index.md` for overlap. Uses `mmw_tools.py overlap_check` to get a ranked shortlist of candidates; reads only shortlisted published files (not the full archive).

If overlap is found, Index surfaces a structured report and four options: [U] Update, [D] Differentiate, [P] Proceed, [A] Abandon. [A] requires double-confirmation (user must type the exact codename) before any deletion occurs.

---

## Research Gate

Before every draft, Caret verifies that `research.md` exists and is non-empty. This gate never runs silently. If research.md is missing, Caret stops and surfaces options: run Turing or proceed without research (explicitly confirmed by user).

---

## Codename Generation

Codenames are derived from the brief: descriptive, lowercase, hyphenated, 2–3 words, characters `[a-z0-9-]` only. Examples: `writers-room-build`, `agent-research-loop`.

If a generated codename collides with an existing folder, Caret generates a variant silently (up to 3 attempts). If all 3 collide, Caret asks the user to provide one.

---

## Draft Versioning

Drafts are never overwritten. Each version is a new file: `draft-v1.md`, `draft-v2.md`, `draft-v3.md`, etc. Use `python scripts/mmw_tools.py draft_version <codename> next` to get the correct next version number before writing.

---

## Phase 11 Handoff Detail

`mmw_tools.py publish <codename>` atomically writes all three published output files and updates status.md. This ensures final.md, `writers-room/published/[slug].md`, and `writers-room/published/[slug]-image-prompt.md` all exist before Index and Cadence are spawned.

**Before spawning Index**, Caret writes `Mode: archive-update` to status.md. Index reads this flag first and skips the overlap gate, going directly to appending to `post-index.md`.

Bring `writers-room/published/[slug].md` to your Hugo environment manually. mmw does not write outside its own directory.

---

## Prism → GitHub Actions Handoff

Prism writes `image-prompt.md` as one focused plain paragraph (no markdown formatting). After Phase 11, `writers-room/published/[slug]-image-prompt.md` is the image generation source. Bring it to Gemini Image Pro or a GitHub Actions workflow to generate the cover image.

---

## Session Resume

`mmw [codename]` resumes an existing piece. Caret reads status.md first and reports the current state before taking any action. Mode survives session boundaries — if `Mode: auto` is in status.md, auto mode applies for all remaining phases.

If status.md contains `[in-progress] user-edit — awaiting mmw:done`, Caret re-surfaces the co-edit prompt for the current draft (co_edit_draft field identifies which draft is being edited).

---

## File Schema

### Piece folder (`writers-room/pieces/[codename]/`)

```
brief.md              ← user intent — source of truth for the piece
status.md             ← codename, description, draft version, agent log
compass-notes.md      ← Compass strategic direction (includes ## Cadence Context)
research.md           ← Turing's grounding document
headlines.md          ← Mark's hook and headline options
audience-signal.md    ← Echo's structural fit check (Phase 3.5, not versioned)
draft-v1.md           ← Caret's first draft
draft-v2.md           ← after first Caret/Mark loop (or user edits)
draft-v3.md           ← after second loop (etc.)
brand-notes-v1.md     ← Mark's review of draft-v1 (PASS/REVISE/HOLD)
brand-notes-v2.md     ← Mark's review of draft-v2
brand-notes-final.md  ← Mark's Phase 8.5 re-alignment check (conditional)
critique-vN.md        ← Devil's accusation audit (version matches draft reviewed)
audience-vN.md        ← Echo's audience review (version matches draft reviewed)
fact-check-vN.md      ← Turing's fact-check (opt-in, manual only)
seo.md                ← Press: Hugo YAML front matter + SEO recommendations
image-prompt.md       ← Prism: one focused paragraph for Gemini Image Pro
final.md              ← publish-ready (written in Phase 11)
```

### Published files (`writers-room/published/`)

```
[slug].md              ← clean copy of final.md
[slug]-image-prompt.md ← copy of image-prompt.md
```

### status.md structure

```markdown
# [codename]
> [plain English one-line description — used by Index without opening other files]

## Current State
- Phase: 3 — Caret first draft
- Mode: auto    ← only present in auto/auto-quick mode; absent = manual
- Current draft: draft-v1.md
- co_edit_draft: draft-v1.md  ← transient; only while awaiting mmw:done
- Slug: (written by Press)    ← exact string replaced by Press on completion
- Next step: Awaiting user direction

## Agent Run Log
- [x] Index → overlap check (no conflicts found)
- [x] Compass → compass-notes.md
- [x] Turing → research.md
- [x] Caret → draft-v1.md [research gate: PASSED]
```

`- Slug: (written by Press)` is an exact-string placeholder. Press locates it by literal match and replaces it with the actual slug value. Any variation causes Press's slug sync to fail silently.

After Press and Prism both complete, Caret writes `Next step: Ready for mmw:proof [codename]`. This is the exact string Caret scans for when `mmw:proof` is called without a codename.

---

---

## Constraints

- All agent system prompts in plain markdown — no code, no JSON
- Stateless file-based architecture — agents communicate through files only
- **Token-Aware Execution**: Context windows are treated as transient; strict limits on web queries (10/10 budget) and explicit `reset_pending` handoffs ensure agents do not accumulate history debt.
- Never overwrite a previous draft — always increment version numbers
- Press outputs valid Hugo YAML front matter matching the schema exactly
- `image-prompt.md`: one focused paragraph — no headers, no bullets, no code fences
- Caret/Mark loop has no iteration cap in manual mode — user exits with [M]
- Auto mode: Phase 5 loop cap = 1 pass; Phase 8 applied without pause; Phase 8.5 skipped
- Index runs before any other agent and always validates post-index.md first
- Compass runs before Turing — research must be focused, not blind
- Caret never skips the research gate silently
- Co-edit: Caret never rewrites the user's edits without flagging; co-edit not available in auto mode (except at Mark HOLD)
- `mmw:proof` is always a human gate in all modes — no agent calls it automatically
- This is a writing tool first
