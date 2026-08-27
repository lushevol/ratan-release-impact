---
type: concept
title: Korea Migration Performance Testing
created: 2026-08-23
updated: 2026-08-23
tags: [performance-testing, migration-testing, korea-migration, cash-settlement, validation]
related: [murex-korea, murex, auto-netting-job, swift-message-reconciliation, cashflow-query-api-performance-optimization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Performance Testing Plan.md"]
---
# Korea Migration Performance Testing

## Definition

Korea migration performance testing is the planned, repeatable validation of migrated settlement data in Murex Korea using dated end-of-day snapshots. The documented workflow combines data ingestion, reconciliation, processing, automatic netting, retry handling, and SWIFT-output comparison.

Although the source is titled a performance-testing plan, it does not define measurable performance criteria. Its stated activities primarily provide functional and output-validation coverage.

## Test Pattern

Each test cycle follows this sequence:

1. Prepare or select a dated EOD dump.
2. Push the dump data into the Murex Korea test scope.
3. Perform reconciliation and analysis.
4. Process the data.
5. Run the auto-netting job.
6. Reprocess cashflows that remain in the `waiting` state.
7. Compare SWIFT messages for the cycle's designated payment cohort.

## Cycle Mapping

The plan maps the input snapshots to payment cohorts as follows:

- 15-June EOD dump → VD17 payments.
- 16-June EOD dump → VD18 payments.
- 18-June EOD dump → VD22 payments.

The source does not explain how these payment cohorts are derived or why the value-date identifiers are non-consecutive.

## Evidence Boundary

This concept describes intended test coverage rather than observed behavior. It does not establish throughput, latency, resource utilization, retry success, SWIFT equivalence, migration completion, or production readiness.

The generic auto-netting step must remain distinct from [[concepts/lien-aware-netting-and-auto-unnetting]], because the source provides no lien-related rules or behavior.
