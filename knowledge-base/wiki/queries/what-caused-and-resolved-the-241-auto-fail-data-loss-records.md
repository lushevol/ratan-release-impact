---
type: query
title: What Caused and Resolved the 241 Auto Fail Data-Loss Records?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, auto-fail, data-integrity, reconciliation, batch-processing]
related: [cash-settlement-lifecycle-job-batch-performance, cash-settlement-batch-job-performance, paginated-cashflow-batch-processing, cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Lifecycle Jobs Performance Test.md"]
---

# What Caused and Resolved the 241 Auto Fail Data-Loss Records?

## Question

What do the 241 Auto Fail records reported as `data lose` represent, and were they recovered, reconciled, or otherwise determined to be expected outcomes?

## Evidence

The performance test processed 234,945 records in `staging` using 235 pages of 1,000 records. It reported:

```text
Success rate: 94.93%
succ: 223028
data lose: 241
```

The same test reported no processing interruption caused by missing data and no database query exceptions, including no exception attributed to excessively long input parameters. Memory remained at 1.76G maximum against an 8 GB heap, and maximum CPU usage was 90.7%.

## Why this remains open

The report concludes that the batch version can replace the original online version, but it does not define:

- The operational meaning of `data lose`.
- Whether the 241 records were rejected, excluded by business rules, transient failures, or actual data loss.
- Whether retries or compensating actions were attempted.
- Whether reconciliation confirmed the final state in downstream systems.
- The denominator and calculation used for the 94.93% success rate.
- The acceptance threshold for incomplete processing.

Resource stability and uninterrupted execution do not establish data-integrity correctness.

## Required evidence

Resolution should identify the affected records and provide:

1. Error or exclusion classifications for all 241 records.
2. Retry and dead-letter outcomes, if applicable.
3. Reconciliation results across the lifecycle service and downstream systems.
4. Evidence that any recoverable records were replayed successfully.
5. A formal success-rate and data-integrity acceptance criterion.
6. Regression results after any `moveStatus` validation or query-projection changes.

Until this evidence is available, the Auto Fail batch implementation should be considered operationally stable but not proven to be a complete replacement for the online implementation.