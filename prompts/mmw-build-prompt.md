# mmw Build Prompt
# Mark My Words — Multi-Agent Writing System

> [!IMPORTANT]
> **AGENTIC INSTRUCTION**: You are building a multi-agent writing system
> called Mark My Words (mmw). Maintain a `task.md` file in the root of
> the writers-room/ project to track your progress through each phase.
> Do not attempt to complete the entire build in one turn.
>
> **task.md format** — use this structure exactly so a resumed session can parse it:
> ```
> ## Build Progress
> - [ ] Step A — Scaffold + Seed files (Steps A and G complete together — do NOT mark [x] until seed files in Step G are written)
> - [ ] Step B — Agent files
> - [ ] Step C — ARCHITECTURE.md
> - [ ] Step D — CLAUDE.md
> - [ ] Step E — Skills
> - [ ] Step F — Brand guidelines
> - [ ] Validation
> ```
> Mark each step `[x]` when complete. On resume, read task.md first and
> continue from the first unchecked item.
>
> **AGENTIC BEST PRACTICES**:
> 1. **Context Refresh**: At the start of every step, re-read the
>    relevant spec file. Do not rely on earlier memory.
> 2. **Git Checkpoints**: At the completion of every step, the user
>    may run `git add . && git commit -m "Checkpoint: [Step Name]"`
>    if they wish. This is optional — versioned files are the primary
>    history.
> 3. **Validation**: After creating each file, confirm it exists
>    and is non-empty before moving to the next.
> 4. **Session Integrity**: If context is lost, read task.md to resume
>    exactly where you left off.
> 5. **Step Boundaries are Context Boundaries**: Each step completes
>    fully and writes its output file(s) before the next step begins.
>    Never carry a step's full output into the next step as in-context
>    text — read it from the file instead. The file system is the
>    memory, not the context window.

---

## Spec Files

All build specs live in `prompts/specs/`. Read the relevant spec before
building each artifact. Do not rely on memory of a previously read spec.

| Spec | Covers |
|---|---|
| `prompts/specs/flow.md` | Workflow, phases, protocols, file schema, constraints, success criteria |
| `prompts/specs/agent-caret.md` | Caret — orchestrator + writer |
| `prompts/specs/agent-mark.md` | Mark — brand + voice |
| `prompts/specs/agent-compass.md` | Compass — strategist |
| `prompts/specs/agent-devil.md` | Devil — critique |
| `prompts/specs/agent-turing.md` | Turing — research |
| `prompts/specs/agent-echo.md` | Echo — audience |
| `prompts/specs/agent-press.md` | Press — publisher |
| `prompts/specs/agent-prism.md` | Prism — visual brand |
| `prompts/specs/agent-index.md` | Index — archivist |
| `prompts/specs/agent-cadence.md` | Cadence — scheduler |

---

## Project Root

> **PROJECT ROOT**: All paths in this prompt are relative to the repository root (the directory containing this file). The build agent runs from the repo root, so relative paths resolve correctly regardless of where the repo is cloned.

---

## Shared String Constants

These strings must be reproduced character-for-character in the agent files that reference them. Change them here first, then rerun the affected steps.

```
SLUG_SENTINEL = "- Slug: (written by Press)"
```

Used in: `.claude/agents/caret.md` (status.md initialization block) and `.claude/agents/press.md` (Edit-tool replace target). Both must match exactly — including parentheses and capitalization. See the cross-check at the end of Step B.

---

## Maintenance Map

Use this table when making targeted changes after the initial build. You do not need to rerun the full build — only the steps listed.

| If you change… | Rerun steps |
|---|---|
| Any agent spec (`prompts/specs/agent-*.md`) | Step B (that agent only) + Validation auto-mode trace |
| `prompts/specs/brand.md` | Step F only |
| `prompts/specs/flow.md` | Step C, Step D, Validation |
| `mmw_tools.py` signatures | Step B (affected agents), Step D, Validation |
| A skill spec (`prompts/specs/skills/<name>.md`) | Step E (that skill only) |
| `prompts/specs/tool-scoping.md` | Step B (all agents) + Validation |
| `SLUG_SENTINEL` value (above) | Step B (caret.md + press.md) + cross-check at end of Step B |

---

## Python Tools (`mmw_tools.py`)

A Python helper script lives at the project root: `mmw_tools.py`. Agents call it via Bash to handle all deterministic file operations — this keeps mechanical work out of agent context windows.

