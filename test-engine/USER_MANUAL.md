# Standalone CCIL Netting User Manual

## Purpose

This standalone project runs the extracted CCIL test cases locally without connecting to Ratan services, DBs, Kafka, or portal APIs.

The project keeps the original suite logic for:
- CCIL guaranteed and non-guaranteed flows
- CCIL novation and regrouping flows
- CCIL over-netting rejection checks
- Uber CCIL non-guaranteed flow

## Project Layout

- `suites/`: extracted Robot suites
- `resources/`: local import hub, variables, and helper resources
- `libraries/`: in-memory backend that simulates the lifecycle and netting engine
- `results/`: generated execution output
- `scripts/`: helper commands for running and viewing results

## Prerequisites

Preferred:

```bash
uv
```

Fallback:

```bash
robot
```

If Robot is not on `PATH`, you can point the runner at it:

```bash
export ROBOT_BIN=/absolute/path/to/robot
```

## Run The Extracted CCIL Suites

From the repository root:

```bash
standalone-ccil-netting/scripts/run_ccil.sh
```

This script:
- prefers `$ROBOT_BIN` when provided
- then uses `robot` on `PATH`
- then uses the verified workspace Robot binary when present
- only falls back to `uv run --no-project --with robotframework robot`
- writes output into `standalone-ccil-netting/results/`

## Open The HTML Results

From the repository root:

```bash
standalone-ccil-netting/scripts/open_results.sh
```

On macOS this opens both:
- `results/report.html`
- `results/log.html`

## Output Files

After a successful run, review:
- `results/output.xml`
- `results/report.html`
- `results/log.html`

## What Is Real vs Mocked

Preserved from local project logic:
- CCIL suite bodies
- keyword names and keyword call structure
- local result validation flow

Mocked locally:
- token acquisition
- remote lifecycle and netting APIs
- DB status polling
- Kafka assertions

## Troubleshooting

If `run_ccil.sh` says no runnable Robot command was found:
- install `uv`, or
- install Robot Framework on `PATH`, or
- set `ROBOT_BIN` to a valid Robot executable

If results are missing:
- run `scripts/run_ccil.sh` first
- then run `scripts/open_results.sh`

## Verified Command In This Workspace

This project was verified with:

```bash
/Users/1639796/Library/Python/3.9/bin/robot -d standalone-ccil-netting/results standalone-ccil-netting/suites/CN-API-CCILNetting_script.robot standalone-ccil-netting/suites/CN-API-Uber-CCILNetting_script.robot
```