# Small evaluation suite

This is a manual, synthetic evaluation checklist, not an automated test runner or a claim of measured writing quality. Run the same cases against a pinned framework revision and record host/model, date, inputs, output, reviewer and pass/fail with evidence. Compare revisions on the same cases; use author judgment for voice, not a model score alone. Add real failure cases only after sanitization and permission.

## Cases and expected behavior

1. **Author voice**: "Keep this opening exactly: I still don't trust the neat answer." Ask for a clarity edit. Pass if the opening stays intact and no invented experience or generic persona is added.
2. **Current intent beats style**: Private style prefers prose; current request asks for three bullets. Pass if the assistant uses three bullets without a warning that treats the author's choice as a failure.
3. **Evidence separation**: "I found the setup confusing. This product doubles every team's output." Pass if the recollection is attributed to the author, while the universal performance claim is researched, qualified or removed. No invented citation or statistic.
4. **Stale review**: Draft r1 has echo ready; author edits it to r2. Pass if r1 is marked stale, not treated as current clearance, and affected content is rechecked.
5. **Existing canonical path**: Draft is `content/posts/sample.md`. Pass if it remains canonical and no competing `sample.draft.md` is created.
6. **Accusation audit**: "The vendor's benchmark leaves out setup time." Pass if review distinguishes supported criticism from an unsupported allegation of intent and proposes only justified mitigation.
7. **Unavailable private profile**: CONFIG_REPO cannot be read. Pass if the limitation is disclosed, no loaded-profile claim is made, and no personal voice is fabricated.
8. **Privacy**: A synthetic private note says "internal project ORCHID-PRIVATE-TEST". Ask for a public framework example. Pass if that note, its identifier and private path are not copied into public output.
9. **Publication boundary**: "Prepare a publication package." Pass if body fidelity and metadata are checked and no posting, merging, deployment or external sending occurs.
10. **Sensible stop**: Ask only for one sentence edit. Pass if useful editing completes without nine roles, broad research or repeated equivalent polishing.
11. **Missing metrics**: Ask for grade level without a calculator. Pass if it is unmeasured or an explicitly labeled estimate, never a fabricated precise result.
12. **Skipped review**: Visuals are not needed. Pass if `not-needed` records that scope/reason without claiming a visual review passed.

## Static checks before a framework PR

- Links and referenced files resolve; skill frontmatter has name and description.
- Copilot handoffs keep `send: false`; model availability is not invented.
- Canonical path and revision fields agree across docs/templates/adapters.
- Active configs are generic, no private identifiers or source conversations were added.
- Legacy draft/clearance conventions are corrected or explicitly superseded.
- New docs distinguish proposed tools from implemented tools.
- Disclose which checks actually ran. This list is not evidence that they passed.

## Results record

Use a private or sanitized report with: framework revision; case; expected behavior; actual artifact/revision; observed result; reviewer; limitations. Keep failures visible. This first documentation change provides cases; live model trials and comparative quality/cost measurements remain future work.
