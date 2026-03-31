#!/usr/bin/env python3
"""
mmw_tools.py — Deterministic helper tools for the Mark My Words multi-agent pipeline.

Usage:
    python mmw_tools.py <tool_name> [args...]

All tools print JSON to stdout and exit 0 on success.
On failure, print a descriptive error to stderr and exit 1.

Tools:
    draft_version <codename> <action>
        action: "latest" → {"path": "writers-room/pieces/<codename>/draft-vN.md", "version": N}
        action: "next"   → {"path": "writers-room/pieces/<codename>/draft-v(N+1).md", "version": N+1}

    status_read <codename> <field>
        Returns {"field": "<field>", "value": "<value>"} or {"field": "<field>", "value": null} if absent.
        Field names are lowercase: "phase", "mode", "slug", "current_draft", "last_agent", "next_step"

    status_write <codename> <json_updates>
        json_updates: JSON object of field→value pairs to update in ## Current State block.
        Returns {"updated": ["field1", "field2", ...]}

    status_log <codename> <entry>
        Appends a log entry under ## Agent Run Log.
        Returns {"appended": true}

    research_prune <notes_path> [max_age_days]
        Removes rows from the research notes table older than max_age_days (default: 90).
        Returns {"pruned": N, "remaining": M}

    overlap_check <brief_path> <index_path>
        Lexical TF-IDF overlap check of brief against post-index entries.
        Returns {"candidates": [{"title": ..., "slug": ..., "score": ..., "shared_keywords": [...]}, ...]}
        Returns top 5 candidates with score > 0, sorted by score desc.

    slug_validate <codename>
        Compares slug in status.md against slug in seo.md.
        Returns {"match": true/false, "status_slug": "...", "seo_slug": "..."}

    preflight <codename>
        Runs Phase 11 pre-flight checks.
        Returns {"ready": true/false, "failures": ["description", ...]}

    publish <codename>
        Atomically writes published output files and updates status.md.
        Returns {"success": true, "published_path": "...", "image_path": "..."}

    index_update <codename>
        Reads status.md metadata and appends a row to post-index.md.
        Returns {"appended": true, "title": "...", "slug": "..."}

    calendar_log <codename> <description> <target_date>
        Appends an entry to calendar.md.
        Returns {"appended": true}
"""

import json
import math
import re
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WRITERS_ROOM = Path("writers-room")
PIECES = WRITERS_ROOM / "pieces"
PUBLISHED = WRITERS_ROOM / "published"
POST_INDEX = WRITERS_ROOM / "index" / "post-index.md"
CALENDAR = WRITERS_ROOM / "cadence" / "calendar.md"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _piece_dir(codename: str) -> Path:
    return PIECES / codename


def _fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(1)


def _ok(data: dict) -> None:
    print(json.dumps(data))
    sys.exit(0)


