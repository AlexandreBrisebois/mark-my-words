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

## What To Build

### Step A — Project Scaffold

Create `writers-room/task.md` first. Then create this full directory structure:

```
/Users/alex/Code/mark-my-words/
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

/Users/alex/Code/mark-my-words/.claude/agents/
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

/Users/alex/Code/mark-my-words/.claude/skills/
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

**CLAUDE.md must be at the project root** (`/Users/alex/Code/mark-my-words/CLAUDE.md`),
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

### Step B — Agent System Prompts (`.claude/agents/`)

**Build order: build all agents except Caret first. Build Caret last.**
Caret's spec cross-references behavior defined in Index, Press, and co-edit.
Build those agents first so that logic is fresh when you write caret.md.

Read each agent spec from `prompts/specs/agent-[name].md` and create the
corresponding file in `.claude/agents/`. Build one agent at a time. Verify
the file exists and is non-empty before moving to the next.

Each agent file must:
- **Begin with YAML frontmatter** that declares the agent's name and permitted tools
- Open with agent name, role, and one-line purpose
- Define personality and communication style
- List all responsibilities explicitly
- Define inputs (exact filenames) and outputs (exact filenames)
- Specify handoff targets
- Apply brand pivot throughout using these exact substitutions:
  - `srvrlss.dev` → `alexandrebrisebois.github.io`
  - `multi-cloud engineer` / `serverless` → `AI agent builder` / `AI Enthusiast`
  - `Technical Outcome Leader` → omit or replace with `builder-in-public`

**Each agent file must open with this frontmatter structure:**

```yaml
---
name: [agent-name]
description: One-line purpose of this agent (use the "One-line purpose" from the spec)
model: claude-sonnet-4-6
tools: [Read, Write, Edit]
---
```

The `tools` value must be a YAML inline sequence (bracketed, comma-separated). This is the format Claude Code parses to enforce tool scoping. Do not write it as a plain string (`tools: Read, Write` is wrong — it will not be parsed as a list). After writing each agent file, read back the `tools:` line and confirm it opens with `[` and closes with `]`. If it is a plain string, rewrite the file before moving to the next agent.

Every agent file must also include `model: claude-sonnet-4-6` in its frontmatter. This ensures all subagents run on a capable model regardless of which model the parent session is using.

**Tool scoping per agent — use exactly these values in frontmatter:**

| Agent | `tools` frontmatter value |
|---|---|
| Caret | Read, Write, Edit, Agent, Glob |
| Mark | Read, Write |
| Compass | Read, Write, Glob |
| Devil | Read, Write |
| Turing | Read, Write, WebSearch, WebFetch, Glob, Bash |
| Echo | Read, Write |
| Press | Read, Write, Edit, Glob, Bash |
| Prism | Read, Write, Glob |
| Index | Read, Write, Glob, Bash |
| Cadence | Read, Write, Bash |

Tool scoping is enforced by Claude Code via the frontmatter — not by prose
instructions inside the file body. Do not rely on written instructions alone
to restrict tool access.

> **Tool names are case-sensitive** and must match Claude Code's registered names
> exactly: `Read`, `Write`, `Edit`, `Agent`, `Glob`, `Bash`, `WebSearch`, `WebFetch`.
> A mistyped tool name will silently fail to scope access — no error is raised.

> **Parallel spawning requires same-response Agent calls.** When Caret spawns a
> parallel pair (Devil║Echo, Press║Prism, Index║Cadence), both Agent tool calls
> must be issued in the same response turn. Sequential calls are functionally
> correct but will not run concurrently.

**Auto-mode behavior — Caret**: When writing `.claude/agents/caret.md`, include these behaviors (read `prompts/specs/agent-caret.md` for full detail):
- Pre-step flag parsing: check for `--auto` in the trigger text, strip it, set mode
- If mode = auto: write `- Mode: auto` in the `## Current State` block of status.md at init; omit in manual mode
- Session resume: read `Mode:` from status.md `## Current State`; if `Mode: auto` present, auto mode applies for all remaining phases
- Phase 5 loop cap in auto: 1 Mark pass only — REVISE applied directly, HOLD logged and exits, PASS exits; co-edit not available
- Phase 8 in auto: apply Devil/Echo feedback directly, produce new draft, log summary, skip Phase 8.5
- Manual mode: surface a concrete next-step prompt after every phase completion (pre-filled command + [C]/[S] options)

