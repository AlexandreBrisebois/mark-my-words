---
name: press-state-contract
description: Manages the stateless snapshot of press.state.md and the final publication assembly.
---

# Press State Contract Skill

Use this skill to ensure consistent state handling and artifact generation for the Press agent.

## State Contract (press.state.md)
- **Rule**: Overwrite on every run. No historical logs.
- **Purpose**: Authoritative "Latest Truth" of the packaging status.

### Snapshot Schema:
```markdown
# Press Snapshot: {timestamp}

## Status
- **Upstream Clearance**: [PASS/FAIL] (Requires signals from devil.state.md and echo.state.md)
- **Draft Alignment**: [PASS/FAIL]
- **Discoverability Score**: [Critical/High/Medium/Low]

## Proposed Package (Auditor's Choice)
- **Title**: 
- **Slug**: 
- **Description**: 
- **Tags**: 
- **TLDR**: 

## Strategic Drift & Risks
- [List any conflicts with upstream agents or user intent]

## Handoff
- **Next Step**: [e.g., User Review / Final Assembly]
```

## Assembly Protocol ({slug}.md)
When instructed to produce the finalized publication file:
1. **Schema Validation**: Ensure all fields match the `configurations/packaging-guidelines.md`.
2. **Frontmatter Assembly**:
   - `title`: Auditor's finalized choice.
   - `slug`: Auditor's finalized choice.
   - `image_prompt`: Pulled from `prism.state.md`.
   - `draft`: Set to `true` by default.
3. **Content Merging**: Prepend the frontmatter to the full content of `{slug}.draft.md`.
4. **File Write**: Save as `{slug}.md`.

## Mandatory Dependencies
- `devil.state.md`: Check for "Risk Clearance: Pass".
- `echo.state.md`: Check for "Clarity Clearance: Pass".
- `mmw-codename-gen`: Slug must match the generated codename exactly.
