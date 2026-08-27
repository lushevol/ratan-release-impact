---
type: concept
title: PostgreSQL Sequential-Scan Triage
tags: [postgresql, performance, sequential-scan, index-optimization, observability]
related: [postgresql, lifecycle-precheck-database-performance, are-lifecycle-precheck-indexes-proven-by-query-plans, postgresql-backup-ddl-lock-contention, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--56--11z02tq]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/DB High CPU Usage Investigation - Since Feb.16th Midnight.md"]
---
# PostgreSQL Sequential-Scan Triage

PostgreSQL sequential-scan triage is a prioritisation method that identifies large tables with comparatively frequent sequential scans and low relative index usage. The investigated RATAN workload used `pg_stat_user_tables` to select tables with more than 100,000 live tuples and more than 10 sequential scans, then ordered them by an index-scan percentage.

```sql
select
	*
from
	(
	select
		round(cast(coalesce(idx_scan, 0) as numeric)/ cast ((seq_scan + coalesce(idx_scan, 0)) as numeric), 4) as index_scan_percentage,
		*
	from
		pg_stat_user_tables
	where
		n_live_tup > 100000
		and seq_scan > 10
	order by
		seq_scan desc ) a
order by
	a.index_scan_percentage asc;
```

## Intended use

The heuristic can identify candidates for investigation, including tables accessed by [[cashflow-lifecycle-service]], [[group-service]], static-service processing, and [[adaptor]]. In the source investigation, it motivated indexes on cashflow group, status-sync queue, holiday-currency, cancellation-record, and lifecycle message-event-source tables.

## Limits

`pg_stat_user_tables` counters are cumulative since the last statistics reset and are not linked to an API, a particular time window, a specific SQL statement, or a CPU spike. A sequential scan can also be optimal when a query returns a large fraction of a table.

Before treating an index as a confirmed remediation, validate:

- the exact SQL and predicates executed by the affected API;
- `EXPLAIN (ANALYZE, BUFFERS)` before and after the change;
- table cardinality and predicate selectivity;
- index size, build duration, and disk capacity;
- write-path, autovacuum, replication, and maintenance effects.

Index creation is DDL and should be assessed separately from the workload diagnosis; see [[postgresql-backup-ddl-lock-contention]].