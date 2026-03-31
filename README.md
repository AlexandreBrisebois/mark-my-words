# mark-my-words

Mark My Words (mmw) is a multi-agent writing system built on Claude Code. It orchestrates a set of specialized agents — researcher, strategist, writer, critic, publisher — through a structured workflow to produce blog posts for [srvrlss.dev](srvrlss.dev).

## Setup

Mark My Words uses a **Claude Project** as its canonical state store. Local files are the editor surface; the Project is the source of truth.

### 1. Initialize Project

To ensure **Claude Code** and its agents have immediate access to the necessary tools, we install dependencies globally. 

```bash
# Install required dependencies globally
pip install --break-system-packages -r requirements.txt

# Run the guided setup script (Automates Validation & Seeding)
python3 scripts/mmw_init-setup.py
```

This script:
1. Guides you through the **claude.ai sessionKey** retrieval.
2. Links your local folder to a **Claude Project**.
3. **Validates the build** (agent stubs, sync masters, skills, seed files).
4. **Seeds the project** with everything in `.claude/agents-sync/` and critical global context files (`guidelines.md`, `calendar.md`, etc.).

> [!CAUTION]
> **Keep your `sessionKey` private.** It grants full access to your Claude account. The `.claude/config.json` file is automatically added to `.gitignore` by the setup script.

### How sync works in practice

Mark My Words uses a **System vs. Runtime** synchronization strategy to minimize token usage and keep the Claude Project knowledge relevant:

- **System Context**: Agent Specs (`.claude/agents-sync/`), Skills (`.claude/skills/`), and Brand Guidelines are static. They are pushed once during initiation or manually via `sync_system`.
- **Runtime Context**: `calendar.md`, `post-index.md`, and `research/notes.md` are dynamic and synced on every agent transition.
- **Piece Context**: Only the files within the active piece folder (e.g., `pieces/codename/*`) are synced during the drafting process.

Caret manages sync automatically during each workflow run:

- **Session start**: pulls the **Runtime Context** and the active piece folder.
- **Pre-spawn**: pulls the input files required by the next agent before spawning it.
- **Post-spawn**: pushes the output files produced by the agent after it completes.
- **Post co-edit (`mmw:done`)**: triggers an immediate push of the edited draft.
- **After proof (`mmw:proof`)**: calls `sync_clean` to remove the piece folder from the project, keeping cloud context lean.

Sync tools are available as direct CLI calls for manual use:

```bash
python scripts/mmw_tools.py sync_system <codename>    # push full project state (System + Runtime + Piece)
python scripts/mmw_tools.py sync_pull <codename>      # pull active piece + runtime files
python scripts/mmw_tools.py sync_push <codename>      # push active piece + runtime files
python scripts/mmw_tools.py sync_clean <codename>     # remove piece from cloud (post-publish)
python scripts/mmw_tools.py sync_targets <agent_name> # inspect what an agent needs to sync
```

---

## How to use

### Start a new piece

Trigger Caret with a topic string, a file path, or bullet brainstorm items:

```
mmw write a post about building this writer's room
mmw path/to/my-notes.md
mmw - First observation about the topic / Second angle / Key constraint
```

Caret generates a codename, creates a piece folder, and writes `brief.md` from your intent. From there it runs the full workflow — Index checks your archive first, then Compass sets strategy, Turing researches, Caret drafts, and Mark reviews voice and headlines.

### Modes

**Manual (default)** — full control. Caret pauses at every decision point.

**Interactive (`--interactive`)** — section-by-section co-writing. You write, Caret reviews. Perfect for hands-on drafting where you want a real-time editor. Cannot be combined with auto modes.

```
mmw --interactive write a post about multi-agent observability
```

**Auto** — unattended. Caret runs the full pipeline and stops only at the human proof gate:

```
mmw --auto write a post about observability in multi-agent systems
```

**Auto-quick** — fast path for short posts or cheap first drafts. Skips Compass, Mark, Devil, and the revision window. Echo runs a lightweight audience check after the draft — if it flags a structural fit issue, you'll get one revise/skip choice before Press and Prism run. Produces a complete draft at low cost:

```
mmw --auto --quick write a post about observability in multi-agent systems
```

Use auto-quick when you need something concrete to react to before committing to a full pipeline run. After it completes, run `mmw [codename]` to continue in manual mode — the full pipeline picks up from the existing draft.

