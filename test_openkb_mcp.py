from __future__ import annotations

import importlib.util
import json
import os
import shlex
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SERVER_PATH = ROOT / ".claude" / "tools" / "openkb-mcp.py"


def load_server_module():
    spec = importlib.util.spec_from_file_location("openkb_mcp", SERVER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


openkb_mcp = load_server_module()


class OpenKbMcpTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.kb_dir = Path(self.tempdir.name)
        (self.kb_dir / ".openkb").mkdir()
        (self.kb_dir / "raw").mkdir()
        wiki = self.kb_dir / "wiki"
        (wiki / "concepts").mkdir(parents=True)
        (wiki / "entities").mkdir()
        (wiki / "index.md").write_text(
            "# Wiki Index\n\n- [[concepts/rebook-exception|Rebook Exception]]\n",
            encoding="utf-8",
        )
        (wiki / "concepts" / "rebook-exception.md").write_text(
            "---\ntype: Concept\ntitle: Rebook Exception\n---\n"
            "# Rebook Exception\nA rebook uses payment-date proximity matching and [[entities/ratan]].\n",
            encoding="utf-8",
        )
        (wiki / "entities" / "ratan.md").write_text(
            "---\ntype: Product\ntitle: Ratan\n---\n# Ratan\nCash settlement platform.\n",
            encoding="utf-8",
        )
        self.index = openkb_mcp.WikiIndex(self.kb_dir)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_search_ranks_and_cites_matching_page(self):
        result = self.index.search("rebook payment date", top_k=2)
        self.assertEqual(result["results"][0]["path"], "wiki/concepts/rebook-exception.md")
        self.assertIn("payment-date proximity", result["results"][0]["snippet"])

    def test_read_rejects_path_traversal(self):
        with self.assertRaisesRegex(ValueError, "inside knowledge-base/wiki"):
            self.index.read("../../outside")

    def test_graph_resolves_wikilinks(self):
        result = self.index.graph("rebook", limit=5)
        rebook = next(
            node for node in result["nodes"] if node["path"] == "wiki/concepts/rebook-exception.md"
        )
        self.assertEqual(rebook["outgoing"], ["wiki/entities/ratan.md"])

    def test_qmd_backend_maps_json_results_to_citable_wiki_pages(self):
        qmd = self.kb_dir / "qmd"
        payload = json.dumps(
            [
                {
                    "file": "qmd://ratan-wiki/concepts/rebook-exception.md",
                    "docid": "abc123",
                    "score": 0.91,
                    "line": 4,
                    "title": "QMD title",
                    "snippet": "A [[concepts/rebook-exception]] hit",
                }
            ]
        )
        qmd.write_text(
            "#!/bin/sh\n"
            f"printf '%s' {shlex.quote(payload)}\n",
            encoding="utf-8",
        )
        qmd.chmod(qmd.stat().st_mode | stat.S_IXUSR)

        with patch.dict(os.environ, {"QMD_BIN": str(qmd)}, clear=False):
            result = self.index.search("rebook", backend="qmd", include_content=True)

        self.assertEqual(result["backend"], "qmd")
        self.assertEqual(result["results"][0]["path"], "wiki/concepts/rebook-exception.md")
        self.assertEqual(result["results"][0]["docid"], "abc123")
        self.assertEqual(result["results"][0]["line"], 4)
        self.assertEqual(result["results"][0]["snippet"], "A concepts/rebook-exception hit")
        self.assertIn("payment-date proximity", result["results"][0]["content"])

    def test_auto_backend_falls_back_when_qmd_query_fails(self):
        qmd = self.kb_dir / "qmd"
        qmd.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
        qmd.chmod(qmd.stat().st_mode | stat.S_IXUSR)

        with patch.dict(os.environ, {"QMD_BIN": str(qmd)}, clear=False):
            result = self.index.search("rebook", backend="auto")

        self.assertEqual(result["backend"], "local")
        self.assertEqual(result["results"][0]["path"], "wiki/concepts/rebook-exception.md")

    def test_auto_backend_prefers_qmd_when_project_index_is_ready(self):
        qmd_dir = self.kb_dir / ".qmd"
        qmd_dir.mkdir()
        (qmd_dir / "index.yml").write_text("collections: {}\n", encoding="utf-8")
        (qmd_dir / "index.sqlite").write_bytes(b"sqlite")
        qmd = self.kb_dir / "qmd"
        payload = json.dumps(
            [
                {
                    "file": "qmd://ratan-wiki/concepts/rebook-exception.md",
                    "score": 0.82,
                    "title": "QMD result",
                    "snippet": "QMD matched this page",
                }
            ]
        )
        qmd.write_text(
            "#!/bin/sh\n"
            f"printf '%s' {shlex.quote(payload)}\n",
            encoding="utf-8",
        )
        qmd.chmod(qmd.stat().st_mode | stat.S_IXUSR)

        with patch.dict(os.environ, {"QMD_BIN": str(qmd)}, clear=False):
            result = self.index.search("rebook", backend="auto")

        self.assertEqual(result["backend"], "qmd")
        self.assertEqual(result["results"][0]["title"], "QMD result")

    def test_qmd_backend_rejects_results_outside_wiki(self):
        qmd = self.kb_dir / "qmd"
        payload = json.dumps([{"file": "/tmp/outside.md", "score": 1}])
        qmd.write_text(
            "#!/bin/sh\n"
            f"printf '%s' {shlex.quote(payload)}\n",
            encoding="utf-8",
        )
        qmd.chmod(qmd.stat().st_mode | stat.S_IXUSR)

        with patch.dict(os.environ, {"QMD_BIN": str(qmd)}, clear=False):
            result = self.index.search("rebook", backend="qmd")

        self.assertEqual(result["result_count"], 0)

    def test_stdio_protocol_lists_and_calls_tools(self):
        process = subprocess.Popen(
            [sys.executable, str(SERVER_PATH), "--kb-dir", str(self.kb_dir)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        assert process.stdin and process.stdout
        try:
            process.stdin.write(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}) + "\n")
            process.stdin.flush()
            listed = json.loads(process.stdout.readline())
            names = {tool["name"] for tool in listed["result"]["tools"]}
            self.assertIn("openkb_search", names)
            self.assertIn("openkb_qmd_query", names)

            process.stdin.write(
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 2,
                        "method": "tools/call",
                        "params": {"name": "openkb_search", "arguments": {"query": "rebook"}},
                    }
                )
                + "\n"
            )
            process.stdin.flush()
            called = json.loads(process.stdout.readline())
            payload = json.loads(called["result"]["content"][0]["text"])
            self.assertEqual(payload["results"][0]["title"], "Rebook Exception")
        finally:
            process.terminate()
            process.wait(timeout=5)
            process.stdin.close()
            process.stdout.close()
            assert process.stderr
            process.stderr.close()


if __name__ == "__main__":
    unittest.main()
