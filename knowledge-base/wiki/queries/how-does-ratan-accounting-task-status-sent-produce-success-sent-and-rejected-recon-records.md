---
type: query
title: How Does RATAN Accounting Task Status SENT Produce SUCCESS, SENT, and REJECTED Reconciliation Records?
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, accounting, status, task-history, reconciliation, open-question]
related: [ratan-accounting-reconciliation-api, accounting-posting-statuses, ratan, tlm, oltp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# How Does RATAN Accounting Task Status SENT Produce SUCCESS, SENT, and REJECTED Reconciliation Records?

## Question

The requirement says that TLM receives accounting records with statuses `SUCCESS`, `SENT`, and `REJECTED`, but also defines the implicit filter:

```sql
ratan_accounting_request_task_history.task_status = 'SENT'
```

It is unclear whether `task_status` is distinct from the accounting response status, whether the filter applies only to delivery tasks, or whether successful and rejected records are represented elsewhere in the response.

## Evidence

The source defines `SUCCESS` as an acknowledged posting, `SENT` as an unanswered posting, and `REJECTED` as a negatively acknowledged posting. It does not provide a schema showing both task status and accounting status.

## Required resolution

Confirm the authoritative status field, the selection logic for each response state, and whether `HOLD`, `MISSING_INFO`, and `DISABLED` are intentionally excluded.