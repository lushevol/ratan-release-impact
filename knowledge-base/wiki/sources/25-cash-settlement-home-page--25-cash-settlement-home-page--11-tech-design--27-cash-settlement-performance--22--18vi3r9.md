---
type: source
title: SQL Performance When Using Bitmap Scan
authors: []
year: 2025
url: "https://www.postgresql.org/message-id/12553.1135634231@sss.pgh.pa.us"
venue: PostgreSQL mailing list reference
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, bitmap-scan, work-mem, cash-settlement, query-performance]
related: [postgresql-work-mem-for-bitmap-scans, postgresql-lossy-bitmap-scans, cashflow-data, explain, postgresql-explain-plan-reading, postgresql-index-bitmap-sequential-scan-selection, cashflow-blotter-query-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance when using bitmap scan.md"]
---
# SQL Performance When Using Bitmap Scan

## Summary

This source records manual `EXPLAIN ANALYZE` tests against `cash_settlement_query_cn.cashflow_data`. The tests compare three cashflow retrieval queries under `work_mem` values of 4 MB, 10 MB, and 30 MB.

The measured execution times improved substantially as `work_mem` increased. For the tested queries and environment, 30 MB was associated with sub-second execution. The source attributes the improvement to avoiding or reducing lossy bitmap behavior, although the underlying plan screenshots are not transcribed and the exact scan nodes require verification.

## Tested SQL

### Query 1

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID')='10075222' and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') between ('2025-04-01') and ('2025-05-07') and jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy')='InterestRate:IRSwap:FixedFloat' order by cfd1_0.created_at desc offset 0 rows fetch first 1000 rows only
```

### Query 2

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where ( jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') in ('READY','RELEASED','SETTLED','CASHFLOW_SUPPRESSED','SWIFT_SUPPRESSED','CANCELLED','ERROR','DEAD','FAILED','NETTED') -- or jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') is null ) and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Is_Commodity')='false' and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMID') in ('40083122', '10037537') -- or jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMID') is null ) and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology') in ('STL-Cust', 'NDF') -- or jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology') is null ) and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy') in ('Credit:Loans:TermLoan') -- or jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy') is null ) and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_Client_Type') not in ('INTEBCH', 'INTECOM', 'INTLACC') or jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_Client_Type') is null ) and jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID')='10075222' order by cfd1_0.created_at desc offset 0 rows fetch first 1000 rows only
```

### Query 3

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology')='NDF' and jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID') = '10075222' and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') in ('READY','RELEASED','SETTLED','CASHFLOW_SUPPRESSED','SWIFT_SUPPRESSED','CANCELLED','ERROR','DEAD','FAILED','NETTED', 'NOSTROMATCH') order by cfd1_0.created_at desc offset 0 rows fetch first 1000 rows only
```

## Benchmark Results

| Query | `work_mem` = 4 MB/default | `work_mem` = 10 MB | `work_mem` = 30 MB |
|---|---:|---:|---:|
| Query 1 | Around 15,000 ms | Around 5,000 ms | Around 400 ms |
| Query 2 | Around 1,600 ms | Around 1,200 ms | Around 400 ms |
| Query 3 | Around 30,000 ms | Around 5,000 ms | Around 600 ms |

Approximate improvement from 4 MB/default to 30 MB was 97% for Query 1, 75% for Query 2, and 98% for Query 3.

## Interpretation

The source explains that a bitmap can become lossy when it exceeds the memory available to the bitmap operation. A lossy bitmap records matching table pages rather than exact tuple locations. PostgreSQL must then inspect rows from those pages and recheck the predicates, increasing CPU and I/O work.

This mechanism is technically plausible for the observed results and is discussed in [[postgresql-lossy-bitmap-scans]] and [[postgresql-work-mem-for-bitmap-scans]]. However, the source does not provide textual plan metrics such as `Heap Blocks: exact`, `Heap Blocks: lossy`, or `Rows Removed by Index Recheck`. The opening description refers to an “Index scan,” while the conclusion refers specifically to a bitmap index scan. The exact scan node should therefore be confirmed with regenerated plan output.

Query 3 remained slower than Queries 1 and 2 at 30 MB. This indicates that query shape, predicate selectivity, matching-row volume, index coverage, table statistics, cache state, or sorting cost may also affect runtime.

## Operational Qualification

The 30 MB result is a benchmark observation, not a universal PostgreSQL setting or proven minimum. `work_mem` is allocated per operation and may be consumed concurrently by multiple sessions and operations. Applying a global increase without capacity analysis could create memory pressure.

Before adopting a production setting, collect textual output from:

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
```

The investigation should record scan node types, exact and lossy heap blocks, index rechecks, actual versus estimated rows, buffer hits and reads, sort method and memory, PostgreSQL version, table size, hardware, concurrency, and cache state.

## Related Wiki Material

This source provides concrete evidence for [[explain]], [[postgresql-explain-plan-reading]], and [[postgresql-index-bitmap-sequential-scan-selection]]. The queries are also relevant to [[cashflow-blotter-query-performance]] and [[value-date-bounded-cashflow-queries]].
