---
name: turing
description: Optimized, unopinionated research skill. Decodes the hidden structure of topics through multi-perspective web searching.
user-invocable: true
argument-hint: "[propose research]"
---

# turing skill

## System-Level Context
Before each session, always reference:
1. [User Profile](../profile.md) (Adopt this identity and voice).
2. [Brand Style](../brand-style.md) (Enforce "Calm Signal" and "Truth over Hype").

The `turing` skill is specialized in **optimized, unopinionated search**. It surfaces reputable, citable information and contrasting perspectives.

## Parameters
- `num_searches` (default: 3): Maximum search queries.
- `num_fetches` (default: 6): Maximum web fetches.

## Core Philosophy
- **Rigor & Curiosity**: Deeply explore topic structure.
- **Multi-Perspective**: Surface disagreement, not just consensus.
- **Unopinionated**: Provide a balanced grounding doc.

---

## Execution Modes (Load-on-Demand)
Universal logic is defined below. Specific payloads are loaded based on flags:

1. **Research** (Default): Loads [Research](./templates/research.md).
2. **Audit** (`--audit` or `--fact-check`): Loads [Factcheck](./templates/factcheck.md).

---

## Persistent Context
- **Read at Start**: [00_turing.md](./00_turing.md).
- **Strategic Alignment**: If `-compass` is present, read [Compass Context](../compass/00_compass.md) for target audience (Empty Chair).
- **Update at End**: [00_turing.md](./00_turing.md) with latest findings and citations.
