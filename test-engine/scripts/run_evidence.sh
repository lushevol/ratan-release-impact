#!/usr/bin/env zsh

set -euo pipefail

ROOT_DIR="${0:A:h:h}"
CHANGE_ID=""
PHASE=""
DOMAIN="all"
OUTPUT_ROOT="${ROOT_DIR}/evidence"
ROBOT_ARGS=()

usage() {
  echo "Usage: ${0} --change-id ID --phase before|after [--domain all|ccil|rebook] [--output-root DIR] [--scenario ID] [-- ROBOT_ARGS...]" >&2
}

while (( $# > 0 )); do
  case "$1" in
    --change-id)
      CHANGE_ID="${2:-}"
      shift 2
      ;;
    --phase)
      PHASE="${2:-}"
      shift 2
      ;;
    --domain)
      DOMAIN="${2:-}"
      shift 2
      ;;
    --output-root)
      OUTPUT_ROOT="${2:-}"
      shift 2
      ;;
    --scenario)
      ROBOT_ARGS+=(--include "${2:-}")
      shift 2
      ;;
    --)
      shift
      ROBOT_ARGS+=("$@")
      break
      ;;
    *)
      usage
      exit 2
      ;;
  esac
done

if [[ -z "${CHANGE_ID}" || ! "${CHANGE_ID}" =~ '^[A-Za-z0-9._-]+$' ]]; then
  echo "--change-id is required and may contain only letters, numbers, dot, underscore, and hyphen." >&2
  exit 2
fi
if [[ "${PHASE}" != "before" && "${PHASE}" != "after" ]]; then
  echo "--phase must be before or after." >&2
  exit 2
fi
if [[ "${DOMAIN}" != "all" && "${DOMAIN}" != "ccil" && "${DOMAIN}" != "rebook" ]]; then
  echo "--domain must be all, ccil, or rebook." >&2
  exit 2
fi
if [[ ! -x "${ROOT_DIR}/.venv/bin/python" ]]; then
  echo "Test engine is not set up. Run ${ROOT_DIR}/scripts/setup.sh." >&2
  exit 1
fi

RUN_DIR="${OUTPUT_ROOT:A}/${CHANGE_ID}/${PHASE}"
RAW_DIR="${RUN_DIR}/raw"
if [[ -e "${RUN_DIR}/run.json" || -e "${RAW_DIR}/output.xml" ]]; then
  echo "Evidence already exists at ${RUN_DIR}; use a new change ID or preserve the existing immutable run." >&2
  exit 1
fi

"${ROOT_DIR}/scripts/validate_catalog.sh" >/dev/null
mkdir -p "${RAW_DIR}"

set +e
"${ROOT_DIR}/scripts/run_domain.sh" "${DOMAIN}" --outputdir "${RAW_DIR}" "${ROBOT_ARGS[@]}"
ROBOT_CODE=$?
set -e

"${ROOT_DIR}/.venv/bin/python" "${ROOT_DIR}/tools/evidence.py" convert \
  --robot-output "${RAW_DIR}/output.xml" \
  --output "${RUN_DIR}/run.json" \
  --change-id "${CHANGE_ID}" \
  --phase "${PHASE}" \
  --domain "${DOMAIN}" \
  --return-code "${ROBOT_CODE}"

echo "Evidence: ${RUN_DIR}/run.json"
exit "${ROBOT_CODE}"
