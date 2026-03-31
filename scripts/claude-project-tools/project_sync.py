#!/usr/bin/env python3
"""
claude_sync.py — Embedded Claude Project Sync Client.

This module provides a direct Python client for Anthropic's internal Claude Project API.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

# ---------------------------------------------------------------------------
# Constants & Configuration
# ---------------------------------------------------------------------------

CLAUDE_DIR = Path(".claude")
CONFIG_FILE = CLAUDE_DIR / "config.json"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)


class ClaudeSyncError(Exception):
    """Custom exception for sync-related failures."""
    pass


# ---------------------------------------------------------------------------
# Config Management
# ---------------------------------------------------------------------------

def load_config() -> Dict[str, Any]:
    """Load configuration from .claude/config.json."""
    if not CONFIG_FILE.exists():
        return {}
    try:
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_config(config: Dict[str, Any]) -> None:
    """Save configuration to .claude/config.json."""
    CLAUDE_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(config, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Claude API Client
# ---------------------------------------------------------------------------

class ClaudeClient:
    """
    A minimalist client for the Claude Projects internal API.
    """

    def __init__(self, session_key: str, org_id: Optional[str] = None, project_id: Optional[str] = None):
        self.session_key = session_key
        self.org_id = org_id
        self.project_id = project_id
        self.base_url = "https://claude.ai/api"

    @property
    def headers(self) -> Dict[str, str]:
        return {
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Referer": "https://claude.ai/",
            "Origin": "https://claude.ai",
        }

    @property
    def cookies(self) -> Dict[str, str]:
        cookies = {"sessionKey": self.session_key}
        if self.org_id:
            cookies["lastActiveOrg"] = self.org_id
        return cookies

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method, 
                url, 
                headers=self.headers, 
                cookies=self.cookies, 
                **kwargs
            )
            response.raise_for_status()
            if response.text:
                return response.json()
            return None
        except requests.RequestException as e:
            msg = f"Claude API Error ({method} {endpoint}): {str(e)}"
            if response := getattr(e, 'response', None):
                try:
                    error_json = response.json()
                    msg += f" - {json.dumps(error_json)}"
                except:
                    msg += f" - {response.text}"
            raise ClaudeSyncError(msg)

    def get_organizations(self) -> List[Dict[str, Any]]:
        """Fetch organizations the user belongs to via bootstrap."""
        data = self._request("GET", "/bootstrap")
        memberships = data.get("account", {}).get("memberships", [])
        return [m.get("organization", {}) for m in memberships if "organization" in m]

    def list_projects(self) -> List[Dict[str, Any]]:
        """List active projects in the current organization."""
        if not self.org_id:
            raise ClaudeSyncError("Organization ID not set.")
        projects = self._request("GET", f"/organizations/{self.org_id}/projects")
        # Filter out archived
        return [p for p in projects if not p.get("archived_at")]

    def create_project(self, name: str, description: str = "") -> Dict[str, Any]:
        """Create a new Claude Project."""
        if not self.org_id:
            raise ClaudeSyncError("Organization ID not set.")
        payload = {
            "name": name,
            "description": description,
            "is_private": True
        }
        return self._request("POST", f"/organizations/{self.org_id}/projects", json=payload)

    def list_docs(self) -> List[Dict[str, Any]]:
        """List all documents in the target project."""
        if not self.org_id or not self.project_id:
            raise ClaudeSyncError("Organization or Project ID not set.")
        return self._request("GET", f"/organizations/{self.org_id}/projects/{self.project_id}/docs")

    def upload_doc(self, file_name: str, content: str) -> Dict[str, Any]:
        """
        Upload a document to the project. 
        Note: The API does not have an 'update' endpoint; we delete and re-upload.
        """
        if not self.org_id or not self.project_id:
            raise ClaudeSyncError("Organization or Project ID not set.")
        
        # 1. Check for existing document with the same name and delete if found
        docs = self.list_docs()
        for doc in docs:
            if doc.get("file_name") == file_name:
                self.delete_doc(doc["uuid"])
        
        # 2. Upload new content
        payload = {"file_name": file_name, "content": content}
        return self._request("POST", f"/organizations/{self.org_id}/projects/{self.project_id}/docs", json=payload)

    def delete_doc(self, doc_uuid: str) -> None:
        """Delete a document from the project."""
        if not self.org_id or not self.project_id:
            raise ClaudeSyncError("Organization or Project ID not set.")
        self._request("DELETE", f"/organizations/{self.org_id}/projects/{self.project_id}/docs/{doc_uuid}")

    def push_files(self, file_paths: List[str], base_dir: Path = Path("project")) -> List[str]:
        """Push multiple local files to the Claude Project."""
        uploaded = []
        for path_str in file_paths:
            path = Path(path_str)
            if not path.exists():
                print(f"  ⚠ Skipping missing file: {path_str}", file=sys.stderr)
                continue
            
            # Normalize path relative to base_dir
            try:
                rel_path = path.relative_to(base_dir)
            except ValueError:
                rel_path = path
            
            file_name = str(rel_path).replace(os.path.sep, "/")
            content = path.read_text(encoding="utf-8")
            
            if not content.strip():
                print(f"  ⚠ Skipping empty file: {path_str}", file=sys.stderr)
                continue
                
            self.upload_doc(file_name, content)
            uploaded.append(file_name)
        return uploaded

    def pull_files(self, targets: List[str], base_dir: Path = Path("project")) -> List[str]:
        """
        Pull specific files from the Claude Project to the local filesystem.
        'targets' are relative paths (e.g. 'test.txt')
        """
        docs = self.list_docs()
        doc_map = {doc["file_name"]: doc for doc in docs}
        
        pulled = []
        base_dir.mkdir(parents=True, exist_ok=True)
        for target in targets:
            normalized_target = target.replace(os.path.sep, "/")
            if normalized_target in doc_map:
                doc = doc_map[normalized_target]
                content = doc.get("content", "")
                local_path = base_dir / target
                local_path.parent.mkdir(parents=True, exist_ok=True)
                local_path.write_text(content, encoding="utf-8")
                pulled.append(target)
        return pulled


# ---------------------------------------------------------------------------
# CLI Implementation (for direct use or testing)
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="claude internal sync tool")
    subparsers = parser.add_subparsers(dest="command")

    # Push
    push_p = subparsers.add_parser("push")
    push_p.add_argument("files", nargs="+", help="Files to push")

    # Pull
    pull_p = subparsers.add_parser("pull")
    pull_p.add_argument("files", nargs="+", help="Files to pull")

    args = parser.parse_args()
    
    config = load_config()
    session_key = config.get("session_key")
    if not session_key:
        print("Error: No session_key found in .claude/config.json. Run setup first.", file=sys.stderr)
        sys.exit(1)
        
    client = ClaudeClient(
        session_key=session_key,
        org_id=config.get("org_id"),
        project_id=config.get("project_id")
    )

    try:
        if args.command == "push":
            uploaded = client.push_files(args.files)
            print(json.dumps({"pushed": True, "files": uploaded}))
        elif args.command == "pull":
            pulled = client.pull_files(args.files)
            print(json.dumps({"pulled": True, "files": pulled}))
    except ClaudeSyncError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
