# Assistant adapter and skill map

This is a prompt/documentation contract, not a runnable orchestration library. A host may read the files directly, or explicitly install supported skills using its own documented process. Tools, models, access and persistence come from the host; this repository creates none of them.

## Minimal invocation

Ask your assistant: "Read AGENTS.md and the editorial contract. Use my authorized private WORKING.md if accessible. Help with this draft's argument and preserve my chosen wording. Select only the expertise needed; do not publish."

For an existing article, provide its canonical path. For new work, use `{slug}.draft.md`. Keep project state in the private project, not this public framework.

## On-demand expertise

| Task | Roles | Read only when needed |
| --- | --- | --- |
| Editorial brief | compass | compass-coaching, compass-strategy |
| Positioning discovery | compass, echo | positioning-discovery |
| Claim research | turing | turing-discovery, turing-vetting, turing-synthesis |
| Draft and revision | caret | caret-voice, caret-drafting, caret-protocol |
| Voice and reader review | mark, echo | mark-core, mmw-human-voice-check, echo-friction-audit |
| Accusation audit | devil | devil-risk-audit, devil-adversarial-lenses |
| Visual direction | prism | prism-visual-strategist, prism-structural-audit |
| Publication packaging | press | press-packaging-audit, press-state-contract |
| Resume and route | mmw | mmw-core, mmw-routing, mmw-state-contract |

Skill files live in `.github/skills/<name>/SKILL.md`. All follow the current editorial contract. No task requires all nine roles or every skill in a role.

## Copilot compatibility

The nine existing `.github/agents/*.agent.md` files remain Copilot-oriented entry points with human-triggered handoffs. Their tool declarations are adapter requests, not evidence that tools are available. Use only supported tools. The model field is omitted so the host's selected model is inherited rather than pinning an obsolete model.

A general assistant can use the same role/skill definitions without supporting Copilot buttons or @mentions. Summarize the next useful action in ordinary language when those controls are absent. Do not claim native installation or automatic cross-session loading.

## Model and effort routing

Use the host's configured efficient general-purpose model by default. A deployment may map that tier to a Sol model where available; it may map an escalation tier to Astra or another stronger model. These are optional mappings, not required model IDs or availability claims.

Escalate only for a specific unresolved reasoning task, contradictory evidence, high-impact review or failed bounded attempt. Record the reason and limit the escalation to that task. Do not run a stronger model for every role by habit. If unavailable, continue with available capability and disclose relevant limitations.

## Future mechanical helpers (not built)

Potential helpers include canonical-path validation, draft hashes, stale-review detection, frontmatter/schema checks, local link validation, and secret/private-data scanning. They need implementation and tests before anyone calls them tools. No automated publication, quality scoring or performance improvement is provided by this PR.

## Design references

These sources informed the design, not measured claims about this framework:
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): task-specific cases and repeatable evaluation.
- [OpenAI skills](https://developers.openai.com/api/docs/guides/tools-skills): scoped reusable instructions and supporting resources.
- [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): focused context and retrieval when needed.
