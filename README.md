# mark-my-words

Mark My Words (MMW) is a multi-agent writing system built on Claude Code. It orchestrates a set of specialized agents — researcher, strategist, writer, critic, publisher — through a structured workflow to produce blog posts for [alexandrebrisebois.github.io](https://alexandrebrisebois.github.io/).

## How to use

### Before the first draft

Before anything else, Index checks your archive for overlapping topics and produces a short report. You'll see four options:

- **[U] Update** — improve an existing post instead of writing a new one
- **[D] Differentiate** — continue but sharpen the angle so it doesn't duplicate
- **[P] Proceed** — no meaningful overlap, carry on
- **[A] Abandon** — discard this piece (you'll be asked to type the codename to confirm)

### Start a new piece

Tell Caret what you want to write:

```
MMW write a post about building this writer's room
```

Caret generates a codename, creates a piece folder, and writes `brief.md` from your intent. From there it runs the full workflow automatically — Compass sets strategy, Turing researches, Caret drafts, Mark reviews the voice and headlines.

### Stay in the loop

The workflow pauses at every decision point. After Mark reviews the first draft you'll see the flagged issues and three options:

- **[C] Co-edit** — Caret surfaces the exact lines that need attention, you edit the draft file directly, then type `MMW:done` to hand it back
- **[R] Revise** — Caret revises based on Mark's notes without your direct edits
- **[N] Move to critique** — exit the loop and send the current draft to Devil and Echo

Your voice always takes precedence. If you edited a line, Caret won't silently rewrite it.

If Mark flags a structural issue that can't be fixed by revision alone, you'll see a **HOLD** instead. The loop exits immediately with three options:

- **[B] Revisit brief** — rethink scope before continuing
- **[C] Co-edit** — take manual control of the draft
- **[S] Proceed anyway** — continue to critique with the draft as-is

### Critique and publish prep

After the draft clears the Mark loop, Devil and Echo run in parallel — Devil audits for unsupported claims, Echo checks audience fit. Caret consolidates their feedback and pauses again so you can revise or proceed.

If you made edits during that revision window, Mark runs a one-pass brand re-alignment check on the updated draft. You'll see a PASS, a REVISE with specific fixes offered, or a HOLD for structural issues. After any fix pass you can choose **[L] Back to creative mode** to keep working with Mark, or **[P] Proceed** to move on.

Press and Prism then run in parallel: Press writes the Hugo front matter and SEO notes, Prism produces the image prompt.

### Declare it done

When you're happy with the draft:

```
MMW:proof [codename]
```

Caret runs a pre-flight check (draft, SEO, slug, image prompt all present), writes `final.md`, copies it to `writers-room/published/[slug].md`, and archives the piece.

### Resume anytime

Sessions can be interrupted and resumed. Pick up where you left off:

```
MMW:bearings [codename]
```

Caret reads `status.md`, reports what's done, and proposes the next step — but never advances automatically. You give the instruction.

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
| `specs/agent-turing.md` | Turing — research |
| `specs/agent-echo.md` | Echo — audience |
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