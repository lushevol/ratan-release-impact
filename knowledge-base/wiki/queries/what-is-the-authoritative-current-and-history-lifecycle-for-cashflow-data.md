---
type: query
title: What Is the Authoritative Current and History Lifecycle for cashflow_data?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-service, history, data-lifecycle, open-question]
related: [cashflow-data, cashflow-data-history, cash-settlement-cashflow-read-model, what-is-the-canonical-cashflow-storage-and-history-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design.md"]
---
# What Is the Authoritative Current and History Lifecycle for `cashflow_data`?

The design defines `cashflow_data` and `cashflow_data_history`, but does not specify how they are populated or kept consistent.

## Questions

1. Is `cashflow_data` the canonical current-state row for each cashflow?
2. Is `cashflow_data_history` append-only?
3. Is a prior current row copied to history before every update?
4. Does history retain every source event, every material change, or only selected lifecycle transitions?
5. Which field determines ordering: source publication time, event date, cashflow version, audit version, or `updated_at`?
6. How are duplicate, replayed, stale, corrected, and out-of-order events handled?
7. Is `id` stable across current and historical records?
8. What retention, archival, purge, and audit requirements apply?
9. How are failed current/history transactions recovered?

## Evidence

The source establishes the existence of both table definitions and their near-identical shapes. It does not establish their write behavior or production deployment. The table names suggest a current/history distinction, but that interpretation requires confirmation.

Resolution should be aligned with [[what-is-the-canonical-cashflow-storage-and-history-model]] and the Query Service ownership model in [[query-service]].