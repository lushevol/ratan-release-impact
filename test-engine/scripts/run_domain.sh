#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
RESULTS_DIR="${ROOT_DIR}/results"
DOMAIN="${1:-all}"
LOCAL_ROBOT="${ROOT_DIR}/.venv/bin/robot"

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

if [[ -x "${LOCAL_ROBOT}" ]]; then
  exec "${LOCAL_ROBOT}" -d "${RESULTS_DIR}" "$@" "${TARGET[@]}"
fi

echo "Test engine is not set up. Run ${ROOT_DIR}/scripts/setup.sh or set ROBOT_BIN." >&2
exit 1
