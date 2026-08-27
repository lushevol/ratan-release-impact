# Ratan Test Engine

This project is the local behavior simulation used by the SDLC POC. It combines
the verified CCIL Netting and ReBook Robot extracts without relying on live
external systems.

Included domains:
- `ccil`: CCIL Netting and Uber CCIL cases
- `rebook`: ReBook, Stella amendment ReBook, and UBER ReBook cases

What is preserved:
- Original extracted suite bodies with only import-path rebasing.
- The domain-specific backend logic already verified in the separate standalone projects.
- Local keyword names and signatures where practical.

What is mocked:
- Auth and session setup.
- Remote lifecycle, trade-confirmation, and netting APIs.
- DB polling.
- Kafka assertions.

Layout:
- `suites/ccil`: CCIL suites
- `suites/rebook`: ReBook suites
- `resources/ccil`: CCIL import hub, variables, and checks
- `resources/rebook`: ReBook import hub, variables, and checks
- `libraries`: domain backends

Helper scripts:
- `scripts/setup.sh`: create the locked local Python environment
- `scripts/run_ccil.sh`: run only the CCIL suites
- `scripts/run_rebook.sh`: run only the ReBook suites
- `scripts/run_all.sh`: run both domains in one execution
- `scripts/validate_catalog.sh`: validate all behavior/scenario/test mappings
- `scripts/run_evidence.sh`: execute an immutable before or after evidence run
- `scripts/compare_evidence.sh`: compare the two phases and render an impact fragment
- `scripts/open_results.sh`: open `report.html` and `log.html`
- `USER_MANUAL.md`: operator guide

## Setup

Install `uv`, then run once from the repository root:

```bash
test-engine/scripts/setup.sh
```

The setup uses `pyproject.toml` and `uv.lock` to create `test-engine/.venv` with
Robot Framework 7.4.2. The runners prefer an explicit `ROBOT_BIN`, then the
locked local environment. `ROBOT_BIN` must point to an executable.

Run:

```bash
test-engine/scripts/run_ccil.sh
test-engine/scripts/run_rebook.sh
test-engine/scripts/run_all.sh
```

Run the SDLC evidence cycle:

```bash
test-engine/scripts/run_evidence.sh --change-id ADO-1 --phase before
test-engine/scripts/run_evidence.sh --change-id ADO-1 --phase after
test-engine/scripts/compare_evidence.sh --change-id ADO-1
```

Use `--domain ccil|rebook` or repeat `--scenario scenario:...` to select the
impact-analysis recommendation set. Each run writes portable evidence under
`test-engine/evidence/<change-id>/` and refuses to overwrite an existing phase.

See `POC_OPERATING_MODEL.md` for the engine's authority and SDLC lifecycle.