**Invocation pattern** (agents use Bash tool):
```
python mmw_tools.py <tool_name> [args...]
```
All tools print JSON to stdout and exit 0 on success. On failure they print a descriptive error to stderr and exit 1.

| Tool | Signature | Returns |
|---|---|---|
| `draft_version` | `<codename> latest\|next` | `{"path": "...", "version": N}` |
| `status_read` | `<codename> <field>` | `{"field": "...", "value": "..."}` |
| `status_write` | `<codename> '<json_updates>'` | `{"updated": [...]}` |
| `status_log` | `<codename> '<entry>'` | `{"appended": true}` |
| `research_prune` | `<notes_path> [max_age_days]` | `{"pruned": N, "remaining": M}` |
| `overlap_check` | `<brief_path> <index_path>` | `{"candidates": [{title, slug, score, shared_keywords}]}` |
| `slug_validate` | `<codename>` | `{"match": true/false, "status_slug": "...", "seo_slug": "..."}` |
| `preflight` | `<codename>` | `{"ready": true/false, "failures": [...]}` |
| `publish` | `<codename>` | `{"success": true, "published_path": "...", "image_path": "..."}` |
| `index_update` | `<codename>` | `{"appended": true, "title": "...", "slug": "..."}` |
| `calendar_log` | `<codename> '<description>' <target_date>` | `{"appended": true}` |

Field names for `status_read` / `status_write` are lowercase: `phase`, `mode`, `slug`, `current_draft`, `last_agent`, `next_step`, `brief_intent`.

**Tool scoping**: Add `Bash` to the tools list for any agent that calls `mmw_tools.py`. See the updated tool scoping table in Step B.

---

## What To Build

### Step A — Project Scaffold

Create `writers-room/task.md` first. Then create this full directory structure:

```
./                             ← repo root
├── CLAUDE.md                  ← project root — triggers mmw, mmw:agent shortcuts
└── writers-room/
    ├── ARCHITECTURE.md
    ├── README.md
    ├── task.md                ← build-time progress tracker (created first)
    ├── brand/
    │   └── guidelines.md
    ├── pieces/                ← all active and completed piece folders
    ├── published/             ← final drafts ready to bring to any publishing environment
    ├── research/
    │   └── notes.md
    ├── index/
    │   └── post-index.md
    ├── cadence/
    │   └── calendar.md

.claude/agents/                ← Local Stubs (thin — redirect to Sync Masters)
    ├── caret.md
    ├── mark.md
    ├── compass.md
    ├── devil.md
    ├── turing.md
    ├── echo.md
    ├── press.md
    ├── index.md
    ├── cadence.md
    └── prism.md

.claude/agents-sync/           ← Sync Masters (full — synced to Claude Project Knowledge)
    ├── caret.md
    ├── mark.md
    ├── compass.md
    ├── devil.md
    ├── turing.md
    ├── echo.md
    ├── press.md
    ├── index.md
    ├── cadence.md
    └── prism.md

.claude/skills/
    ├── mmw/
    │   └── SKILL.md
    ├── mmw-turing/
    │   └── SKILL.md
    ├── mmw-devil/
    │   └── SKILL.md
    ├── mmw-echo/
    │   └── SKILL.md
    ├── mmw-press/
    │   └── SKILL.md
    ├── mmw-prism/
    │   └── SKILL.md
    ├── mmw-compass/
    │   └── SKILL.md
    ├── mmw-mark/
    │   └── SKILL.md
    ├── mmw-cadence/
    │   └── SKILL.md
    ├── mmw-index/
    │   └── SKILL.md
    ├── mmw-bearings/
    │   └── SKILL.md
    └── mmw-proof/
        └── SKILL.md
```

After creating `pieces/` and `published/`, write an empty `.gitkeep` file in each so Git tracks them.

Also create `.claude/agents/` explicitly before writing any agent files — write an empty `.gitkeep` there too. This guarantees the directory exists when Step B begins, since `Write` tool behavior on missing parent directories is not guaranteed.

**CLAUDE.md must be at the project root** (`./CLAUDE.md`),
not inside `writers-room/`. This is required for Claude Code to recognize the
mmw triggers and `mmw:agent` shortcuts in every new session.

**Agent files must be in `.claude/agents/`** relative to the project root.
This is the directory Claude Code scans to register native subagents. Files
in `writers-room/agents/` will not be auto-discovered.

