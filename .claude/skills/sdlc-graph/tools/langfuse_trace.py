"""Optional Langfuse tracing for SDLC impact-analysis runs.

Tracing is deliberately fail-open: the graph tools remain dependency-free and
continue to work when Langfuse is not installed or is unavailable. Inputs are
represented by a SHA-256 digest so requirement text and repository data are not
sent to the tracing backend by default.
"""

from __future__ import annotations

import hashlib
import importlib
import os
import time
from contextlib import contextmanager
from typing import Any, Iterator


def _load_dotenv() -> None:
    """Load simple KEY=VALUE entries without overriding the process environment."""
    path = os.path.join(os.getcwd(), ".env")
    try:
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key, value = key.strip(), value.strip().strip("\"'")
                if key and key not in os.environ:
                    os.environ[key] = value
    except OSError:
        pass


_load_dotenv()
if os.getenv("LANGFUSE_BASE_URL") and not os.getenv("LANGFUSE_HOST"):
    os.environ["LANGFUSE_HOST"] = os.environ["LANGFUSE_BASE_URL"]


def _enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY")) and bool(os.getenv("LANGFUSE_SECRET_KEY"))


def _digest(value: Any) -> str:
    return hashlib.sha256(repr(value).encode("utf-8")).hexdigest()


class Trace:
    """Small adapter supporting current and legacy Langfuse Python clients."""

    def __init__(self, name: str, metadata: dict[str, Any]):
        self.trace_id: str | None = None
        self._client: Any = None
        self._observation: Any = None
        self._started = time.time()
        if not _enabled():
            return
        try:
            module = importlib.import_module("langfuse")
            self._client = getattr(module, "get_client", lambda: module.Langfuse())()
            if hasattr(self._client, "start_as_current_observation"):
                self._observation = self._client.start_as_current_observation(
                    as_type=metadata.pop("observation_type", "span"), name=name,
                    input={"input_sha256": metadata.get("input_sha256")}, metadata=metadata,
                )
                self._observation.__enter__()
                self.trace_id = (
                    self._client.get_current_trace_id()
                    if hasattr(self._client, "get_current_trace_id")
                    else getattr(self._observation, "trace_id", None)
                )
            elif hasattr(self._client, "trace"):
                self._observation = self._client.trace(name=name, metadata=metadata)
                self.trace_id = getattr(self._observation, "id", None)
        except Exception:
            self._client = None
            self._observation = None

    def update(self, metadata: dict[str, Any], *, output: Any = None, error: Exception | None = None) -> None:
        if self._observation is None:
            return
        payload = {**metadata, "duration_ms": round((time.time() - self._started) * 1000, 2)}
        try:
            if error:
                payload["error"] = type(error).__name__
            if hasattr(self._observation, "update"):
                self._observation.update(metadata=payload, output=output)
            elif hasattr(self._observation, "update_trace"):
                self._observation.update_trace(metadata=payload, output=output)
        except Exception:
            pass

    def close(self) -> None:
        if self._observation is not None:
            try:
                self._observation.__exit__(None, None, None)
            except Exception:
                pass
        if self._client is not None:
            try:
                self._client.flush()
            except Exception:
                pass


@contextmanager
def impact_trace(name: str, input_value: Any, metadata: dict[str, Any] | None = None) -> Iterator[Trace]:
    trace = Trace(name, {"input_sha256": _digest(input_value), **(metadata or {})})
    try:
        yield trace
    except Exception as error:
        trace.update({}, error=error)
        raise
    finally:
        trace.close()
