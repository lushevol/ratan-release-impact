#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
CACHE_DIR="${UV_CACHE_DIR:-${TMPDIR:-/tmp}/ratan-test-engine-uv-cache}"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install it from https://docs.astral.sh/uv/ and rerun this script." >&2
  exit 1
fi

export UV_CACHE_DIR="${CACHE_DIR}"

if [[ ! -f "${ROOT_DIR}/uv.lock" ]]; then
  echo "Missing ${ROOT_DIR}/uv.lock; restore the committed lockfile before setup." >&2
  exit 1
fi

uv sync --project "${ROOT_DIR}" --locked

"${ROOT_DIR}/.venv/bin/python" -c 'import robot; print(f"Robot Framework {robot.__version__}")'
echo "Test engine is ready. Run ${ROOT_DIR}/scripts/run_all.sh"
