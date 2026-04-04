# Mark My Words (mmw)

Mark My Words is a writers' room — a team of specialized AI agents that help you produce high-impact, long-form content while keeping your voice at the center.

Instead of one AI that tries to do everything, you work with specialists. Each one handles a distinct part of the editorial process. Call them in the order that fits your thinking. Skip steps when you don't need them. Iterate on strategy, research, and drafting as many times as you want.

---

## Your Editorial Team

These agents live in `.github/agents/`. You invoke them directly by name.

| Agent | Role | When to Use |
| :--- | :--- | :--- |
| **compass** | Editorial Strategist | Defining Audience, Angle, Stakes, and Scope before you begin. |
| **turing** | Expert Research Agent | Finding evidence, grounding claims, and identifying blind spots. |
| **caret** | Drafting & Revision | High-fidelity drafting, revision, and narrative Flow. |
| **mark** | Brand Guardian Auditor | Auditing for brand fit, tone, and specific voice constraints. |
| **echo** | Clarity & Resonance Auditor | Simulating reader friction points and clarity gaps. |
| **devil** | Risk & Resistance Auditor | Identifying credibility gaps and reputational risks. |
| **prism** | Visual Translator | Generating image prompts aligned with the drafted narrative. |
| **press** | Publication & Discoverability Auditor | Final proofing, SEO metadata, and publication-ready frontmatter. |
| **mmw** | Workflow Orchestrator | Suggesting next steps and checking current project status. |

---

## How It Works

Each agent reads shared state files to understand what work has already been done. You don't wait for orchestration. You call whoever you need next.

- **Read state files**: `compass.state.md`, `turing.state.md`, `caret.state.md`, etc. Each file preserves that agent's context and decisions.
- **Call agents directly**: `@compass`, `@turing`, `@caret`. No wrapper required.
- **Iterate freely**: Run the same agent multiple times. Strategy → Research → Strategy (refined) → Draft. Whatever your process needs.
- **Use mmw to recover status**: If you're returning to a piece after time away, `@mmw` will read the folder, determine where you stand, and suggest the next step.

---

## Setup & Personalization

1. Clone this repository.
2. Open the folder in VS Code.
3. Ensure GitHub Copilot extension is installed.
4. **Make it yours** (takes 5 minutes): Edit the files in `configurations/` to define your own style and voice. These files are the "North Star" for every agent call:
   - `configurations/profile.md` — Your name, site, core topic, and perspective.
   - `configurations/brand-style.md` — Your voice, tone, and zero-tolerance words.
   - `configurations/READABILITY.md` — Your target reading level (e.g., Grade 8).
   - `configurations/visual-brand.md` — Your preferred visual aesthetic for images.

---

## First Steps

### Start with strategy
Open Copilot Chat and call your strategist:

```
@compass Here's my idea: I want to write about [topic]. The problem I'm solving is [problem]. The audience is [who].
```

**Compass** will return a strategic brief. It saves its thinking to `compass.state.md`.

### Then research
Call your researcher with the compass output:

```
@turing -compass What are the current patterns in [topic]? What am I missing?
```

**Turing** saves findings to `turing.state.md`. You can iterate: refine your strategy with compass again, then run turing with fresh research priorities.

### Then draft
When you're ready:

```
@caret -compass -turing Draft the opening and first section. Use the compass strategy and turing research.
```

**Caret** creates `{slug}.draft.md` and saves its work to `caret.state.md`.

### Then audit and refine
Run whichever auditors help most to sharpen the draft:

```
@mark Audit this draft for brand fit and tone.
@echo Find where readers will bounce.
@devil Identify credibility gaps.
```

Edit the draft manually. Run auditors again. Iterate until you're satisfied.

### Then finalize
When the draft is solid:

```
@press Prepare this for publication.
```

**Press** generates SEO metadata and publication-ready frontmatter. Everything is ready for production.

