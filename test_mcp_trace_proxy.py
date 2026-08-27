import json
import os
import select
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parent
PROXY = ROOT / ".claude" / "tools" / "mcp_trace_proxy.py"
TRACE_TOOLS = ROOT / ".claude" / "skills" / "sdlc-graph" / "tools"
sys.path.insert(0, str(TRACE_TOOLS))
import langfuse_trace

CHILD = r"""
import json
import sys

for line in sys.stdin:
    request = json.loads(line)
    if "id" not in request:
        continue
    response = {
        "jsonrpc": "2.0",
        "id": request["id"],
        "result": {"method": request.get("method")},
    }
    print(json.dumps(response), flush=True)
"""


class FakeObservation:
    def __init__(self) -> None:
        self.updates = []

    def update(self, **kwargs) -> None:
        self.updates.append(kwargs)


class FakeObservationContext:
    def __init__(self, observation: FakeObservation) -> None:
        self.observation = observation
        self.closed = False

    def __enter__(self) -> FakeObservation:
        return self.observation

    def __exit__(self, *_args) -> None:
        self.closed = True


class FakeLangfuseClient:
    def __init__(self) -> None:
        self.observation = FakeObservation()
        self.context = FakeObservationContext(self.observation)

    def start_as_current_observation(self, **_kwargs) -> FakeObservationContext:
        return self.context

    def get_current_trace_id(self) -> str:
        return "trace-id"

    def flush(self) -> None:
        pass


class LangfuseTraceTest(unittest.TestCase):
    def test_updates_entered_observation_and_closes_context(self) -> None:
        client = FakeLangfuseClient()
        module = SimpleNamespace(get_client=lambda: client)
        with (
            mock.patch.dict(
                os.environ,
                {"LANGFUSE_PUBLIC_KEY": "public", "LANGFUSE_SECRET_KEY": "secret"},
            ),
            mock.patch.object(langfuse_trace.importlib, "import_module", return_value=module),
            mock.patch.object(langfuse_trace, "_client", None),
            mock.patch.object(langfuse_trace, "_flush_registered", False),
        ):
            trace = langfuse_trace.Trace("mcp.test.list", {"observation_type": "tool"})
            trace.update({"response": "ok"}, output={"jsonrpc": "2.0", "error": None})
            trace.close()

        self.assertEqual(trace.trace_id, "trace-id")
        self.assertTrue(client.context.closed)
        self.assertEqual(client.observation.updates[0]["metadata"]["response"], "ok")
        self.assertEqual(client.observation.updates[0]["output"]["jsonrpc"], "2.0")


class DotenvLoadingTest(unittest.TestCase):
    def test_local_dotenv_precedes_default_and_process_environment_wins(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, ".env.local").write_text(
                "LANGFUSE_PUBLIC_KEY=local-public\n",
                encoding="utf-8",
            )
            Path(directory, ".env").write_text(
                "LANGFUSE_PUBLIC_KEY=default-public\n"
                "LANGFUSE_SECRET_KEY=default-secret\n"
                "LANGFUSE_BASE_URL=http://default.example\n",
                encoding="utf-8",
            )
            with (
                mock.patch.dict(os.environ, {"LANGFUSE_BASE_URL": "http://process.example"}, clear=True),
                mock.patch.object(langfuse_trace.os, "getcwd", return_value=directory),
            ):
                langfuse_trace._load_dotenv()

                self.assertEqual(os.environ["LANGFUSE_PUBLIC_KEY"], "local-public")
                self.assertEqual(os.environ["LANGFUSE_SECRET_KEY"], "default-secret")
                self.assertEqual(os.environ["LANGFUSE_BASE_URL"], "http://process.example")


class McpTraceProxyTest(unittest.TestCase):
    def test_notification_does_not_block_following_request(self) -> None:
        env = os.environ.copy()
        env["LANGFUSE_PUBLIC_KEY"] = ""
        env["LANGFUSE_SECRET_KEY"] = ""
        process = subprocess.Popen(
            [
                sys.executable,
                str(PROXY),
                "--server",
                "test",
                "--",
                sys.executable,
                "-u",
                "-c",
                CHILD,
            ],
            cwd=ROOT,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        assert process.stdin and process.stdout
        try:
            frames = [
                {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
                {"jsonrpc": "2.0", "method": "notifications/initialized"},
                {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
            ]
            for frame in frames:
                process.stdin.write(json.dumps(frame) + "\n")
            process.stdin.flush()

            responses = []
            for _ in range(2):
                ready, _, _ = select.select([process.stdout], [], [], 5)
                self.assertTrue(ready, "proxy timed out waiting for an MCP response")
                responses.append(json.loads(process.stdout.readline()))

            self.assertEqual([response["id"] for response in responses], [1, 2])
            self.assertEqual(responses[1]["result"]["method"], "tools/list")
        finally:
            process.stdin.close()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.terminate()
                process.wait(timeout=5)
            process.stdout.close()
            if process.stderr:
                process.stderr.close()


if __name__ == "__main__":
    unittest.main()
