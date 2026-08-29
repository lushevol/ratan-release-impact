---
type: entity
title: ratan_cashflow_scbml_history
created: 2026-08-23
updated: 2026-08-23
tags: [postgresql-table, ratan, cashflow-history, scbml, cashflow-auto-netting]
related: [ratan, scbml, ratan-cashflow-history-composite-index, postgresql-concurrent-index-creation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Create Index on  table ratan_cashflow_scbml_history.md"]
---
# ratan_cashflow_scbml_history

`ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history` is a PostgreSQL cashflow-history table in the [[ratan]] environment. Its name identifies an association with scbml cashflow data.

The source proposes a new index to support lookup patterns involving `cashflow_status`, `sub_status_event_type`, and `active` in the Cashflow Auto Netting context.

```sql
CREATE INDEX CONCURRENTLY if not exists ratan_cashflow_scbml_history_active_status_idx ON ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history (cashflow_status, sub_status_event_type,active);
```

The source does not define the table schema, row volume, current indexes, constraints, retention policy, or the application queries that would use this index. The expected benefit is therefore conditional on actual query predicates and execution plans.

A replacement-table proposal uses `ratan_cashflow_scbml_history_v2` during copying and renames the original table to `ratan_cashflow_scbml_history_bak` at cutover. That procedure requires additional synchronization and dependency controls before production use.