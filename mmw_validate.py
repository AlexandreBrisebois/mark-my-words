#!/usr/bin/env python3
"""
mmw_validate.py — Build validation script for the Mark My Words multi-agent system.

Exits 0 if all checks pass. Exits 1 with a failure summary if any check fails.

Run from the project root:
    python mmw_validate.py
"""

import re
import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print(
        "mmw validate: ERROR — PyYAML is required. Install it with: pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(1)

# ---------------------------------------------------------------------------
# Required file lists
# ---------------------------------------------------------------------------

SEED_FILES = [
    "writers-room/brand/guidelines.md",
    "writers-room/index/post-index.md",
    "writers-room/cadence/calendar.md",
    "writers-room/research/notes.md",
]

AGENT_FILES = [
    ".claude/agents/caret.md",
    ".claude/agents/mark.md",
    ".claude/agents/compass.md",
    ".claude/agents/devil.md",
    ".claude/agents/turing.md",
    ".claude/agents/echo.md",
    ".claude/agents/press.md",
    ".claude/agents/prism.md",
    ".claude/agents/index.md",
    ".claude/agents/cadence.md",
]

# Sync masters hold full instructions; SLUG_SENTINEL checks run against these.
SYNC_MASTER_FILES = [
    ".claude/agents-sync/caret.md",
    ".claude/agents-sync/mark.md",
    ".claude/agents-sync/compass.md",
    ".claude/agents-sync/devil.md",
    ".claude/agents-sync/turing.md",
    ".claude/agents-sync/echo.md",
    ".claude/agents-sync/press.md",
    ".claude/agents-sync/prism.md",
    ".claude/agents-sync/index.md",
    ".claude/agents-sync/cadence.md",
]

SKILL_FILES = [
    ".claude/skills/mmw/SKILL.md",
    ".claude/skills/mmw-turing/SKILL.md",
    ".claude/skills/mmw-devil/SKILL.md",
    ".claude/skills/mmw-echo/SKILL.md",
    ".claude/skills/mmw-press/SKILL.md",
    ".claude/skills/mmw-prism/SKILL.md",
    ".claude/skills/mmw-compass/SKILL.md",
    ".claude/skills/mmw-mark/SKILL.md",
    ".claude/skills/mmw-cadence/SKILL.md",
    ".claude/skills/mmw-index/SKILL.md",
    ".claude/skills/mmw-bearings/SKILL.md",
    ".claude/skills/mmw-proof/SKILL.md",
]

SLUG_SENTINEL = "- Slug: (written by Press)"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_frontmatter(path: Path) -> Optional[dict]:
    """
    Parse YAML frontmatter from a file delimited by --- blocks.
    Returns the parsed dict, or None if no frontmatter found.
    """
    content = path.read_text(encoding="utf-8")
    # Frontmatter must start at line 1 with ---
    if not content.startswith("---"):
        return None
    # Find closing ---
    rest = content[3:]
    end = rest.find("---")
    if end == -1:
        return None
    fm_block = rest[:end].strip()
    try:
        return yaml.safe_load(fm_block) or {}
    except yaml.YAMLError:
        return None


# ---------------------------------------------------------------------------
# Check 1: Required files exist and are non-empty
# ---------------------------------------------------------------------------


def check_files_exist(failures: list[str]) -> None:
    all_required = SEED_FILES + AGENT_FILES + SYNC_MASTER_FILES + SKILL_FILES
    for rel_path in all_required:
        p = Path(rel_path)
        if not p.exists():
            failures.append(f"[MISSING] {rel_path}")
        elif p.stat().st_size == 0:
            failures.append(f"[EMPTY] {rel_path}")


# ---------------------------------------------------------------------------
# Check 2: Agent frontmatter — tools: is a YAML inline sequence (list)
# ---------------------------------------------------------------------------


def check_agent_tools(failures: list[str]) -> None:
    # Check both stubs and sync masters for correct frontmatter
    for rel_path in AGENT_FILES + SYNC_MASTER_FILES:
        p = Path(rel_path)
        if not p.exists():
            continue  # already caught by check_files_exist
        fm = _parse_frontmatter(p)
        if fm is None:
            failures.append(f"[NO FRONTMATTER] {rel_path} — YAML frontmatter block not found")
            continue
        tools = fm.get("tools")
        if tools is None:
            failures.append(f"[MISSING TOOLS] {rel_path} — 'tools' field not found in frontmatter")
        elif isinstance(tools, str):
            failures.append(
                f"[TOOLS NOT LIST] {rel_path} — tools field is a plain string "
                f"('{tools}'). Must be a YAML inline sequence: [Read, Write, ...]"
            )
        elif not isinstance(tools, list):
            failures.append(
                f"[TOOLS INVALID] {rel_path} — tools field is not a list (got {type(tools).__name__})"
            )


# ---------------------------------------------------------------------------
# Check 3: Agent frontmatter — model: is present
# ---------------------------------------------------------------------------


def check_agent_model(failures: list[str]) -> None:
    for rel_path in AGENT_FILES + SYNC_MASTER_FILES:
        p = Path(rel_path)
        if not p.exists():
            continue
        fm = _parse_frontmatter(p)
        if fm is None:
            continue  # already flagged
        model = fm.get("model")
        if not model:
            failures.append(f"[MISSING MODEL] {rel_path} — 'model' field not found in frontmatter")


# ---------------------------------------------------------------------------
# Check 4: SLUG_SENTINEL consistency in sync masters
#
# The local stubs are intentionally thin (redirect-only) and do not carry
# the SLUG_SENTINEL. The authoritative instruction files are the Sync Masters
# in .claude/agents-sync/. The sentinel must appear in both caret and press
# sync masters — caret uses it to write status.md at init; press uses it as
# the Edit-tool replace target.
# ---------------------------------------------------------------------------


def check_slug_sentinel(failures: list[str]) -> None:
    for rel_path in [
        ".claude/agents-sync/caret.md",
        ".claude/agents-sync/press.md",
    ]:
        p = Path(rel_path)
        if not p.exists():
            continue  # already caught by check_files_exist
        content = p.read_text(encoding="utf-8")
        if SLUG_SENTINEL not in content:
            failures.append(
                f"[SLUG MISMATCH] {rel_path} does not contain the expected "
                f"SLUG_SENTINEL: '{SLUG_SENTINEL}'"
            )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    failures: list[str] = []

    check_files_exist(failures)
    check_agent_tools(failures)
    check_agent_model(failures)
    check_slug_sentinel(failures)

    agent_count = len(AGENT_FILES)
    skill_count = len(SKILL_FILES)
    seed_count = len(SEED_FILES)
    sync_count = len(SYNC_MASTER_FILES)

    if not failures:
        print(
            f"mmw validate: all checks passed "
            f"({agent_count} agent stubs, {sync_count} sync masters, "
            f"{skill_count} skills, {seed_count} seed files)"
        )
        sys.exit(0)
    else:
        print("mmw validate: FAILED\n")
        for f in failures:
            print(f"  {f}")
        print(
            "\nFix the above before tracing workflow paths manually."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
