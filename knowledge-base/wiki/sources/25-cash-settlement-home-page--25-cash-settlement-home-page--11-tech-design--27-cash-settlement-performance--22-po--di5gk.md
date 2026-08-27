---
type: source
title: PostgreSQL work_mem and to_number_ratan() Performance Risk Analysis
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, cash-settlement, performance, work-mem, jsonb, query-service]
related: [postgresql-work-mem-sizing, jsonb-numeric-expression-indexing, to-number-ratan, query-service, ultra-cashflow-query, cash-settlement-performance-and-stress-testing, postgresql-sequential-scan-triage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md"]
---
# PostgreSQL work_mem and to_number_ratan() Performance Risk Analysis

## Summary

This source evaluates two PostgreSQL performance changes for the Cash Settlement query workload:

1. Increasing `work_mem` from 4 MB to 30 MB for query-service sessions to reduce lossy bitmap index scans.
2. Introducing the user-defined function `to_number_ratan()` so numeric values extracted from the JSONB `cashflow` column can be indexed with a PostgreSQL expression index.

The tests used approximately four million rows in `CASH_SETTLEMENT_QUERY_CN.CASHFLOW_DATA` and a 500-user query-service load test through `cashflowUltraQuery`.

## Memory estimate

The documented planning estimate is:

```text
40 connections × 6 query-service instances × (30 MB − 4 MB)
= 240 × 26 MB
= 6,240 MB
= 6.24 GB
```

The production PostgreSQL machine is described as having 64 GB of memory and approximately 55% baseline usage. The source estimates approximately 64% usage after the change and concludes that the change is safe under that assumption.

This is a simplified estimate rather than a strict upper bound. PostgreSQL can allocate `work_mem` per operation, and one query may contain multiple memory-consuming operations or parallel workers.

## SQL performance tests

### Numeric JSONB filtering

The tested query was:

```sql
SELECT *
FROM CASH_SETTLEMENT_QUERY_CN.CASHFLOW_DATA CFD1_0
WHERE CASH_SETTLEMENT_QUERY_CN.TO_NUMBER_RATAN(
    JSONB_EXTRACT_PATH_TEXT(
        CFD1_0.CASHFLOW,
        'Cashflow',
        'Payment_Amount'
    ),
    '99999999999999999.999999'
) = 43454.7
ORDER BY CFD1_0.CREATED_AT DESC
LIMIT 1000;
```

The reported execution times were:

| Implementation | Execution time |
| --- | ---: |
| Before, using the `created_at` index | 339,321.217 ms |
| After, using the `to_number_ratan()` expression index | 0.323 ms |

The result is a dramatic directional improvement for this query shape. The source does not include the exact function definition, expression-index DDL, execution plans, cache state, or row-count validation, so the result should not be generalized without further verification.

### Bitmap index scan

The tested query was:

```sql
EXPLAIN ANALYZE
SELECT *
FROM CASH_SETTLEMENT_QUERY_CN.CASHFLOW_DATA CFD1_0
WHERE JSONB_EXTRACT_PATH_TEXT(
          CFD1_0.CASHFLOW,
          'Entity',
          'Booking_Entity_SCI_FMID'
      ) = '10075222'
  AND JSONB_EXTRACT_PATH_TEXT(
          CFD1_0.CASHFLOW,
          'Cashflow',
          'Payment_Date'
      ) BETWEEN ('2025-04-01') AND ('2025-05-07')
  AND JSONB_EXTRACT_PATH_TEXT(
          CFD1_0.CASHFLOW,
          'Instrument_Common',
          'ISDA_Taxonomy'
      ) = 'InterestRate:IRSwap:FixedFloat'
  AND JSONB_EXTRACT_PATH_TEXT(
          CFD1_0.CASHFLOW,
          'Cashflow',
          'Is_Commodity'
      ) = 'false'
  AND JSONB_EXTRACT_PATH_TEXT(
          CFD1_0.CASHFLOW,
          'Entity',
          'Counterparty_Client_Type'
      ) IN ('INTEBCH', 'INTECOM', 'INTLACC')
ORDER BY CFD1_0.CREATED_AT DESC
LIMIT 1000;
```

The reported execution times were:

| Configuration | Execution time |
| --- | ---: |
| `work_mem = 4MB` | 10,073.726 ms |
| `work_mem = 30MB` | 534.751 ms |

This is approximately an 18.8× speedup for the tested query. The source attributes the improvement to avoiding lossy bitmap scan behavior.

## Query-service load tests

The application tests used 500 users and replayed GraphQL requests with JMeter. Requests were captured through GraphiQL at:

```text
http://localhost:9006/graphiql?path=/graphql
```

### Numeric-field query

The query filtered `Cashflow.Payment_Amount` for `43454.7` through `cashflowUltraQuery`.

| Metric | Before, no numeric-field index | After, expression index on `to_number_ratan()` |
| --- | ---: | ---: |
| QPS | 5.4, mostly invalid because requests took minutes | 45.4 |

The QPS comparison is directional only because the baseline contained mostly invalid or incomplete results.

### Bitmap-index query

The query combined booking entity, payment date, ISDA taxonomy, commodity status, and counterparty client type filters.

| Metric | Before, `work_mem=4MB` | After, `work_mem=30MB` |
| --- | ---: | ---: |
| QPS | 5.5, mostly invalid because of database connection timeouts | 24.7 |
| Memory | 33.3 GB → 34.5 GB | 33.3 GB → 35.3 GB |

The load test indicates improved post-change throughput, but the baseline is not a clean successful-throughput benchmark. The memory measurements also do not establish equivalent test duration, cache state, completion rate, or workload distribution.

## Risk assessment

The source supports these narrow conclusions:

- The `to_number_ratan()` expression-index approach can make the tested numeric JSONB query practical.
- Increasing `work_mem` to 30 MB materially improved the tested bitmap-index query.
- The observed test-environment memory increase was not obviously hazardous.

Further validation is required for:

- The exact volatility declaration and implementation of `to_number_ratan()`.
- Null, malformed, negative, high-precision, and locale-sensitive numeric values.
- Actual execution plans and confirmation that the intended indexes are used.
- Index write and storage overhead.
- Sustained production-like concurrency and mixed query workloads.
- Multiple `work_mem` consumers and parallel query workers.
- Monitoring thresholds and rollback criteria.

These findings extend [[concepts/cash-settlement-performance-and-stress-testing]] with PostgreSQL-specific evidence and are directly relevant to [[entities/ultra-cashflow-query]].
