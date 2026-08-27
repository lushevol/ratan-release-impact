#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional, Union

from robot.api import TestSuiteBuilder


EVIDENCE_MODE = "observed_in_test_engine_simulation"
MOCKED_BOUNDARIES = ["authentication", "remote-apis", "database-polling", "kafka"]


class CatalogError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise CatalogError(f"Expected an object in {path}")
    return value


def unique_by(rows: Iterable[dict[str, Any]], key: str, label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value:
            raise CatalogError(f"{label} has no non-empty {key}")
        if value in result:
            raise CatalogError(f"Duplicate {label} {key}: {value}")
        result[value] = row
    return result


def catalog(engine_root: Path) -> dict[str, Any]:
    catalog_root = engine_root / "catalog"
    behaviors_document = load_json(catalog_root / "behaviors.json")
    scenarios_document = load_json(catalog_root / "scenarios.json")
    mappings_document = load_json(catalog_root / "test-mappings.json")
    behaviors = unique_by(behaviors_document.get("behaviors", []), "id", "behavior")
    scenarios = unique_by(scenarios_document.get("scenarios", []), "id", "scenario")
    mappings = unique_by(mappings_document.get("mappings", []), "test_id", "test mapping")
    defaults = mappings_document.get("defaults", {})

    mapping_keys: dict[tuple[str, str], dict[str, Any]] = {}
    for mapping in mappings.values():
        source = mapping.get("source")
        name = mapping.get("test_name")
        key = (source, name)
        if not isinstance(source, str) or not isinstance(name, str):
            raise CatalogError(f"Invalid source or test_name for {mapping['test_id']}")
        if key in mapping_keys:
            raise CatalogError(f"Duplicate test identity: {source}::{name}")
        if mapping.get("behavior_id") not in behaviors:
            raise CatalogError(f"Unknown behavior for {mapping['test_id']}: {mapping.get('behavior_id')}")
        scenario = scenarios.get(mapping.get("scenario_id"))
        if scenario is None:
            raise CatalogError(f"Unknown scenario for {mapping['test_id']}: {mapping.get('scenario_id')}")
        if scenario.get("behavior_id") != mapping.get("behavior_id"):
            raise CatalogError(f"Behavior mismatch for {mapping['test_id']}")
        mapping_keys[key] = {**defaults, **mapping}

    return {
        "behaviors": behaviors,
        "scenarios": scenarios,
        "mappings": mappings,
        "mapping_keys": mapping_keys,
        "mapping_owner": mappings_document.get("mapping_owner", {}),
    }


def relative_source(source: Union[str, Path], engine_root: Path) -> str:
    path = Path(source)
    try:
        return path.resolve().relative_to(engine_root.resolve()).as_posix()
    except ValueError:
        parts = path.parts
        if "suites" in parts:
            return Path(*parts[parts.index("suites") :]).as_posix()
        return path.as_posix()


def suite_tests(engine_root: Path) -> list[dict[str, Any]]:
    root_suite = TestSuiteBuilder().build(str(engine_root / "suites"))
    tests: list[dict[str, Any]] = []

    def visit(suite: Any) -> None:
        for test in suite.tests:
            tests.append(
                {
                    "source": relative_source(test.source, engine_root),
                    "test_name": test.name,
                    "tags": sorted(str(tag) for tag in test.tags),
                }
            )
        for child in suite.suites:
            visit(child)

    visit(root_suite)
    return tests


def validate_catalog(engine_root: Path) -> dict[str, Any]:
    values = catalog(engine_root)
    discovered = suite_tests(engine_root)
    discovered_keys = {(row["source"], row["test_name"]) for row in discovered}
    mapped_keys = set(values["mapping_keys"])
    errors: list[str] = []

    for key in sorted(discovered_keys - mapped_keys):
        errors.append(f"Unmapped Robot test: {key[0]}::{key[1]}")
    for key in sorted(mapped_keys - discovered_keys):
        errors.append(f"Mapping has no Robot test: {key[0]}::{key[1]}")

    for test in discovered:
        mapping = values["mapping_keys"].get((test["source"], test["test_name"]))
        if mapping is None:
            continue
        required_tags = {mapping["behavior_id"], mapping["scenario_id"]}
        missing_tags = required_tags - set(test["tags"])
        if missing_tags:
            errors.append(f"Missing tags for {mapping['test_id']}: {', '.join(sorted(missing_tags))}")

    if errors:
        raise CatalogError("\n".join(errors))

    return {
        "schema_version": 1,
        "status": "valid",
        "behavior_count": len(values["behaviors"]),
        "scenario_count": len(values["scenarios"]),
        "test_mapping_count": len(values["mappings"]),
        "verification_approval": "pending",
    }


def source_fingerprint(engine_root: Path) -> str:
    included = ["catalog", "libraries", "resources", "scripts", "suites", "tools", "pyproject.toml", "uv.lock"]
    files: list[Path] = []
    for item in included:
        path = engine_root / item
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(candidate for candidate in path.rglob("*") if candidate.is_file() and "__pycache__" not in candidate.parts)
    digest = hashlib.sha256()
    for path in sorted(files):
        digest.update(path.relative_to(engine_root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def git_value(engine_root: Path, args: list[str], fallback: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(engine_root.parent), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 and result.stdout.strip() else fallback


def requirement_refs(tags: list[str], documentation: str) -> list[str]:
    references: set[str] = set()
    for tag in tags:
        if tag.upper().startswith("REQ:"):
            references.update(part.strip() for part in tag[4:].split(",") if part.strip())
    for match in re.finditer(r"REQ:\s*([0-9][0-9, ]*)", documentation, re.IGNORECASE):
        references.update(part.strip() for part in match.group(1).split(",") if part.strip())
    return sorted(references)


def robot_tests(output_root: ET.Element, engine_root: Path, mappings: dict[tuple[str, str], dict[str, Any]]) -> list[dict[str, Any]]:
    tests: list[dict[str, Any]] = []

    def visit(suite: ET.Element, parents: tuple[str, ...]) -> None:
        suite_name = suite.attrib.get("name", "")
        suite_path = parents + ((suite_name,) if suite_name else ())
        source = relative_source(suite.attrib.get("source", ""), engine_root)
        for test in suite.findall("test"):
            name = test.attrib.get("name", "")
            mapping = mappings.get((source, name))
            if mapping is None:
                raise CatalogError(f"No catalog mapping for executed test: {source}::{name}")
            status_element = test.find("status")
            status = status_element.attrib.get("status", "UNKNOWN") if status_element is not None else "UNKNOWN"
            elapsed = status_element.attrib.get("elapsed") if status_element is not None else None
            if elapsed is None and status_element is not None:
                elapsed = status_element.attrib.get("elapsedtime")
            tags = sorted(tag.text or "" for tag in test.findall("tag") if tag.text)
            documentation_element = test.find("doc")
            documentation = documentation_element.text if documentation_element is not None and documentation_element.text else ""
            tests.append(
                {
                    "test_id": mapping["test_id"],
                    "test_name": name,
                    "source_path": f"test-engine/{source}",
                    "source_line": int(test.attrib["line"]) if test.attrib.get("line", "").isdigit() else None,
                    "suite": " / ".join(suite_path),
                    "behavior_id": mapping["behavior_id"],
                    "scenario_id": mapping["scenario_id"],
                    "relationship": mapping.get("relationship", "EXERCISES"),
                    "assertion_status": mapping.get("assertion_status", "supported"),
                    "verification_approval": mapping.get("verification_approval", "pending"),
                    "status": status,
                    "elapsed_seconds": float(elapsed) if elapsed else None,
                    "message": (status_element.text or "").strip() if status_element is not None else "",
                    "tags": tags,
                    "requirement_refs": requirement_refs(tags, documentation),
                }
            )
        for child in suite.findall("suite"):
            visit(child, suite_path)

    for suite in output_root.findall("suite"):
        visit(suite, ())
    return sorted(tests, key=lambda row: row["test_id"])


def convert_run(args: argparse.Namespace) -> dict[str, Any]:
    engine_root = args.engine_root.resolve()
    values = catalog(engine_root)
    xml_root = ET.parse(args.robot_output).getroot()
    tests = robot_tests(xml_root, engine_root, values["mapping_keys"])
    statuses = Counter(test["status"] for test in tests)
    generated = xml_root.attrib.get("generated") or datetime.now(timezone.utc).isoformat()
    safe_generated = re.sub(r"[^0-9]", "", generated)[:20]
    dirty_paths = [
        "test-engine/catalog",
        "test-engine/libraries",
        "test-engine/resources",
        "test-engine/scripts",
        "test-engine/suites",
        "test-engine/tools",
        "test-engine/pyproject.toml",
        "test-engine/uv.lock",
    ]
    dirty = git_value(engine_root, ["status", "--porcelain", "--", *dirty_paths], "") != ""
    diagnostics: list[dict[str, Any]] = []
    if not tests:
        diagnostics.append(
            {
                "severity": "fatal",
                "code": "NO_TESTS_EXECUTED",
                "detail": "Robot output contains no executed test cases for the selected scope.",
                "analysis_can_continue": False,
            }
        )
    elif statuses.get("FAIL", 0):
        diagnostics.append(
            {
                "severity": "error",
                "code": "SIMULATION_TEST_FAILURES",
                "detail": f"{statuses['FAIL']} simulation test case(s) failed.",
                "analysis_can_continue": True,
            }
        )
    elif args.return_code != 0:
        diagnostics.append(
            {
                "severity": "fatal",
                "code": "ROBOT_EXECUTION_ERROR",
                "detail": f"Robot exited with code {args.return_code} without a test assertion failure.",
                "analysis_can_continue": False,
            }
        )
    pending = sum(1 for test in tests if test["verification_approval"] != "approved")
    if pending:
        diagnostics.append(
            {
                "severity": "warning",
                "code": "BUSINESS_VERIFICATION_MAPPING_PENDING",
                "detail": f"{pending} executed test mappings remain EXERCISES until the POC owner approves VERIFIES.",
                "analysis_can_continue": True,
            }
        )
    diagnostics.append(
        {
            "severity": "warning",
            "code": "SIMULATED_EXTERNAL_BOUNDARIES",
            "detail": "Authentication, remote APIs, database polling, and Kafka are mocked.",
            "analysis_can_continue": True,
        }
    )
    return {
        "schema_version": 1,
        "kind": "test-engine-run",
        "run_id": f"test-engine:{args.change_id}:{args.phase}:{safe_generated}",
        "change_id": args.change_id,
        "phase": args.phase,
        "domain": args.domain,
        "evidence_mode": EVIDENCE_MODE,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "robot": {
            "generator": xml_root.attrib.get("generator", "unknown"),
            "generated_at": generated,
            "return_code": args.return_code,
        },
        "engine_baseline": {
            "repository": "ratan-release-impact",
            "commit": git_value(engine_root, ["rev-parse", "HEAD"], "unknown"),
            "working_tree_dirty": dirty,
            "source_fingerprint_sha256": source_fingerprint(engine_root),
        },
        "scope": {
            "domains": [args.domain] if args.domain != "all" else ["ccil", "rebook"],
            "mocked_boundaries": MOCKED_BOUNDARIES,
            "production_code_executed": False,
        },
        "summary": {
            "total": len(tests),
            "passed": statuses.get("PASS", 0),
            "failed": statuses.get("FAIL", 0),
            "skipped": statuses.get("SKIP", 0),
            "other": len(tests) - statuses.get("PASS", 0) - statuses.get("FAIL", 0) - statuses.get("SKIP", 0),
        },
        "mapping_owner": values["mapping_owner"],
        "tests": tests,
        "diagnostics": diagnostics,
    }


def comparison_classification(before: Optional[dict[str, Any]], after: Optional[dict[str, Any]]) -> str:
    if before is None:
        return "target_observed" if after and after["status"] == "PASS" else "target_not_observed"
    if after is None:
        return "missing_after"
    pair = (before["status"], after["status"])
    if pair == ("PASS", "PASS"):
        return "preserved_behavior"
    if pair[0] == "PASS" and pair[1] != "PASS":
        return "candidate_simulation_regression"
    if pair[0] != "PASS" and pair[1] == "PASS":
        return "baseline_recovered"
    if pair[0] == "FAIL" and pair[1] == "FAIL":
        return "persistent_failure"
    return "inconclusive"


def markdown_comparison(comparison: dict[str, Any]) -> str:
    summary = comparison["summary"]
    lines = [
        "## Test-engine simulation evidence",
        "",
        f"- Change: `{comparison['change_id']}`",
        f"- Simulation verdict: **{comparison['simulation_verdict']}**",
        f"- Production implementation proof: **{comparison['production_proof_verdict']}**",
        f"- Evidence mode: `{comparison['evidence_mode']}`",
        f"- Compared tests: {summary['total']}",
        f"- Simulation source changed: {'yes' if comparison['engine_changed'] else 'no'}",
        "- Mocked boundaries: authentication, remote APIs, database polling, Kafka",
        "",
        "A passing comparison demonstrates consistency in the local simulation. It does not execute or prove the production implementation.",
        "",
        "| Test | Scenario | Before | After | Classification |",
        "|---|---|---:|---:|---|",
    ]
    for row in comparison["tests"]:
        name = row["test_name"].replace("|", "\\|")
        lines.append(
            f"| `{name}` | `{row['scenario_id']}` | {row['before_status']} | {row['after_status']} | `{row['classification']}` |"
        )
    lines.extend(
        [
            "",
            "### Evidence limitation",
            "",
            "The result is `NOT_PROVEN` for production behavior because this POC uses local Python simulation backends and mocks all external integrations. Production conformance requires executable evidence from the changed implementation.",
            "",
        ]
    )
    return "\n".join(lines)


def compare_runs(before_path: Path, after_path: Path) -> dict[str, Any]:
    before_run = load_json(before_path)
    after_run = load_json(after_path)
    if before_run.get("change_id") != after_run.get("change_id"):
        raise CatalogError("Before and after runs have different change_id values")
    if before_run.get("phase") != "before" or after_run.get("phase") != "after":
        raise CatalogError("Comparison requires a before run and an after run")
    before = {test["test_id"]: test for test in before_run.get("tests", [])}
    after = {test["test_id"]: test for test in after_run.get("tests", [])}
    rows: list[dict[str, Any]] = []
    for test_id in sorted(set(before) | set(after)):
        before_test = before.get(test_id)
        after_test = after.get(test_id)
        representative = after_test or before_test
        rows.append(
            {
                "test_id": test_id,
                "test_name": representative["test_name"],
                "behavior_id": representative["behavior_id"],
                "scenario_id": representative["scenario_id"],
                "before_status": before_test["status"] if before_test else "NOT_PRESENT",
                "after_status": after_test["status"] if after_test else "NOT_PRESENT",
                "classification": comparison_classification(before_test, after_test),
            }
        )
    counts = Counter(row["classification"] for row in rows)
    blocking = {"candidate_simulation_regression", "target_not_observed", "missing_after"}
    if any(counts[name] for name in blocking):
        simulation_verdict = "FAIL"
    elif counts["persistent_failure"] or counts["inconclusive"]:
        simulation_verdict = "INCONCLUSIVE"
    else:
        simulation_verdict = "PASS"
    before_fingerprint = before_run.get("engine_baseline", {}).get("source_fingerprint_sha256")
    after_fingerprint = after_run.get("engine_baseline", {}).get("source_fingerprint_sha256")
    engine_changed = before_fingerprint != after_fingerprint
    return {
        "schema_version": 1,
        "kind": "test-engine-comparison",
        "comparison_id": f"test-engine-comparison:{before_run['change_id']}",
        "change_id": before_run["change_id"],
        "evidence_mode": EVIDENCE_MODE,
        "simulation_verdict": simulation_verdict,
        "production_proof_verdict": "NOT_PROVEN",
        "before_run_id": before_run.get("run_id"),
        "after_run_id": after_run.get("run_id"),
        "engine_changed": engine_changed,
        "before_source_fingerprint_sha256": before_fingerprint,
        "after_source_fingerprint_sha256": after_fingerprint,
        "summary": {"total": len(rows), **dict(sorted(counts.items()))},
        "tests": rows,
        "diagnostics": [
            {
                "severity": "info",
                "code": "SIMULATION_SOURCE_CHANGED" if engine_changed else "SIMULATION_SOURCE_UNCHANGED",
                "detail": "The executable simulation source changed between phases." if engine_changed else "The executable simulation source was identical in both phases.",
                "analysis_can_continue": True,
            },
            {
                "severity": "warning",
                "code": "PRODUCTION_IMPLEMENTATION_NOT_EXECUTED",
                "detail": "The comparison executes the local simulation, not production repository code.",
                "analysis_can_continue": True,
            }
        ],
    }


def parser() -> argparse.ArgumentParser:
    root = Path(__file__).resolve().parents[1]
    command = argparse.ArgumentParser(description="Validate and produce SDLC evidence from the local test engine")
    command.set_defaults(engine_root=root)
    subcommands = command.add_subparsers(dest="command", required=True)

    validate = subcommands.add_parser("validate", help="Validate catalogs against Robot suites")
    validate.add_argument("--engine-root", type=Path, default=root)

    convert = subcommands.add_parser("convert", help="Convert Robot output.xml into portable run evidence")
    convert.add_argument("--engine-root", type=Path, default=root)
    convert.add_argument("--robot-output", type=Path, required=True)
    convert.add_argument("--output", type=Path, required=True)
    convert.add_argument("--change-id", required=True)
    convert.add_argument("--phase", choices=["before", "after"], required=True)
    convert.add_argument("--domain", choices=["all", "ccil", "rebook"], default="all")
    convert.add_argument("--return-code", type=int, required=True)

    compare = subcommands.add_parser("compare", help="Compare before and after run evidence")
    compare.add_argument("--before", type=Path, required=True)
    compare.add_argument("--after", type=Path, required=True)
    compare.add_argument("--output", type=Path, required=True)
    compare.add_argument("--markdown-output", type=Path, required=True)
    return command


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "validate":
            result = validate_catalog(args.engine_root.resolve())
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0
        if args.command == "convert":
            result = convert_run(args)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(f"Wrote {args.output}")
            return 0
        if args.command == "compare":
            result = compare_runs(args.before, args.after)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            args.markdown_output.write_text(markdown_comparison(result), encoding="utf-8")
            print(f"Wrote {args.output}")
            print(f"Wrote {args.markdown_output}")
            return 0
    except (CatalogError, ET.ParseError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
