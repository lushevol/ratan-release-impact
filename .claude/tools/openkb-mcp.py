#!/usr/bin/env python3
"""Expose the repository's OpenKB knowledge base over MCP stdio."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Iterable


TOKEN_RE = re.compile(r"[A-Za-z0-9]+")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
MAX_CONTENT_CHARS = 20_000


def tokens(value: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(value)]


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if separator and key.strip() in {"title", "type", "description"}:
            values[key.strip()] = value.strip().strip('"\'')
    return values


def _title(text: str, fallback: str) -> str:
    metadata = _frontmatter(text)
    if metadata.get("title"):
        return metadata["title"]
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _snippet(text: str, terms: list[str], phrase: str, width: int = 700) -> str:
    searchable = text.lower()
    positions = [searchable.find(phrase)] if phrase else []
    positions.extend(searchable.find(term) for term in terms)
    positions = [position for position in positions if position >= 0]
    center = min(positions) if positions else 0
    start = max(0, center - width // 3)
    end = min(len(text), start + width)
    excerpt = text[start:end]
    excerpt = WIKILINK_RE.sub(lambda match: match.group(2) or match.group(1), excerpt)
    excerpt = re.sub(r"\s+", " ", excerpt).strip()
    if start:
        excerpt = "..." + excerpt
    if end < len(text):
        excerpt += "..."
    return excerpt


@dataclass(frozen=True)
class WikiPage:
    path: str
    title: str
    page_type: str | None
    text: str
    term_counts: Counter[str]
    title_counts: Counter[str]
    path_counts: Counter[str]
    links: tuple[str, ...]


class WikiIndex:
    def __init__(self, kb_dir: Path):
        self.kb_dir = kb_dir.resolve()
        self.wiki_dir = (self.kb_dir / "wiki").resolve()
        if not self.wiki_dir.is_dir():
            raise ValueError(f"Missing OpenKB wiki directory: {self.wiki_dir}")
        self._signature: tuple[int, int, int] | None = None
        self._pages: tuple[WikiPage, ...] = ()
        self._by_path: dict[str, WikiPage] = {}
        self._incoming: dict[str, tuple[str, ...]] = {}
        self._outgoing: dict[str, tuple[str, ...]] = {}

    def _markdown_files(self) -> list[Path]:
        return sorted(self.wiki_dir.rglob("*.md"))

    def _filesystem_signature(self, files: Iterable[Path]) -> tuple[int, int, int]:
        count = 0
        total_size = 0
        newest_mtime = 0
        for path in files:
            stat = path.stat()
            count += 1
            total_size += stat.st_size
            newest_mtime = max(newest_mtime, stat.st_mtime_ns)
        return count, total_size, newest_mtime

    def refresh(self, force: bool = False) -> None:
        files = self._markdown_files()
        signature = self._filesystem_signature(files)
        if not force and signature == self._signature:
            return

        pages: list[WikiPage] = []
        for path in files:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
            relative = path.relative_to(self.wiki_dir).as_posix()
            title = _title(text, path.stem.replace("-", " ").title())
            metadata = _frontmatter(text)
            pages.append(
                WikiPage(
                    path=f"wiki/{relative}",
                    title=title,
                    page_type=metadata.get("type"),
                    text=text,
                    term_counts=Counter(tokens(text)),
                    title_counts=Counter(tokens(title)),
                    path_counts=Counter(tokens(relative)),
                    links=tuple(match.group(1).strip() for match in WIKILINK_RE.finditer(text)),
                )
            )

        self._pages = tuple(pages)
        self._by_path = {page.path.lower(): page for page in pages}
        self._build_graph()
        self._signature = signature

    def _build_graph(self) -> None:
        exact: dict[str, str] = {}
        by_stem: dict[str, list[str]] = defaultdict(list)
        for page in self._pages:
            relative = page.path.removeprefix("wiki/").removesuffix(".md")
            exact[relative.lower()] = page.path
            by_stem[Path(relative).name.lower()].append(page.path)

        outgoing: dict[str, list[str]] = defaultdict(list)
        incoming: dict[str, list[str]] = defaultdict(list)
        for page in self._pages:
            for raw_target in page.links:
                target = raw_target.strip().removeprefix("wiki/").removesuffix(".md").lower()
                resolved = exact.get(target)
                if resolved is None and "/" not in target and len(by_stem[target]) == 1:
                    resolved = by_stem[target][0]
                if resolved and resolved not in outgoing[page.path]:
                    outgoing[page.path].append(resolved)
                    incoming[resolved].append(page.path)
        self._outgoing = {key: tuple(value) for key, value in outgoing.items()}
        self._incoming = {key: tuple(value) for key, value in incoming.items()}

    @property
    def pages(self) -> tuple[WikiPage, ...]:
        self.refresh()
        return self._pages

    def status(self) -> dict:
        self.refresh()
        raw_files = sum(1 for path in (self.kb_dir / "raw").rglob("*") if path.is_file())
        return {
            "knowledge_base": str(self.kb_dir),
            "wiki_pages": len(self._pages),
            "raw_documents": raw_files,
            "config": str(self.kb_dir / ".openkb" / "config.yaml"),
        }

    def search(self, query: str, top_k: int = 8, include_content: bool = False) -> dict:
        self.refresh()
        query_terms = list(dict.fromkeys(tokens(query)))
        if not query_terms:
            raise ValueError("query must contain at least one letter or number")
        phrase = " ".join(query.lower().split())
        document_count = max(len(self._pages), 1)
        document_frequency = {
            term: sum(1 for page in self._pages if page.term_counts[term])
            for term in query_terms
        }

        ranked: list[tuple[float, WikiPage]] = []
        for page in self._pages:
            score = 0.0
            for term in query_terms:
                frequency = page.term_counts[term]
                if not frequency:
                    continue
                inverse_frequency = math.log((document_count + 1) / (document_frequency[term] + 1)) + 1
                score += inverse_frequency * math.sqrt(min(frequency, 16))
                score += page.title_counts[term] * inverse_frequency * 4
                score += page.path_counts[term] * inverse_frequency * 2
            title_lower = page.title.lower()
            path_lower = page.path.lower()
            text_lower = page.text.lower()
            if phrase and phrase in title_lower:
                score += 24
            elif phrase and phrase in path_lower:
                score += 16
            elif phrase and phrase in text_lower:
                score += 8
            if score > 0:
                ranked.append((score, page))
        ranked.sort(key=lambda item: (-item[0], item[1].path))

        results = []
        for score, page in ranked[:top_k]:
            item = {
                "path": page.path,
                "title": page.title,
                "type": page.page_type,
                "score": round(score, 3),
                "snippet": _snippet(page.text, query_terms, phrase),
            }
            if include_content:
                item["content"] = page.text[:MAX_CONTENT_CHARS]
                item["content_truncated"] = len(page.text) > MAX_CONTENT_CHARS
            results.append(item)
        return {"query": query, "result_count": len(results), "results": results}

    def read(self, requested_path: str) -> dict:
        candidate = requested_path.strip().removeprefix("openkb://")
        candidate = candidate.removeprefix("wiki/")
        if not candidate.endswith(".md"):
            candidate += ".md"
        resolved = (self.wiki_dir / candidate).resolve()
        try:
            resolved.relative_to(self.wiki_dir)
        except ValueError as error:
            raise ValueError("path must remain inside knowledge-base/wiki") from error
        if not resolved.is_file():
            raise ValueError(f"wiki page not found: wiki/{candidate}")
        text = resolved.read_text(encoding="utf-8")
        return {
            "path": f"wiki/{resolved.relative_to(self.wiki_dir).as_posix()}",
            "title": _title(text, resolved.stem),
            "content": text,
        }

    def graph(self, query: str | None = None, limit: int = 50) -> dict:
        self.refresh()
        selected = self._pages
        if query:
            terms = tokens(query)
            selected = tuple(
                page
                for page in selected
                if all(
                    term in page.title.lower() or term in page.path.lower() or term in page.text.lower()
                    for term in terms
                )
            )
        nodes = []
        for page in selected[:limit]:
            nodes.append(
                {
                    "path": page.path,
                    "title": page.title,
                    "type": page.page_type,
                    "outgoing": list(self._outgoing.get(page.path, ())),
                    "incoming": list(self._incoming.get(page.path, ())),
                }
            )
        return {"query": query, "node_count": len(nodes), "nodes": nodes}


TOOLS = [
    {
        "name": "openkb_status",
        "description": "Report the local OpenKB root, compiled wiki-page count, raw-document count, and config path.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "openkb_search",
        "description": "Search the compiled OpenKB wiki locally and return ranked, path-cited excerpts. This works without an LLM credential.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Terms or phrase to search for."},
                "top_k": {"type": "integer", "minimum": 1, "maximum": 50, "default": 8},
                "include_content": {"type": "boolean", "default": False},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "openkb_read",
        "description": "Read one exact OpenKB wiki page by its cited path.",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "A wiki-relative path such as wiki/concepts/rebook-exception.md."}},
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "openkb_graph",
        "description": "Inspect resolved OpenKB wikilinks and incoming/outgoing page relationships.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Optional title, path, or content filter."},
                "limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 50},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "openkb_query",
        "description": "Ask OpenKB's model-backed Q&A agent to synthesize an answer from the wiki. Requires the OpenKB CLI and its configured LLM credential.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string"},
                "timeout_seconds": {"type": "integer", "minimum": 10, "maximum": 600, "default": 180},
            },
            "required": ["question"],
            "additionalProperties": False,
        },
    },
]


class OpenKbMcpServer:
    def __init__(self, kb_dir: Path):
        self.index = WikiIndex(kb_dir)

    def call_tool(self, name: str, arguments: dict) -> dict:
        if name == "openkb_status":
            payload = self.index.status()
        elif name == "openkb_search":
            top_k = max(1, min(int(arguments.get("top_k", 8)), 50))
            payload = self.index.search(
                str(arguments.get("query", "")),
                top_k=top_k,
                include_content=bool(arguments.get("include_content", False)),
            )
        elif name == "openkb_read":
            payload = self.index.read(str(arguments.get("path", "")))
        elif name == "openkb_graph":
            limit = max(1, min(int(arguments.get("limit", 50)), 200))
            query = arguments.get("query")
            payload = self.index.graph(str(query) if query else None, limit=limit)
        elif name == "openkb_query":
            payload = self._query(
                str(arguments.get("question", "")),
                max(10, min(int(arguments.get("timeout_seconds", 180)), 600)),
            )
        else:
            raise ValueError(f"unknown tool: {name}")
        return {"content": [{"type": "text", "text": json.dumps(payload, ensure_ascii=False, indent=2)}]}

    def _query(self, question: str, timeout_seconds: int) -> dict:
        if not question.strip():
            raise ValueError("question must not be blank")
        executable = os.environ.get("OPENKB_BIN") or shutil.which("openkb")
        if not executable:
            raise RuntimeError("OpenKB CLI not found; install openkb and ensure it is on PATH")
        command = [executable, "--kb-dir", str(self.index.kb_dir), "query", question, "--raw"]
        try:
            completed = subprocess.run(
                command,
                cwd=self.index.kb_dir.parent,
                env=os.environ.copy(),
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired as error:
            raise RuntimeError(f"OpenKB query timed out after {timeout_seconds} seconds") from error
        if completed.returncode:
            detail = ANSI_RE.sub("", completed.stderr or completed.stdout).strip()
            raise RuntimeError(f"OpenKB query failed ({completed.returncode}): {detail}")
        return {"question": question, "answer": ANSI_RE.sub("", completed.stdout).strip()}

    def handle(self, request: dict) -> dict | None:
        request_id = request.get("id")
        method = request.get("method")
        if request_id is None:
            return None
        try:
            if method == "initialize":
                requested = (request.get("params") or {}).get("protocolVersion", "2024-11-05")
                result = {
                    "protocolVersion": requested,
                    "capabilities": {"tools": {"listChanged": False}, "resources": {"listChanged": False}},
                    "serverInfo": {"name": "ratan-openkb", "version": "1.0.0"},
                    "instructions": "Search OpenKB first, then read exact cited pages before treating business rules as evidence.",
                }
            elif method == "ping":
                result = {}
            elif method == "tools/list":
                result = {"tools": TOOLS}
            elif method == "tools/call":
                params = request.get("params") or {}
                result = self.call_tool(str(params.get("name", "")), params.get("arguments") or {})
            elif method == "resources/list":
                result = {
                    "resources": [
                        {"uri": "openkb://wiki/index.md", "name": "OpenKB wiki index", "mimeType": "text/markdown"},
                        {"uri": "openkb://wiki/AGENTS.md", "name": "OpenKB wiki schema", "mimeType": "text/markdown"},
                    ]
                }
            elif method == "resources/read":
                uri = str((request.get("params") or {}).get("uri", ""))
                page = self.index.read(uri)
                result = {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": page["content"]}]}
            else:
                return _error(request_id, -32601, f"method not found: {method}")
            return {"jsonrpc": "2.0", "id": request_id, "result": result}
        except (OSError, RuntimeError, TypeError, ValueError) as error:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {"content": [{"type": "text", "text": str(error)}], "isError": True},
            }


def _error(request_id: object, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def read_message(stream: BinaryIO) -> tuple[dict, bool]:
    first = stream.readline()
    if not first:
        raise EOFError
    if first.lower().startswith(b"content-length:"):
        length = int(first.split(b":", 1)[1].strip())
        while True:
            header = stream.readline()
            if header in {b"\n", b"\r\n", b""}:
                break
        return json.loads(stream.read(length)), True
    return json.loads(first), False


def write_message(stream: BinaryIO, response: dict, framed: bool) -> None:
    body = json.dumps(response, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if framed:
        stream.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    stream.write(body)
    if not framed:
        stream.write(b"\n")
    stream.flush()


def main() -> int:
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb-dir", type=Path, default=project_root / "knowledge-base")
    args = parser.parse_args()
    server = OpenKbMcpServer(args.kb_dir)
    while True:
        try:
            request, framed = read_message(sys.stdin.buffer)
        except EOFError:
            break
        except (json.JSONDecodeError, TypeError, ValueError) as error:
            write_message(sys.stdout.buffer, _error(None, -32700, str(error)), False)
            continue
        response = server.handle(request)
        if response is not None:
            write_message(sys.stdout.buffer, response, framed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
