---
type: source
title: DB High CPU Usage Investigation - Since Feb.16th Midnight
authors: []
year: 2025
url: ""
venue: Internal technical design documentation
tags: [cash-settlement, ratan, postgresql, performance, database-cpu, indexing]
related: [cash-settlement-batch-job-performance, postgresql-sequential-scan-triage, lifecycle-precheck-database-performance, are-lifecycle-precheck-indexes-proven-by-query-plans, which-cash-settlement-indexes-were-deployed-on-february-16-and-what-was-the-effect-of-each, is-ratan-stella-message-event-source-trade-id-index-misnamed, ratan, postgresql, cashflow-lifecycle-service, group-service, orchestration, rule-service, adaptor, postgresql-backup-ddl-lock-contention, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--aw6os5]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/DB High CPU Usage Investigation - Since Feb.16th Midnight.md"]
---
# DB High CPU Usage Investigation - Since Feb.16th Midnight

This internal investigation examines high PostgreSQL CPU utilisation during [[ratan]] inbound cashflow and batch-payment processing. It reports production observations following a 16 February index release, controlled service-isolation tests, a sequential-scan triage query, and a proposed seven-index creation and rollback script.

## Reported production CPU change

The source counts CPU samples above 90%, with the scan tool sampling every 30 seconds.

| Date | High CPU peak times above 90% |
| --- | ---: |
| Tue Feb 04 | 124 |
| Wed Feb 05 | 208 |
| Thu Feb 06 | 297 |
| Mon Feb 17 | 27 |

The source states that the 16 February enhancement materially reduced peak frequency and that netting-related peaks disappeared. Residual high CPU remained, so the report continued with reproduction and isolation testing.

This is evidence of an operational improvement, but it is not a throughput-normalised controlled comparison: dates, workloads, concurrency, database configuration, and transaction volumes are not provided.

## Reproduction and service isolation

A generated batch file containing 1,000 payments was used to reproduce the issue. Subsequent isolation tests sent 500 cashflows while selected services were stopped or started.

- Test case 1 associated CPU above 90% with configurations involving [[adaptor]], [[group-service]], and later orchestration. The source excluded [[rule-service]] in this test but retained workflow, message-event, and lifecycle processing as suspects.
- Test case 2, after adaptor and group fixes, retained lifecycle and [[orchestration]] as suspects while excluding message-event.
- Test case 3 kept CPU below 30% when lifecycle was stopped and orchestration was started after sending 500 cashflows. The source therefore excluded orchestration as the direct issue under this setup.
- Test case 4 ran five status-update batches of 200 items with orchestration stopped; CPU remained below 30%. The source therefore distinguished the Lifecycle Service status-update API from the implicated precheck API.

The evidence narrows the leading residual suspect to Lifecycle Service precheck activity, documented by [[lifecycle-precheck-database-performance]]. It does not establish a definitive database root cause because request traces, SQL statements, query plans, wait events, lock statistics, cache state, and controlled load characteristics are absent.

## Sequential-scan triage

The report reviewed database operations and used `pg_stat_user_tables` to identify large tables with sequential scans. It named the following as two main contributors:

```sql
-- static service
CREATE INDEX if not exists ratan_static_cashflow_currency_holiday_iso_currency_code_idx ON ratanone.ratan_static_cashflow_currency_holiday USING btree (iso_currency_code, version, ratan_label);

-- lifecycle service
CREATE INDEX if not exists ratan_stella_message_event_source_originating_trade_id_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (originating_trade_id);
```

The source-recorded scan-rate query is preserved below.

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

As captured in [[postgresql-sequential-scan-triage]], these aggregate counters are useful for prioritising tables but cannot attribute scans to a particular API call or time period. Query-level traces and `EXPLAIN (ANALYZE, BUFFERS)` are needed to prove that a targeted index supports a costly precheck query.

## Reported performance test result

The source compares two stated test periods:

- Before indexing: one 5,000-payment batch caused database CPU to reach 90%.
- After indexing: “4X PT” processed 30,000 payments in one hour while database CPU remained below 60%.

The result indicates materially improved CPU headroom, but “4X PT” is undefined and the workloads are not clearly comparable. The source provides no latency percentiles, I/O metrics, error rates, query plans, or confirmation that every listed index was deployed before the latter test. It contributes bounded evidence to [[cash-settlement-batch-job-performance]].

## Index creation and rollback script

The source’s full proposed DDL is retained verbatim. The use of `CREATE INDEX IF NOT EXISTS` does not establish deployment status or rollout safety. In particular, the source does not address concurrent index build mode, locking, disk capacity, replication impact, write overhead, or migration-window controls; these concerns are adjacent to [[postgresql-backup-ddl-lock-contention]].

```sql
-- group service
CREATE INDEX if not exists idx_cashflow_group_mxg_trade_id ON ratan_cashflow_group_management_service.ratan_cashflow_group USING btree (mxg_trade_id);
CREATE INDEX if not exists idx_status_sync_blocking_queue_cfid_bizversion ON ratan_cashflow_group_management_service.ratan_cashflow_status_sync_up_blocking_queue USING btree (cashflow_id, business_version);
CREATE INDEX if not exists idx_status_sync_blocking_queue_exceptionId ON ratan_cashflow_group_management_service.ratan_cashflow_status_sync_up_blocking_queue USING btree (exception_id);

-- static service
CREATE INDEX if not exists ratan_static_cashflow_currency_holiday_iso_currency_code_idx ON ratanone.ratan_static_cashflow_currency_holiday USING btree (iso_currency_code, version, ratan_label);

-- adaptor service
CREATE INDEX if not exists mxg_cashflow_cancel_record_trn_original_id_status_idx ON rantan_mxg_cashflow_adaptor.mxg_cashflow_cancel_record USING btree (trn_original_id, flow_id, status);

-- lifecycle service
CREATE INDEX if not exists ratan_stella_message_event_source_trade_id_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (settlement_date);
CREATE INDEX if not exists ratan_stella_message_event_source_originating_trade_id_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (originating_trade_id);
CREATE INDEX if not exists ratan_stella_message_event_source_trade_id_major_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (trade_id, major_version);

-------------------- rollback --------------------
-- group service
DROP INDEX if exists idx_cashflow_group_mxg_trade_id;
DROP INDEX if exists idx_status_sync_blocking_queue_cfid_bizversion;
DROP INDEX if exists idx_status_sync_blocking_queue_exceptionId;

-- static service
DROP INDEX if exists ratan_static_cashflow_currency_holiday_iso_currency_code_idx;

-- adaptor service
DROP INDEX if exists mxg_cashflow_cancel_record_trn_original_id_status_idx;

-- lifecycle service
DROP INDEX if exists ratan_stella_message_event_source_trade_id_idx;
DROP INDEX if exists ratan_stella_message_event_source_originating_trade_id_idx;
DROP INDEX if exists ratan_stella_message_event_source_trade_id_major_idx;
```

## Unresolved points

- The body calls out two main contributors, but the appendix proposes seven indexes across Group Service, Static Service, Adaptor Service, and Lifecycle Service.
- The report does not identify which indexes were actually released on 16 February, their rollout order, or the measured effect of each.
- `ratan_stella_message_event_source_trade_id_idx` is defined on `settlement_date`, creating an index-name and indexed-column mismatch.
- The adaptor schema name is recorded as `rantan_mxg_cashflow_adaptor`; its spelling should be confirmed before operational use.
- Additional indexes may impose write amplification, storage, autovacuum, replication, and backup/migration costs not evaluated in the source.