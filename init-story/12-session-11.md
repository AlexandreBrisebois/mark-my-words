## Session 11 — Inlining the Migration (add to the story)

The build prompt had one step that wasn't like the others. Every other
instruction pointed inward — read a spec, build an artifact, write to
the repo. One step pointed outward: read seven GitHub Copilot prompt
files from a path on the author's machine and migrate their logic into
the agent specs.

That dependency was a problem waiting to surface. A different machine,
a moved file, a renamed directory — any of these would silently break
the build. The spec would run fine until the moment it needed those
files, and then stop with no clear guidance.

The fix was straightforward. The migration was a one-time operation.
The logic from those seven files now lives in the specs directly.

### What was done

Seven source files, each migrated to its target agent spec:

| Source | Target | What was added |
|---|---|---|
| `brand-voice.instructions.md` | Mark | Voice characteristics table, emotional registers, cadence rules, identity guardrails, "What NOT to Do", Human Voice Check |
| `brand-strategy.prompt.md` | Compass | Outcome Narrative Guardrail — full framing language |
| `content-writer.prompt.md` | Caret | Story arc detail, core writing rules, cross-domain metaphor framework, channel templates, bad→good narrative example |
| `accusation-audit.prompt.md` | Devil | Accusation audit definition, when-to-run guidance, audit format instruction |
| `seo-audit.prompt.md` | Press | Full Phase 1–5 SEO audit methodology: technical, E-E-A-T, semantic intent, multi-persona, synthesis + constraints |
| `seo-blog-audit.prompt.md` | Index | Full Phase 1–7 portfolio audit detail: inventory, cannibalization, topical gaps, internal linking, freshness, three-lens synthesis, three-horizon action plan + constraints |
| `visual-brand-validator-dual-mode.prompt.md` | Prism | Full Quick Audit and Strategic Audit output structures, input format, response requirements, audience framing |

---