#!/usr/bin/env python3
"""
mmw_init-setup.py — Guided setup for the Mark My Words Claude Project Sync Layer.

This script:
  1. Checks for an existing claudesync installation (or installs it).
  2. Guides the user through sessionKey retrieval with step-by-step instructions.
  3. Runs `claudesync login` to store the session key securely.
  4. Runs `claudesync init` to link the local mark-my-words folder to a Claude Project.
  5. Validates the connection before exiting.

Run once during initial setup. Re-run only if you need to re-link to a different project.

Usage:
    python mmw_init-setup.py
"""

import subprocess
import sys
import shutil
import textwrap
from pathlib import Path

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


def _run(args: list[str], capture: bool = False) -> subprocess.CompletedProcess:
    """Run a subprocess. On failure, print stderr and sys.exit(1)."""
    result = subprocess.run(
        args,
        capture_output=capture,
        text=True,
    )
    return result


# ---------------------------------------------------------------------------
# Step 1 — Check / Install claudesync
# ---------------------------------------------------------------------------


def step_install(total: int) -> None:
    _step(1, total, "Checking for claudesync…")

    if shutil.which("claudesync"):
        result = _run(["claudesync", "--version"], capture=True)
        version = result.stdout.strip() or result.stderr.strip() or "unknown"
        _ok(f"claudesync is already installed ({version})")
        return

    _warn("claudesync not found in PATH.")
    _info(
        "claudesync is a community-maintained CLI tool that syncs files between "
        "your local filesystem and a Claude Project. It is not made by Anthropic."
    )

    if not _confirm("Install claudesync via pip now?"):
        _err("Setup cancelled. Install claudesync manually: pip install claudesync")
        sys.exit(1)

    print()
    result = _run([sys.executable, "-m", "pip", "install", "claudesync"])
    if result.returncode != 0:
        _err("pip install failed. Try: pip install --user claudesync")
        sys.exit(1)

    _ok("claudesync installed.")


# ---------------------------------------------------------------------------
# Step 2 — sessionKey Retrieval Guide
# ---------------------------------------------------------------------------


