---
type: concept
title: PostgreSQL Concurrent Index Creation
created: 2026-08-23
updated: 2026-08-23
tags: [postgresql, database-indexing, online-schema-change, production-operations]
related: [ratan-cashflow-scbml-history, ratan-cashflow-history-composite-index, what-is-the-authoritative-ratan-cashflow-history-index-deployment-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Create Index on  table ratan_cashflow_scbml_history.md"]
---
# PostgreSQL Concurrent Index Creation

`CREATE INDEX CONCURRENTLY` is a PostgreSQL index-build mode intended to avoid the normal exclusive table lock associated with index creation. It is appropriate for the proposed index on [[ratan-cashflow-scbml-history]] where application availability is a primary concern.

## Operational behavior

A concurrent build enables reads and writes to continue during most of its execution. It does not mean that the operation has no production impact. The build can consume substantial I/O, CPU, disk space, replication capacity, and transaction-management resources. It can also wait for transactions that delay build completion.

The command must be executed outside a transaction block. Deployment tooling must therefore support non-transactional DDL for this operation.

## Failure and retry control

A failed concurrent build can leave an invalid index object. Before retrying, operators should confirm the object state through PostgreSQL catalog metadata and remove the affected index only when the identified index is the failed deployment artifact.

Name-based checks such as `indexname LIKE '%invalid%'` are insufficient because PostgreSQL does not require invalid indexes to have names containing `invalid`.

## Monitoring

`pg_stat_progress_create_index` can expose an active build's phase and progress. Joining it with `pg_stat_activity` adds session identity, start time, duration, database, user, and client details.

```sql
SELECT * FROM pg_stat_progress_create_index;
```

```sql
SELECT 
  p.pid, p.datname, p.usename, p.client_addr,
  p.query_start, now() - p.query_start AS duration,
  i.schemaname, i.indexrelname, i.command,
  i.phase, i.blocks_total, i.blocks_done,
  round(100 * i.blocks_done / NULLIF(i.blocks_total, 0), 2) AS progress_pct
FROM pg_stat_progress_create_index i
JOIN pg_stat_activity p ON i.pid = p.pid;
```

## Deployment prerequisites

Before executing a production build, establish the PostgreSQL version, table size, write rate, replication topology, existing index definitions, disk headroom, target query plans, scheduling constraints, and the cleanup or rollback procedure. See [[what-is-the-authoritative-ratan-cashflow-history-index-deployment-contract]].