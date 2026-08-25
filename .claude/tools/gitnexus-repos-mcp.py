#!/usr/bin/env python3
"""Run the official GitNexus MCP server against this harness's real repos only.

GitNexus discovers repositories through a global registry. This launcher creates
an isolated, filtered registry for the lifetime of the MCP process, preventing
unrelated user indexes and the analysis harness itself from appearing as code
evidence.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Analysis harness root")
    args = parser.parse_args()
    root = args.root.resolve()
    repos_root = (root / "repos").resolve()
    if not repos_root.is_dir():
        raise SystemExit(f"Missing real-repository directory: {repos_root}")

    source_home = Path(os.environ.get("GITNEXUS_HOME", Path.home() / ".gitnexus"))
    registry_path = source_home / "registry.json"
    try:
        entries = json.loads(registry_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        entries = []
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid GitNexus registry {registry_path}: {error}") from error
    if not isinstance(entries, list):
        raise SystemExit(f"GitNexus registry must be an array: {registry_path}")

    allowed = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            continue
        try:
            repo_path = Path(entry["path"]).resolve()
            repo_path.relative_to(repos_root)
        except ValueError:
            continue
        if repo_path.parent != repos_root or not (repo_path / ".gitnexus").is_dir():
            continue
        allowed.append(entry)
    allowed.sort(key=lambda item: (item.get("name", ""), item.get("path", "")))
    if not allowed:
        raise SystemExit(f"No indexed repositories found directly under {repos_root}")

    temp_home = Path(tempfile.mkdtemp(prefix="gitnexus-repos-mcp-"))
    try:
        isolated = temp_home / ".gitnexus"
        isolated.mkdir()
        (isolated / "registry.json").write_text(json.dumps(allowed, indent=2) + "\n", encoding="utf-8")
        env = os.environ.copy()
        env["GITNEXUS_HOME"] = str(isolated)
        completed = subprocess.run(["gitnexus", "mcp"], cwd=root, env=env)
        return completed.returncode
    finally:
        shutil.rmtree(temp_home, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
