---
type: query
title: Is RATAN Accounting Reconciliation Filtered by Release Time or Task-History Created At?
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, accounting, timestamp, task-history, reconciliation, open-question]
related: [ratan-accounting-reconciliation-api, korea-accounting-reconciliation, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# Is RATAN Accounting Reconciliation Filtered by Release Time or Task-History Created At?

## Question

The API parameters are named `startReleaseTime` and `endReleaseTime`, but the documented predicates compare them with `ratan_accounting_request_task_history.created_at`.

## Evidence

The lower boundary is exclusive:

```sql
created_at > startReleaseTime
```

The upper boundary is inclusive:

```sql
created_at <= endReleaseTime
```

The maximum interval is three days.

## Required resolution

Confirm whether `created_at` is the intended proxy for accounting release time or whether a separate release timestamp exists. Define the behavior for records created near the interval boundaries.