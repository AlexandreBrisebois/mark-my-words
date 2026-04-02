# Strategy Template

Use this when generating a strategic snapshot before research or drafting.

## Execution Protocol

### Phase 1: Thinking
Use a `<thinking>` block to identify the core problem and the editorial angle. State what the piece is really about and what lens gives it the most value.

### Phase 2: Editorial Direction
- Define **Piece Type**: Type 1 (high stakes, hard to reverse) or Type 2 (reversible, decide fast).
- Run the **Empty Chair Test**: Would a busy CTO who didn't ask for this still find immediate value within 5 seconds? Answer directly.

### Phase 3: Research Roadmap
- **Focus Areas**: List 2-3 specific topics or questions research must answer.
- **Avoid**: Name the angles, framings, or tangents that would undermine the editorial angle.

### Phase 4: Strategic Context
- Define the `intention` field value for the draft's frontmatter. One sentence: what this piece must make the reader believe or do.

## Required Outputs
1. **Piece Type**: [Type 1 or Type 2] + one-line justification.
2. **Editorial Angle**: One clear sentence stating the specific lens.
3. **Empty Chair Test**: CTO verdict — passes or fails, and why.
4. **Research Roadmap**: Focus areas + explicit avoidances.
5. **Strategic Snapshot**: Who (audience), What (claim), Why (reason to care now).
6. **Intention**: The `intention` value for frontmatter.

## Guardrails
- Keep recommendations within the active draft directory scope.
- Do not request or reference files outside the active draft directory tree.
