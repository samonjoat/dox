#!/usr/bin/env python3
"""Minimal structural validator for DOX AGENTS.md trees.

This linter intentionally validates only machine-checkable structure:
- root AGENTS.md exists
- protected root core markers exist and are ordered
- every AGENTS.md has a Child DOX Index
- child-index entries that reference AGENTS.md files resolve to real files
- non-root AGENTS.md files use the standard DOX section set
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CORE_START_RE = re.compile(r"<!--\s*DOX-CORE-START\b[^>]*-->")
CORE_END_RE = re.compile(r"<!--\s*DOX-CORE-END\b[^>]*-->")
REQUIRED_CHILD_SECTIONS = [
    "Purpose",
    "Ownership",
    "Local Contracts",
    "Work Guidance",
    "Verification",
    "Child DOX Index",
]
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    "coverage",
    "__pycache__",
}
CHILD_PATH_RE = re.compile(r"^\s*-\s+`([^`]*AGENTS\.md)`")
CHILD_ENTRY_RE = re.compile(r"^\s*-\s+`([^`]*AGENTS\.md)`\s+[—-]\s+\S")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_agents_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("AGENTS.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        files.append(path)
    return sorted(files)


def headings(text: str) -> list[str]:
    return [line.strip("# ").strip() for line in text.splitlines() if line.startswith("## ")]


def child_index_body(text: str) -> list[str]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "## Child DOX Index":
            body: list[str] = []
            for nxt in lines[i + 1 :]:
                if nxt.startswith("## "):
                    break
                body.append(nxt)
            return body
    return []


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()
    root_agents = root / "AGENTS.md"

    if not root_agents.exists():
        return [f"missing root AGENTS.md: {root_agents}"]

    agents_files = iter_agents_files(root)
    agents_set = {p.resolve() for p in agents_files}
    root_text = read_text(root_agents)

    start_match = CORE_START_RE.search(root_text)
    end_match = CORE_END_RE.search(root_text)
    if start_match is None:
        errors.append("root AGENTS.md missing DOX-CORE-START HTML comment marker")
    if end_match is None:
        errors.append("root AGENTS.md missing DOX-CORE-END HTML comment marker")
    if start_match is not None and end_match is not None and start_match.start() > end_match.start():
        errors.append("root AGENTS.md DOX core HTML comment markers are out of order")

    for agents_path in agents_files:
        rel = agents_path.relative_to(root)
        text = read_text(agents_path)
        hs = headings(text)

        if "Child DOX Index" not in hs:
            errors.append(f"{rel}: missing ## Child DOX Index")

        if agents_path != root_agents:
            for section in REQUIRED_CHILD_SECTIONS:
                if section not in hs:
                    errors.append(f"{rel}: missing ## {section}")

        for line in child_index_body(text):
            path_match = CHILD_PATH_RE.match(line)
            if not path_match:
                continue

            child_rel = path_match.group(1)
            if not CHILD_ENTRY_RE.match(line):
                errors.append(f"{rel}: child index entry for {child_rel} missing description")

            child_path = (agents_path.parent / child_rel).resolve()
            if child_path not in agents_set:
                errors.append(f"{rel}: child index points to missing {child_rel}")
            else:
                try:
                    child_path.relative_to(agents_path.parent.resolve())
                except ValueError:
                    errors.append(f"{rel}: child index escapes parent subtree: {child_rel}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a DOX AGENTS.md tree")
    parser.add_argument("root", nargs="?", default=".", help="repository root, default: current directory")
    args = parser.parse_args()

    root = Path(args.root)
    errors = validate(root)
    if errors:
        print("DOX lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DOX lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