> **Note**: Seed files for `index/`, `cadence/`, and `research/` are defined in
> Step G below. Step A is only complete when both the scaffold and seed files
> are written — agents depend on these files existing before any workflow runs.
>
> **Do not mark Step A `[x]` until Step G seed files are also written.** Step A and Step G complete together.

---

### Step B — Agent Stubs (`.claude/agents/`)

> **Dual-output architecture**: `.claude/agents/` holds **Local Stubs** — thin files that Claude Code reads to register each agent (name, model, tools). The full operating instructions live in **Sync Masters** at `.claude/agents-sync/`, which are uploaded to Claude Project Knowledge. Step H generates the Sync Masters.

**Build order: build all agents except Caret first. Build Caret last.**
Caret's spec cross-references behavior defined in Index, Press, and co-edit.
Build those agents first so that logic is fresh when you write caret.md.

Read each agent spec from `prompts/specs/agent-[name].md` and create the
corresponding file in `.claude/agents/`. Build one agent at a time. Verify
the file exists and is non-empty before moving to the next.

Each agent file must **ONLY** contain:
1. The **YAML frontmatter** that declares the agent's name and permitted tools
2. A required redirect message pointing back to the Sync Master

Do **not** include personality, responsibilities, or execution logic in the local stub. Wait for Step H to write those full instructions.

**Each agent file must look exactly like this snippet:**

```yaml
---
name: [agent-name]
description: One-line purpose of this agent (use the "One-line purpose" from the spec)
model: claude-sonnet-4-6
tools: [Read, Write, Edit]
---

# [Agent Name] — Stub

Your full operating instructions are in `.claude/agents-sync/[agent-name].md`. Read that file before doing anything else.

> This stub exists so Claude Code can identify and register this agent. All behaviour, protocols, and phase logic live in the Sync Master.
```

The `tools` value must be a YAML inline sequence (bracketed, comma-separated). This is the format Claude Code parses to enforce tool scoping. Do not write it as a plain string (`tools: Read, Write` is wrong — it will not be parsed as a list). After writing each agent file, read back the `tools:` line and confirm it opens with `[` and closes with `]`. If it is a plain string, rewrite the file before moving to the next agent.

Every agent file must also include `model: claude-sonnet-4-6` in its frontmatter. This ensures all subagents run on a capable model regardless of which model the parent session is using.

**Tool scoping per agent**: Read `prompts/specs/tool-scoping.md` for the authoritative tool scoping table — do not infer from memory. That file also documents the YAML inline sequence requirement and case-sensitivity rules.

> **Parallel spawning requires same-response Agent calls.** When Caret spawns a
> parallel pair (Devil║Echo, Press║Prism, Index║Cadence), both Agent tool calls
> must be issued in the same response turn. Sequential calls are functionally
> correct but will not run concurrently.

**mmw_tools.py usage — Caret**: When writing `.claude/agents/caret.md`, instruct Caret to use `mmw_tools.py` via Bash for all deterministic operations:
- **Draft version resolution**: Instead of scanning draft-vN.md files manually, call `python mmw_tools.py draft_version <codename> latest` (to read) or `draft_version <codename> next` (before writing a new draft).
- **status.md field reads**: Instead of reading the full status.md and parsing fields in prose, call `python mmw_tools.py status_read <codename> <field>` for single-field lookups (e.g., `mode`, `phase`, `slug`, `current_draft`).
- **status.md field updates**: Instead of using Edit tool to update individual fields in status.md, call `python mmw_tools.py status_write <codename> '{"phase": "3 — First draft", "current_draft": "draft-v1.md"}'`.
- **status.md log entries**: Instead of appending log lines via Edit tool, call `python mmw_tools.py status_log <codename> '[x] Turing → research.md'`.
- **Phase 11 pre-flight**: Instead of checking 6 conditions individually, call `python mmw_tools.py preflight <codename>`. If `ready` is false, surface `failures` to the user.
- **Phase 11 publish**: Instead of reading and writing files individually, call `python mmw_tools.py publish <codename>`. This atomically writes final.md, published/[slug].md, and published/[slug]-image-prompt.md and updates status.md.

