---
type: source
title: Create Index on ratan_cashflow_scbml_history Table
created: 2026-08-23
updated: 2026-08-23
tags: [postgresql, ratan, cashflow-auto-netting, database-indexing, settlement-day-2]
related: [ratan, scbml, postgresql-concurrent-index-creation, ratan-cashflow-history-composite-index, what-is-the-authoritative-ratan-cashflow-history-index-deployment-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Create Index on  table ratan_cashflow_scbml_history.md"]
authors: []
year: 0
url: ""
venue: ""
---
# Create Index on ratan_cashflow_scbml_history Table

This source proposes adding a composite index to the Ratan cashflow-history table used in the Cashflow Auto Netting context. It recommends an in-place PostgreSQL concurrent index build and also describes a replacement-table migration alternative.

The target data object belongs to the [[ratan]] ecosystem and has an SCBML-oriented history-table name associated with [[scbml]].

## Recommended approach: concurrent index creation

The source recommends creating the index directly on the live table.

```sql
CREATE INDEX CONCURRENTLY if not exists ratan_cashflow_scbml_history_active_status_idx ON ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history (cashflow_status, sub_status_event_type,active);
```

The proposed composite index order is:

1. `cashflow_status`
2. `sub_status_event_type`
3. `active`

The source presents `CONCURRENTLY` as suitable for continuously running production systems because it avoids an exclusive table lock during most of the build and permits normal reads and writes to continue.

This source does not provide the target query patterns, existing index definitions, query plans, data volume, selectivity, or before-and-after performance measurements. Consequently, the expected Auto Netting performance benefit remains unverified. See [[ratan-cashflow-history-composite-index]].

## Source-provided failure handling

```sql
-- check invalid indexes
SELECT * FROM pg_indexes WHERE schemaname = 'ratan_cashflow_lifecycle_service' AND indexname LIKE '%invalid%';

-- delete invalid indexes
DROP INDEX CONCURRENTLY IF EXISTS ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history_active_status_idx;
```

The source notes that a failed concurrent index build can leave an invalid index requiring cleanup before a retry.

The supplied detection query is not an authoritative validity check: index names do not necessarily contain `invalid` when an index is invalid. Deployment validation should inspect PostgreSQL catalog state, including `pg_index.indisvalid`, rather than infer validity from a name pattern.

## Source-provided progress monitoring

```sql
-- View the progress of all indexes that are being created
SELECT * FROM pg_stat_progress_create_index;

-- Detailed monitoring queries
SELECT 
  p.pid, p.datname, p.usename, p.client_addr,
  p.query_start, now() - p.query_start AS duration,
  i.schemaname, i.indexrelname, i.command,
  i.phase, i.blocks_total, i.blocks_done,
  round(100 * i.blocks_done / NULLIF(i.blocks_total, 0), 2) AS progress_pct
FROM pg_stat_progress_create_index i
JOIN pg_stat_activity p ON i.pid = p.pid;
```

These queries provide operational visibility into the index-build session, elapsed duration, phase, and block-level progress.

## Source characterization of `CONCURRENTLY`

The source states that concurrent creation:

- avoids an exclusive table lock;
- uses two table scans, including a second scan for changes since the first;
- may fail without breaking the table;
- has minimal read/write impact;
- requires no maintenance window; and
- is appropriate for 24×7 systems.

These statements should be qualified during production planning. A concurrent index build avoids the normal blocking table lock but may still consume I/O, CPU, storage, replication capacity, and transaction resources. It also must be executed outside a transaction block.

The source lists limitations concerning unique indexes and expression indexes. These are not complete PostgreSQL restrictions: PostgreSQL supports `CREATE UNIQUE INDEX CONCURRENTLY`, subject to uniqueness validation and operational handling. PostgreSQL version and deployment-tool behavior must be confirmed before execution.

## Alternative approach: replacement-table migration

The source also provides a table-copy and rename procedure.

```sql
CREATE TABLE ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history_v2(LIKE ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history INCLUDING all)
```

```sql
CREATE INDEX if not exists ratan_cashflow_scbml_history_active_status_idx ON ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history_v2 (cashflow_status, sub_status_event_type,active);
```

```sql
select * from pg_catalog.pg_indexes where schemaname = 'ratan_cashflow_lifecycle_service' and tablename = 'ratan_cashflow_scbml_history_v2';
```

```sql
INSERT INTO ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history_v2 SELECT * FROM ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history;
```

```sql
ALTER TABLE ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history RENAME TO ratan_cashflow_scbml_history_bak;
ALTER TABLE ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history_v2 RENAME TO ratan_cashflow_scbml_history;
```

```sql
select count(*) from ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history;

select count(*) fromratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history_v2;
```

```sql
select * from pg_catalog.pg_indexes where schemaname = 'ratan_cashflow_lifecycle_service' and tablename = 'ratan_cashflow_scbml_history';
```

This alternative is not a production-ready online migration procedure as documented. The copy can miss concurrent source-table changes, and the source specifies neither synchronization nor a cutover lock strategy. Dependencies such as triggers, grants, foreign keys, views, sequences, and application references require explicit assessment. `LIKE ... INCLUDING all` may also copy indexes, making the explicit index creation redundant or potentially conflicting.

The stated post-cutover count check has a syntax error (`fromfrom`) and references `ratan_cashflow_scbml_history_v2` after that table has been renamed. A valid comparison after cutover would compare the active table with `ratan_cashflow_scbml_history_bak`, but row counts alone do not establish data consistency.

## Operational conclusion

The source preference for `CREATE INDEX CONCURRENTLY` is reasonable as a starting approach, subject to query-plan validation, PostgreSQL-version confirmation, capacity assessment, monitoring, catalog-based validity checks, and a tested cleanup or rollback procedure. The replacement-table approach requires a separately designed, synchronized migration and should not be used as a drop-in fallback.