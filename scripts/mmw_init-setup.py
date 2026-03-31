#!/usr/bin/env python3
"""
mmw_init-setup.py — Guided setup for the Mark My Words Claude Project Sync Layer.

This script:
  1. Guides the user through sessionKey retrieval.
  2. Verifies the sessionKey and selects a Claude Organization.
  3. Links the local folder to a Claude Project (existing or new).
  4. Saves configuration to .claude/config.json.

Usage:
    python scripts/mmw_init-setup.py
"""

import json
import sys
import textwrap
from pathlib import Path

# Internal sync module
from mmw_sync import ClaudeClient, save_config, ClaudeSyncError

# ---------------------------------------------------------------------------
# UI Helpers
# ---------------------------------------------------------------------------

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
DIM    = "\033[2m"


def _header(text: str) -> None:
    width = 70
    print()
    print(BOLD + CYAN + "─" * width + RESET)
    print(BOLD + CYAN + f"  {text}" + RESET)
    print(BOLD + CYAN + "─" * width + RESET)


def _step(n: int, total: int, text: str) -> None:
    print(f"\n{BOLD}[{n}/{total}]{RESET} {text}")


def _ok(text: str) -> None:
    print(f"  {GREEN}✓{RESET} {text}")


def _warn(text: str) -> None:
    print(f"  {YELLOW}⚠{RESET}  {text}")


def _err(text: str) -> None:
    print(f"  {RED}✗{RESET}  {text}", file=sys.stderr)


def _info(text: str) -> None:
    for line in textwrap.wrap(text, width=67):
        print(f"  {DIM}{line}{RESET}")


def _pause(prompt: str = "Press Enter to continue…") -> None:
    input(f"\n  {BOLD}{prompt}{RESET}")


def _confirm(question: str) -> bool:
    answer = input(f"\n  {BOLD}{question} [y/N]: {RESET}").strip().lower()
    return answer in ("y", "yes")


# ---------------------------------------------------------------------------
# Step 1 — sessionKey Retrieval Guide
# ---------------------------------------------------------------------------

def step_session_key_guide(total: int) -> str:
    _step(1, total, "Retrieve your claude.ai sessionKey")

    print()
    _info(
        "Mark My Words authenticates with claude.ai using your browser session cookie. "
        "You need to copy the `sessionKey` value from your browser's DevTools. "
        "Keep this value private — it grants full access to your Claude account."
    )

    print(f"""
  {BOLD}How to get your sessionKey:{RESET}

  {CYAN}Chrome / Edge:{RESET}
    1. Open https://claude.ai and sign in.
    2. Press F12 (or Cmd+Option+I on Mac) to open DevTools.
    3. Click the {BOLD}Application{RESET} tab.
    4. In the left sidebar, expand {BOLD}Cookies{RESET} → select {BOLD}https://claude.ai{RESET}.
    5. Find the row named {BOLD}sessionKey{RESET}.
    6. Click the row and copy the full {BOLD}Value{RESET} field.
       (It starts with "sk-ant-…")

  {CYAN}Firefox:{RESET}
    1. Open https://claude.ai and sign in.
    2. Press F12 → click {BOLD}Storage{RESET} tab.
    3. Expand {BOLD}Cookies{RESET} → select {BOLD}https://claude.ai{RESET}.
    4. Find {BOLD}sessionKey{RESET} and copy its Value.

  {YELLOW}⚠  Never commit this key to Git. Never share it.{RESET}
    """)

    while True:
        key = input(f"\n  {BOLD}Paste your sessionKey: {RESET}").strip()
        if key.startswith("sk-ant-sid"):
            return key
        _err("Invalid sessionKey format. It should start with 'sk-ant-sid'. Please try again.")


# ---------------------------------------------------------------------------
# Step 2 — Organization Selection
# ---------------------------------------------------------------------------

