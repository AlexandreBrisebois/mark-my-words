# Mark My Words (mmw)

Mark My Words is a "Writers' Room" editorial suite designed to help you produce high-impact, long-form content while keeping your human voice at the center of the narrative.

The project offers two distinct ways to interact with your editorial team. **Choose the model that best fits your workflow.**

---

## Choose Your Interaction Model

You can deploy Mark My Words as either a **Guided Agent Suite** or a **Modular Toolkit**.

> [!IMPORTANT]
> **Total Isolation:** These two options are completely independent entities. Changes to one (e.g., personalizing your profile) do not impact the other. We recommend selecting **one** model and deleting the other to maintain a clean environment.

### Option A: Custom Agent Suite (Recommended)
**Best for: Guided deep work and persona-driven editorial sessions.**
- **Location**: `copilot/agents/`
- **Summon**: Use standalone names like `@turing`, `@caret`, or the orchestrator `@mmw`.
- **Experience**: The "Writing Room Director" (`@mmw`) manages the session flow, providing specialist handoffs and strategic guidance.

### Option B: Modular Skills & Slash Commands
**Best for: High-speed, manual command-style edits.**
- **Location**: `copilot/skills/`
- **Summon**: Use slash commands under the master skill, e.g., `@mmw /turing`, `@mmw /caret`.
- **Experience**: A versatile toolkit where you manually invoke specific specialists for targeted tasks.

---

## Comparison Matrix

| Feature | Option A: Custom Agents | Option B: Modular Skills |
| :--- | :--- | :--- |
| **Summon** | Standalone (@caret) | Slash Command (@mmw /caret) |
| **Philosophy** | Writing Room (Persona-led) | Toolkit (Manual-led) |
| **Isolation** | High (Self-contained) | High (Self-contained) |
| **Token Usage** | Ultra-lean (Isolated Prompting) | Moderate (Shared Skill Buffer) |
| **Discovery** | High (Appears in `@` list) | Moderate (Slash command autocomplete) |

---

## The Specialist Roster

Regardless of the model you choose, your "Writing Room" consists of these specialized roles:

| Phase | Specialist | Role | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **Strategy** | `compass` | Strategy Director | Sets editorial angle & "Empty Chair" persona. |
| **Research** | `turing` | Research & Grounding | Multi-perspective search & fact-checking. |
| **Drafting** | `caret` | Copy Editor & Voice | Narrative flow, high-impact drafting, hooks. |
| **Auditing** | `mark` | Brand Guardian | Passive audit for tone, cadence, and banned words. |
| **Auditing** | `devil` | Adversarial Auditor | Identifies credibility gaps & reputation risk. |
| **Auditing** | `echo` | Audience Evaluator | Reader simulation (Executive vs. Builder). |
| **Visuals** | `prism` | Visual Translator | Generates Gemini Image Pro visual prompts. |
| **Production** | `press` | Production Editor | Hugo frontmatter, SEO, and final proofing. |

---

## Core Philosophy

*   **Voice First**: AI is the assistant; the writer is the editor.
*   **Calm Signal**: Minimalist, editorial, and warm content over hype and clickbait.
*   **Persistent Context**: Each specialist maintains its own "memory" in a companion file (e.g., `00_compass.md`), allowing for state preservation across sessions.

---

## Setup & Selection

1.  **Choose Your Model**: Navigate to `copilot/agents/` (Option A) or `copilot/skills/` (Option B).
2.  **Personalize Your Identity**:
    -   If using **Agents**: Edit `copilot/agents/profile.md` and `copilot/agents/brand-style.md`.
    -   If using **Skills**: Edit `copilot/skills/profile.md` and `copilot/skills/brand-style.md`.
3.  **Clean Your Workspace**: Delete the directory (agents or skills) that you do not intend to use.
4.  **Start Writing**: Open Copilot Chat and summon your chosen entity (e.g., `@mmw` for Agents or `@mmw /compass` for Skills).

> [!NOTE]
> Mark My Words is designed for long-form, "build-in-public" retrospectives and technical deep dives where expertise and vulnerability are the primary assets.