**Auto-mode behavior — Caret**: When writing `.claude/agents/caret.md`, include these behaviors (read `prompts/specs/agent-caret.md` for full detail):
- Pre-step flag parsing: check for `--auto` in the trigger text, strip it, set mode
- If mode = auto: write `- Mode: auto` in the `## Current State` block of status.md at init; omit in manual mode
- Session resume: read `Mode:` from status.md `## Current State`; if `Mode: auto` present, auto mode applies for all remaining phases
- Phase 5 loop cap in auto: 1 Mark pass only — REVISE applied directly, HOLD logged and exits, PASS exits; co-edit not available
- Phase 8 in auto: apply Devil/Echo feedback directly, produce new draft, log summary, skip Phase 8.5
- Manual mode: surface a concrete next-step prompt after every phase completion (pre-filled command + [C]/[S] options)

**Flexible invocation input — Caret**: When writing `.claude/agents/caret.md`, include this behavior (read `prompts/specs/agent-caret.md` § Flexible invocation input for full detail):
- After stripping flags, Caret determines the input type:
  - **Topic string** — use directly to generate codename (current behavior)
  - **File path** — Caret reads the file as the brief foundation, derives codename from its content, writes brief.md from the file's content
  - **Bullet brainstorm** (items prefixed with `-`) — Caret structures the bullets into brief.md (angle, intent, constraints), then generates the codename from that structure
- Input type detection happens before codename generation — never before flag stripping.

**Auto-quick mode behavior — Caret**: When writing `.claude/agents/caret.md`, include these behaviors (read `prompts/specs/agent-caret.md` § Auto-quick mode for full detail):
- Pre-step flag parsing: check for both `--auto` and `--quick` in the trigger text. If both present, strip them and set mode = auto-quick. Write `- Mode: auto-quick` in `## Current State` of status.md at init.
- Session resume: if `Mode: auto-quick` is present in status.md, auto-quick mode applies for all remaining phases.
- Auto-quick skips these phases entirely — log each skip in status.md as `[skip] Phase N — auto-quick mode`:
  - Phase 1 (Compass) — `[skip] Phase 1 — auto-quick mode`
  - Phase 4 (Mark headlines) — `[skip] Phase 4 — auto-quick mode`
  - Phase 5 (Mark loop) — `[skip] Phase 5 — auto-quick mode`
  - Phase 6+7 (Devil+Echo) — `[skip] Phase 6+7 — auto-quick mode`
  - Phase 8 (revision window) — `[skip] Phase 8 — auto-quick mode`
  - Phase 8.5 — `[skip] Phase 8.5 — auto-quick mode`
- Auto-quick runs: Phase 0 (Index), Phase 2 (Turing — single focused search only, no deep dive), Phase 3 (Caret drafts from brief + research; no compass-notes.md available), Phase 9+10 (Press ║ Prism), mmw:proof gate, Phase 11.
- Draft-elaborator use case: after auto-quick completes, the user may run `mmw [codename]` to continue in manual mode — the full pipeline picks up from the existing draft.

**Deadline-constrained auto upgrade — Caret**: When writing `.claude/agents/caret.md`, include this behavior (read `prompts/specs/agent-caret.md` § Deadline-aware mode upgrade for full detail):
- In auto mode only (not already auto-quick), before Phase 0, Caret reads `writers-room/cadence/calendar.md`.
- If the codename appears with a target publish date and that date is <3 days from today, Caret upgrades mode to auto-quick and logs `[auto] Publish deadline in N days — fast path activated` in status.md.
- If no calendar entry exists for this codename, auto mode runs at full depth unchanged.
- This check runs at startup only — not on session resume.

**mmw_tools.py usage — Turing**: When writing `.claude/agents/turing.md`, instruct Turing to:
- **Prune research notes**: Instead of date-math and manual file rewrite, call `python mmw_tools.py research_prune writers-room/research/notes.md` at the end of every research pass. The tool removes entries older than 90 days and returns pruned/remaining counts.
- **Mode check at startup**: Use `python mmw_tools.py status_read <codename> mode` to read the mode field instead of reading and parsing the full status.md.

**Auto-mode behavior — Turing**: When writing `.claude/agents/turing.md`, include these behaviors (read `prompts/specs/agent-turing.md` for full detail):
- At startup, read `Mode:` from status.md; if `Mode: auto` or `Mode: auto-quick`, skip the deep dive entirely
- Log `[auto] Deep dive skipped` under `## Deep Dive Candidates (skipped — auto mode)` in research.md
- Proceed to Phase 3 immediately without surfacing candidates

