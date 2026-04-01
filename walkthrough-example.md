# End-to-End Writer's Workflow: Claude-Native Multi-Agents

This walkthrough demonstrates the "Mark My Words" system in action. We are drafting a technical post titled: **"The Challenges of Building Claude-Native Multi-Agent Solutions."**

---

## 1. Setting the North Star: `@mmw /compass`

**User**: "@mmw /compass here is my initial brief. I want to talk about how we orchestrate multiple Claude instances for complex coding tasks."

**Compass Response**:
*   **Thinking**: The writer is moving from simple prompting to complex orchestration. The "Editorial Angle" should be the shift from "Prompt Engineering" to "System Architecture."
*   **Piece Type**: **Type 1** (High Stakes). Architectural decisions are hard to reverse once the agent loop is established.
*   **Empty Chair Test**: The reader is a **CTO or AI Architect** looking for reliability, not just "magic."
*   **Strategic Snapshot**:
    - **Who**: Engineering Leaders.
    - **What**: Navigating the latency and token costs of multi-agent loops.
    - **Why**: To build production-grade AI systems, not just prototypes.

> [!NOTE]
> `00_compass.md` is updated with this snapshot.

---

## 2. Grounding in Reality: `@mmw /turing -compass`

**User**: "@mmw /turing -compass what are the prevailing patterns for agentic loops in Claude 3.5 Sonnet?"

**Turing Response**:
*   Performs multi-perspective search on "Computer Use," "Model Context Protocol (MCP)," and "Chain-of-Thought" overhead.
*   **Findings**: Identification of the "Agent-Handover" pattern vs. the "Orchestrator-Worker" pattern.
*   **Citations**: References to Anthropic's "Building Effective Agents" guide and various GitHub MCP implementations.

---

## 3. Creating the Narrative: `@mmw /caret -compass -turing`

**User**: "@mmw /caret -compass -turing draft the 'Hook' and 'Exploration' phases for our post."

**Caret Response**:
*   Embodies the author's voice (Reflective, Maker-metaphor).
*   **The Hook**: "Building an agentic loop feels like teaching a team of virtuosos to play in a room with a 5-second echo. The talent is there, but the coordination is where the music breaks."
*   **The Exploration**: Dives into the token-heavy reality of Claude's context window when agents start talking to each other.

---

## 4. Guarding the Brand: `@mmw /mark`

**User**: "@mmw /mark audit this draft for brand alignment."

**Mark Response**:
*   **Verdict**: **REVISE**.
*   **Brand Drift**:
    - **Banned Word**: "Furthermore" used in the second paragraph. *Recommendation: Use a short, punchy sentence instead.*
    - **Cadence**: Third paragraph exceeds the **4-sentence limit**.
*   **Human Voice Check**: "Could only this author (based on `profile.md`) have written it?" -> Yes, the maker-metaphors and specific focus on agent architecture align with the profile.

---

## 5. Persona Simulation: `@mmw /echo --lens executive`

**User**: "@mmw /echo --lens executive find the bounce points."

**Echo Response**:
*   **Persona**: Strategic Leader (Time-poor).
*   **Bounce Point**: "The technical deep-dive into MCP JSON schemas (Paragraph 4)."
*   **Friction**: "I'm looking for the business impact of latency, but I'm getting bogged down in syntax."
*   **Verdict**: **Bounced** at Paragraph 4.

---

## 6. Adversarial Audit: `@mmw /devil --damage`

**User**: "@mmw /devil --damage identify unintended messages."

**Devil Response**:
*   **Unintended Message**: "The draft implies that Claude-native is the *only* way, potentially alienating readers using vendor strategies (OpenAI/Gemini)."
*   **Challenge Question**: "Are you building a solution, or are you building a moat for a single provider? The reader will smell the vendor lock-in."

---

## 7. Visual Translation: `@mmw /prism`

**User**: "@mmw /prism generate the image prompt for this post."

**Prism Response**:
*   **Visual Snapshot**: "A minimalist, high-contrast photograph of several vintage analog clock gears interlocking, but with a subtle digital glow emanating from the central axle. Warm teak wood background. Calm Signal aesthetic."

> [!TIP]
> This prompt is stored in `00_prism.md` for the production editor.

---

## 8. Final Press: `@mmw /press --proof`

**User**: "@mmw /press --proof"

**Press Response**:
*   Generates `claude-native-multi-agent-challenges.md`.
*   Includes YAML frontmatter with tags: `#agenticarchecture`, `#claudeai`, `#engineeringleadership`.
*   Generates `claude-native-multi-agent-challenges-image-prompt.md` with the finalized visual assets.
*   The post is now **production-ready** for Hugo.
