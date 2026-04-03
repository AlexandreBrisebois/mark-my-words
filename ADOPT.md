# Adopting Mark My Words

This guide walks you through installing Mark My Words and making it your own.

## 1. Installation

1. Clone this repository.
2. Open the folder in VS Code.
3. Confirm the GitHub Copilot extension is installed and active.

## 2. Personalization (5 Minutes)

Mark My Words separates your personal identity from the editorial core. To make it yours, edit these files in `.github/agents/configurations/`:

### Essential
- **profile.md** — Your name, website, topic, origin story
- **brand-style.md** — Your voice, tone, and banned words

### Optional  
- **READABILITY.md** — Your readability target (default: Grade 8)
- **visual-brand.md** — Your visual aesthetic guidelines

These files are loaded at every agent run. Changes apply instantly.

## 3. Make Your First Agent Call

Open Copilot Chat and try this:

```
@compass I want to write about [your topic]. 
The core problem is [what problem you're solving].
The reader is [who this is for].
```

Compass will return a strategic brief and save its thinking to `compass.state.md`.

## 4. Understand the Workflow (No Lock-in)

The default sequence is:

```
compass (strategy)
  → turing (research)
    → caret (draft)
      → mark, echo, devil (audit in any order)
        → prism (visual)
          → press (publish)
```

**But you don't have to follow it.** You can:
- Skip steps you don't need
- Call agents in any order
- Run the same agent multiple times
- Iterate: compass → turing → compass (refined) → turing → caret

All agents read each other's state files to recover context. You never need to repeat information.

## 5. Restore Workflow Status

If you return to a piece after time away:

```
@mmw What's the current status of this piece?
```

The orchestrator will read your folder, determine where you stand, and suggest the next step.

---

## Architecture Overview

Each agent maintains its own state file in your working folder:

- `compass.state.md` — Strategy and editorial direction
- `turing.state.md` — Research findings and evidence
- `caret.state.md` — Draft versions and editing decisions
- `mark.state.md` — Brand audit results
- `echo.state.md` — Reader experience feedback
- `devil.state.md` — Credibility and risk analysis
- `prism.state.md` — Visual direction and image prompts
- `press.state.md` — Publication metadata and frontmatter

These state files are the durable layer. If a session ends or you switch computers, agents recover context by reading these files. Nothing is lost.

---

## Example Workflow

This shows one real iteration cycle:

```
Step 1: Strategy
@compass Here's my idea about AI agents in production. I want to help CTOs understand the cost model.

Step 2: Research
@turing -compass What do recent benchmarks show about latency and token costs in multi-agent loops?

Step 3: Refine Strategy
@compass -turing Based on the research, should I narrow the angle or broaden the scope?

Step 4: Draft
@caret -compass -turing Now draft the opening section and the main cost model analysis.

Step 5: Audit
@mark Audit this draft for brand alignment.
@echo Where will engineering leaders bounce?
@devil What credibility gaps exist?

Step 6: Finalize
@press Prepare for publication.
```

Each agent reads the state files before and after to know what happened before. You stay in control throughout.

---

**Happy writing!**
