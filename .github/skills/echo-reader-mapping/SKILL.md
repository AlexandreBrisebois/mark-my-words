---
name: echo-reader-mapping
description: Logic for mapping global audience models to specific draft knowledge gaps. Use to simulate "Persona-Based Audits."
---

# Echo Reader Mapping

Use this skill to simulate real-world readers and identify "Curse of Knowledge" friction points.

## Methodology

### 1. Persona Extraction
Read `configurations/profile.md` to identify the core audiences (e.g., LoB Leaders, CTOs, Senior Engineers).

### 2. Knowledge Proximity Check
For the chosen persona, evaluate:
- **Assumed Context**: What does this reader *not* know that the draft assumes?
- **Goal Alignment**: Does this draft help them achieve their specific ROI or technical goal?
- **Skeptic Audit**: If this reader is a skeptic, where would they "mistrust" the claim?

### 3. The "So What?" Filter
Simulate the reader asking "So what?" after every section. If the answer isn't in the text, it's a **Blocking** clarity issue.

## Personas (Standard)
- **LoB Leader**: Focuses on ROI, organizational friction, and "Why now?"
- **CTO Suite**: Focuses on risk, scalability, and technical debt.
- **Senior Engineer**: Focuses on implementation trade-offs and "How it works."

## Rationale
Auditing for "everyone" is auditing for "no one." Mapping to a specific reader allows for sharper, more actionable revision moves.
