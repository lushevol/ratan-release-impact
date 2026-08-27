# User Manual

## Purpose

`test-engine` is a single local simulation for the extracted CCIL Netting and
ReBook Robot suites.

## Included Coverage

- CCIL:
  - `CN-API-CCILNetting_script.robot`
  - `CN-API-Uber-CCILNetting_script.robot`
- ReBook:
  - `CN-API-ReBook.robot`
  - `CN-API-StellaAmendment-Rebook.robot`
  - `STML-API-UBER-Rebook.robot`

## Setup

Install `uv`, then run once:

```bash
test-engine/scripts/setup.sh
```

This creates `test-engine/.venv` from the committed lockfile. For an existing
Robot installation, `ROBOT_BIN=/path/to/robot` remains supported and takes
precedence over the local environment.

## Run Commands

Run CCIL only:

```bash
test-engine/scripts/run_ccil.sh
```

Run ReBook only:

```bash
test-engine/scripts/run_rebook.sh
```

Run both domains:

```bash
test-engine/scripts/run_all.sh
```

Pass extra Robot arguments after the script name. Example:

```bash
test-engine/scripts/run_rebook.sh --test CN-API-Rebook-001-001
```

## Results

- Output directory: `test-engine/results/`
- Open HTML results:

```bash
test-engine/scripts/open_results.sh
```

The helper uses `open` on macOS and `xdg-open` on Linux.

## SDLC Evidence Runs

Validate the behavior catalog:

```bash
test-engine/scripts/validate_catalog.sh
```

Capture the current simulation before implementation:

```bash
test-engine/scripts/run_evidence.sh \
  --change-id ADO-1 \
  --phase before \
  --domain rebook
```

After the reviewed scenario/model change, capture the same scope and compare:

```bash
test-engine/scripts/run_evidence.sh \
  --change-id ADO-1 \
  --phase after \
  --domain rebook

test-engine/scripts/compare_evidence.sh --change-id ADO-1
```

To run selected scenarios, repeat `--scenario`:

```bash
test-engine/scripts/run_evidence.sh \
  --change-id ADO-1 \
  --phase before \
  --scenario scenario:rebook:cn-api:001-001 \
  --scenario scenario:rebook:cn-api:001-002
```

Each phase produces `run.json`. Comparison produces `comparison.json` and
`impact-fragment.md`, which supplies the verification-matrix section of the
requirement impact report. Existing phase evidence is immutable and will not be
overwritten.

## Fidelity Boundary

- CCIL grouping, resultant creation, novation, suppression, and over-netting rejection remain modeled by the verified CCIL backend.
- ReBook window and exception behavior remain modeled by the verified ReBook backend.
- External integrations such as DB, Kafka, and remote service calls remain mocked locally.
- A passing result is `observed_in_test_engine_simulation`; it is not production evidence.
