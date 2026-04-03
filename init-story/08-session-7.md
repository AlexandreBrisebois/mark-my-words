## Session 7 — Prompt Architecture (add to the story)

After the agents were designed, a new problem emerged: the build prompt
was getting long. ~1,400 lines. One file doing two different jobs —
build-time instructions and runtime behavior — with no separation
between them.

The question asked: *should it be broken down into specs and an
orchestrating prompt, like in software development?*

The answer was yes. But the more important insight was the follow-on:
not just splitting build from runtime, but giving **each agent its own
spec file**. The same way a software project has one file per service,
not one file for the whole system.

### What was built

```
prompts/
├── mmw-build-prompt.md         ← thin orchestrator: reads specs, builds artifacts
└── specs/
    ├── flow.md                 ← canonical workflow, phases, protocols, file schema
    ├── agent-caret.md
    ├── agent-mark.md
    ├── agent-compass.md
    ├── agent-devil.md
    ├── agent-turing.md
    ├── agent-echo.md
    ├── agent-press.md
    ├── agent-prism.md
    ├── agent-index.md
    └── agent-cadence.md
```

### Why it matters (for the story)

The split revealed a structural insight: the original monolith had two
sources of truth fighting each other. The phase specs lived in the build
prompt, but the same logic needed to live in the generated agent files.
No single file was authoritative.

The new structure has a clear contract:
- `flow.md` owns the workflow. Phases, gates, protocols. Change it once,
  rebuild what depends on it.
- Each `agent-X.md` owns only that agent's behavior. Personality,
  responsibilities, inputs, outputs, rules.
- The build prompt owns nothing except the order of operations.

The analogy that surfaced: this is the same reason software projects
have service specs, interface contracts, and a deployment script — not
one enormous README that is also the code.

### The recursion worth noting

The first thing MMW will write is a post about building MMW. The prompt
architecture is now part of that story — not just the agent roster and
naming, but the decision to treat a prompt system with the same
structural discipline as a software project.

That decision was made in a conversation, not in advance. Same as
everything else in this system.

### Additional angle for Compass

- **The architecture angle**: What prompt engineering and software
  architecture have in common. The moment you recognize that a prompt
  is not just instructions but a system with its own coupling,
  separation of concerns, and single-responsibility principle — that's
  the moment the discipline changes.

---