**Deadline-constrained auto**: If a piece has a target publish date in `calendar.md` and it is fewer than 3 days away, auto mode activates the quick path automatically. Caret logs the reason in status.md.

### Before the first draft

Before anything else, Index checks your archive for overlapping topics and produces a short report. You'll see four options:

- **[U] Update** — improve an existing post instead of writing a new one
- **[D] Differentiate** — continue but sharpen the angle so it doesn't duplicate
- **[P] Proceed** — no meaningful overlap, carry on
- **[A] Abandon** — discard this piece (you'll be asked to type the codename to confirm)

On [S]: Turing is skipped and Caret drafts from the brief and compass-notes alone. To adjust the angle after Compass has run, use `mmw:compass [codename]` directly.

### The Outline Gate (Phase 2.5) — manual/interactive only

Before the first draft is written, Caret synthesizes `brief.md`, `compass-notes.md`, and `research.md` into an `outline.md`. This is your structural sign-off point.

- **[C] Co-edit outline** — tweak the narrative arc or move sections around yourself.
- **[P] Proceed to Draft** — use the current outline to build the first full draft.

### Drafting and Section Reviews

**Automatic Citations**: During drafting, Caret and Turing manage citations automatically. All research data used is mapped to inline brackets `[N]` and a formal `## References` section is appended to your draft.

**Interactive Mode workflow**:
If running with `--interactive`, Caret creates an empty `draft-v1.md`. You write a section, then call:

```
mmw:review [codename]
```

Caret provides immediate **Section Feedback** (Clarity, Flow, Style, and Evidence) and suggests specific line edits for just that section before you move to the next.

### The Mark loop & Hook Refinement

After a full draft is ready, Mark reviews voice and brand alignment. In addition to the standard review, Phase 4 now generates **Hook Alternatives** at the bottom of `headlines.md`:

1. **Data-driven**: A hook anchored in a surprising statistic from your research.
2. **Story-driven**: A specific builder-in-public anecdote.
3. **Question-driven**: A tension-building question tuned to your target persona.

The first pass is a **voice check** ("is this piece distinctly yours?"). Subsequent passes are **polish passes** (banned words, rhythm, pronouns). After each pass:

- **[C] Co-edit** — Caret surfaces the exact lines that need attention, you edit the draft file directly, then type `mmw:done` to hand it back
- **[R] Revise** — Caret revises based on Mark's notes without your direct edits
- **[M] Move to critique** — exit the loop and send the current draft to Devil and Echo

Your voice always takes precedence. If you edited a line, Caret won't silently rewrite it. There is no iteration cap — you decide when to move on.

If Mark flags a structural issue, you'll see a **HOLD** instead. The loop exits immediately:

- **[B] Revisit brief** — re-examine the premise (the angle is the problem, not the lines)
- **[C] Co-edit** — take manual control of the draft
- **[M] Move to critique** — proceed to Devil and Echo with the draft as-is

In auto mode, HOLD also surfaces to you — it's the one interruption auto mode will make during the Mark pass. You can co-edit or skip it and continue.

### Critique and the revision window

After the draft clears the Mark loop, Devil and Echo run in parallel — Devil audits for unsupported claims, Echo checks audience fit through two named reader personas: **The Executive** (strategic CTO, reads for credibility signal) and **The Builder** (hands-on engineer, reads for "did they actually build it?").

Caret surfaces the feedback files directly and waits:

```
Feedback files:
  critique-vN.md (Devil)
  audience-vN.md (Echo)

  [C] Co-edit
  [R] Revise
  [T] Re-research
  [F] Fact-check  ← only shown if Devil flagged credibility concerns
  [P] Proceed to Press and Prism
  [X] Prioritize — Caret synthesizes Must / Worth / Already Working Well
```

Read the files first. Use **[X] Prioritize** if you want Caret to synthesize the feedback into a structured triage before choosing an action.

**[F] Fact-check**: Turing checks every draft claim against research.md and produces `fact-check-vN.md` with three sections — Confirmed, Ungrounded, Inaccurate. If a claim is ungrounded, you can run `mmw:turing [codename] --find-citation "[claim]"` to search for a supporting source. Caret reads the fact-check alongside Devil and Echo feedback in the combined revision pass.

**Single-persona mode**: Steer Echo to focus on one persona — `mmw:echo [codename] --persona "The Executive"` — when your brief specifies the primary audience.

After revising, you can run a brand re-alignment check on the updated draft before moving to publish prep — select **[B] Brand check** from the post-revision menu. Outcomes:

- **PASS** → `[L] Back to draft` or `[P] Proceed to Press and Prism`
- **REVISE** → `[C] Co-edit` / `[R] Revise` / `[P] Proceed` — then same [L]/[P] choice
- **HOLD** → `[B] Revisit brief` / `[C] Co-edit` / `[P] Proceed`

### Publish prep

Press and Prism run in parallel: Press writes the Hugo front matter and SEO notes, Prism produces the image prompt.

### Declare it done

When you're happy with the draft:

```
mmw:proof [codename]
```

Caret runs a pre-flight check (draft, SEO, slug, image prompt all present), writes `final.md`, copies it to `writers-room/published/[slug].md`, copies `image-prompt.md` to `writers-room/published/[slug]-image-prompt.md`, and archives the piece.

### Resume anytime

Sessions can be interrupted and resumed. Pick up where you left off:

```
mmw:bearings [codename]
```

Caret reads `status.md`, reports what's done, what's outstanding, and proposes the next step — but never advances automatically. You give the instruction.

## Sub-agent shortcuts

Each shortcut bypasses Caret and goes directly to the named agent:

| Shortcut | Agent | What it does |
|---|---|---|
| `mmw:turing [codename]` | Turing | Research pass on the active piece |
| `mmw:turing [codename] --fact-check` | Turing | Fact-check draft claims against research.md |
| `mmw:turing [codename] --find-citation "[claim]"` | Turing | Search for a citation, append to fact-check-vN.md |
| `mmw:devil [codename]` | Devil | Accusation audit on the latest draft |
| `mmw:echo [codename]` | Echo | Audience check (both personas) on the latest draft |
| `mmw:echo [codename] --persona "The Executive"` | Echo | Audience check — The Executive only |
| `mmw:echo [codename] --persona "The Builder"` | Echo | Audience check — The Builder only |
| `mmw:press [codename]` | Press | SEO audit + Hugo front matter for the latest draft |
| `mmw:prism [codename]` | Prism | Image prompt for the latest draft |
| `mmw:compass [codename]` | Compass | Strategic direction (or next post ideas if no codename) |
| `mmw:mark [codename]` | Mark | Brand review on the latest draft |
| `mmw:review [codename]` | Caret | Section feedback loop (interactive mode) |
| `mmw:cadence` | Cadence | Editorial calendar state and cadence suggestions |
| `mmw:index [codename]` | Index | Overlap check (or portfolio SEO audit if no codename) |
| `mmw:bearings [codename]` | Caret inline | Session orientation — handled inline by Caret |

## How to run the build

Point Claude Code at the build prompt:

```
prompts/mmw-build-prompt.md
```

This builds the full project scaffold, all agent files, and supporting docs from the specs in `prompts/specs/`.

## Spec structure

All build specs live in `prompts/specs/`. Each file is independently editable.

| File | Covers |
|---|---|
| `specs/flow.md` | Workflow, phases, protocols, file schema, constraints |
| `specs/agent-caret.md` | Caret — orchestrator + writer |
| `specs/agent-mark.md` | Mark — brand + voice |
| `specs/agent-compass.md` | Compass — strategist |
| `specs/agent-devil.md` | Devil — critique |
| `specs/agent-turing.md` | Turing — research + fact-check |
| `specs/agent-echo.md` | Echo — audience (The Executive, The Builder) |
| `specs/agent-press.md` | Press — publisher |
| `specs/agent-prism.md` | Prism — visual brand |
| `specs/agent-index.md` | Index — archivist |
| `specs/agent-cadence.md` | Cadence — scheduler |

## Making changes

- **Add a new agent**: create `specs/agent-newname.md`, add it to the tool scoping table in `mmw-build-prompt.md`, rebuild that agent.
- **Change a phase or protocol**: edit `specs/flow.md` only. Agent specs reference it but don't own it.
- **Change an agent's behavior**: edit `specs/agent-X.md` only, then rebuild that one agent from its spec.
- **Rebuild a single agent**: tell Claude Code to read `specs/agent-X.md` and regenerate `.claude/agents/X.md`.

## Repo layout

```
prompts/
├── mmw-build-prompt.md     ← build orchestrator
└── specs/                  ← one spec per agent + flow spec
.claude/agents/             ← generated agent files (Claude Code subagents)
writers-room/               ← generated content, brand files, piece folders
```
