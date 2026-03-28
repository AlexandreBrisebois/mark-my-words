# MMW Build Prompt
# Mark My Words — Multi-Agent Writing System

> [!IMPORTANT]
> **AGENTIC INSTRUCTION**: You are building a multi-agent writing system
> called Mark My Words (MMW). Maintain a `task.md` file in the root of
> the writers-room/ project to track your progress through each phase.
> Do not attempt to complete the entire build in one turn.
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

## Context

I am an AI Enthusiast building and documenting this system publicly as
part of my blog. My goal is to learn about AI, leveraging AI, building
AI agents, writing about the learning process, and sharing honest
retrospectives in public.

The blog lives at https://alexandrebrisebois.github.io/ and is built
with Hugo on GitHub Pages.
Blog root: `/Users/alex/Code/AlexandreBrisebois.github.io/`

My existing GitHub Copilot prompts are at:
`/Users/alex/Library/Application Support/Code/User/prompts/`

**Migrate the following files into the new agent system.** Preserve all
logic. Update all brand references from multi-cloud/srvrlss.dev to
AI Enthusiast framing:

| Source File | Migrates To |
|---|---|
| `brand-voice.instructions.md` | Mark |
| `brand-strategy.prompt.md` | Compass |
| `content-writer.prompt.md` | Caret |
| `accusation-audit.prompt.md` | Devil |
| `seo-audit.prompt.md` | Press |
| `seo-blog-audit.prompt.md` | Index |
| `visual-brand-validator-dual-mode.prompt.md` | Prism |

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

Create `task.md` first. Then create this full directory structure:

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
    ├── posts/
    │   ├── drafts/
    │   └── published/
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

**CLAUDE.md must be at the project root** (`/Users/alex/Code/mark-my-words/CLAUDE.md`),
not inside `writers-room/`. This is required for Claude Code to recognize the
MMW triggers and `MMW:agent` shortcuts in every new session.

**Agent files must be in `.claude/agents/`** relative to the project root.
This is the directory Claude Code scans to register native subagents. Files
in `writers-room/agents/` will not be auto-discovered.

---

### Step B — Agent System Prompts (`.claude/agents/`)

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
- Preserve all logic from the corresponding Copilot prompt file listed in the migration table
- Apply brand pivot throughout using these exact substitutions:
  - `srvrlss.dev` → `alexandrebrisebois.github.io`
  - `multi-cloud engineer` / `serverless` → `AI agent builder` / `AI Enthusiast`
  - `Technical Outcome Leader` → omit or replace with `builder-in-public`

**Each agent file must open with this frontmatter structure:**

```yaml
---
name: [agent-name]
tools: [Tool1, Tool2, ...]
---
```

**Tool scoping per agent — use exactly these values in frontmatter:**

| Agent | `tools` frontmatter value |
|---|---|
| Caret | Read, Write, Edit, Grep, Agent, Glob |
| Mark | Read, Write |
| Compass | Read, Write |
| Devil | Read, Write |
| Turing | Read, Write, WebSearch, WebFetch |
| Echo | Read, Write |
| Press | Read, Write, Edit, Glob |
| Prism | Read, Write, Glob |
| Index | Read, Write, Glob |
| Cadence | Read, Write |

Tool scoping is enforced by Claude Code via the frontmatter — not by prose
instructions inside the file body. Do not rely on written instructions alone
to restrict tool access.

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
- The Prism → image-prompt.txt → GitHub Actions handoff
- Full file schema with status.md structure
- Session resume: how to re-enter mid-workflow via status.md

---

### Step D — CLAUDE.md

**Location**: `/Users/alex/Code/mark-my-words/CLAUDE.md` (project root — not inside writers-room/).

Read `prompts/specs/flow.md` before writing. Cover:
- What Mark My Words is — one paragraph
- Both trigger aliases: MMW and Mark My Words
- All sub-agent shortcuts with examples (note: each invokes a native Claude Code subagent defined in `.claude/agents/`)
- `MMW:proof` — the human gate that triggers Phase 11. Explain that no agent calls this automatically; it is always a deliberate human decision
- Caret as the default entry point
- Codename generation rules: derived from brief, descriptive, lowercase hyphenated, 2–3 words
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

- That image-prompt.txt must be plain text, no markdown
- Hugo blog root: `/Users/alex/Code/AlexandreBrisebois.github.io/`
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
| Codename | Description | Slug | Status | Topics | Published | Links |
|---|---|---|---|---|---|---|
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

When the build is complete, verify the success criteria in `prompts/specs/flow.md` § Success Criteria can be traced through the built artifacts. Do not run a live session — just confirm all required files exist and that the agent files contain the logic needed to execute each step.
