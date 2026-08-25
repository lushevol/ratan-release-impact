#!/usr/bin/env python3
"""Analyze SDLC graph impact from a requirement or changed source paths."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from graph_query import load_seed_config, seed_changes, seed_requirement, traverse


def changed_from_git(workspace: Path, base_ref: str) -> list[str]:
    result = subprocess.check_output(["git", "diff", "--name-only", base_ref, "--"], cwd=workspace, text=True)
    return sorted({line.strip() for line in result.splitlines() if line.strip()})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=Path("sdlc-graph-output/graph.json"))
    parser.add_argument("--config", type=Path, default=Path("sdlc-graph-config.json"), help="Requirement seeding policy JSON")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--requirement")
    group.add_argument("--changed-file", action="append", dest="changed_files")
    group.add_argument("--base-ref")
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    graph = json.loads(args.graph.read_text(encoding="utf-8"))
    if args.requirement:
        mode, input_value = "REQUIREMENT", args.requirement
        config = load_seed_config(str(args.config)) if args.config.is_file() else load_seed_config()
        seeds = seed_requirement(graph["nodes"], args.requirement, config=config)
    else:
        changed = args.changed_files or changed_from_git(args.graph.resolve().parents[1], args.base_ref)
        mode, input_value = "CODE_CHANGE", changed
        seeds = seed_changes(graph["nodes"], changed)
    result = {"schema_version": graph["schema_version"], "mode": mode, "input": input_value,
              **traverse(graph, seeds, args.depth)}
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0 if seeds else 3


if __name__ == "__main__":
    raise SystemExit(main())
