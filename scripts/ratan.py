#!/usr/bin/env python3
"""AI-friendly maintenance commands for the Ratan release-impact harness.

The CLI intentionally uses only the Python standard library. It is safe to run
from a fresh checkout before the project's virtual environment exists.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "repos" / "manifest.json"
KB_DIR = ROOT / "knowledge-base"


def command_path(command: str) -> str | None:
    candidate = Path(command)
    if candidate.is_absolute() or "/" in command:
        path = candidate if candidate.is_absolute() else ROOT / candidate
        return str(path) if path.exists() else None
    return shutil.which(command)


def display_command(parts: Iterable[object]) -> str:
    return " ".join(shlex.quote(str(part)) for part in parts)


def run_command(parts: list[object], *, cwd: Path = ROOT, capture: bool = False,
                timeout: int | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    command = [str(part) for part in parts]
    print(f"+ {display_command(command)}", flush=True)
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=capture,
        timeout=timeout,
        check=check,
        env=os.environ.copy(),
    )


def load_manifest(path: Path = MANIFEST) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise SystemExit(f"repository manifest not found: {path}") from error
    except json.JSONDecodeError as error:
        raise SystemExit(f"invalid repository manifest {path}: {error}") from error
    if not isinstance(payload, dict) or not isinstance(payload.get("repositories"), list):
        raise SystemExit("repository manifest must contain a repositories array")
    names: set[str] = set()
    for entry in payload["repositories"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
            raise SystemExit("each manifest repository needs a name")
        name = entry["name"]
        if name in names:
            raise SystemExit(f"duplicate repository in manifest: {name}")
        names.add(name)
        relative = entry.get("path", f"repos/{name}")
        relative_path = Path(relative) if isinstance(relative, str) else Path("/")
        if (not isinstance(relative, str) or relative_path.is_absolute()
                or relative_path.parts[:1] != ("repos",) or len(relative_path.parts) != 2):
            raise SystemExit(f"manifest path must be relative: {relative}")
    return payload


def selected_entries(payload: dict[str, Any], only: list[str] | None) -> list[dict[str, Any]]:
    entries = [entry for entry in payload["repositories"] if isinstance(entry, dict)]
    if not only:
        return entries
    wanted = set(only)
    known = {entry["name"] for entry in entries}
    unknown = sorted(wanted - known)
    if unknown:
        raise SystemExit(f"repositories not in manifest: {', '.join(unknown)}")
    return [entry for entry in entries if entry["name"] in wanted]


def entry_path(entry: dict[str, Any]) -> Path:
    return ROOT / str(entry.get("path", f"repos/{entry['name']}"))


def entry_url(entry: dict[str, Any], payload: dict[str, Any]) -> str | None:
    value = entry.get("url")
    if isinstance(value, str) and value.strip():
        return value.strip()
    template = payload.get("remote_template")
    if not isinstance(template, str) or not template.strip():
        return None
    org = os.environ.get("RATAN_GIT_ORG", "").strip()
    if "${RATAN_GIT_ORG}" in template and not org:
        return None
    return template.replace("${RATAN_GIT_ORG}", org).format(name=entry["name"])


def git_value(path: Path, *args: str) -> str | None:
    try:
        value = subprocess.check_output(
            ["git", "-C", str(path), *args], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    return value or None


def repo_status(entry: dict[str, Any]) -> dict[str, Any]:
    path = entry_path(entry)
    git_dir = path / ".git"
    index_dir = path / ".gitnexus"
    status: dict[str, Any] = {
        "name": entry["name"],
        "path": str(path.relative_to(ROOT)),
        "required": bool(entry.get("required", True)),
        "present": path.is_dir(),
        "git": git_dir.is_dir() or git_dir.is_file(),
        "indexed": index_dir.is_dir(),
        "branch": git_value(path, "branch", "--show-current") if git_dir.exists() else None,
        "commit": git_value(path, "rev-parse", "HEAD") if git_dir.exists() else None,
        "remote": git_value(path, "remote", "get-url", "origin") if git_dir.exists() else None,
        "dirty": None,
    }
    if status["git"]:
        status["dirty"] = bool(git_value(path, "status", "--porcelain"))
        if index_dir.exists():
            status["index_updated"] = datetime.fromtimestamp(
                index_dir.stat().st_mtime, tz=timezone.utc
            ).isoformat()
    return status


def output(payload: Any, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    elif isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                print("  ".join(f"{key}={value}" for key, value in item.items()))
            else:
                print(item)
    elif isinstance(payload, dict):
        for key, value in payload.items():
            print(f"{key}: {value}")
    else:
        print(payload)


def cmd_deps(args: argparse.Namespace) -> int:
    required = ["git", args.python, "node", "npm", "uv"]
    optional = ["qmd", "openkb", "gitnexus"]
    checks: list[dict[str, Any]] = []
    for name in required + optional:
        path = command_path(name)
        item: dict[str, Any] = {"name": name, "required": name in required, "available": path is not None, "path": path}
        if path:
            try:
                version = subprocess.run([path, "--version"], text=True, capture_output=True, timeout=5, check=False)
                item["version"] = (version.stdout or version.stderr).strip().splitlines()[0] if (version.stdout or version.stderr).strip() else None
            except (OSError, subprocess.TimeoutExpired):
                item["version"] = None
        checks.append(item)
    checks.extend([
        {"name": "root_venv", "required": True, "available": (ROOT / ".venv/bin/python").is_file(), "path": str(ROOT / ".venv/bin/python")},
        {"name": "test_engine_venv", "required": False, "available": (ROOT / "test-engine/.venv/bin/python").is_file(), "path": str(ROOT / "test-engine/.venv/bin/python")},
        {"name": "qmd_config", "required": True, "available": (KB_DIR / ".qmd/index.yml").is_file(), "path": str(KB_DIR / ".qmd/index.yml")},
        {"name": "qmd_database", "required": True, "available": (KB_DIR / ".qmd/index.sqlite").is_file(), "path": str(KB_DIR / ".qmd/index.sqlite")},
        {"name": "mcp_config", "required": True, "available": (ROOT / ".mcp.json").is_file(), "path": str(ROOT / ".mcp.json")},
    ])
    missing = [item["name"] for item in checks if item["required"] and not item["available"]]
    payload = {"ok": not missing, "missing": missing, "checks": checks}
    output(payload, args.json)
    return 0 if not missing or not args.strict else 1


def cmd_repo_clone(args: argparse.Namespace) -> int:
    payload = load_manifest(Path(args.manifest).resolve() if args.manifest else MANIFEST)
    results: list[dict[str, Any]] = []
    failed = False
    for entry in selected_entries(payload, args.only):
        path = entry_path(entry)
        url = entry_url(entry, payload)
        item = {"name": entry["name"], "path": str(path.relative_to(ROOT)), "url": url, "action": "skip"}
        if (path / ".git").exists():
            if args.update:
                if not url:
                    item.update(action="error", reason="manifest has no URL; set an explicit url or remote_template")
                    failed = True
                else:
                    run_command(["git", "-C", path, "pull", "--ff-only"], check=False)
                    item["action"] = "updated"
            else:
                item["reason"] = "already cloned"
        elif path.exists():
            item.update(action="error", reason="path exists but is not a git checkout")
            failed = True
        elif not url:
            item.update(action="error", reason="manifest has no URL; set an explicit url or remote_template")
            failed = True
        elif args.dry_run:
            item["action"] = "would_clone"
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            result = run_command(["git", "clone", "--branch", entry.get("branch", "main"), url, path], check=False)
            item["action"] = "cloned" if result.returncode == 0 else "error"
            if result.returncode:
                failed = True
        results.append(item)
    output(results, args.json)
    return 1 if failed else 0


def cmd_repo_index(args: argparse.Namespace) -> int:
    payload = load_manifest(Path(args.manifest).resolve() if args.manifest else MANIFEST)
    gitnexus = command_path("gitnexus")
    if not gitnexus:
        print("gitnexus is not installed; run ./scripts/setup.sh or install it globally", file=sys.stderr)
        return 1
    failed = False
    for entry in selected_entries(payload, args.only):
        path = entry_path(entry)
        if not (path / ".git").exists():
            print(f"skip {entry['name']}: not cloned", file=sys.stderr)
            continue
        command: list[object] = [gitnexus, "analyze"]
        if args.force:
            command.append("--force")
        if args.pdg:
            command.append("--pdg")
        if args.embeddings:
            command.append("--embeddings")
        result = run_command(command, cwd=path, check=False)
        failed = failed or result.returncode != 0
    return 1 if failed else 0


def cmd_repo_install(args: argparse.Namespace) -> int:
    payload = load_manifest(Path(args.manifest).resolve() if args.manifest else MANIFEST)
    failed = False
    for entry in selected_entries(payload, args.only):
        path = entry_path(entry)
        if not (path / ".git").exists():
            print(f"skip {entry['name']}: not cloned", file=sys.stderr)
            continue
        kind = str(entry.get("kind", "")).lower()
        if kind == "node" or (path / "package.json").is_file():
            executable = command_path("npm")
            if not executable:
                print("npm is not installed", file=sys.stderr)
                failed = True
                continue
            install_mode = "ci" if (path / "package-lock.json").is_file() else "install"
            command: list[object] = [executable, install_mode]
        elif kind == "maven" or (path / "pom.xml").is_file():
            wrapper = path / "mvnw"
            executable = str(wrapper) if wrapper.is_file() and os.access(wrapper, os.X_OK) else command_path("mvn")
            if not executable:
                print(f"{entry['name']}: Maven is not installed and no mvnw wrapper exists", file=sys.stderr)
                failed = True
                continue
            command = [executable, "-DskipTests", "dependency:go-offline"]
        else:
            print(f"skip {entry['name']}: unsupported dependency descriptor", file=sys.stderr)
            continue
        if args.dry_run:
            print(f"would install {entry['name']}: {display_command(command)}")
            continue
        result = run_command(command, cwd=path, check=False)
        failed = failed or result.returncode != 0
    return 1 if failed else 0


def cmd_repo_status(args: argparse.Namespace) -> int:
    payload = load_manifest(Path(args.manifest).resolve() if args.manifest else MANIFEST)
    statuses = [repo_status(entry) for entry in selected_entries(payload, args.only)]
    missing_required = [item["name"] for item in statuses if item["required"] and not item["present"]]
    output({"ok": not missing_required, "missing_required": missing_required, "repositories": statuses}, args.json)
    return 0 if not missing_required else 1


def run_openkb(operation: str, values: list[str], *, check: bool = True) -> int:
    executable = command_path(os.environ.get("OPENKB_BIN", "openkb"))
    if not executable:
        print("openkb is not installed; run ./scripts/setup.sh", file=sys.stderr)
        return 1
    result = run_command([executable, "--kb-dir", KB_DIR, operation, *values], check=False)
    if check and result.returncode:
        return result.returncode
    return result.returncode


def refresh_qmd() -> int:
    executable = command_path(os.environ.get("QMD_BIN", "qmd"))
    if not executable:
        print("qmd is not installed; wiki changed but the search index was not rebuilt", file=sys.stderr)
        return 1
    return run_command([executable, "update"], cwd=KB_DIR, check=False).returncode


def cmd_kb(args: argparse.Namespace) -> int:
    operation = args.operation
    if operation == "status":
        raw = list((KB_DIR / "raw").rglob("*")) if (KB_DIR / "raw").is_dir() else []
        wiki = list((KB_DIR / "wiki").rglob("*.md")) if (KB_DIR / "wiki").is_dir() else []
        payload = {"kb_dir": str(KB_DIR), "raw_documents": sum(item.is_file() for item in raw), "wiki_pages": len(wiki),
                   "qmd_configured": (KB_DIR / ".qmd/index.yml").is_file(), "qmd_ready": (KB_DIR / ".qmd/index.sqlite").is_file()}
        output(payload, args.json)
        return 0 if payload["qmd_ready"] else 1
    if operation == "lint":
        values = ["--fix"] if args.fix else []
        return run_openkb("lint", values)
    if operation == "compile":
        code = run_openkb("recompile", ["--all", "--yes"])
        if code:
            return code
        return 0 if args.no_qmd else refresh_qmd()
    if operation in {"add", "update"}:
        source = Path(args.path).expanduser()
        if not source.is_absolute():
            source = (ROOT / source).resolve()
        if not source.exists():
            print(f"source does not exist: {source}", file=sys.stderr)
            return 1
        code = run_openkb("add", [source])
        if code:
            return code
        return 0 if args.no_qmd else refresh_qmd()
    if operation == "delete":
        code = run_openkb("remove", ["-y", args.identifier])
        if code:
            return code
        return 0 if args.no_qmd else refresh_qmd()
    raise SystemExit(f"unsupported knowledge-base operation: {operation}")


def load_mcp_config() -> dict[str, Any]:
    try:
        payload = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid .mcp.json: {error}") from error
    servers = payload.get("mcpServers") if isinstance(payload, dict) else None
    if not isinstance(servers, dict):
        raise SystemExit(".mcp.json must contain an mcpServers object")
    return servers


def parse_mcp_output(raw: bytes) -> list[dict[str, Any]]:
    """Parse newline JSON and MCP Content-Length framed responses."""
    responses: list[dict[str, Any]] = []
    cursor = 0
    while cursor < len(raw):
        line_end = raw.find(b"\n", cursor)
        if line_end < 0:
            break
        line = raw[cursor:line_end].strip()
        cursor = line_end + 1
        if line.lower().startswith(b"content-length:"):
            try:
                length = int(line.split(b":", 1)[1].strip())
            except (IndexError, ValueError):
                continue
            while cursor < len(raw):
                header_end = raw.find(b"\n", cursor)
                if header_end < 0:
                    return responses
                header = raw[cursor:header_end].strip()
                cursor = header_end + 1
                if not header:
                    break
            body = raw[cursor:cursor + length]
            cursor += length
            try:
                value = json.loads(body)
            except json.JSONDecodeError:
                continue
        else:
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
        if isinstance(value, dict):
            responses.append(value)
    return responses


def probe_mcp(name: str, config: dict[str, Any], timeout: int) -> dict[str, Any]:
    command = config.get("command")
    args = config.get("args", [])
    if not isinstance(command, str) or not isinstance(args, list):
        return {"server": name, "ok": False, "error": "command/args are invalid"}
    executable = command_path(command)
    if not executable:
        return {"server": name, "ok": False, "error": f"command not found: {command}"}
    command_line = [executable, *[str(value) for value in args]]
    requests = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "ratan-status", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
    ]
    try:
        probe_env = os.environ.copy()
        # Health probes must not wait on optional Langfuse export retries.
        probe_env["LANGFUSE_PUBLIC_KEY"] = ""
        probe_env["LANGFUSE_SECRET_KEY"] = ""
        completed = subprocess.run(
            command_line,
            cwd=ROOT,
            input=("\n".join(json.dumps(item) for item in requests) + "\n").encode(),
            capture_output=True,
            timeout=timeout,
            check=False,
            env=probe_env,
        )
    except subprocess.TimeoutExpired:
        return {"server": name, "ok": False, "error": f"timed out after {timeout}s", "command": display_command(command_line)}
    responses = parse_mcp_output(completed.stdout)
    listed = next((item for item in responses if item.get("id") == 2 and isinstance(item.get("result"), dict)), None)
    error = next((item.get("error") for item in responses if item.get("id") == 2 and item.get("error")), None)
    tools = listed["result"].get("tools", []) if listed else []
    # A proxy may return its child's non-zero shutdown code after receiving EOF
    # even though initialize/tools-list completed successfully. The protocol
    # response is the health signal; retain the process code for diagnostics.
    ok = listed is not None
    result: dict[str, Any] = {"server": name, "ok": ok, "command": display_command(command_line), "tool_count": len(tools) if isinstance(tools, list) else 0, "exit_code": completed.returncode}
    if error:
        result["error"] = error
    if completed.returncode and completed.stderr.strip():
        result["stderr"] = completed.stderr.decode(errors="replace").strip()[-1000:]
    if not ok and "error" not in result:
        result["error"] = "tools/list did not return a valid response"
    return result


def cmd_mcp_status(args: argparse.Namespace) -> int:
    servers = load_mcp_config()
    names = args.server or sorted(servers)
    unknown = sorted(set(names) - set(servers))
    if unknown:
        print(f"MCP servers not configured: {', '.join(unknown)}", file=sys.stderr)
        return 1
    results = [probe_mcp(name, servers[name], args.timeout) for name in names]
    output({"ok": all(item["ok"] for item in results), "servers": results}, args.json)
    return 0 if all(item["ok"] for item in results) else 1


def cmd_graph(args: argparse.Namespace) -> int:
    tool = ROOT / ".claude/skills/sdlc-graph/tools/generate_all_graphs.py"
    command: list[object] = [sys.executable, tool, "--descriptions", ROOT / "config/architecture-descriptions.json"]
    if args.open:
        command.append("--open")
    return run_command(command, check=False).returncode


def cmd_tests(args: argparse.Namespace) -> int:
    python = ROOT / ".venv/bin/python"
    executable = str(python) if python.is_file() else sys.executable
    command: list[object] = [executable, "-m", "unittest", "discover", "-s", ROOT / "tests", "-v"]
    return run_command(command, check=False).returncode


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="ratan", description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    deps = sub.add_parser("deps", help="check local toolchain, indexes, and MCP configuration")
    deps.add_argument("--python", default="python3")
    deps.add_argument("--json", action="store_true")
    deps.add_argument("--strict", action="store_true", help="return failure when required checks are missing")
    deps.set_defaults(func=cmd_deps)

    repos = sub.add_parser("repos", help="clone, index, or inspect business repositories")
    repo_sub = repos.add_subparsers(dest="operation", required=True)
    for name, help_text in [("clone", "clone repositories from manifest"), ("install", "install Node/Maven dependencies in each clone"), ("index", "run GitNexus analysis in each clone"), ("status", "show clone and index status")]:
        item = repo_sub.add_parser(name, help=help_text)
        item.add_argument("--manifest", type=Path)
        item.add_argument("--only", action="append", help="limit to one repository; repeatable")
        item.add_argument("--json", action="store_true")
        item.set_defaults(func={"clone": cmd_repo_clone, "install": cmd_repo_install, "index": cmd_repo_index, "status": cmd_repo_status}[name])
    repo_sub.choices["clone"].add_argument("--dry-run", action="store_true")
    repo_sub.choices["clone"].add_argument("--update", action="store_true", help="pull existing clones fast-forward only")
    repo_sub.choices["install"].add_argument("--dry-run", action="store_true")
    repo_sub.choices["index"].add_argument("--force", action="store_true")
    repo_sub.choices["index"].add_argument("--pdg", action="store_true")
    repo_sub.choices["index"].add_argument("--embeddings", action="store_true")

    kb = sub.add_parser("kb", help="maintain raw OpenKB documents and compiled wiki")
    kb_sub = kb.add_subparsers(dest="operation", required=True)
    status = kb_sub.add_parser("status")
    status.add_argument("--json", action="store_true")
    status.set_defaults(func=cmd_kb)
    lint = kb_sub.add_parser("lint")
    lint.add_argument("--fix", action="store_true")
    lint.set_defaults(func=cmd_kb)
    compile_parser = kb_sub.add_parser("compile")
    compile_parser.add_argument("--no-qmd", action="store_true")
    compile_parser.set_defaults(func=cmd_kb)
    for name in ("add", "update"):
        item = kb_sub.add_parser(name)
        item.add_argument("path", help="raw document or directory")
        item.add_argument("--no-qmd", action="store_true")
        item.set_defaults(func=cmd_kb)
    delete = kb_sub.add_parser("delete")
    delete.add_argument("identifier", help="OpenKB filename, slug, or unique substring")
    delete.add_argument("--no-qmd", action="store_true")
    delete.set_defaults(func=cmd_kb)

    mcp = sub.add_parser("mcp", help="probe configured MCP servers with initialize/tools-list")
    mcp_sub = mcp.add_subparsers(dest="operation", required=True)
    mcp_status = mcp_sub.add_parser("status")
    mcp_status.add_argument("--server", action="append", help="limit to one configured server; repeatable")
    mcp_status.add_argument("--timeout", type=int, default=15)
    mcp_status.add_argument("--json", action="store_true")
    mcp_status.set_defaults(func=cmd_mcp_status)

    graph = sub.add_parser("graph", help="generate the SDLC graph bundle")
    graph_sub = graph.add_subparsers(dest="operation", required=True)
    graph_build = graph_sub.add_parser("build")
    graph_build.add_argument("--open", action="store_true")
    graph_build.set_defaults(func=cmd_graph)

    tests = sub.add_parser("test", help="run root unittest suite")
    tests.set_defaults(func=cmd_tests)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return int(args.func(args))
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except (OSError, subprocess.SubprocessError) as error:
        print(f"ratan: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
