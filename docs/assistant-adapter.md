# Assistant adapter and skill map

This is a prompt/documentation contract, not a runnable orchestration library. A host may read the files directly, or explicitly install supported skills using its own documented process. Tools, models, access and persistence come from the host; this repository creates none of them.

## Natural invocation and just-in-time context

Use [AGENTS.md](../AGENTS.md) and [the compact routing index](routing.md). A request such as “Give this an accusation audit” is enough once the framework is available to the assistant. “Use Mark My Words” is an optional explicit cue, not a magic command or installation step.

The five working roles are Editor (mmw, compass, caret), Researcher (turing), Reader & Brand Reviewer (echo, mark), Challenger (devil), and Producer (press, prism). They organize expertise; they are not five required agent processes.

Read the editorial contract once per verified framework revision in the active context, then fetch only the chosen skill and necessary private/source context. Reread when the framework revision changes or the contract is no longer available. Consult only selected entries of [the skill catalog](skill-catalog.md); its shared rules plus each row define use-when, inputs, outputs, scope and stopping conditions.

For an accusation audit, start with the current draft, audience/purpose and devil-risk-audit, not SEO, visuals or every reviewer. For Hugo packaging without images, load packaging guidance and Press skills only as needed, not Prism. More [loading recipes](routing.md) cover revision, voice and fact checks.

A connector-backed assistant performs these reads explicitly. There is no automatic dispatcher, host skill installation or private-repository access. Loading fewer files does not unload previously read context. A separate focused reviewer can provide useful independence when supported and warranted; give it only the current artifact, scope and minimum authorized context, not the full drafting conversation by default.

For an existing article, keep its canonical path. Store real project state privately. Mixed intent gets bounded outputs and only their necessary skills; no nine-role pipeline.

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