**Manual mode — Phase 8 triage — Caret**: When writing `.claude/agents/caret.md`, include this behavior (read `prompts/specs/flow.md` § Phase 8 and `prompts/specs/agent-caret.md` § Manual mode — Phase 8 triage for full detail):
- After Devil and Echo complete, Caret synthesizes critique-vN.md and audience-vN.md into a structured triage before presenting options:
  - **Must address before publishing**: Devil's REVISE items + Echo persona bounce points
  - **Worth addressing if time allows**: Devil's Challenge Questions + minor Echo notes
  - **Already working well**: positive signals from both
- [F] Fact-check option: show this option **only** if Devil flagged credibility concerns in critique-vN.md. If shown and selected, Turing runs `--fact-check` and produces fact-check-vN.md.
- When producing a post-Phase 8 draft (after [C] or [R]): Caret reads critique-vN.md + audience-vN.md + fact-check-vN.md (if it exists) and addresses all in one combined revision pass. Reports what it addressed from each file.
- [P] Proceed: no new draft version is created. Press reads the existing latest draft.

**Phase 11 outputs — Caret**: When writing `.claude/agents/caret.md`, Phase 11 must use `python mmw_tools.py publish <codename>` to atomically write all published output files:
- Writes `final.md` (clean copy of latest draft)
- Writes `writers-room/published/[slug].md`
- Writes `writers-room/published/[slug]-image-prompt.md`
- Updates status.md phase and next_step fields
All three file writes happen in one atomic operation. Both published/ files must exist before Index and Cadence are spawned in parallel.

**mmw_tools.py usage — Press**: When writing `.claude/agents/press.md`, instruct Press to:
- **Slug sync verification**: After writing the slug to status.md via the Edit tool (the existing exact-string replace for the `SLUG_SENTINEL` value defined above), call `python mmw_tools.py slug_validate <codename>` to confirm the values match. If `match` is false, log the mismatch and correct the value before proceeding.

**mmw_tools.py usage — Index**: When writing `.claude/agents/index.md`, instruct Index to:
- **Overlap candidate scan (Phase 0)**: Instead of reading the full post-index.md table in context, call `python mmw_tools.py overlap_check writers-room/pieces/<codename>/brief.md writers-room/index/post-index.md`. The tool returns a ranked shortlist of up to 5 lexical overlap candidates with scores and shared keywords. Index then reads only the shortlisted entries (or their published files) to make the editorial judgment — not the full table.
- **Archive update (Phase 11)**: Instead of reading status.md and appending a formatted row in prose, call `python mmw_tools.py index_update <codename>`. The tool extracts metadata from status.md and seo.md and appends the correctly formatted row to post-index.md.

**mmw_tools.py usage — Cadence**: When writing `.claude/agents/cadence.md`, instruct Cadence to:
- **Calendar entry append**: Instead of reading and manually appending a formatted row, call `python mmw_tools.py calendar_log <codename> '<description>' <target_date>`. Description should be the one-liner from status.md; target_date in YYYY-MM-DD format.

**Cross-check before moving to Step C**: Read back the status.md initialization block in `.claude/agents/caret.md` and the Edit-tool replace target in `.claude/agents/press.md`. Confirm both use the `SLUG_SENTINEL` value defined at the top of this prompt — character for character. If they differ, fix whichever is wrong before continuing.

---

### Step C — ARCHITECTURE.md

Read `prompts/specs/ARCHITECTURE.md` and copy it perfectly into `writers-room/ARCHITECTURE.md`.
Do not summarize or synthesize it. Ensure it is written exactly character-for-character as it appears in the spec.

---

### Step D — CLAUDE.md

**Location**: `./CLAUDE.md` (project root — not inside writers-room/).

Read `prompts/specs/flow.md` before writing. Cover:
- What Mark My Words is — one paragraph
- **Single trigger**: `mmw` is the only recognized trigger. `MMW` and `Mark My Words` are not triggers. Document this explicitly.
- **Invocation modes** (read from flow.md § Modes):
  - `mmw [topic]` — manual mode (default)
  - `mmw --auto [topic]` — auto mode: runs full pipeline without pausing, stops at `mmw:proof`. Note: a Mark HOLD verdict (structural issue) is logged in status.md but does not pause the workflow — auto mode may produce drafts with unresolved structural flags. Use manual mode for complex or high-stakes pieces.
  - Caret strips `--auto` before generating the codename
