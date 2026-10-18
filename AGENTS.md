# Mark My Words: assistant entry

Read [the editorial contract](docs/editorial-contract.md) before editorial work. It is the current runtime contract; older conflicting workflow rules are superseded as described there.

Start from the user's current task, not a nine-agent pipeline. Select only useful expertise from [the skill map](docs/assistant-adapter.md). One assistant can perform several roles; names are lenses, not a requirement to spawn agents.

Load only the authorized private profile and relevant project context that are actually accessible. Public `configurations/` files are sanitized templates, not an author's identity. Do not assume repository instructions are installed into the host assistant or that a private repository can be read.

Keep private configuration, drafts, review findings, and conversation-derived examples out of this public repository and its issues/PRs. Follow the host's permission and safety rules. Never publish, merge, deploy, or send externally just because an editorial review says ready.