def step_select_org(total: int, client: ClaudeClient) -> str:
    _step(2, total, "Select Organization")
    
    try:
        orgs = client.get_organizations()
    except ClaudeSyncError as e:
        _err(f"Failed to fetch organizations: {str(e)}")
        sys.exit(1)

    if not orgs:
        _err("No Claude organizations found for this account.")
        sys.exit(1)

    if len(orgs) == 1:
        org = orgs[0]
        _ok(f"Using Organization: {org.get('name')} ({org.get('uuid')})")
        return org['uuid']

    print("\n  Available Organizations:")
    for i, org in enumerate(orgs, 1):
        print(f"    {i}. {org.get('name')} ({org.get('uuid')})")
    
    while True:
        try:
            choice = int(input(f"\n  Select an organization [1-{len(orgs)}]: "))
            if 1 <= choice <= len(orgs):
                return orgs[choice-1]['uuid']
        except ValueError:
            pass
        _err(f"Please enter a number between 1 and {len(orgs)}.")


# ---------------------------------------------------------------------------
# Step 3 — Project Selection / Creation
# ---------------------------------------------------------------------------

def step_select_project(total: int, client: ClaudeClient) -> str:
    _step(3, total, "Select or Create Claude Project")
    
    try:
        projects = client.list_projects()
    except ClaudeSyncError as e:
        _err(f"Failed to fetch projects: {str(e)}")
        sys.exit(1)

    print("\n  Available Projects:")
    for i, p in enumerate(projects, 1):
        print(f"    {i}. {p.get('name')} ({p.get('uuid')})")
    print(f"    {len(projects) + 1}. [Create New Project]")

    while True:
        try:
            choice = int(input(f"\n  Select a project [1-{len(projects)+1}]: "))
            if 1 <= choice <= len(projects):
                return projects[choice-1]['uuid']
            if choice == len(projects) + 1:
                name = input("\n  Enter name for new project [mark-my-words]: ").strip() or "mark-my-words"
                desc = input("  Enter a brief description: ").strip()
                new_p = client.create_project(name, desc)
                _ok(f"Created project: {new_p.get('name')}")
                return new_p['uuid']
        except ValueError:
            pass
        _err(f"Please enter a number between 1 and {len(projects)+1}.")


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def summary() -> None:
    _header("Setup Complete")

    print(f"""
  {GREEN}✓{RESET} Configuration saved to {BOLD}.claude/config.json{RESET}.
  {GREEN}✓{RESET} {BOLD}claudesync{RESET} dependency removed.

  {BOLD}Next steps — run these in order:{RESET}

  {BOLD}Step 1 — Validate the build{RESET}

    Confirm all agent stubs, sync masters, skills, and seed files
    are present and correctly formed:

      {CYAN}python scripts/mmw_validate.py{RESET}

  {BOLD}Step 2 — Seed the Claude Project{RESET}

    Push full agent instructions (sync masters) and global context
    files to your Claude Project Knowledge:

      {CYAN}python scripts/mmw_tools.py sync_push init{RESET}

  {BOLD}Step 3 — Start writing{RESET}

    Open a new Claude Code session in this folder and run:

      {CYAN}mmw [your topic]{RESET}

    Sync is handled automatically via the embedded client.
    """)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    _header("Mark My Words — Embedded Sync Setup")

    _info(
        "This script configures the bidirectional sync layer using a built-in "
        "Python client. No external tools are required."
    )

    if not _confirm("Ready to begin setup?"):
        print("\n  Cancelled.")
        sys.exit(0)

    TOTAL_STEPS = 3

    session_key = step_session_key_guide(TOTAL_STEPS)
    
    # Initialize client with just the key to start
    client = ClaudeClient(session_key=session_key)
    
    org_id = step_select_org(TOTAL_STEPS, client)
    client.org_id = org_id
    
    project_id = step_select_project(TOTAL_STEPS, client)
    
    # Save final config
    save_config({
        "session_key": session_key,
        "org_id": org_id,
        "project_id": project_id
    })
    
    # Update .gitignore
    gitignore = Path(".gitignore")
    entries_to_add = [".claude/config.json", ".claudesync/"]
    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        with gitignore.open("a", encoding="utf-8") as f:
            for entry in entries_to_add:
                if entry not in content:
                    f.write(f"\n{entry}\n")
    else:
        gitignore.write_text("\n".join(entries_to_add) + "\n", encoding="utf-8")

    _ok("Configuration finalized.")
    summary()


if __name__ == "__main__":
    main()