- `/mmw` is the primary slash command (registered as a Skill in `.claude/skills/`). The plain-text `mmw` remains a fallback for sessions where skills are not loaded.
- All sub-agent shortcuts — now registered as skills (`/mmw-turing`, `/mmw-devil`, etc.) with plain-text `mmw:agent` variants documented as fallbacks. Note: each invokes a native Claude Code subagent defined in `.claude/agents/`.
- `mmw:proof` — the human gate that triggers Phase 11. Explain that no agent calls this automatically; it is always a deliberate human decision — in both manual and auto mode. State explicitly that `mmw:proof` is handled inline by Caret — there is no `.claude/agents/proof.md`. When the user types `mmw:proof [codename]`, Caret reads the piece folder and executes the Phase 11 pre-flight directly.
- State explicitly that `mmw:bearings` is handled inline by Caret — there is no `.claude/agents/bearings.md`. When the user types `mmw:bearings [codename]`, Caret reads status.md and reports the current state of the piece before proposing a next step.
- Caret as the default entry point
- **Session resume**: `mmw [codename]` resumes an existing piece. Caret reads status.md first. If `Mode: auto` is present in status.md, auto mode applies for all remaining phases.
- Codename generation rules: derived from brief, descriptive, lowercase hyphenated, 2–3 words, characters `[a-z0-9-]` only
- The full ordered workflow summary
- The iterative loop, co-edit mode, and 2-iteration circuit breaker
- Co-edit mode worked example:

```
## Co-Edit Mode

Co-edit is triggered when the user types [C] or "co-edit" at any
loop pause point, or after any Devil/Echo review.

Example session:
  Mark reviewed draft-v1.md → brand-notes-v1.md [REVISE]
  User: C
  Caret: [surfaces specific flagged lines with current text and issue]
  User: [edits draft-v1.md directly in their editor]
  User: mmw:done
  Caret: [reads edited file, integrates remaining issues,
          produces draft-v2.md, reports exactly what it changed
          beyond the user's edits]

Co-edit is the most important feature in this system.
The user's voice is the point. Everything else serves that.
```

- That image-prompt.md must be one focused paragraph — no headers, no bullets, no code fences
- Final drafts land in `writers-room/published/[slug].md` and the image prompt lands in `writers-room/published/[slug]-image-prompt.md` — bring them to your publishing environment manually. mmw does not write outside its own directory.
- Parallel agent recovery: if you return to a session and status.md shows `[partial]` with no recent activity, the agent likely timed out. Use the relevant `mmw:agent` shortcut to retry the missing agent. Example: `[partial] Echo → pending` means `mmw:echo` to retry.
- Scaffold recovery: if `mmw:proof` stops with "writers-room/published/ directory missing", the project scaffold is incomplete. Fix: run `mkdir -p writers-room/published/` from the project root, then retry `mmw:proof [codename]`.
- Reminder: this is a writing tool — responses should be editorial, thoughtful, and concise. Not a coding tool.

---

### Step E — Skills (`.claude/skills/`)

Create one skill directory per mmw command. Each skill provides guaranteed slash-command routing instead of relying on CLAUDE.md trigger-word parsing. Skills are stored at `.claude/skills/<name>/SKILL.md`.

**Create all twelve skill directories and their SKILL.md files.** For each skill, read the corresponding spec file from `prompts/specs/skills/` and write its contents verbatim to the target path. Do not paraphrase — copy exactly.

| Skill | Spec file | Target path |
|---|---|---|
| `/mmw` | `prompts/specs/skills/mmw.md` | `.claude/skills/mmw/SKILL.md` |
| `/mmw-turing` | `prompts/specs/skills/mmw-turing.md` | `.claude/skills/mmw-turing/SKILL.md` |
| `/mmw-devil` | `prompts/specs/skills/mmw-devil.md` | `.claude/skills/mmw-devil/SKILL.md` |
| `/mmw-echo` | `prompts/specs/skills/mmw-echo.md` | `.claude/skills/mmw-echo/SKILL.md` |
| `/mmw-press` | `prompts/specs/skills/mmw-press.md` | `.claude/skills/mmw-press/SKILL.md` |
| `/mmw-prism` | `prompts/specs/skills/mmw-prism.md` | `.claude/skills/mmw-prism/SKILL.md` |
| `/mmw-compass` | `prompts/specs/skills/mmw-compass.md` | `.claude/skills/mmw-compass/SKILL.md` |
| `/mmw-mark` | `prompts/specs/skills/mmw-mark.md` | `.claude/skills/mmw-mark/SKILL.md` |
| `/mmw-cadence` | `prompts/specs/skills/mmw-cadence.md` | `.claude/skills/mmw-cadence/SKILL.md` |
| `/mmw-index` | `prompts/specs/skills/mmw-index.md` | `.claude/skills/mmw-index/SKILL.md` |
| `/mmw-bearings` | `prompts/specs/skills/mmw-bearings.md` | `.claude/skills/mmw-bearings/SKILL.md` |
| `/mmw-proof` | `prompts/specs/skills/mmw-proof.md` | `.claude/skills/mmw-proof/SKILL.md` |