def _read(path: Path) -> str:
    if not path.exists():
        _fail(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def _latest_draft_version(codename: str) -> int:
    """Return highest N from draft-vN.md files, or 0 if none exist."""
    piece_dir = _piece_dir(codename)
    if not piece_dir.exists():
        _fail(f"Piece folder not found: {piece_dir}")
    versions = []
    for f in piece_dir.iterdir():
        m = re.match(r"^draft-v(\d+)\.md$", f.name)
        if m:
            versions.append(int(m.group(1)))
    return max(versions, default=0)


def _status_path(codename: str) -> Path:
    return _piece_dir(codename) / "status.md"


def _parse_current_state(content: str) -> dict:
    """Parse ## Current State block into a dict of lowercase field → value."""
    m = re.search(r"## Current State\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    fields = {}
    # Match lines like: - Phase: 0 — Index overlap gate
    for line in block.splitlines():
        lm = re.match(r"^-\s+([^:]+):\s*(.*)$", line)
        if lm:
            key = lm.group(1).strip().lower().replace(" ", "_")
            fields[key] = lm.group(2).strip()
    return fields


def _update_current_state(content: str, updates: dict) -> str:
    """Update fields in ## Current State block. Adds new fields if not present."""
    m = re.search(r"(## Current State\n)(.*?)(\n##|\Z)", content, re.DOTALL)
    if not m:
        _fail("status.md is missing ## Current State block")

    block = m.group(2)
    lines = block.splitlines()

    # Build a map of canonical key → line index for existing fields
    existing = {}  # canonical_key → line_index
    for i, line in enumerate(lines):
        lm = re.match(r"^-\s+([^:]+):\s*(.*)$", line)
        if lm:
            key = lm.group(1).strip().lower().replace(" ", "_")
            existing[key] = i

    for raw_key, value in updates.items():
        canonical = raw_key.lower().replace(" ", "_")
        # Find display name: prefer title-case with spaces
        display = raw_key.replace("_", " ").title()
        new_line = f"- {display}: {value}"

        if canonical in existing:
            lines[existing[canonical]] = new_line
        else:
            lines.append(new_line)

    new_block = "\n".join(lines)
    return content[: m.start(2)] + new_block + content[m.end(2) :]


# ---------------------------------------------------------------------------
# Tool: draft_version
# ---------------------------------------------------------------------------


def draft_version(codename: str, action: str) -> None:
    if action not in ("latest", "next"):
        _fail(f"draft_version: action must be 'latest' or 'next', got '{action}'")

    current = _latest_draft_version(codename)

    if action == "latest":
        if current == 0:
            _fail(f"No draft-vN.md files found in {_piece_dir(codename)}")
        path = str(PIECES / codename / f"draft-v{current}.md")
        _ok({"path": path, "version": current})
    else:  # next
        nxt = current + 1
        path = str(PIECES / codename / f"draft-v{nxt}.md")
        _ok({"path": path, "version": nxt})


# ---------------------------------------------------------------------------
# Tool: status_read
# ---------------------------------------------------------------------------

# Map user-supplied field name aliases to canonical keys
_FIELD_ALIASES = {
    "phase": "phase",
    "mode": "mode",
    "slug": "slug",
    "current_draft": "current_draft",
    "current draft": "current_draft",
    "last_agent": "last_agent",
    "last agent": "last_agent",
    "next_step": "next_step",
    "next step": "next_step",
    "brief_intent": "brief_intent",
    "brief intent": "brief_intent",
}


def status_read(codename: str, field: str) -> None:
    path = _status_path(codename)
    content = _read(path)
    fields = _parse_current_state(content)

    canonical = _FIELD_ALIASES.get(field.lower().replace(" ", "_"), field.lower().replace(" ", "_"))
    value = fields.get(canonical, None)
    _ok({"field": field, "value": value})


# ---------------------------------------------------------------------------
# Tool: status_write
# ---------------------------------------------------------------------------


def status_write(codename: str, json_updates: str) -> None:
    try:
        updates = json.loads(json_updates)
    except json.JSONDecodeError as e:
        _fail(f"status_write: invalid JSON: {e}")

    path = _status_path(codename)
    content = _read(path)
    updated = _update_current_state(content, updates)
    path.write_text(updated, encoding="utf-8")
    _ok({"updated": list(updates.keys())})


# ---------------------------------------------------------------------------
# Tool: status_log
# ---------------------------------------------------------------------------


def status_log(codename: str, entry: str) -> None:
    path = _status_path(codename)
    content = _read(path)

    log_marker = "## Agent Run Log"
    if log_marker not in content:
        _fail(f"status.md is missing '{log_marker}' section")

    # Append entry as a new list item before any trailing content
    log_entry = f"- {entry}"
    # Insert after the ## Agent Run Log header line
    idx = content.index(log_marker) + len(log_marker)
    # Move past any blank line immediately after the header
    rest = content[idx:]
    nl_match = re.match(r"(\n+)", rest)
    skip = len(nl_match.group(1)) if nl_match else 0

    insert_pos = idx + skip
    new_content = content[:insert_pos] + log_entry + "\n" + content[insert_pos:]
    path.write_text(new_content, encoding="utf-8")
    _ok({"appended": True})


# ---------------------------------------------------------------------------
# Tool: research_prune
# ---------------------------------------------------------------------------


def research_prune(notes_path: str, max_age_days: int = 90) -> None:
    path = Path(notes_path)
    if not path.exists():
        _fail(f"research_prune: file not found: {path}")

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)
    cutoff = date.today() - timedelta(days=max_age_days)

    header_lines = []
    data_lines = []
    in_header = True

    for line in lines:
        stripped = line.strip()
        if in_header and (stripped.startswith("|") or stripped == ""):
            header_lines.append(line)
            # Stop treating as header after we pass the separator row
            if re.match(r"^\|[-|: ]+\|$", stripped):
                in_header = False
        else:
            data_lines.append(line)

    kept = []
    pruned = 0

    for line in data_lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            kept.append(line)
            continue
        # Parse first column as date
        cols = [c.strip() for c in stripped.strip("|").split("|")]
        if not cols:
            kept.append(line)
            continue
        date_str = cols[0]
        try:
            row_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            kept.append(line)
            continue

        if row_date < cutoff:
            pruned += 1
        else:
            kept.append(line)

    new_content = "".join(header_lines + kept)
    path.write_text(new_content, encoding="utf-8")
    _ok({"pruned": pruned, "remaining": len(kept)})


# ---------------------------------------------------------------------------
# Tool: overlap_check
# ---------------------------------------------------------------------------

_STOP_WORDS = frozenset(
    "a an the and or but in on at to for of with by from is are was were be been "
    "have has had do does did will would could should may might shall i we you he "
    "she it they their there this that these those what which who how when where why "
    "how about post blog write writing piece article".split()
)


def _tokenize(text: str) -> list[str]:
    return [
        w.lower()
        for w in re.findall(r"[a-z]+", text.lower())
        if w.lower() not in _STOP_WORDS and len(w) > 2
    ]


def overlap_check(brief_path: str, index_path: str) -> None:
    brief_text = _read(Path(brief_path))
    index_text = _read(Path(index_path))

    brief_tokens = _tokenize(brief_text)
    if not brief_tokens:
        _ok({"candidates": []})

    brief_tf = Counter(brief_tokens)
    brief_total = sum(brief_tf.values())

    # Parse post-index.md table rows
    # Expected columns: Title | Slug | Date | Tags | Description
    rows = []
    for line in index_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cols) < 2:
            continue
        if re.match(r"^[-|: ]+$", stripped.replace("|", "").strip()):
            continue  # separator row
        if cols[0].lower() in ("title", ""):
            continue  # header row
        title = cols[0] if len(cols) > 0 else ""
        slug = cols[1] if len(cols) > 1 else ""
        description = cols[4] if len(cols) > 4 else ""
        rows.append({"title": title, "slug": slug, "description": description})

    if not rows:
        _ok({"candidates": []})

    # Build IDF across all index entries
    doc_count = len(rows)
    doc_freq: Counter = Counter()
    tokenized_rows = []
    for row in rows:
        tokens = _tokenize(f"{row['title']} {row['description']}")
        tokenized_rows.append(tokens)
        for t in set(tokens):
            doc_freq[t] += 1

    def idf(term: str) -> float:
        df = doc_freq.get(term, 0)
        if df == 0:
            return 0.0
        return math.log((doc_count + 1) / (df + 1)) + 1.0

    # Score each row
    candidates = []
    for row, row_tokens in zip(rows, tokenized_rows):
        row_tf = Counter(row_tokens)
        row_total = sum(row_tf.values()) or 1
        shared = set(brief_tf.keys()) & set(row_tf.keys())
        if not shared:
            continue
        score = sum(
            (brief_tf[t] / brief_total) * (row_tf[t] / row_total) * idf(t) ** 2
            for t in shared
        )
        candidates.append(
            {
                "title": row["title"],
                "slug": row["slug"],
                "score": round(score, 4),
                "shared_keywords": sorted(shared),
            }
        )

    candidates.sort(key=lambda c: c["score"], reverse=True)
    _ok({"candidates": candidates[:5]})


