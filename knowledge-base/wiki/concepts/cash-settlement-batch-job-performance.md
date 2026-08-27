---
type: concept
title: Cash Settlement Batch-Job Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, batch-jobs, performance, capacity]
related: [ratan, paginated-cashflow-batch-processing, long-running-batch-job-api-execution, is-six-gb-jvm-heap-sufficient-for-ratan-auto-materialize-at-uk-volume, does-the-ebbs-accounting-job-meet-uk-volume-performance-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
---
# Cash Settlement Batch-Job Performance

Cash Settlement batch-job qualification should establish that a job can complete its eligible workload within an agreed operational window while maintaining safe memory use, correct outcomes, and repeatable behavior under production-representative conditions.

The stated UK planning assumption is 40,000 daily cashflows. Daily volume alone is insufficient for qualification: the peak eligible population per invocation, schedule, concurrent workloads, database contention, data validity mix, retry behavior, and completion-time SLO also determine readiness.

## Current evidence

Dev tests at 50k show successful reported runs for Auto Materialize V2, Auto Fail V1, and Auto Release V2. However, the evidence does not establish the full four-job definition of done:

- Auto Materialize V2 fails at 100k with a 2 GB maximum heap.
- Auto Fail has only one reported 50k run.
- Auto Release V1 is marked TBD and appears to contain copied materialization results.
- The Accounting job for EBBS feeds has no reported test result.

Invalid mocked records are reported as “not materialized.” These counts should be separated from valid-record completion, expected functional exclusions, and technical failures.

## Minimum performance evidence

A qualification record should include workload composition, eligible and ineligible counts, elapsed time by stage, heap and Metaspace profile, database and downstream dependency behavior, error and retry counts, concurrency assumptions, and repeated-run variance. A successful result should be explicitly tied to a defined completion SLO and target environment.

See [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--21--1yk3s57]] for the available Dev measurements.