To update a skill in the future, edit its spec file in `prompts/specs/skills/` and rerun Step E for that skill only (see Maintenance Map above).


**After writing all twelve SKILL.md files**, verify each exists and is non-empty before moving to Step F.

**Naming convention note**: Skill names use `[a-z0-9-]` only — no spaces, underscores, or special characters. The plain-text fallbacks (`mmw:turing`, `mmw:devil`, etc.) remain documented in CLAUDE.md for sessions where skills have not loaded, but the slash-command form is the canonical invocation.

---

### Step F — Brand Guidelines (`writers-room/brand/guidelines.md`)

Write `writers-room/brand/guidelines.md` based on the brand spec at `prompts/specs/brand.md`. Copy the full contents of that spec into the guidelines file — this is the runtime copy that agents read during piece workflows.

---

### Step G — Seed Files

Create all three files during scaffold. Each must exist before any agent runs —
Turing reads `research/notes.md` at the start of every research pass.

**index/post-index.md**:
```markdown
| Title | Slug | Date | Tags | Description |
|---|---|---|---|---|
```

**cadence/calendar.md**:
```markdown
| Codename | Description | Target Publish | Status | Notes |
|---|---|---|---|---|
```

**research/notes.md**:
```markdown
| Date | Codename | Finding | Source | Tags |
|---|---|---|---|---|
```

---

## Validation

When the build is complete, verify the following success criteria can be traced through the built artifacts. Do not run a live session — just confirm all required files exist and that the agent files contain the logic needed to execute each step.

**Step 1 — Run the automated pre-flight script:**

```
python mmw_validate.py
```

This script (spec: `prompts/specs/validate.md`) checks that all required files exist and are non-empty, that every agent's `tools:` frontmatter is a YAML inline sequence (not a plain string), that every agent has `model:` set, and that the `SLUG_SENTINEL` string matches in both caret.md and press.md. Fix all failures before continuing.

If `mmw_validate.py` has not been built yet, perform these checks manually:
- `writers-room/brand/guidelines.md` — contains the banned words list
- `writers-room/index/post-index.md` — contains the markdown table header
- `writers-room/cadence/calendar.md` — contains the markdown table header
- `writers-room/research/notes.md` — contains the markdown table header
- All 10 agent files in `.claude/agents/` — read the `tools:` line in each and confirm it opens with `[` and closes with `]`. See `prompts/specs/tool-scoping.md` for the authoritative list of expected values.
- All 12 skill directories in `.claude/skills/` — verify each contains a `SKILL.md` file that is non-empty: `mmw`, `mmw-turing`, `mmw-devil`, `mmw-echo`, `mmw-press`, `mmw-prism`, `mmw-compass`, `mmw-mark`, `mmw-cadence`, `mmw-index`, `mmw-bearings`, `mmw-proof`.

**Step 2 — Trace the workflow paths manually** (semantic reasoning required — the script cannot do this):

**Auto-mode trace** (verify caret.md and turing.md contain the required logic):
- `mmw --auto [topic]` → Caret strips `--auto`, generates codename, writes `- Mode: auto` to status.md
- Turing reads `Mode: auto` from status.md → skips deep dive, logs `[auto] Deep dive skipped`
- Phase 5: Caret runs 1 Mark pass, applies REVISE directly or exits on PASS/HOLD
- Phase 8: Caret applies Devil/Echo feedback directly, logs summary, skips Phase 8.5
- `mmw:proof` → still a human gate; auto mode pauses and waits
- Session resume: `mmw [codename]` → Caret reads `Mode: auto` from status.md → continues in auto mode
- Phase 11: Caret calls `mmw_tools.py publish <codename>` which writes both `writers-room/published/[slug].md` and `writers-room/published/[slug]-image-prompt.md` atomically

