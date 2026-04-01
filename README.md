# Mark My Words (mmw)

Mark My Words is a "Writers' Room" — a suite of specialized **GitHub Copilot Skills** designed to help you produce high-impact, long-form content while keeping your human voice at the center of the narrative.

Designed for the modern technical blog, this system turns your Copilot chat into a strategic partnership with a team of editorial experts who maintain **Persistent Context** across your writing sessions.

---

## Modular Specialists

The Writers' Room is organized into specialized roles. Use **Flags** to unlock specific workflows and **Teacher Mode** (`--teach`) to learn the craft as you write.

| Phase | Skill | Role | Key Flags |
| :--- | :--- | :--- | :--- |
| **Strategy** | `@mmw /compass` | Strategy Director | (Default) |
| **Research** | `@mmw /turing` | Research & Grounding | `--audit`, `--fact-check` |
| **Drafting** | `@mmw /caret` | Copy Editor & Voice | `--prfaq`, `--brief`, `--linkedIn`, `--teach` |
| **Auditing** | `@mmw /mark` | Brand Guardian | `--teach` |
| **Auditing** | `@mmw /devil` | Adversarial Auditor | `--damage`, `--lens [persona]`, `--teach` |
| **Auditing** | `@mmw /echo` | Reader Persona Sim | `--lens executive`, `--lens builder`, `--teach` |
| **Visuals** | `@mmw /prism` | Visual Brand | (Default) |
| **Production** | `@mmw /press` | Production Editor | `--audit`, `--portfolio`, `--proof`, `--teach` |

---

## The Writer's Workflow (End-to-End)

Mark My Words is designed for a collaborative, iterative workflow. You lead the narrative; the skills provide the guardrails.

### 1. Strategic Anchor — `@mmw /compass`
Before writing, define your editorial strategy. **Compass** identifies the "Editorial Angle" and the **"Empty Chair"** (your specific reader persona).
*   **Result**: A strategic snapshot that ensures your piece delivers value, not filler.

### 2. Grounded Research — `@mmw /turing`
Avoid the "hallucination trap." Use **Turing** to perform multi-perspective searches and surface reputable citations.
*   **Flags**: Use `--audit` to fact-check an existing draft against the web.
*   **Context**: Use `-compass` to align research with your strategic goals.

### 3. Narrative Drafting — `@mmw /caret`
Transform research into a high-impact story. **Caret** follows a strict **Story Arc**: Hook → Exploration → Insight → Deeper Dive → Reflection.
*   **Context**: Mention other skills (e.g., `-compass -turing`) to pull in their persistent context.

### 4. Brand & Persona Audits — `@mmw /mark`, `@mmw /echo`, `@mmw /devil`
Subject your draft to rigorous critique before it hits the web:
*   **Mark**: The Passive Brand Guardian. Flags "banned words" (like *furthermore* or *utilize*) and enforces the "Truth over Hype" principle.
*   **Echo**: Reader simulation. Use `--lens executive` or `--lens builder` to find "bounce points" where readers lose interest.
*   **Devil**: Adversarial auditing. Identifies unintended messages or reputation risks. Use `--damage` for a high-intensity audit.

### 5. Final Production — `@mmw /prism` & `@mmw /press`
The final polish for the technical web.
*   **Prism**: Translates your draft into a focused visual prompt for **Gemini Image Pro**.
*   **Press**: The Production Editor. Generates the final Hugo-ready `{slug}.md` file. It automatically integrates the visual snapshot from Prism.

---

## Try This: Workflow Combinations

Unlock the full power of the Writers' Room with these command patterns:

*   **Strategic Start**: `@mmw /compass` → `@mmw /turing -compass`
*   **Educational Draft**: `@mmw /caret --teach -compass -turing`
*   **Audience Stress-Test**: `@mmw /echo --lens executive` → `@mmw /devil --damage`
*   **The Final Mile**: `@mmw /prism` → `@mmw /press --proof`

---

## Core Philosophy

*   **Voice First**: AI is the assistant; the writer is the editor.
*   **Calm Signal**: Minimalist, editorial, and warm content over hype and clickbait.
*   **No Infrastructure**: No complex file hierarchies. Just you, your draft, and your skills.

---

## Cumulative Insights (The 00-Series)

Each skill maintains its own "memory" in a companion file (e.g., `00_compass.md`). This allows for **Persistent Context** across chat sessions.

1.  **State Loading**: Skills read their `00_` file at the start of every session.
2.  **Cross-Skill Context**: Include context from any skill by using its name with a `-` prefix (e.g., `-mark`, `-devil`).
3.  **Human Visibility**: You can always read these files to see the "why" behind the editorial guidance.

---

## Setup

1.  Open your project in VS Code with the GitHub Copilot extension.
2.  Ensure the skills are located in `skills/github-copilot/`.
3.  **Personalize Your Profile**: Edit `skills/github-copilot/profile.md` with your own name, website, and mission. MMW will automatically adopt this identity.
4.  (Optional) **Adjust Your Style**: Modify `skills/github-copilot/brand-style.md` if you want to override the default "Calm Signal" principles.
5.  Start a conversation in Copilot Chat by referencing the relevant skill (e.g., `@mmw /compass`).

> [!NOTE]
> Mark My Words is designed for long-form, "build-in-public" retrospectives and technical deep dives where expertise and vulnerability are the primary assets.
