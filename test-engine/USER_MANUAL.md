# User Manual

## Purpose

`standalone-ratan-subsets` is a single local harness for the extracted CCIL Netting and ReBook Robot suites.

## Included Coverage

- CCIL:
  - `CN-API-CCILNetting_script.robot`
  - `CN-API-Uber-CCILNetting_script.robot`
- ReBook:
  - `CN-API-ReBook.robot`
  - `CN-API-StellaAmendment-Rebook.robot`
  - `STML-API-UBER-Rebook.robot`

## Prerequisites

- A runnable Robot Framework binary available through one of:
  - `ROBOT_BIN=/path/to/robot`
  - `robot` on `PATH`
  - `uv` on `PATH`

If `ROBOT_BIN` is set, it must point to an executable Robot binary.

## Run Commands

Run CCIL only:

```bash
standalone-ratan-subsets/scripts/run_ccil.sh
```

Run ReBook only:

```bash
standalone-ratan-subsets/scripts/run_rebook.sh
```

Run both domains:

```bash
standalone-ratan-subsets/scripts/run_all.sh
```

Pass extra Robot arguments after the script name. Example:

```bash
standalone-ratan-subsets/scripts/run_rebook.sh --test CN-API-Rebook-001-001
```

## Results

- Output directory: `standalone-ratan-subsets/results/`
- Open HTML results:
- Open HTML results:

```bash
standalone-ratan-subsets/scripts/open_results.sh
```

The helper uses `open` on macOS and `xdg-open` on Linux.

## Fidelity Boundary

- CCIL grouping, resultant creation, novation, suppression, and over-netting rejection remain modeled by the verified CCIL backend.
- ReBook window and exception behavior remain modeled by the verified ReBook backend.
- External integrations such as DB, Kafka, and remote service calls remain mocked locally.