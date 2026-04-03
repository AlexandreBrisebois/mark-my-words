# Mark My Words (mmw)

Mark My Words is a writers' room — a team of specialized agents that help you produce high-impact, long-form content while keeping your voice at the center.

Instead of one AI that tries to do everything, you work with specialists. Each one handles a distinct part of the editorial process. Call them in the order that fits your thinking. Skip steps when you don't need them. Iterate on strategy, research, and drafting as many times as you want.

---

## Your Editorial Team

These agents live in `.github/agents/`. You invoke them directly by name.

| Agent | Role | When to Use |
| :--- | :--- | :--- |
| **compass** | Strategy Director | Setting editorial direction before you research or draft. |
| **turing** | Research & Grounding | Finding evidence, testing claims, checking for blind spots. |
| **caret** | Copy Editor & Voice | Drafting, revision, and narrative flow. |
| **mark** | Brand Guardian | Auditing for brand fit, tone, and cadence. |
| **devil** | Adversarial Auditor | Finding credibility gaps, unintended messages, reputation risk. |
| **echo** | Audience Evaluator | Simulating reader experience (executive, builder, skeptic). |
| **prism** | Visual Translator | Generating image prompts aligned with the piece. |
| **press** | Production Editor | Hugo frontmatter, SEO metadata, final proofing. |
| **mmw** | Workflow Orchestrator | Determining where a piece stands and suggesting next steps (optional). |

---

## How It Works

Each agent reads shared state files to understand what work has already been done. You don't wait for orchestration. You call whoever you need next.

- **Read state files**: `compass.state.md`, `turing.state.md`, `caret.state.md`, etc. Each file preserves that agent's context and decisions.
- **Call agents directly**: `@compass`, `@turing`, `@caret`. No wrapper required.
- **Iterate freely**: Run the same agent multiple times. Strategy → Research → Strategy (refined) → Draft. Whatever your process needs.
- **Use mmw to recover status**: If you're returning to a piece after time away, `@mmw` will read the folder, determine where you stand, and suggest the next step.

---

## Setup

1. Clone this repository.
2. Open the folder in VS Code.
3. Ensure GitHub Copilot extension is installed.
4. Edit your personalization files (takes 5 minutes):
   - `.github/agents/configurations/profile.md` — Your name, site, topic, origin story
   - `.github/agents/configurations/brand-style.md` — Your voice, tone, banned words
   - `.github/agents/configurations/READABILITY.md` — Your readability target
   - `.github/agents/configurations/visual-brand.md` — Your visual aesthetic

---

## First Steps

### Start with strategy
Open Copilot Chat and call your strategist:

```
@compass Here's my idea: I want to write about [topic]. The problem I'm solving is [problem]. The audience is [who].
```

Compass will return a strategic brief. It saves its thinking to `compass.state.md`.

### Then research
Call your researcher with the compass output:

```
@turing -compass What are the current patterns in [topic]? What am I missing?
```

Turing saves findings to `turing.state.md`. You can iterate: refine your strategy with compass again, then run turing with fresh research priorities.

### Then draft
When you're ready:

```
@caret -compass -turing Draft the opening and first section. Use the compass strategy and turing research.
```

Caret creates `{slug}.draft.md` and saves its work to `caret.state.md`.

### Then audit and refine
Run whichever auditors help most:

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

Press generates SEO metadata, Hugo frontmatter, and image prompts. Everything is production-ready.
