# Mark My Words (mmw)

An open-source editorial framework for an author and an assistant working together. Keep the author's voice, choose the expertise the piece needs, and keep personal configuration private.

## Start here

1. Ask your assistant to read [AGENTS.md](AGENTS.md) and [the editorial contract](docs/editorial-contract.md).
2. Provide your task and canonical draft path, if one exists.
3. If authorized and accessible, point it privately to CONFIG_REPO/WORKING.md. [Configuration loading](docs/configuration.md) explains the boundary; nothing is automatically installed or loaded.
4. Select a useful outcome: a brief, claim check, targeted revision, accusation audit, visual direction, or publication package.
5. Review the result. Packaging is not permission to publish.

New drafts use `{slug}.draft.md`; existing publication files stay canonical without forced renaming. Reviews reference the exact draft revision so old clearance cannot silently survive an edit.

## The editorial team

| Role | Expertise |
| --- | --- |
| compass | Audience, angle, stakes and scope |
| turing | Evidence, uncertainty and research |
| caret | Drafting and author-led revision |
| mark | Voice and editorial consistency |
| echo | Reader clarity and payoff |
| devil | Accusations, credibility and risk |
| prism | Visual meaning and structure |
| press | Metadata and publication packaging |
| mmw | Context recovery and next-step routing |

These are on-demand lenses, not nine mandatory calls. One assistant can use several. [The adapter and skill map](docs/assistant-adapter.md) covers general assistants and the existing Copilot entry points in `.github/agents/`.

## Private by design

The five files in [configurations/](configurations/) are generic templates. Personalized profiles, voice samples, unpublished work and real project state belong in a private repository/workspace. Do not paste private configurations or conversations into public PRs.

See [adoption](ADOPT.md), [project template](templates/project.state.md), [review template](templates/review.state.md), and [evaluation cases](docs/evaluation.md).

## Status and history

This is a documentation/prompt framework, not an installed plugin, executable workflow, benchmarked quality system or automated publisher. Historical `specs/`, `init-story/`, `AGENT_REVIEW_PROMPT.md` and `walkthrough-example.md` remain available as design history, not current runtime instructions. Existing historical public content is not removed or made private by this update.