def step_session_key_guide(total: int) -> None:
    _step(2, total, "Retrieve your claude.ai sessionKey")

    print()
    _info(
        "claudesync authenticates with claude.ai using your browser session cookie. "
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

    _pause("Once you have the sessionKey copied, press Enter to continue…")


# ---------------------------------------------------------------------------
# Step 3 — claudesync login
# ---------------------------------------------------------------------------


def step_login(total: int) -> None:
    _step(3, total, "Log in to claudesync")

    _info(
        "Running `claudesync login`. You will be prompted to paste your sessionKey "
        "and select your Claude organisation. Follow the prompts in your terminal."
    )
    print()

    result = _run(["claudesync", "login"])

    if result.returncode != 0:
        _err(
            "claudesync login failed. Check that your sessionKey is correct and "
            "that you have an active claude.ai subscription."
        )
        sys.exit(1)

    _ok("Login successful.")


# ---------------------------------------------------------------------------
# Step 4 — Manual Project Creation Reminder
# ---------------------------------------------------------------------------


def step_project_reminder(total: int) -> None:
    _step(4, total, "Create your Claude Project (manual step)")

    print(f"""
  Before linking, you must create a {BOLD}Claude Project{RESET} in the claude.ai web UI.
  Mark My Words uses this project as its canonical state store.

  {CYAN}How to create a Claude Project:{RESET}
    1. Go to https://claude.ai
    2. Click {BOLD}Projects{RESET} in the left sidebar.
    3. Click {BOLD}+ New Project{RESET}.
    4. Name it something descriptive, e.g. {BOLD}mark-my-words{RESET}.
    5. (Optional) Add a brief description: "mmw multi-agent writing system state store."
    6. Click {BOLD}Create{RESET}.

  You do {BOLD}not{RESET} need to add any files manually — claudesync will handle that.
    """)

    _pause("Once the project is created in claude.ai, press Enter to continue…")


# ---------------------------------------------------------------------------
# Step 5 — claudesync init (project link)
# ---------------------------------------------------------------------------


def step_init(total: int) -> None:
    _step(5, total, "Link this folder to your Claude Project")

    _info(
        "Running `claudesync init` from the mark-my-words project root. "
        "You will be asked to select an organisation and the project you just created. "
        "claudesync will write a .claudesync/ config folder here — do not delete it."
    )
    print()

    result = _run(["claudesync", "init"])

    if result.returncode != 0:
        _err(
            "claudesync init failed. Ensure you completed the login step and "
            "that your Claude Project was created before running this step."
        )
        sys.exit(1)

    _ok("Project linked.")

    # Gitignore check
    gitignore = Path(".gitignore")
    claudesync_entry = ".claudesync/"
    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        if claudesync_entry not in content:
            _warn(
                ".claudesync/ is not in your .gitignore. "
                "Your sessionKey config should not be committed."
            )
            if _confirm("Add .claudesync/ to .gitignore now?"):
                with gitignore.open("a", encoding="utf-8") as f:
                    f.write(f"\n# claudesync config (contains auth state)\n{claudesync_entry}\n")
                _ok("Added .claudesync/ to .gitignore.")
    else:
        _warn("No .gitignore found. Create one and add .claudesync/ to it.")


# ---------------------------------------------------------------------------
# Step 6 — Validate Connection
# ---------------------------------------------------------------------------


def step_validate(total: int) -> None:
    _step(6, total, "Validating connection to Claude Project…")

    # A lightweight check: `claudesync status` or `claudesync ls` if available.
    # Fallback: just confirm .claudesync/ config was written.
    claudesync_dir = Path(".claudesync")
    if not claudesync_dir.exists():
        _err(
            ".claudesync/ config directory not found. "
            "claudesync init may not have completed successfully. Re-run this script."
        )
        sys.exit(1)

    # Try a status check if the subcommand exists
    result = _run(["claudesync", "status"], capture=True)
    if result.returncode == 0:
        _ok("Connection verified via `claudesync status`.")
        if result.stdout.strip():
            print()
            for line in result.stdout.strip().splitlines():
                print(f"    {DIM}{line}{RESET}")
    else:
        # Older versions may not have `status` — config existence is enough
        _ok(
            ".claudesync/ config found. Connection assumed valid. "
            "Run `claudesync push` to verify file transfer."
        )


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


def summary() -> None:
    _header("Setup Complete")

    print(f"""
  {GREEN}✓{RESET} claudesync is installed and linked to your Claude Project.

  {BOLD}Next steps — run these in order:{RESET}

  {BOLD}Step 1 — Validate the build{RESET}

    Confirm all agent stubs, sync masters, skills, and seed files
    are present and correctly formed:

      {CYAN}python mmw_validate.py{RESET}

    Fix any failures before proceeding.

  {BOLD}Step 2 — Seed the Claude Project{RESET}

    Push full agent instructions (sync masters) and global context
    files to your Claude Project Knowledge:

      {CYAN}claudesync push{RESET}

    This uploads everything in {BOLD}.claude/agents-sync/{RESET} (full agent specs)
    plus the four global context files:
      • {BOLD}writers-room/brand/guidelines.md{RESET}
      • {BOLD}writers-room/cadence/calendar.md{RESET}
      • {BOLD}writers-room/index/post-index.md{RESET}
      • {BOLD}writers-room/research/notes.md{RESET}

    Agents running inside a Claude Project session load these files
    automatically as ambient context — no tool call required.

  {BOLD}Step 3 — Start writing{RESET}

    Open a new Claude Code session in this folder and run:

      {CYAN}mmw [your topic]{RESET}

    Caret handles all sync automatically from this point forward:
      — pulls piece inputs before spawning each agent
      — pushes outputs after each agent completes
      — prunes published piece folders from the project on proof

  {BOLD}If you need to re-link to a different project later:{RESET}

      {CYAN}python mmw_init-setup.py{RESET}

  {DIM}See README.md § Cloud Sync Setup for the full reference.{RESET}
    """)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    _header("Mark My Words — Claude Project Sync Setup")

    print(f"""
  {DIM}This script sets up the bidirectional sync layer between your local
  mark-my-words files and a Claude Project. The project acts as the
  canonical state store for the mmw multi-agent system.

  You will need:
    • A claude.ai account with an active subscription
    • Your browser open at https://claude.ai to copy a session cookie
    • Network access to claude.ai{RESET}
    """)

    if not _confirm("Ready to begin setup?"):
        print("\n  Cancelled. Run this script again when ready.")
        sys.exit(0)

    TOTAL_STEPS = 6

    step_install(TOTAL_STEPS)
    step_session_key_guide(TOTAL_STEPS)
    step_login(TOTAL_STEPS)
    step_project_reminder(TOTAL_STEPS)
    step_init(TOTAL_STEPS)
    step_validate(TOTAL_STEPS)
    summary()


if __name__ == "__main__":
    main()
