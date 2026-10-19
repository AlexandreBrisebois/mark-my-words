# Choose the smallest useful role

Infer intent from the whole request, not a keyword. "Use Mark My Words" is optional. These are five instruction sets, not five required agents.

| Request | Load |
| --- | --- |
| Shape an idea, draft, revise, or resume a project | [Editor](../skills/editor/SKILL.md) |
| Check a claim or find missing evidence | [Researcher](../skills/researcher/SKILL.md) |
| Review clarity, reader payoff, voice, or brand fit | [Reader & Brand Reviewer](../skills/reader-brand/SKILL.md) |
| Accusation audit, strongest objection, or publication premortem | [Challenger](../skills/challenger/SKILL.md) |
| Metadata, SEO, publication package, or visual direction | [Producer](../skills/producer/SKILL.md) |

Start with one role and only its relevant subchecks. For a mixed request, name bounded outputs and sequence dependencies: claim check then paragraph revision means Researcher then Editor, not the full panel. If material ambiguity remains, ask one question; otherwise use a reversible assumption.

Minimum context:
- Small revision: passage, enough surrounding text, protected choices. No automatic research or review panel.
- Claim check: exact claim, context and available sources. No author profile by default.
- Accusation audit: current draft/revision, audience and purpose. No SEO, visuals or voice history.
- Voice review: current text and relevant authorized style/examples. No packaging.
- Metadata without images: current body/revision and actual destination schema. No visual configuration or image work.

Use [private configuration](configuration.md) only as needed. Stop at the requested result, a meaningful blocker, or the agreed budget. Skipped checks are not endorsements.
