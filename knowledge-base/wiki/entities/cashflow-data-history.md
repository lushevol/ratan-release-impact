---
type: entity
title: cashflow_data_history
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-service, database-table, history, postgresql, history-table, cashflow]
related: [cashflow-data, query-service, cash-settlement-cashflow-read-model, what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data, what-is-the-canonical-cashflow-storage-and-history-model, cashflow, postgresql, postgresql-toast-storage, replacement-table-purge-and-swap]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Query Service - cashflow_data_history purge.md"]
---
# `cashflow_data_history`

`cashflow_data_history` is a Cash Settlement Query Service database table associated with historical Cashflow data. It is related to the domain entity [[cashflow]] and to the current query table [[cashflow-data]].

## Role and record shape

According to the Cash Settlement Query Service database design, `cashflow_data_history` has an almost identical denormalized record shape to [[cashflow-data]], including cashflow, trade, entity, portfolio, instrument, SSI, payment-routing, workflow, and provenance fields.

According to the RATANONE purge-design source, the table is the historical Cashflow storage table in the `cash_settlement_query_cn` PostgreSQL schema. In that context, it supports historical retrieval of Cashflow lifecycle and settlement information. Its database representation contains both a `cashflow` JSON payload and extracted `cashflow__*` columns.

The table name and the RATANONE source both indicate a historical role. However, the original Query Service database-design source does not confirm that the table is deployed, append-only, immutable, or an authoritative audit store.

## Schema and lifecycle gaps

The Query Service database-design source defines only:

```sql
id text primary key
```

That source does not define:

- A foreign key or explicit relationship to `cashflow_data`.
- A history sequence or effective-time range.
- A unique business identity and version constraint.
- Retention, archival, or purge rules.
- Write ordering or duplicate-event handling.
- The event or update operation that creates a history row.

The relationship between `cashflow_data` and `cashflow_data_history` is therefore unresolved in the Query Service database-design source. An authoritative rule is needed to establish whether history records represent every source event, every current-row replacement, selected status changes, or another lifecycle boundary.

These questions are tracked in [[what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]] and [[what-is-the-canonical-cashflow-storage-and-history-model]].

## Storage characteristics

The RATANONE purge-design source reports that the table grows rapidly because large historical `jsonb` objects are stored through PostgreSQL TOAST. Reported storage figures are:

| Storage component | Reported size |
|---|---:|
| Total table size | 10 GB |
| Heap table size | 1,648 MB |
| TOAST/index-related size | 8,677 MB |
| Associated TOAST table `pg_toast_1500907339` | 8,446 MB |
| Separately reported indexes | 234 MB |

According to that evidence, the historical JSON payload is the primary storage concern rather than ordinary indexes.

## Proposed slim historical projection

The RATANONE purge-design source proposes a slim representation retaining selected Cashflow identity, version, lifecycle, payment-date, netting, splitting, and NSTP exception fields.

The apparent full column set remains present in the replacement table, while nonessential values are set to `null`. The source does not establish which fields are mandatory for audit, regulatory retention, downstream processing, or user-interface behavior. Null compatibility must therefore be tested before migration.

## Replacement candidate and cutover

The preferred replacement candidate in the RATANONE purge-design source is:

```text
cashflow_data_history_temp_slim_all_column
```

In a one-million-row DEV test, this table measured 537 MB with only 8,192 bytes of TOAST storage, compared with 5,535 MB for the original-payload test table.

The proposed old-table name after cutover is:

```text
cashflow_data_history_purge
```

## Operational caveats

According to the RATANONE purge-design source, a table rename does not by itself address:

- Writes occurring while the replacement table is populated.
- Locks and long-running transactions.
- Grants, ownership, triggers, constraints, sequences, publications, or replica identity.
- Rollback and reconciliation.
- The apparent mismatch in the source DDL, where the primary key is added to `cashflow_data_history` while other indexes target the replacement table.

The production retention period is also unresolved in that source; the three-month predicate appears only in the in-place update experiment.