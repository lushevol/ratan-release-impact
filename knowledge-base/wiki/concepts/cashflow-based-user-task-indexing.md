---
type: concept
title: Cashflow-Based User Task Indexing
created: 2026-08-24
updated: 2026-08-24
tags: [database-indexing, camunda, user-task, cashflow, query-performance]
related: [camunda-task-completion-bottleneck, bulk-exception-processing-performance, camunda, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result.md"]
---

# Cashflow-Based User Task Indexing

The checker performance analysis identifies `userTaskService.queryActiveTask` as a database bottleneck because the query searches by `cashflowId` without an index.

## Proposed index

The source proposes the following composite index on `ratan_cashflow_user_task`:

```sql
CREATE INDEX idx_ratan_cashflow_user_task_cid_bt_bv_active
    ON ratan_cashflow_user_task (cashflow_id, business_type, business_version, active);
```

The column order places `cashflow_id` first, followed by workflow classification and active-state filtering.

## Intended query path

The index is intended to support active user-task lookup for a cashflow while also filtering by:

- `business_type`
- `business_version`
- `active`

The source states that the corresponding query code should use `cashflowId` as the first query condition.

## Validation requirements

Adding the index should be validated against the actual SQL query and execution plan. Important checks include:

- Predicate order and equality conditions.
- Selectivity of `cashflow_id`.
- Whether `business_type`, `business_version`, and `active` are always present.
- Index-only or table lookup behavior.
- Write overhead and storage cost.
- Before-and-after latency under concurrent checker batches.

The source marks this improvement item as struck through, suggesting implementation, but provides no query plans or measured before-and-after result.
