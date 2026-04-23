---
name: press-packaging-audit
description: Technical heuristics and audit logic for evaluating discoverability, SEO, and AI retrieval readiness.
---

# Press Packaging Audit Skill

Use this skill to perform a technical evaluation of article packaging (Title, Description, Slug, Tags) against MMW standards.

## Audit Workflow
1. **Context Check**: Read `brief.md` and upstream states (`turing`, `compass`, `mark`).
2. **Draft Fidelity**: Compare proposed packaging against the actual content of `{slug}.draft.md`.
3. **Drift Detection**: Identify "Strategic Drift" (e.g., the title is more sensational than the draft, or the tags don't match the entities).
4. **Voice Audit**: Call `mmw-human-voice-check` to ensure metadata is free from generic AI patterns ("In today's digital landscape...", "Comprehensive guide").

## Technical Heuristics
- **Title**: Must be unique, descriptive, and concisely signal the main value. 
- **Description**: Must summarize the specific takeaway, not just restate the title.
- **Slug**: Must be lowercase-hyphenated and align with `mmw-codename-gen`.
- **Headings**: Verify a single `<h1>` and a logical hierarchy (`<h2>`, `<h3>`).
- **Entities**: Ensure key people, products, and concepts are explicitly named in metadata.

## Audit Severity Labels
- **Critical**: Blocking publication (e.g., technical error, broken slug, misleading claim).
- **High**: Significant impact on discovery or trust.
- **Medium**: Optimization opportunity.
- **Low**: Minor stylistic refinement.

## Constraints
- **Offline Only**: Do not use web tools. Rely on internal lenses and repo configurations.
- **No Overlap**: Do not edit the body content of the draft. Identify issues for `caret` or propose metadata alternatives.
