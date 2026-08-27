---
type: entity
title: cash_settlement_query_cn.cashflow_data
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, cash-settlement, cashflow, jsonb, query-table]
related: [postgresql-work-mem-for-bitmap-scans, postgresql-lossy-bitmap-scans, cashflow-blotter-query-performance, value-date-bounded-cashflow-queries]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance when using bitmap scan.md"]
---
# cash_settlement_query_cn.cashflow_data

## Role

`cash_settlement_query_cn.cashflow_data` is the PostgreSQL table queried in all three bitmap-scan performance tests documented by the source.

The queries read the `cashflow` JSONB column, filter nested business values, sort by `created_at DESC`, and return up to 1,000 rows.

## Observed Query Fields

The tested predicates extract values from these JSONB paths:

- `Entity.Booking_Entity_SCI_FMID`
- `Cashflow.Payment_Date`
- `Cashflow.Cashflow_State`
- `Cashflow.Is_Commodity`
- `Entity.Counterparty_SCI_FMID`
- `Instrument_Common.Murex_Product_Typology`
- `Instrument_Common.ISDA_Taxonomy`
- `Entity.Counterparty_Client_Type`

The source does not provide the table DDL, row count, index definitions, PostgreSQL version, or statistics. Index coverage and data distribution therefore remain important unknowns when interpreting the benchmark.

## Performance Context

At the tested `work_mem` values, approximate runtimes ranged from 400 ms to 30,000 ms depending on query shape and memory setting. See [[postgresql-work-mem-for-bitmap-scans]] and the original benchmark source for the complete SQL and results.
