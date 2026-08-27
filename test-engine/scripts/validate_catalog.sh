#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"

if [[ ! -x "${PYTHON_BIN}" ]]; then
  echo "Test engine is not set up. Run ${ROOT_DIR}/scripts/setup.sh." >&2
  exit 1
fi

exec "${PYTHON_BIN}" "${ROOT_DIR}/tools/evidence.py" validate
