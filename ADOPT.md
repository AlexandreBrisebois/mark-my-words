# Adopting Mark My Words

## General assistant

Read [AGENTS.md](AGENTS.md), then [the editorial contract](docs/editorial-contract.md). Provide the actual task and draft. The assistant should load only the skills needed, say what context it could access, and preserve your chosen edits.

## Keep configuration private

Maintain `WORKING.md` and the five configuration files at the paths your private entry point designates in your own authorized private workspace. Use the public [configuration templates](configurations/) as blank starting points, not as a real person's voice. Follow [configuration loading](docs/configuration.md). No credentials or private repository mapping belongs in this public repository.

## Existing Copilot workflow

Open a checkout with your supported Copilot setup. The nine agent definitions remain in `.github/agents/`; the host must actually support and discover them. Select your host model. Invoke a role such as `@compass`, `@caret` or `@devil` where supported. Handoff buttons remain human-triggered. The current contract replaces obsolete mandatory stages and stale label-based gates.

Do not move private files into a public checkout merely to satisfy legacy paths. Resolve them explicitly from the private entry point. If the host cannot read them, provide the minimum authorized context or use clearly labeled generic defaults.

## First piece

"Review this draft for reader clarity. Keep the opening I chose. Research only factual claims that need verification. Return a scoped review tied to this revision; do not publish."

For a new piece, choose `{slug}.draft.md`. For an existing article, keep its actual path canonical. Store a private project snapshot and selected review artifacts using [these templates](templates/). A file's existence is not proof of completed work. If persistence is unavailable, retain explicit revision labels in the conversation and say what was not saved.

## Check the setup

Use the synthetic cases in [evaluation](docs/evaluation.md). Confirm private data stays private, an edit invalidates old reviews, and a packaging request does not trigger publication. Record observed results without claiming unmeasured quality or cost improvements.
