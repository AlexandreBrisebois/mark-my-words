# Mark My Words (mmw)

Mark My Words is a "Writers' Room" — a suite of specialized **GitHub Copilot Skills** designed to help you produce high-impact, long-form content while keeping your human voice at the center of the narrative.

Built for [srvrlss.dev](https://srvrlss.dev), this system turns your Copilot chat into a strategic partnership with a team of editorial experts who maintain **Persistent Context** across your writing sessions.

---

## The Writer's Journey

You call each skill individually to iterate on your draft.

### 1. Setting the North Star — `@mmw /compass`
Before you write a word, use the **Compass** skill to define your editorial strategy.
*   **What it does**: Identifies the "Editorial Angle" and the "Empty Chair" (the specific reader persona).
*   **Persistent Insight**: Creates `00_compass.md` to anchor all future research and drafting decisions.
*   **Context Sharing**: Use `-compass` as a flag in other skills (e.g., `@turing -compass`) to include this strategy.
*   **Result**: A strategic snapshot that ensures your piece isn't just "filler" content.

### 2. Grounding in Reality — `@mmw /turing`
Avoid the "hallucination trap" by grounding your work in real research.
*   **What it does**: Performs deep, multi-perspective searches and surfaces reputable citations.
*   **Persistent Insight**: Maintains `00_turing.md` to track research findings and citable evidence across runs.
*   **Result**: A grounding document (or inline notes) that provides the factual floor for your draft.

### 3. Drafting with the Narrative Arc — `@mmw /caret`
When it's time to put words on the page, the **Caret** skill follows a strict "Story Arc."
*   **What it does**: Builds the narrative: **Hook → Exploration → Insight → Deeper Dive → Reflection**.
*   **Persistent Insight**: Updates `00_caret.md` to track narrative progress and tone adjustments.
*   **Result**: A draft built on "Calm Signal" aesthetics—minimalist, editorial, and warm.

### 4. Guarding the Brand — `@mmw /mark`
Ensure every piece sounds like a human wrote it, not an AI.
*   **What it does**: Flags "banned words," generates **TLDRs**, and scores the draft against the "Truth over Hype" principle.
*   **Persistent Insight**: Logs brand scores and banned word hits in `00_mark.md` to ensure voice consistency.
*   **Result**: PASS/REVISE verdicts, 3 Headline/Hook alternatives, and a brand-aligned TLDR.

### 5. The Adversarial Audit — `@mmw /devil` & `@mmw /echo`
Before you publish, subject your draft to rigorous critique.
*   **Devil**: Acts as an "Accusation Auditor," identifying unintended reads or "humblebragging."
*   **Echo**: Simulates reader personas (**The Executive**, **The Builder**) to find "bounce points."
*   **Persistent Insight**: Both skills maintain history (`00_devil.md`, `00_echo.md`) to track recurring friction.

### 6. Technical Polish — `@mmw /press` & `@mmw /prism`
The final steps to get your piece ready for the web.
*   **Press**: Generates Hugo YAML front matter (using `mark`'s TLDR) and runs a multi-persona SEO audit. Use the `--proof` flag to automate the creation of your final `{slug}.md` publication file.
*   **Prism**: Translates your draft into a focused image prompt for **Gemini Image Pro**. The final prompt is persisted for use by the `press --proof` command.
*   **Persistent Insight**: Maintains `00_press.md` and `00_prism.md` to track technical and visual versions.
*   **Result**: A well-formed Hugo post (`{slug}.md`) and a dedicated image prompt file (`{slug}-image-prompt.md`).

---

## Core Philosophy

*   **Voice First**: AI is the assistant; the writer is the editor.
*   **Calm Signal**: We prioritize minimalist, editorial, and warm content over hype and clickbait.
*   **Persistent Insights**: Every skill learns from your draft, building a cumulative record of strategic and editorial decisions.
*   **No Infrastructure**: No complex file hierarchies or CLI agents. Just you, your draft, and your skills.

---

## Cumulative Insights (The 00-Series)

Each skill automatically creates and maintains a companion file in your current directory (e.g., `00_compass.md`). These files serve as the "memory" of your editorial room:

1.  **State Loading**: When you call a skill, it first reads its `00_` file to understand previous context.
2.  **State Saving**: At the end of every interaction, the skill updates its state, ensuring continuity across chat sessions.
3.  **Cross-Skill Context**: You can include context from other skills by mentioning their names with a `-` prefix. 
    *   **Example**: `@caret -compass -mark` will read your editorial strategy and brand guidelines before drafting.
    *   **Available to Caret**: `-compass`, `-devil`, `-echo`, `-mark`, `-turing`.
    *   **Available to Turing**: `-compass`.
4.  **Human Visibility**: You can read these files to see the "why" behind the editorial guidance.

---

## Setup

1.  Open your project in VS Code with the GitHub Copilot extension.
2.  Ensure the skills are located in `skills/github-copilot/`.
3.  Start a conversation in Copilot Chat by referencing the relevant skill (e.g., `@mmw /compass`).

> [!NOTE]
> Mark My Words is designed for long-form, "build-in-public" retrospectives and technical deep dives where expertise and vulnerability are the primary assets.
