---
name: echo-state-contract
description: Protocol for maintaining the "Stateless Snapshot" in echo.state.md and enforcing the Tiered Redline Policy.
---

# Echo State Contract

Use this skill to ensure all audit findings are recorded according to the "Mark My Words" architectural standards.

## 1. The Verdict Protocol
Every run must conclude with a clear verdict in `echo.state.md`:
- **CLEAR**: No blocking issues. Ready for next agent.
- **POLISH**: Minor issues (e.g., zero-tolerance words). Recommended fix but not blocking.
- **BLOCKED**: High friction, jargon-heavy, or momentum failure. Requires `caret` revision.

## 2. Tiered Redline Policy
Apply feedback across two layers:
- **In-Draft Redlines**: Only for **BLOCKING** issues and **Heavyweight Polish** (Zero-Tolerance words). 
  - Use format: `[comment]: # (Echo [VERDICT]: {Description} -> Move: {Action})`
- **State File Snapshots**: Overwrite `echo.state.md` with:
  - **The Verdict**
  - **The Active Reader Model** (Who was simulated)
  - **Detailed Friction Map** (Notes on structure, scent, and payoff)
  - **Downstream Handoff** (Status for `caret` or `mark/press`)

## 3. Statelessness
- **ALWAYS** overwrite `echo.state.md`. Do not append.
- Ensure the state file contains the "Current Truth" only.

## Rationale
Stateless snapshots ensure that downstream agents like `caret` don't get buried in historical logs and can focus on the immediate revision to-do list.
