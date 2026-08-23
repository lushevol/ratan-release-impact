#!/usr/bin/env python3
"""Small stdio MCP client for the LLM Wiki server used by requirement-impact."""
from __future__ import annotations

import json
import os
import select
import subprocess
from typing import Any


DEFAULT_COMMAND = "/Applications/LLM Wiki.app/Contents/Resources/mcp-server/dist/src/index.js"


class WikiMcp:
    def __init__(self, command: str = DEFAULT_COMMAND):
        self.process = subprocess.Popen(
            ["node", command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        self.next_id = 1
        self._request("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "requirement-impact", "version": "1.0"}})
        self._notify("notifications/initialized")

    def _write(self, message: dict[str, Any]) -> None:
        assert self.process.stdin is not None
        self.process.stdin.write((json.dumps(message, ensure_ascii=True) + "\n").encode())
        self.process.stdin.flush()

    def _read(self) -> dict[str, Any]:
        assert self.process.stdout is not None
        ready, _, _ = select.select([self.process.stdout], [], [], 8)
        if not ready:
            raise TimeoutError("timed out waiting for Wiki MCP response")
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError("Wiki MCP closed stdout")
        return json.loads(line)

    def _request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        request_id = self.next_id
        self.next_id += 1
        self._write({"jsonrpc": "2.0", "id": request_id, "method": method, "params": params})
        response = self._read()
        if "error" in response:
            raise RuntimeError(str(response["error"]))
        return response.get("result", {})

    def _notify(self, method: str) -> None:
        self._write({"jsonrpc": "2.0", "method": method})

    def call(self, name: str, arguments: dict[str, Any]) -> Any:
        result = self._request("tools/call", {"name": name, "arguments": arguments})
        texts = [item.get("text", "") for item in result.get("content", []) if item.get("type") == "text"]
        joined = "\n".join(texts)
        try:
            return json.loads(joined)
        except json.JSONDecodeError:
            return joined

    def close(self) -> None:
        self.process.kill()
        self.process.wait(timeout=2)


def search(query: str, command: str = DEFAULT_COMMAND, project_id: str = "current", top_k: int = 8) -> Any:
    client = WikiMcp(command)
    try:
        return client.call("llm_wiki_search", {"project_id": project_id, "query": query, "top_k": top_k, "include_content": True})
    finally:
        client.close()

