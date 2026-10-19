# Mark My Words (mmw)

An open-source editorial framework for an author and an assistant working together. Keep the author's voice, choose the expertise the piece needs, and keep personal configuration private.

## Start here

1. Ask naturally for editorial help. [AGENTS.md](AGENTS.md) starts with [a compact routing index](docs/routing.md); “Use Mark My Words” is optional.
2. Provide your task and canonical draft path, if one exists.
3. If authorized and accessible, point it privately to CONFIG_REPO/WORKING.md. [Configuration loading](docs/configuration.md) explains the boundary; nothing is automatically installed or loaded.
4. Select a useful outcome: a brief, claim check, targeted revision, accusation audit, visual direction, or publication package.
5. Review the result. Packaging is not permission to publish.

New drafts use `{slug}.draft.md`; existing publication files stay canonical without forced renaming. Reviews reference the exact draft revision so old clearance cannot silently survive an edit.

## Five working roles

| Role | What it helps with | Existing compatibility names |
| --- | --- | --- |
| Editor | Ideas, drafts, revision and next steps | mmw, compass, caret |
| Researcher | Claims, evidence and uncertainty | turing |
| Reader & Brand Reviewer | Clarity, payoff and author voice | echo, mark |
| Challenger | Accusations, objections and credibility | devil |
| Producer | Metadata, publication packages and visuals | press, prism |

Ask “Tighten this paragraph,” “Give this an accusation audit,” or “Prepare Hugo frontmatter.” The assistant selects the necessary skill, not all skills in a role. Mixed requests can use a bounded combination; ordinary conversation needs no editorial workflow.

[Routing recipes](docs/routing.md) show what to load and skip. The [skill catalog](docs/skill-catalog.md) is a lookup, not mandatory reading. [Adapter guidance](docs/assistant-adapter.md) explains prompt-guided retrieval and the unchanged nine Copilot entry points.

## Private by design

The five files in [configurations/](configurations/) are generic templates. Personalized profiles, voice samples, unpublished work and real project state belong in a private repository/workspace. Do not paste private configurations or conversations into public PRs.

See [adoption](ADOPT.md), [project template](templates/project.state.md), [review template](templates/review.state.md), and [evaluation cases](docs/evaluation.md).

## Status and history

This is a documentation/prompt framework, not an installed plugin, executable workflow, benchmarked quality system or automated publisher. Historical `specs/`, `init-story/`, `AGENT_REVIEW_PROMPT.md` and `walkthrough-example.md` remain available as design history, not current runtime instructions. Existing historical public content is not removed or made private by this update.
