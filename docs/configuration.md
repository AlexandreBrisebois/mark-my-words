# Private configuration loading

The public `configurations/` directory contains generic templates only. Keep personalized copies in an authorized private repository/workspace, not in a public fork.

## Minimal private layout

- `WORKING.md`: private entry point with the author-approved context map, precedence and project paths.
- `configurations/profile.md` (or the path designated by WORKING.md): identity, existing mission, audience and positioning boundaries.
- `configurations/brand-style.md`: voice choices and authorized examples.
- `configurations/READABILITY.md`: readability preferences, not invented measurements.
- `configurations/visual-brand.md`: visual direction when needed.
- `configurations/packaging-guidelines.md`: actual destination schema and approval boundaries.

No additional profile manifest is required. CONFIG_REPO is a placeholder chosen privately by the user, not a repository to guess or create automatically. Keep any real mapping out of public files.

## Loading contract

1. Read the current user request and public `AGENTS.md`.
2. If the user has designated CONFIG_REPO and access is available, read `CONFIG_REPO/WORKING.md` and only the relevant files it identifies. Verify the paths and revisions from the actual source. Load profile/style for voice work; add readability, visuals or packaging only as needed.
3. An adapter resolves legacy `configurations/<file>` references to the corresponding authorized private file identified by WORKING.md. This is a documented resolution convention, not an implemented loader. If the host cannot resolve it, the assistant must read the explicit files or ask for the minimum context.
4. If private context is unavailable, say so and use current user-provided context or generic defaults, labeled as such. Never impersonate an unknown author or claim configuration was loaded.
5. Record applied configuration references privately with the project. Preserve existing mission/About content unless explicitly asked to revise it.

## Data boundary

Public: generic procedures, skill definitions, schemas, synthetic fixtures.
Private: personalized files, real project drafts, reviews, author choices, context maps, conversation extracts, access details.
Publication: only the specific content and destination the author has approved.

A private repository does not automatically become available in another assistant session. Cloning, reading these docs, or opening a PR does not install a skill, create credentials, or authorize cross-repository access. Do not copy a private profile into the public checkout to make old paths work. Ignore rules are a convenience, not a security guarantee: inspect every diff before pushing.
