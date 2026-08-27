#!/usr/bin/env python3
"""Trace MCP JSON-RPC traffic while transparently proxying a child server."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import BinaryIO

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "sdlc-graph" / "tools"))
from langfuse_trace import impact_trace


def read_frame(stream: BinaryIO) -> tuple[bytes, dict]:
    first = stream.readline()
    if not first:
        raise EOFError
    if first.lower().startswith(b"content-length:"):
        length = int(first.split(b":", 1)[1].strip())
        headers = [first]
        while True:
            header = stream.readline()
            headers.append(header)
            if header in {b"\n", b"\r\n", b""}:
                break
        body = stream.read(length)
        return b"".join(headers) + body, json.loads(body)
    return first, json.loads(first)


def operation(request: dict) -> tuple[str, str]:
    params = request.get("params") or {}
    method = request.get("method", "notification")
    tool = params.get("name") if method == "tools/call" else None
    return method, str(tool or method).replace("/", "-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", required=True)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a child MCP command is required after --")
    child = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=sys.stderr)
    assert child.stdin and child.stdout
    try:
        while True:
            try:
                request_frame, request = read_frame(sys.stdin.buffer)
            except EOFError:
                break
            method, operation_name = operation(request)
            metadata = {
                "mcp_server": args.server,
                "rpc_method": method,
                "observation_type": "tool" if method == "tools/call" else "span",
            }
            with impact_trace(f"mcp.{args.server}.{operation_name}", request.get("params", {}), metadata) as trace:
                child.stdin.write(request_frame)
                child.stdin.flush()
                response_frame, response = read_frame(child.stdout)
                sys.stdout.buffer.write(response_frame)
                sys.stdout.buffer.flush()
                trace.update(
                    {"response": "error" if "error" in response else "ok", "request_id": request.get("id")},
                    output={"jsonrpc": response.get("jsonrpc"), "error": response.get("error", {}).get("code") if isinstance(response.get("error"), dict) else None},
                )
    finally:
        if child.poll() is None:
            child.terminate()
        child.wait(timeout=5)
    return child.returncode or 0


if __name__ == "__main__":
    raise SystemExit(main())
