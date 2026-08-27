# Standalone Ratan Subsets

This project merges the verified standalone CCIL Netting and ReBook extracts into one self-contained local simulation.

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
- `scripts/run_ccil.sh`: run only the CCIL suites
- `scripts/run_rebook.sh`: run only the ReBook suites
- `scripts/run_all.sh`: run both domains in one execution
- `scripts/open_results.sh`: open `report.html` and `log.html`
- `USER_MANUAL.md`: operator guide

The runners prefer `ROBOT_BIN`, then `robot` on `PATH`, then `uv run --no-project`.
If `ROBOT_BIN` is set, it must point to an executable Robot binary or the script exits with an error.

Use:

```bash
standalone-ratan-subsets/scripts/run_ccil.sh
standalone-ratan-subsets/scripts/run_rebook.sh
standalone-ratan-subsets/scripts/run_all.sh
```