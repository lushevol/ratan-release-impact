---
type: query
title: Are Lifecycle Precheck Indexes Proven by Query Plans?
tags: [postgresql, lifecycle-service, precheck, indexes, query-plans, performance]
related: [lifecycle-precheck-database-performance, postgresql-sequential-scan-triage, cashflow-lifecycle-service, postgresql, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--56--11z02tq]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/DB High CPU Usage Investigation - Since Feb.16th Midnight.md"]
---
# Are Lifecycle Precheck Indexes Proven by Query Plans?

The source associates Lifecycle Service precheck activity with residual database CPU spikes and proposes indexes on `ratan_cashflow_lifecycle_service.ratan_stella_message_event_source`. It does not provide query text or plan evidence showing that the precheck API uses these indexes.

## Evidence needed

- Captured precheck SQL statements and bind-value shapes under representative load.
- `EXPLAIN (ANALYZE, BUFFERS)` before and after index deployment.
- A mapping from each query predicate and join to the relevant index.
- Table cardinality, value distribution, and predicate selectivity.
- Index usage, buffer reads, latency, and CPU metrics under comparable workload.
- Write-path and operational effects, including index size, autovacuum, replication, and build safety.

## Candidate indexes

```sql
CREATE INDEX if not exists ratan_stella_message_event_source_trade_id_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (settlement_date);
CREATE INDEX if not exists ratan_stella_message_event_source_originating_trade_id_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (originating_trade_id);
CREATE INDEX if not exists ratan_stella_message_event_source_trade_id_major_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (trade_id, major_version);
```

The first index’s name and indexed column should be resolved separately in [[is-ratan-stella-message-event-source-trade-id-index-misnamed]].