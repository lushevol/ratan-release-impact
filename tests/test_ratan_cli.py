import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ratan_cli", ROOT / "scripts" / "ratan.py")
assert SPEC and SPEC.loader
ratan = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ratan)


class RatanCliTest(unittest.TestCase):
    def test_manifest_contains_unique_direct_repository_paths(self):
        payload = ratan.load_manifest()
        names = [entry["name"] for entry in payload["repositories"]]
        paths = [entry["path"] for entry in payload["repositories"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(paths), len(set(paths)))
        self.assertTrue(all(path.startswith("repos/") for path in paths))

    def test_manifest_template_requires_org_and_expands_it(self):
        payload = {"remote_template": "git@github.com:${RATAN_GIT_ORG}/{name}.git"}
        entry = {"name": "example", "url": None}
        with patch.dict(os.environ, {}, clear=True):
            self.assertIsNone(ratan.entry_url(entry, payload))
        with patch.dict(os.environ, {"RATAN_GIT_ORG": "acme"}, clear=False):
            self.assertEqual(ratan.entry_url(entry, payload), "git@github.com:acme/example.git")

    def test_mcp_parser_accepts_line_and_content_length_frames(self):
        newline = json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"ok": True}}).encode() + b"\n"
        body = json.dumps({"jsonrpc": "2.0", "id": 2, "result": {"tools": []}}).encode()
        framed = b"Content-Length: " + str(len(body)).encode() + b"\r\n\r\n" + body
        responses = ratan.parse_mcp_output(newline + framed)
        self.assertEqual([item["id"] for item in responses], [1, 2])

    def test_load_manifest_rejects_absolute_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps({"repositories": [{"name": "x", "path": "/tmp/x"}]}), encoding="utf-8")
            with self.assertRaises(SystemExit):
                ratan.load_manifest(path)


if __name__ == "__main__":
    unittest.main()