**Auto-mode behavior — Turing**: When writing `.claude/agents/turing.md`, include these behaviors (read `prompts/specs/agent-turing.md` for full detail):
- At startup, read `Mode:` from status.md; if `Mode: auto`, skip the deep dive entirely
- Log `[auto] Deep dive skipped` under `## Deep Dive Candidates (skipped — auto mode)` in research.md
- Proceed to Phase 3 immediately without surfacing candidates

**Cross-check before moving to Step C**: Read back the status.md initialization block in `.claude/agents/caret.md` and the Edit-tool replace target in `.claude/agents/press.md`. Confirm both reference the exact string `- Slug: (written by Press)` — character for character, including parentheses and capitalization. If they differ, fix whichever is wrong before continuing.

---

### Step C — ARCHITECTURE.md

Read `prompts/specs/flow.md` before writing. Cover:
- How Caret orchestrates the sub-agents
- The full ordered workflow with all 11 phases
- **Manual vs auto mode**: invocation syntax, what differs per phase (Phase 5 loop cap, Phase 8 no-pause, Phase 8.5 skipped, Turing deep dive skipped), proof gate always a human step in both modes
- The three parallel execution pairs: Devil ║ Echo, Press ║ Prism, Index ║ Cadence
- The iterative Caret/Mark loop, co-edit mode, and circuit breaker logic
- The Index overlap gate and startup validation
- The research gate in Caret
- Codename generation rules
- Draft versioning rules — never overwrite, always increment
- The Prism → image-prompt.md → GitHub Actions handoff
- Full file schema with status.md structure — include the optional `Mode: auto` field:
  ```
  ## Current State
  - Phase: 0 — Index overlap gate
  - Mode: auto    ← only present in auto mode; absent = manual
  - Current draft: draft-v2.md
  ...
  ```
- Session resume: how to re-enter mid-workflow via status.md; how Mode survives session boundaries

---

### Step D — CLAUDE.md

**Location**: `/Users/alex/Code/mark-my-words/CLAUDE.md` (project root — not inside writers-room/).

Read `prompts/specs/flow.md` before writing. Cover:
- What Mark My Words is — one paragraph
- **Single trigger**: `mmw` is the only recognized trigger. `MMW` and `Mark My Words` are not triggers. Document this explicitly.
- **Invocation modes** (read from flow.md § Modes):
  - `mmw [topic]` — manual mode (default)
  - `mmw --auto [topic]` — auto mode: runs full pipeline without pausing, stops at `mmw:proof`
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
- Final drafts land in `writers-room/published/[slug].md` — bring them to your publishing environment manually. mmw does not write outside its own directory.
- Parallel agent recovery: if you return to a session and status.md shows `[partial]` with no recent activity, the agent likely timed out. Use the relevant `mmw:agent` shortcut to retry the missing agent. Example: `[partial] Echo → pending` means `mmw:echo` to retry.
- Scaffold recovery: if `mmw:proof` stops with "writers-room/published/ directory missing", the project scaffold is incomplete. Fix: run `mkdir -p writers-room/published/` from the project root, then retry `mmw:proof [codename]`.
- Reminder: this is a writing tool — responses should be editorial, thoughtful, and concise. Not a coding tool.

---

### Step E — Skills (`.claude/skills/`)

Create one skill directory per mmw command. Each skill provides guaranteed slash-command routing instead of relying on CLAUDE.md trigger-word parsing. Skills are stored at `.claude/skills/<name>/SKILL.md`.

**Create all twelve skill directories and their SKILL.md files:**

---

#### `/mmw` — Main entry point

`.claude/skills/mmw/SKILL.md`:
```yaml
---
name: mmw
description: Launch the Mark My Words writing system. Spawns Caret as orchestrator for a new piece or resumes an existing one by codename.
argument-hint: [topic or codename]
---

Spawn the `caret` subagent defined in `.claude/agents/caret.md`, passing `$ARGUMENTS` as the user's topic, brief, or codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw [topic or codename]" and do nothing further.
```

---

#### `/mmw-turing` — Research pass

`.claude/skills/mmw-turing/SKILL.md`:
```yaml
---
name: mmw-turing
description: Run a research pass on an active mmw piece. Spawns Turing directly, bypassing Caret.
argument-hint: [codename]
---

Spawn the `turing` subagent defined in `.claude/agents/turing.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-turing [codename]" and do nothing further.
```

---

#### `/mmw-devil` — Accusation audit

`.claude/skills/mmw-devil/SKILL.md`:
```yaml
---
name: mmw-devil
description: Run an accusation audit on the latest draft of an active mmw piece. Spawns Devil directly.
argument-hint: [codename]
---

