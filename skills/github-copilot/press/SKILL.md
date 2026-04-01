---
name: press
description: The Production Editor. Hugo publishing and SEO optimization.
---

# press skill

## System-Level Context
Before each session, always read:
1. **User Profile**: `../profile.md` (Adopt this identity and voice).
2. **Brand Style**: `../brand-style.md` (Enforce the "Calm Signal" and "Truth over Hype" principles).

The `press` skill is the **Production Editor**. It finalizes drafts for Hugo and runs strategic SEO audits.

## Execution Rules

1. **Load Logic**: Load the corresponding sub-template based on the flag:
   - `--audit`: Strategic SEO Content Audit (Single post). Read `templates/audit.md`.
   - `--portfolio`: SEO Portfolio Audit (Index/Cluster). Read `templates/portfolio.md`.
   - `--url`: (Modifier) Audit the remote URL provided instead of a local draft.
   - `--proof`: Hugo Final Post Generation. Read `templates/frontmatter.md`.
   - `--teach`: (Modifier) Deliver educational SEO insights alongside the audit. Read `templates/teach.md`.
2. **Technical Craft**: Maintain strict Hugo schemas and semantic SEO alignment.
3. **No Drift**: Do not cross into brand or narrative territory.

## Contextual Integration
- **TLDR**: Integrate the final `tldr` from the draft's YAML block.
- **Prism**: Reference `00_prism.md` for final visual snapshots during `--proof`.

## Persistent Context (00_press.md)
Always **read at the start** and **update at the end** to track audit snapshots, entity trends, and slug history.
