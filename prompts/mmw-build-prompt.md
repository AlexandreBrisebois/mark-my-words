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

Used in: `.claude/agents/                ← Full Agent Specs
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

Also create `.claude/agents/                ← Full Agent Specs
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

.claude/skills/`). The plain-text `mmw` remains a fallback for sessions where skills are not loaded.
- All sub-agent shortcuts — now registered as skills (`/mmw-turing`, `/mmw-devil`, etc.) with plain-text `mmw:agent` variants documented as fallbacks. Note: each invokes a native Claude Code subagent defined in `.claude/agents/                ← Full Agent Specs
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

.claude/skills/`)

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
- All 10 agent files in `.claude/agents/                ← Full Agent Specs
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

.claude/skills/` — verify each contains a `SKILL.md` file that is non-empty: `mmw`, `mmw-turing`, `mmw-devil`, `mmw-echo`, `mmw-press`, `mmw-prism`, `mmw-compass`, `mmw-mark`, `mmw-cadence`, `mmw-index`, `mmw-bearings`, `mmw-proof`.

**Step 2 — Trace the workflow paths manually** (semantic reasoning required — the script cannot do this):

**Auto-mode trace** (verify caret.md and turing.md contain the required logic):
- `mmw --auto [topic]` → Caret strips `--auto`, generates codename, writes `- Mode: auto` to status.md
- Turing reads `Mode: auto` from status.md → skips deep dive, logs `[auto] Deep dive skipped`
- Phase 5: Caret runs 1 Mark pass, applies REVISE directly or exits on PASS/HOLD
- Phase 8: Caret applies Devil/Echo feedback directly, logs summary, skips Phase 8.5
- `mmw:proof` → still a human gate; auto mode pauses and waits
- Session resume: `mmw [codename]` → Caret reads `Mode: auto` from status.md → continues in auto mode
- Phase 11: Caret calls `scripts/mmw_tools.py publish <codename>` which writes both `writers-room/published/[slug].md` and `writers-room/published/[slug]-image-prompt.md` atomically

**Auto-quick trace** (verify caret.md contains the required logic):
- `mmw --auto --quick [topic]` → Caret strips both flags, writes `- Mode: auto-quick` to status.md
- Phase 1 skipped — logs `[skip] Phase 1 — auto-quick mode`
- Phase 0 (Index) runs as normal
- Phase 2 (Turing) runs — single focused search, no deep dive — logs `[auto] Deep dive skipped`
- Phase 3 (Caret draft) runs — from brief + research only; no compass-notes.md
- Phases 4, 5, 6+7, 8, 8.5 all skipped — each logged in status.md
- Phase 9+10 (Press ║ Prism) runs in parallel
- `mmw:proof` → human gate; waits
- Phase 11: same as auto, including both published/ file writes via `scripts/mmw_tools.py publish`
- Deadline-constrained upgrade: if `calendar.md` shows target date <3 days away in auto mode, caret.md upgrades to auto-quick and logs `[auto] Publish deadline in N days — fast path activated`

**Manual / Interactive trace** (reflects decoupled execution and context reset boundaries):

1. User types: `/mmw --interactive write a post about building this writer's room`
2. Caret strips flags, generates codename `writers-room-build`, creates folder, writes brief.md and status.md with `- Mode: interactive`
3. Phase 0 (Index) runs overlap check and passes.
4. Phase 1 (Compass) runs, sets angle, and Caret prompts to proceed to Turing.
5. Phase 2 (Turing) runs, produces research.md. Caret surfaces findings and executes Context Reset Boundary.
6. User types `/clear`
7. User types `mmw:bearings writers-room-build` -> Caret reads next_step and presents Outline Gate/Drafting options.
8. Caret reads brief, compass, research → produces an outline.md and waits for Co-edit or Draft.
9. Caret proceeds to draft, pauses and creates section-by-section review loop (`mmw:review` then `mmw:done`).
10. Caret executes Context Reset Boundary after draft completion.
11. User types `/clear`, then `mmw:bearings writers-room-build`.
12. Phase 5 (Mark loop) runs, reviews draft, surfaces findings, loop pauses if [REVISE] or [HOLD].
13. User enters Co-edit, edits draft, types `mmw:done`. Caret integrates and loop completes with [PASS].
14. Mark loop exits -> Caret executes Context Reset Boundary.
15. User types `/clear`, then `mmw:bearings writers-room-build`.
16. Phase 6+7 (Devil ║ Echo) run in parallel, Caret verifies completion.
17. Phase 8 (Revision window) surfaces critique. User revises draft.
18. Revision completes -> Caret executes Context Reset Boundary.
19. User types `/clear`, then `mmw:bearings writers-room-build`.
20. Phase 9+10 (Press ║ Prism) run in parallel -> wait for proof.
21. User types: `mmw:proof writers-room-build`.
22. Pre-flight passes; final.md and published files written atomically via `scripts/mmw_tools.py publish`.
23. Phase 11 finishes with Index ║ Cadence running in parallel to update logs.

---
