#!/usr/bin/env python3
"""Build, validate, and publish every SDLC graph projection with one command."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from graph_query import service_catalog


SKILL_ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = SKILL_ROOT.parents[2]
TOOLS = SKILL_ROOT / "tools"
OUTPUT_NAME = "sdlc-graph-output"


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


def write_ai_outputs(candidate: Path, descriptions: Path) -> None:
    graph = json.loads((candidate / "graph.json").read_text(encoding="utf-8"))
    dependency_catalog = json.loads((candidate / "dependencies.json").read_text(encoding="utf-8"))
    (candidate / "services.json").write_text(
        json.dumps(service_catalog(graph, dependency_catalog), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if descriptions.is_file():
        shutil.copy2(descriptions, candidate / "business-description-overrides.json")
    mcp = {
        "name": "sdlc-graph",
        "transport": "stdio",
        "command": "python3",
        "args": [
            ".claude/skills/sdlc-graph/tools/sdlc_graph_mcp.py",
            "--data-dir", OUTPUT_NAME,
        ],
    }
    (candidate / "mcp-server.json").write_text(json.dumps(mcp, indent=2) + "\n", encoding="utf-8")
    roles = {
        "graph.json": "canonical_graph",
        "services.json": "ai_service_catalog",
        "dependencies.json": "runtime_dependency_catalog",
        "business-description-context.json": "ai_enrichment_context",
        "business-description-overrides.json": "applied_business_descriptions",
        "summary.json": "generation_summary",
        "relationship-viewer.html": "interactive_visualization",
        "mcp-server.json": "mcp_launch_configuration",
    }
    artifacts = []
    for path in sorted(item for item in candidate.rglob("*") if item.is_file()):
        relative = path.relative_to(candidate).as_posix()
        artifacts.append({
            "path": relative,
            "role": roles.get(relative, "repository_projection" if relative.startswith("repositories/") else "supporting_artifact"),
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    manifest = {
        "schema_version": graph["schema_version"],
        "canonical_graph": "graph.json",
        "ai_entry_point": "services.json",
        "visualization": "relationship-viewer.html",
        "mcp_configuration": "mcp-server.json",
        "artifacts": artifacts,
    }
    (candidate / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repos", type=Path, default=WORKSPACE / "repos")
    parser.add_argument("--out", type=Path, default=WORKSPACE / OUTPUT_NAME)
    parser.add_argument("--descriptions", type=Path, default=WORKSPACE / "architecture-descriptions.json",
                        help="Optional AI/curated business-description overrides")
    parser.add_argument("--open", action="store_true", help="Open the published viewer in the default browser")
    args = parser.parse_args()
    output = args.out.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".sdlc-graph-", dir=output.parent) as temporary:
        candidate = Path(temporary) / OUTPUT_NAME
        run(sys.executable, TOOLS / "build_graph.py", "--workspace", WORKSPACE, "--repos", args.repos, "--out", candidate,
            "--descriptions", args.descriptions)
        run(sys.executable, TOOLS / "prepare_ai_context.py", candidate / "graph.json", "--output", candidate / "business-description-context.json")
        run(sys.executable, TOOLS / "render_graph.py", candidate / "graph.json", "--output", candidate / "relationship-viewer.html")
        run(sys.executable, TOOLS / "validate_graph.py", candidate / "graph.json", "--workspace", WORKSPACE,
            "--dependencies", candidate / "dependencies.json")
        write_ai_outputs(candidate, args.descriptions.resolve())
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
