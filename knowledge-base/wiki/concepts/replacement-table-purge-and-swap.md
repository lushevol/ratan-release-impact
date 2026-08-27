---
type: concept
title: Replacement-Table Purge and Swap
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, data-retention, table-migration, cutover, cash-settlement]
related: [cashflow-data-history, postgresql, postgresql-jsonb-history-payload-slimming, postgresql-toast-storage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Query Service - cashflow_data_history purge.md"]
---
# Replacement-Table Purge and Swap

## Definition

Replacement-table purge and swap is a database-maintenance technique in which a compact replacement table is populated from an existing table, indexed and validated, and then renamed into the original table's name.

For `cashflow_data_history`, the proposed sequence is:

```sql
alter table cash_settlement_query_cn.cashflow_data_history
    rename to cashflow_data_history_purge;

alter table cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column
    rename to cashflow_data_history;
```

## Rationale

The technique avoids the temporary table growth observed during a large in-place `jsonb` update. In the DEV test, the selected replacement candidate had a total size of 537 MB for one million rows and only 8,192 bytes of TOAST storage.

Preserving the apparent column set while nulling nonessential values is intended to reduce application and entity-definition changes.

## Required safeguards

The source does not define a production-ready cutover procedure. A safe implementation must address:

- Writes arriving during replacement-table population.
- Atomicity and lock duration of the rename.
- Long-running transactions.
- Canonical column types and constraints.
- Primary keys, indexes, triggers, grants, ownership, sequences, and publications.
- Replica identity and replication behavior.
- Row-count and content reconciliation.
- Backup and rollback.
- Retention and disposal of `cashflow_data_history_purge`.

The source's primary-key DDL targets `cashflow_data_history`, while the other proposed indexes target `cashflow_data_history_temp_slim_all_column`; this inconsistency requires correction before execution.