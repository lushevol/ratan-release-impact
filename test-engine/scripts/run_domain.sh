#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
RESULTS_DIR="${ROOT_DIR}/results"
DOMAIN="${1:-all}"

mkdir -p "${RESULTS_DIR}"

case "${DOMAIN}" in
  ccil)
    shift
    TARGET=("${ROOT_DIR}/suites/ccil")
    ;;
  rebook)
    shift
    TARGET=("${ROOT_DIR}/suites/rebook")
    ;;
  all)
    shift
    TARGET=("${ROOT_DIR}/suites/ccil" "${ROOT_DIR}/suites/rebook")
    ;;
  *)
    echo "Usage: ${0} [ccil|rebook|all] [robot args...]" >&2
    exit 2
    ;;
esac

if [[ -n "${ROBOT_BIN:-}" ]]; then
  if [[ -x "${ROBOT_BIN}" ]]; then
    exec "${ROBOT_BIN}" -d "${RESULTS_DIR}" "$@" "${TARGET[@]}"
  fi

  echo "ROBOT_BIN is set but not executable: ${ROBOT_BIN}" >&2
  exit 1
fi

if command -v robot >/dev/null 2>&1; then
  exec robot -d "${RESULTS_DIR}" "$@" "${TARGET[@]}"
fi

if command -v uv >/dev/null 2>&1; then
  exec uv run --no-project --with robotframework robot -d "${RESULTS_DIR}" "$@" "${TARGET[@]}"
fi

echo "No runnable Robot Framework command found. Install uv or set ROBOT_BIN to a Robot executable." >&2
exit 1