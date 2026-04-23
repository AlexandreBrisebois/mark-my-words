---
name: devil-state-contract
description: Protocol for maintaining the Stateless Snapshot of the Devil agent and generating Turing Research Requests.
---

# Devil State Contract Skill

This skill governs how Devil records findings and communicates gaps.

## 1. The Verdict Protocol (devil.state.md)
Every run must conclude with a clear verdict in `devil.state.md`. Always **OVERWRITE** the file with:
- **CLEAR**: No high-severity risks. Ready for publication.
- **POLISH**: Moderate risks identified. Mitigation recommended but not blocking.
- **BLOCKED**: High-severity reputational, technical, or logical risk. Requires `caret` revision or `turing` research.

## 2. Tiered Redline Policy
Apply feedback across two layers:
- **In-Draft Redlines**: Only for **BLOCKING** risks (e.g., false claims, major logic gaps).
  - Use format: `[comment]: # (Devil [VERDICT]: {Risk} -> Move: {Mitigation})`
- **State File Snapshots**: Overwrite `devil.state.md` with:
  - **The Verdict**
  - **Weighted Warning**: The "Price" of publishing this piece.
  - **Detailed Risk Map**: Specific adversarial lenses applied and their findings.
  - **Turing Research Request**: If evidence is missing (see below).

## 3. Turing Research Request
If an audit reveals a credibility gap or an unsupported claim, generate a prompt for the user to hand over to **Turing**.

### Template:
> **TURING RESEARCH REQUEST**
> **Context**: [The claim being audited]
> **Gap**: [Why this claim is currently "Borrowed Certainty"]
> **Requirement**: [Specific evidence or data needed to stabilize this claim]
