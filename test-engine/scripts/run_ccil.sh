#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
RESULTS_DIR="${ROOT_DIR}/results"
SUITE_1="${ROOT_DIR}/suites/CN-API-CCILNetting_script.robot"
SUITE_2="${ROOT_DIR}/suites/CN-API-Uber-CCILNetting_script.robot"

mkdir -p "${RESULTS_DIR}"

if [[ -n "${ROBOT_BIN:-}" && -x "${ROBOT_BIN}" ]]; then
  exec "${ROBOT_BIN}" -d "${RESULTS_DIR}" "${SUITE_1}" "${SUITE_2}"
fi

if command -v robot >/dev/null 2>&1; then
  exec robot -d "${RESULTS_DIR}" "${SUITE_1}" "${SUITE_2}"
fi

if [[ -x "/Users/1639796/Library/Python/3.9/bin/robot" ]]; then
  exec "/Users/1639796/Library/Python/3.9/bin/robot" -d "${RESULTS_DIR}" "${SUITE_1}" "${SUITE_2}"
fi

if command -v uv >/dev/null 2>&1; then
  exec uv run --no-project --with robotframework robot -d "${RESULTS_DIR}" "${SUITE_1}" "${SUITE_2}"
fi

echo "No runnable Robot Framework command found. Install uv or set ROBOT_BIN to a Robot executable." >&2
exit 1