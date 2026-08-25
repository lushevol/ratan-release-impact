#!/usr/bin/env python3
"""Build, validate, and publish every SDLC graph projection with one command."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = SKILL_ROOT.parents[2]
TOOLS = SKILL_ROOT / "tools"


def run(*parts: object) -> None:
    command = [str(part) for part in parts]
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=WORKSPACE, check=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})


def publish(candidate: Path, target: Path) -> None:
    backup = target.with_name(f".{target.name}.previous")
    if backup.exists():
        shutil.rmtree(backup)
    if target.exists():
        target.replace(backup)
    try:
        candidate.replace(target)
    except Exception:
        if backup.exists():
            backup.replace(target)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repos", type=Path, default=WORKSPACE / "repos")
    parser.add_argument("--out", type=Path, default=WORKSPACE / "system-graph")
    parser.add_argument("--open", action="store_true", help="Open the published viewer in the default browser")
    args = parser.parse_args()
    output = args.out.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".sdlc-graph-", dir=output.parent) as temporary:
        candidate = Path(temporary) / "system-graph"
        run(sys.executable, TOOLS / "build_graph.py", "--workspace", WORKSPACE, "--repos", args.repos, "--out", candidate)
        run(sys.executable, TOOLS / "render_graph.py", candidate / "graph.json", "--output", candidate / "relationship-viewer.html")
        run(sys.executable, TOOLS / "validate_graph.py", candidate / "graph.json", "--workspace", WORKSPACE,
            "--dependencies", candidate / "dependencies.json")
        publish(candidate, output)
    if args.open:
        run("open", output / "relationship-viewer.html")
    graph = json.loads((output / "graph.json").read_text(encoding="utf-8"))
    summary = {
        "output": str(output), "viewer": str(output / "relationship-viewer.html"),
        "repositories": sum(bool(repo["visible"]) for repo in graph["repositories"]),
        "nodes": len(graph["nodes"]), "edges": len(graph["edges"]), "evidence": len(graph["evidence"]),
    }
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
