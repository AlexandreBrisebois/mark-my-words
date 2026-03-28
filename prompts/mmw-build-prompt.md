# MMW Build Prompt
# Mark My Words — Multi-Agent Writing System

> [!IMPORTANT]
> **AGENTIC INSTRUCTION**: You are building a multi-agent writing system
> called Mark My Words (MMW). Maintain a `task.md` file in the root of
> the writers-room/ project to track your progress through each phase.
> Do not attempt to complete the entire build in one turn.
>
> **task.md format** — use this structure exactly so a resumed session can parse it:
> ```
> ## Build Progress
> - [ ] Step A — Scaffold + Seed files (Steps A and F complete together — do NOT mark [x] until seed files in Step F are written)
> - [ ] Step B — Agent files
> - [ ] Step C — ARCHITECTURE.md
> - [ ] Step D — CLAUDE.md
> - [ ] Step E — Brand guidelines
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
├── CLAUDE.md                  ← project root — triggers MMW, MMW:agent shortcuts
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
```

After creating `pieces/` and `published/`, write an empty `.gitkeep` file in each so Git tracks them.

**CLAUDE.md must be at the project root** (`/Users/alex/Code/mark-my-words/CLAUDE.md`),
not inside `writers-room/`. This is required for Claude Code to recognize the
MMW triggers and `MMW:agent` shortcuts in every new session.

**Agent files must be in `.claude/agents/`** relative to the project root.
This is the directory Claude Code scans to register native subagents. Files
in `writers-room/agents/` will not be auto-discovered.

> **Note**: Seed files for `index/`, `cadence/`, and `research/` are defined in
> Step F below. Step A is only complete when both the scaffold and seed files
> are written — agents depend on these files existing before any workflow runs.

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

**Cross-check before moving to Step C**: Read back the status.md initialization block in `.claude/agents/caret.md` and the Edit-tool replace target in `.claude/agents/press.md`. Confirm both reference the exact string `- Slug: (written by Press)` — character for character, including parentheses and capitalization. If they differ, fix whichever is wrong before continuing.

---

### Step C — ARCHITECTURE.md

Read `prompts/specs/flow.md` before writing. Cover:
- How Caret orchestrates the sub-agents
- The full ordered workflow with all 11 phases
- The three parallel execution pairs: Devil ║ Echo, Press ║ Prism, Index ║ Cadence
- The iterative Caret/Mark loop, co-edit mode, and circuit breaker logic
- The Index overlap gate and startup validation
- The research gate in Caret
- Codename generation rules
- Draft versioning rules — never overwrite, always increment
- The Prism → image-prompt.md → GitHub Actions handoff
- Full file schema with status.md structure
- Session resume: how to re-enter mid-workflow via status.md

---

### Step D — CLAUDE.md

**Location**: `/Users/alex/Code/mark-my-words/CLAUDE.md` (project root — not inside writers-room/).

Read `prompts/specs/flow.md` before writing. Cover:
- What Mark My Words is — one paragraph
- Both trigger aliases: MMW and Mark My Words
- All sub-agent shortcuts with examples (note: each invokes a native Claude Code subagent defined in `.claude/agents/`)
- `MMW:proof` — the human gate that triggers Phase 11. Explain that no agent calls this automatically; it is always a deliberate human decision. State explicitly that `MMW:proof` is handled inline by Caret — there is no `.claude/agents/proof.md`. When the user types `MMW:proof [codename]`, Caret reads the piece folder and executes the Phase 11 pre-flight directly.
- State explicitly that `MMW:bearings` is handled inline by Caret — there is no `.claude/agents/bearings.md`. When the user types `MMW:bearings [codename]`, Caret reads status.md and reports the current state of the piece before proposing a next step.
- Caret as the default entry point
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
  User: MMW:done
  Caret: [reads edited file, integrates remaining issues,
          produces draft-v2.md, reports exactly what it changed
          beyond the user's edits]

Co-edit is the most important feature in this system.
The user's voice is the point. Everything else serves that.
```

- That image-prompt.md must be one focused paragraph — no headers, no bullets, no code fences
- Final drafts land in `writers-room/published/[slug].md` — bring them to your publishing environment manually. MMW does not write outside its own directory.
- Parallel agent recovery: if you return to a session and status.md shows `[partial]` with no recent activity, the agent likely timed out. Use the relevant `MMW:agent` shortcut to retry the missing agent. Example: `[partial] Echo → pending` means `MMW:echo` to retry.
- Scaffold recovery: if `MMW:proof` stops with "writers-room/published/ directory missing", the project scaffold is incomplete. Fix: run `mkdir -p writers-room/published/` from the project root, then retry `MMW:proof [codename]`.
- Reminder: this is a writing tool — responses should be editorial, thoughtful, and concise. Not a coding tool.

---

### Step E — Brand Guidelines (`writers-room/brand/guidelines.md`)

Write starter brand guidelines for Mark based on:
- Author: Alexandre Brisebois, AI Enthusiast, builder-in-public
- Brand pivot: from multi-cloud engineering to AI agent building and learning in public
- Audience: CTOs, engineers, technical leaders — skeptical, time-poor, technically sharp
- Tone: honest, reflective, direct — no hype, no fluff, no consulting-deck polish
- Blog aesthetic: minimalist, editorial, warm — "Calm Signal"
- Visual: warm off-white #F7F5F0, calm green accent #2D6A4F, near-black ink #1A1A18
- Topics: AI agents, building in public, retrospectives, failure, recovery, honest learning
- Voice: first person, contemplative, exploratory, honestly excited
- Microsoft is origin story, not current identity
- The old WordPress blog is archive, not content to migrate
- Banned words enforced at all times: Utilize, Deep-dive, Game-changing, Synergy, Very, Extremely, Robust, Additionally, Furthermore, Moreover, Leverage
- Pronoun rules: "We" for shared capability and success, "I" for vulnerability and opinion, never "I built" or "I achieved" alone
- Emotional register default: reflective-vulnerable blended with urgently excited

---

### Step F — Seed Files

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

1. User types: `MMW write a post about building this writer's room`
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
    - Prism reads latest draft-vN.md → image-prompt.md as one focused paragraph
24. User types: `MMW:proof writers-room-build`
25. Pre-flight check passes — draft, seo.md, slug, image-prompt.md all present
26. final.md written and copied to `writers-room/published/writers-room-build.md`
27. Index ║ Cadence run in parallel:
    - Index updates post-index.md with new entry
    - Cadence logs codename, description, and target publish date in calendar.md
