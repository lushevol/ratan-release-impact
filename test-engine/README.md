# Standalone CCIL Netting

This project extracts the CCIL-focused Robot suites from the main Ratan repository into a self-contained local simulation.

What is preserved:
- Original CCIL case names and overall case flow.
- Local keyword names and signatures where practical.
- CCIL grouping, resultant creation, novation, suppression, and over-netting rejection behavior.

What is mocked:
- Auth and session setup.
- Remote lifecycle and netting APIs.
- DB polling.
- Kafka assertions.

Helper scripts:
- `scripts/run_ccil.sh`: run both extracted CCIL suites.
- `scripts/open_results.sh`: open `report.html` and `log.html`.
- `USER_MANUAL.md`: operator-facing usage guide.

The runner prefers an existing Robot executable before falling back to `uv`.

Run:

```bash
standalone-ccil-netting/scripts/run_ccil.sh
```

Verified fallback in this workspace:

```bash
/Users/1639796/Library/Python/3.9/bin/robot -d standalone-ccil-netting/results standalone-ccil-netting/suites/CN-API-CCILNetting_script.robot standalone-ccil-netting/suites/CN-API-Uber-CCILNetting_script.robot
```