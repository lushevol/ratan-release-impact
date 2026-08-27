---
type: concept
title: Ratan Cashflow History Composite Index
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, postgresql, composite-index, cashflow-auto-netting, query-performance]
related: [ratan, scbml, ratan-cashflow-scbml-history, postgresql-concurrent-index-creation, what-is-the-authoritative-ratan-cashflow-history-index-deployment-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Create Index on  table ratan_cashflow_scbml_history.md"]
---
# Ratan Cashflow History Composite Index

The proposed index for [[ratan-cashflow-scbml-history]] is a three-column PostgreSQL composite index intended for Cashflow Auto Netting-related lookup patterns in [[ratan]].

```sql
CREATE INDEX CONCURRENTLY if not exists ratan_cashflow_scbml_history_active_status_idx ON ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history (cashflow_status, sub_status_event_type,active);
```

## Key order

The defined column order is:

1. `cashflow_status`
2. `sub_status_event_type`
3. `active`

Composite-index usefulness depends on the predicates, joins, sort requirements, and selectivity of the actual application queries. In particular, the leading-column order should be validated against representative Auto Netting workloads.

## Evidence boundary

The source specifies the index definition but provides no SQL workload, `EXPLAIN` or `EXPLAIN ANALYZE` output, baseline latency, cardinality estimate, table size, or post-deployment benchmark. It therefore does not demonstrate that this index improves performance.

The preferred deployment method in the source is described in [[postgresql-concurrent-index-creation]]. Deployment and performance acceptance criteria remain tracked in [[what-is-the-authoritative-ratan-cashflow-history-index-deployment-contract]].