**Auto-quick trace** (verify caret.md contains the required logic):
- `mmw --auto --quick [topic]` → Caret strips both flags, writes `- Mode: auto-quick` to status.md
- Phase 1 skipped — logs `[skip] Phase 1 — auto-quick mode`
- Phase 0 (Index) runs as normal
- Phase 2 (Turing) runs — single focused search, no deep dive — logs `[auto] Deep dive skipped`
- Phase 3 (Caret draft) runs — from brief + research only; no compass-notes.md
- Phases 4, 5, 6+7, 8, 8.5 all skipped — each logged in status.md
- Phase 9+10 (Press ║ Prism) runs in parallel
- `mmw:proof` → human gate; waits
- Phase 11: same as auto, including both published/ file writes via `mmw_tools.py publish`
- Deadline-constrained upgrade: if `calendar.md` shows target date <3 days away in auto mode, caret.md upgrades to auto-quick and logs `[auto] Publish deadline in N days — fast path activated`

**Manual-mode trace** (existing workflow, unchanged):

1. User types: `/mmw write a post about building this writer's room` (or plain-text `mmw write a post about building this writer's room` as fallback)
2. Caret generates codename `writers-room-build`, creates folder, writes brief.md and status.md with plain English description
3. Index validates post-index.md — reports N entries found
4. Index checks brief.md against post-index.md — no overlap found
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
16. User types: mmw:done
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
    - Prism reads latest draft-vN.md → image-prompt.md as one focused paragraph
24. User types: `mmw:proof writers-room-build`
25. Pre-flight check passes — draft, seo.md, slug, image-prompt.md all present
26. final.md written and copied to `writers-room/published/writers-room-build.md`
27. Index ║ Cadence run in parallel:
    - Index updates post-index.md with new entry
    - Cadence logs codename, description, and target publish date in calendar.md

---

### Step H — Sync Masters (`.claude/agents-sync/`)

**Build order: same as Step B — all agents except Caret first, Caret last.**

The Sync Masters are the authoritative, full-spec instruction files for each agent. They live in `.claude/agents-sync/` and are uploaded to Claude Project Knowledge via `claudesync push`. Agents running inside a Claude Project session load these files automatically as ambient context — they do not need to read them via a tool call.

Create `.claude/agents-sync/` if it does not exist. For each agent:

1. Read `prompts/specs/agent-[name].md` — same source spec as Step B
2. Write the full agent file to `.claude/agents-sync/[name].md` — **identical to what you would have written in `.claude/agents/` before the dual-output model was introduced**
3. Each Sync Master must include:
   - **YAML frontmatter** (same as the stub) — name, description, model, tools
   - Full personality, responsibilities, and all behavioral rules (these are now fully consolidated in the agent specs and must be copied verbatim without summarizing)
   - **`## Sync Protocol` section** (immediately after Personality, before Responsibilities) with this exact content for all agents **EXCEPT Caret**:

```markdown
## Sync Protocol

When invoked directly (e.g. `mmw:[name] [codename]`), the codename is passed in your invocation context.

Before reading any input files, run via Bash:
```
python mmw_tools.py sync_pull <codename>
```

After writing all output files, run via Bash:
```
python mmw_tools.py sync_push <codename>
```

If either call fails, log `[sync-warn] sync_pull failed — using local files` or `[sync-warn] sync_push failed — <error>` in status.md and continue. Never block work for a sync failure.
```

> **For Caret Only**: Do **not** inject the generic `## Sync Protocol` section. Caret's spec (`prompts/specs/agent-caret.md`) already contains a complex, specialized `## Cloud Project Sync Protocol` block. Just copy Caret's spec verbatim.

4. Verify each file exists and is non-empty before moving to the next agent

**Stub vs. Sync Master distinction**:

| File | Location | Contains | Purpose |
|---|---|---|---|
| Local Stub | `.claude/agents/[name].md` | YAML frontmatter + redirect line + sync block | Claude Code agent registration |
| Sync Master | `.claude/agents-sync/[name].md` | Full instructions (all phases, logic, constraints) | Claude Project Knowledge source |

**After all Sync Masters are written**, print this instruction for the user:

```
Step H complete. To seed the Claude Project with agent instructions:
  claudesync push

This uploads .claude/agents-sync/ to your Claude Project Knowledge, making
full agent instructions available as ambient context in every Project session.

If claudesync is not yet configured, run:
  python mmw-init-setup.py
```

> **Do not mark Step H `[x]` until all 10 Sync Master files exist and are non-empty.**