# ---------------------------------------------------------------------------
# Tool: slug_validate
# ---------------------------------------------------------------------------

def _extract_slug_from_status(content: str) -> Optional[str]:
    fields = _parse_current_state(content)
    slug = fields.get("slug")
    if not slug or slug == "(written by Press)":
        return None
    return slug


def _extract_slug_from_seo(content: str) -> Optional[str]:
    # Look for "slug: <value>" in YAML front matter block
    m = re.search(r"^slug:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
    if m:
        return m.group(1).strip().strip('"\'')
    return None


def slug_validate(codename: str) -> None:
    piece_dir = _piece_dir(codename)
    status_content = _read(piece_dir / "status.md")
    seo_path = piece_dir / "seo.md"
    seo_content = _read(seo_path)

    status_slug = _extract_slug_from_status(status_content)
    seo_slug = _extract_slug_from_seo(seo_content)

    match = (status_slug is not None) and (seo_slug is not None) and (status_slug == seo_slug)
    _ok({"match": match, "status_slug": status_slug, "seo_slug": seo_slug})


# ---------------------------------------------------------------------------
# Tool: preflight
# ---------------------------------------------------------------------------


def preflight(codename: str) -> None:
    piece_dir = _piece_dir(codename)
    failures = []

    # 1. seo.md exists
    seo_path = piece_dir / "seo.md"
    if not seo_path.exists():
        failures.append("seo.md does not exist")
    else:
        seo_content = seo_path.read_text(encoding="utf-8")

    # 2. Slug in status.md is populated
    status_path = piece_dir / "status.md"
    if not status_path.exists():
        failures.append("status.md does not exist")
        _ok({"ready": False, "failures": failures})

    status_content = status_path.read_text(encoding="utf-8")
    status_slug = _extract_slug_from_status(status_content)
    if not status_slug:
        failures.append("Slug field in status.md is not populated (still placeholder or missing)")

    # 3. Slug in status.md matches slug in seo.md
    if seo_path.exists() and status_slug:
        seo_slug = _extract_slug_from_seo(seo_content)
        if not seo_slug:
            failures.append("Slug not found in seo.md")
        elif seo_slug != status_slug:
            failures.append(
                f"Slug mismatch: status.md has '{status_slug}', seo.md has '{seo_slug}'"
            )

    # 4. image-prompt.md exists
    if not (piece_dir / "image-prompt.md").exists():
        failures.append("image-prompt.md does not exist")

    # 5. Latest draft-vN.md exists
    latest = _latest_draft_version(codename)
    if latest == 0:
        failures.append("No draft-vN.md found in piece folder")

    # 6. writers-room/published/ directory exists
    if not PUBLISHED.exists():
        failures.append("writers-room/published/ directory does not exist")

    _ok({"ready": len(failures) == 0, "failures": failures})


# ---------------------------------------------------------------------------
# Tool: publish
# ---------------------------------------------------------------------------


def publish(codename: str) -> None:
    piece_dir = _piece_dir(codename)

    # Resolve slug from status.md
    status_path = piece_dir / "status.md"
    status_content = _read(status_path)
    slug = _extract_slug_from_status(status_content)
    if not slug:
        _fail("publish: slug is not populated in status.md — run Press first")

    # Resolve final.md (latest draft)
    latest = _latest_draft_version(codename)
    if latest == 0:
        _fail("publish: no draft-vN.md found")
    draft_path = piece_dir / f"draft-v{latest}.md"
    draft_content = _read(draft_path)

    # image-prompt.md
    image_prompt_path = piece_dir / "image-prompt.md"
    image_content = _read(image_prompt_path)

    # Write final.md
    final_path = piece_dir / "final.md"
    final_path.write_text(draft_content, encoding="utf-8")

    # Ensure published/ exists
    PUBLISHED.mkdir(parents=True, exist_ok=True)

    # Write published files
    pub_post = PUBLISHED / f"{slug}.md"
    pub_image = PUBLISHED / f"{slug}-image-prompt.md"
    pub_post.write_text(draft_content, encoding="utf-8")
    pub_image.write_text(image_content, encoding="utf-8")

    # Update status.md
    updated = _update_current_state(
        status_content,
        {"phase": "11 — Published", "next_step": "Published"},
    )
    status_path.write_text(updated, encoding="utf-8")

    _ok(
        {
            "success": True,
            "published_path": str(pub_post),
            "image_path": str(pub_image),
            "final_path": str(final_path),
        }
    )


# ---------------------------------------------------------------------------
# Tool: index_update
# ---------------------------------------------------------------------------


def index_update(codename: str) -> None:
    piece_dir = _piece_dir(codename)
    status_content = _read(piece_dir / "status.md")

    # Extract description from > blockquote (one-liner below # codename heading)
    desc_m = re.search(r"^>\s+(.+)$", status_content, re.MULTILINE)
    description = desc_m.group(1).strip() if desc_m else ""

    # Extract slug
    slug = _extract_slug_from_status(status_content) or ""

    # Extract title from seo.md if available (hugo front matter "title:")
    title = ""
    seo_path = piece_dir / "seo.md"
    if seo_path.exists():
        seo_content = seo_path.read_text(encoding="utf-8")
        tm = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", seo_content, re.MULTILINE | re.IGNORECASE)
        if tm:
            title = tm.group(1).strip()
    if not title:
        title = codename

    # Extract date from seo.md or today
    pub_date = date.today().isoformat()
    if seo_path.exists():
        dm = re.search(r"^date:\s*(.+)$", seo_content, re.MULTILINE | re.IGNORECASE)
        if dm:
            pub_date = dm.group(1).strip().split("T")[0]

    # Extract tags from seo.md
    tags = ""
    if seo_path.exists():
        tag_m = re.search(r"^tags:\s*\[(.+?)\]", seo_content, re.MULTILINE | re.IGNORECASE)
        if tag_m:
            tags = tag_m.group(1).strip()

    # Append row to post-index.md
    index_content = _read(POST_INDEX)
    new_row = f"| {title} | {slug} | {pub_date} | {tags} | {description} |"
    new_content = index_content.rstrip() + "\n" + new_row + "\n"
    POST_INDEX.write_text(new_content, encoding="utf-8")

    _ok({"appended": True, "title": title, "slug": slug})


# ---------------------------------------------------------------------------
# Tool: calendar_log
# ---------------------------------------------------------------------------


def calendar_log(codename: str, description: str, target_date: str) -> None:
    cal_content = _read(CALENDAR)
    new_row = f"| {codename} | {description} | {target_date} | Scheduled |  |"
    new_content = cal_content.rstrip() + "\n" + new_row + "\n"
    CALENDAR.write_text(new_content, encoding="utf-8")
    _ok({"appended": True})


# ---------------------------------------------------------------------------
# CLI dispatch
# ---------------------------------------------------------------------------

_TOOLS = {
    "draft_version": (draft_version, ["codename", "action"]),
    "status_read": (status_read, ["codename", "field"]),
    "status_write": (status_write, ["codename", "json_updates"]),
    "status_log": (status_log, ["codename", "entry"]),
    "research_prune": (research_prune, ["notes_path"]),
    "overlap_check": (overlap_check, ["brief_path", "index_path"]),
    "slug_validate": (slug_validate, ["codename"]),
    "preflight": (preflight, ["codename"]),
    "publish": (publish, ["codename"]),
    "index_update": (index_update, ["codename"]),
    "calendar_log": (calendar_log, ["codename", "description", "target_date"]),
}


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    tool_name = sys.argv[1]
    args = sys.argv[2:]

    if tool_name not in _TOOLS:
        _fail(f"Unknown tool: '{tool_name}'. Available: {', '.join(_TOOLS)}")

    fn, param_names = _TOOLS[tool_name]

    # Special case: research_prune has an optional second argument
    if tool_name == "research_prune":
        if len(args) == 0:
            _fail("research_prune requires at least <notes_path>")
        elif len(args) == 1:
            research_prune(args[0])
        else:
            try:
                research_prune(args[0], int(args[1]))
            except ValueError:
                _fail(f"research_prune: max_age_days must be an integer, got '{args[1]}'")
        return

    if len(args) != len(param_names):
        _fail(
            f"{tool_name} requires {len(param_names)} argument(s): "
            f"{', '.join(f'<{p}>' for p in param_names)}. Got {len(args)}."
        )

    fn(*args)


if __name__ == "__main__":
    main()