Spawn the `devil` subagent defined in `.claude/agents/devil.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-devil [codename]" and do nothing further.
```

---

#### `/mmw-echo` — Audience check

`.claude/skills/mmw-echo/SKILL.md`:
```yaml
---
name: mmw-echo
description: Run an audience check on the latest draft of an active mmw piece. Spawns Echo directly.
argument-hint: [codename]
---

Spawn the `echo` subagent defined in `.claude/agents/echo.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-echo [codename]" and do nothing further.
```

---

#### `/mmw-press` — SEO + Hugo front matter

`.claude/skills/mmw-press/SKILL.md`:
```yaml
---
name: mmw-press
description: Run an SEO audit and generate Hugo front matter for the latest draft of an active mmw piece. Spawns Press directly.
argument-hint: [codename]
---

Spawn the `press` subagent defined in `.claude/agents/press.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-press [codename]" and do nothing further.
```

---

#### `/mmw-prism` — Image prompt

`.claude/skills/mmw-prism/SKILL.md`:
```yaml
---
name: mmw-prism
description: Generate a Gemini Image Pro prompt for the latest draft of an active mmw piece. Spawns Prism directly.
argument-hint: [codename]
---

Spawn the `prism` subagent defined in `.claude/agents/prism.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-prism [codename]" and do nothing further.
```

---

#### `/mmw-compass` — Strategic direction

`.claude/skills/mmw-compass/SKILL.md`:
```yaml
---
name: mmw-compass
description: Run a strategic direction pass on an active mmw piece, or generate next post ideas if no codename is provided. Spawns Compass directly.
argument-hint: [codename]
---

Spawn the `compass` subagent defined in `.claude/agents/compass.md`, passing `$ARGUMENTS` as the active piece codename (or empty for a next-post-ideas pass).
```

---

#### `/mmw-mark` — Brand review

`.claude/skills/mmw-mark/SKILL.md`:
```yaml
---
name: mmw-mark
description: Run a brand and voice review on the latest draft of an active mmw piece. Spawns Mark directly.
argument-hint: [codename]
---

Spawn the `mark` subagent defined in `.claude/agents/mark.md`, passing `$ARGUMENTS` as the active piece codename.

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-mark [codename]" and do nothing further.
```

---

#### `/mmw-cadence` — Editorial calendar

`.claude/skills/mmw-cadence/SKILL.md`:
```yaml
---
name: mmw-cadence
description: Check the editorial calendar state and get cadence suggestions. Spawns Cadence directly.
---

Spawn the `cadence` subagent defined in `.claude/agents/cadence.md`.
```

---

#### `/mmw-index` — Overlap check or portfolio audit

`.claude/skills/mmw-index/SKILL.md`:
```yaml
---
name: mmw-index
description: Run an overlap check on an active mmw piece, or run a portfolio SEO audit if no codename is provided. Spawns Index directly.
argument-hint: [codename]
---

Spawn the `index` subagent defined in `.claude/agents/index.md`, passing `$ARGUMENTS` as the active piece codename (or empty for a portfolio SEO audit).
```

---

#### `/mmw-bearings` — Session orientation

`.claude/skills/mmw-bearings/SKILL.md`:
````yaml
---
name: mmw-bearings
description: Get a session orientation report for an active mmw piece — what has been done, current draft, outstanding work, and proposed next step.
argument-hint: [codename]
---

Invoke Caret inline (do not spawn a subagent). Read `writers-room/pieces/$ARGUMENTS/status.md` and the agent run log, then produce a concise orientation report:

```
Bearings: [codename]
Description: [one-line description from status.md]

Done:
  [x] [each completed agent run from the log]

Current draft: [latest draft-vN.md]
Outstanding: [summary of what is not yet done]

Next step: [proposed next action]
  [C] Continue  [S] Stop
```

If `$ARGUMENTS` is empty, respond: "Usage: /mmw-bearings [codename]" and do nothing further. Always pause after the report — never auto-advance.
````

---

#### `/mmw-proof` — Declare draft final (human gate)

`.claude/skills/mmw-proof/SKILL.md`:
```yaml
---
name: mmw-proof
description: Declare an mmw piece final. Runs pre-flight checks and, if all pass, writes final.md and publishes to writers-room/published/. This is always a deliberate human decision — no agent calls this automatically.
argument-hint: [codename]
---

