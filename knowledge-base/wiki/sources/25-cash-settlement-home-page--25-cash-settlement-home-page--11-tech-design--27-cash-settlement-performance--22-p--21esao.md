---
type: source
title: SQL Performance in Different Conditions
authors: []
year: 2025
url: ""
venue: "Cash Settlement Performance"
tags: [cash-settlement, postgresql, performance-testing, jsonb, staging]
related: [cash-settlement-query-cn-cashflow-data, postgresql, jsonb-expression-indexed-query-performance, postgresql-query-cache-warm-up-effects, which-expression-indexes-support-cashflow-data-date-filters-and-sorts, are-cashflow-blotter-negative-predicate-rewrites-semantically-safe, postgresql-sequential-scan-triage, cashflow-blotter-query-performance, cashflow-blotter-query-optimization-options, cash-settlement-cashflow-read-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md"]
---
# SQL Performance in Different Conditions

This source records exploratory staging benchmarks for queries against [[cash-settlement-query-cn-cashflow-data]]. It compares ordering by `created_at DESC` with ordering by JSONB-extracted filter fields under date, numeric, positive, and negative predicate shapes.

The evidence is preliminary. The original comparison tables have detached timing rows and inconsistent layout, and the referenced `EXPLAIN ANALYZE` screenshots are not available as text. Exact index DDL, PostgreSQL version, plan nodes, row estimates, buffer statistics, sort methods, and concurrent workload are not recorded.

## Test environment

```text
stag_host: uklvaddbs097.uk.dev.net
stag_port: 6524
stag_user: ratanone_stg
stag_database: ratanone_staging

table: cashflow_data
table data volume(cashflow_data): 1359511

work_mem: 4MB
shared_buffers: 15972MB
```

The source reports approximately 77,000 rows for 2025-03-18 and 250,000 rows for 2025-03-19. It uses both the unqualified table name `cashflow_data` and `cash_settlement_query_cn.cashflow_data`; their precise relationship is not stated.

## Representative SQL

```sql
explain analyse
select
      cfd1_0.xxxx,
      cfd1_0...
      cfd1_0...
      cfd1_0...,
      cfd1_0.updated_at
    from
        xxx_data cfd1_0
    where
        jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') between ('2025-03-19') and ('2025-03-19')
    order by
        cfd1_0.created_at desc
    offset
        0 rows
    fetch
        first 1000 rows only;
```

## Recorded query shapes

### Payment_Date, one-day range

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') between ('2025-03-19') and ('2025-03-19') order by jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') desc offset 0 rows fetch first 1000 rows only
```

### Payment_Date, seven-day range

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') between ('2025-03-19') and ('2025-03-25') order by jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') desc offset 0 rows fetch first 1000 rows only
```

### Event_Date range

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Event_Date') between ? and ?
```

The source explicitly states that no index exists on `Event_Date`.

### Payment amount

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where to_number(jsonb_extract_path_text (cfd1_0.cashflow, 'Cashflow', 'Payment_Amount'), '99999999999999999.999999')<=10000000::numeric
```

### Booking_System_Event

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where ( jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Booking_System_Event')<>'' or jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Booking_System_Event') is null )
```

The source explicitly states that no index exists on `Booking_System_Event`.

### Complex negative predicates

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where ( jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') not in ('READY','RELEASED','SETTLED','CASHFLOW_SUPPRESSED','SWIFT_SUPPRESSED','CANCELLED','ERROR','DEAD','FAILED','NETTED') or jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') is null ) and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Is_Commodity')='false' and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMID') not in ('40083122', '10037537') or jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMID') is null ) and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology') not in ('STL-Cust', 'NDF') or jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology') is null ) and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy') not in ('Credit:Loans:TermLoan') or jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy') is null ) and ( jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_Client_Type') not in ('INTEBCH', 'INTECOM', 'INTLACC') or jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_Client_Type') is null ) and jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID')='10075222' order by cfd1_0.created_at desc offset 0 rows fetch first 1000 rows only
```

### Selective positive predicates

```sql
explain analyse select * from cash_settlement_query_cn.cashflow_data cfd1_0 where jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') in ('WAITING') and jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID') in ('400001378', '10020899') and jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMCODE') not in ('SHANGHAI CLE HOU*SHA') -- and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date')='2025-03-18' -- and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_Sub_State') in ('Pending Operator') order by -- jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') desc -- cfd1_0.id desc -- cfd1_0.created_at desc -- jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMCODE') -- jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID') offset 0 rows fetch first 1000 rows only
```

## Reported observations

| Scenario | Reported timings | Interpretation boundary |
|---|---|---|
| One-day `Payment_Date` | JSONB `Payment_Date` ordering was reported at 1.1–1.5 s cold and 50–100 ms warm in one run, while `created_at` ordering was 20–40 s. Other rows report `created_at` at 0.7–1.0 s and JSONB ordering at up to 5 s cold. | The source does not establish a stable winner. |
| Seven-day `Payment_Date` | Results range from approximately 200 ms to 8 s depending on run, date volume, and execution repetition. | The two orderings appear broadly comparable, but testing was not controlled. |
| `Event_Date` | Several runs took approximately 14–21 s for either sort, while ordering by `Event_Date` reached 40–50 s in some runs. | The absent index is a plausible factor but is not proven as the sole cause. |
| Numeric payment amount | `created_at` ordering was approximately 50 ms; ordering by the condition field was approximately 500 ms cold and 100 ms warm. | Casting via `to_number(...)` must match any candidate expression index exactly. |
| `Booking_System_Event` | `created_at` ordering was approximately 50–100 ms; ordering by the condition field was approximately 30–40 s. | A broad predicate and missing index were reported. |
| Complex `NOT IN` predicates | Approximately 40 s cold and 30 s warm. The undocumented “all `IN`” alternative was approximately 15 s cold and 100 ms warm. | The rewrite must not be accepted without semantic-equivalence review. |
| Positive filter case | Approximately 14 s cold and 2.8 s warm before the reported rewrite, then approximately 100 ms for both runs afterward. | The source changed predicates and sort order, so it cannot isolate one causal factor. |

## Findings to carry forward

- JSONB filtering and sorting should be validated through matching expression indexes and actual plans; see [[jsonb-expression-indexed-query-performance]].
- High `Rows Removed by Filter` values are useful signals for investigating inefficient access paths, but they are not independent proof of the source of elapsed time. See [[postgresql-sequential-scan-triage]].
- Repeated executions were often faster, consistent with shared-buffer or operating-system cache effects. These warm timings are not production latency guarantees; see [[postgresql-query-cache-warm-up-effects]].
- Text date comparisons depend on a stable lexically sortable representation such as ISO `YYYY-MM-DD`.
- Changing `NOT IN (...) OR ... IS NULL` to `IN (...)` can change business behavior because SQL null semantics and future reference-data values matter.

## Required follow-up evidence

Capture each representative case with:

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)
```

For every run, retain index DDL, PostgreSQL version, parameters, returned-row count, execution sequence, cache condition, concurrent activity, and pagination offset. Resolve [[which-expression-indexes-support-cashflow-data-date-filters-and-sorts]] before treating these results as an indexing recommendation, and resolve [[are-cashflow-blotter-negative-predicate-rewrites-semantically-safe]] before adopting predicate rewrites.