Invoke Caret inline (do not spawn a subagent). Execute the Phase 11 pre-flight directly for the piece named by `$ARGUMENTS`:

1. Verify `writers-room/pieces/$ARGUMENTS/seo.md` exists
2. Verify the `Slug:` field in `writers-room/pieces/$ARGUMENTS/status.md` is populated
3. Verify the slug in `status.md` matches the slug in `seo.md`
4. Verify `writers-room/pieces/$ARGUMENTS/image-prompt.md` exists
5. Verify the latest `draft-vN.md` exists in the piece folder
6. Verify `writers-room/published/` directory exists

If all checks pass, write `final.md`, copy its content to `writers-room/published/[slug].md`, update `status.md`, write `Mode: archive-update` to `status.md`, then spawn Index and Cadence in parallel.

If `$ARGUMENTS` is empty: scan `status.md` files in `writers-room/pieces/` for any piece containing `Next step: Ready for mmw:proof`, list them, and ask the user to confirm which one to proof. Never assume.
```

---

**After writing all twelve SKILL.md files**, verify each exists and is non-empty before moving to Step F.

**Naming convention note**: Skill names use `[a-z0-9-]` only — no spaces, underscores, or special characters. The plain-text fallbacks (`mmw:turing`, `mmw:devil`, etc.) remain documented in CLAUDE.md for sessions where skills have not loaded, but the slash-command form is the canonical invocation.

---

### Step F — Brand Guidelines (`writers-room/brand/guidelines.md`)

Write starter brand guidelines for Mark based on:
- Author: Alexandre Brisebois, AI Enthusiast, Agentic AI, building and learning in public
- Audience: CTOs, engineers, technical leaders — skeptical, time-poor, technically sharp
- Tone: honest, reflective, direct — no hype, no fluff, no consulting-deck polish
- Blog aesthetic: minimalist, editorial, warm — "Calm Signal"
- Visual: warm off-white #F7F5F0, calm green accent #2D6A4F, near-black ink #1A1A18
- Topics: AI, Public Cloud, building in public, retrospectives, failure, recovery, honest learning
- Voice: first person, contemplative, exploratory, honestly excited
- Banned words enforced at all times: Utilize, Deep-dive, Game-changing, Synergy, Very, Extremely, Robust, Additionally, Furthermore, Moreover, Leverage
- Pronoun rules: "We" for shared capability and success, "I" for vulnerability and opinion, never "I built" or "I achieved" alone
- Emotional register default: reflective-vulnerable blended with urgently excited

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

**Pre-flight file check** (verify all of these exist and are non-empty before tracing the workflow):
- `writers-room/brand/guidelines.md` — contains the banned words list
- `writers-room/index/post-index.md` — contains the markdown table header
- `writers-room/cadence/calendar.md` — contains the markdown table header
- `writers-room/research/notes.md` — contains the markdown table header
- All 10 agent files in `.claude/agents/` — read back the `tools:` line in each file and confirm it opens with `[` and closes with `]`. A plain string (e.g., `tools: Read, Write`) will not raise an error but silently disables tool scoping at runtime. Fix any that fail this check before proceeding.
- All 12 skill directories in `.claude/skills/` — verify each contains a `SKILL.md` file that is non-empty: `mmw`, `mmw-turing`, `mmw-devil`, `mmw-echo`, `mmw-press`, `mmw-prism`, `mmw-compass`, `mmw-mark`, `mmw-cadence`, `mmw-index`, `mmw-bearings`, `mmw-proof`.

**Auto-mode trace** (verify caret.md and turing.md contain the required logic):
- `mmw --auto [topic]` → Caret strips `--auto`, generates codename, writes `- Mode: auto` to status.md
- Turing reads `Mode: auto` from status.md → skips deep dive, logs `[auto] Deep dive skipped`
- Phase 5: Caret runs 1 Mark pass, applies REVISE directly or exits on PASS/HOLD
- Phase 8: Caret applies Devil/Echo feedback directly, logs summary, skips Phase 8.5
- `mmw:proof` → still a human gate; auto mode pauses and waits
- Session resume: `mmw [codename]` → Caret reads `Mode: auto` from status.md → continues in auto mode

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
