---
type: entity
title: cash_settlement_query_cn.cashflow_data
tags: [cash-settlement, postgresql, cashflow, jsonb, query-table, database-table]
related: [postgresql, jsonb-expression-indexed-query-performance, cashflow-blotter-query-performance, cash-settlement-cashflow-read-model, which-expression-indexes-support-cashflow-data-date-filters-and-sorts, value-date-bounded-cashflow-queries, postgresql-jsonb-expression-index-matching]
created: 2026-08-24
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md"]
---
# cash_settlement_query_cn.cashflow_data

## Role

`cash_settlement_query_cn.cashflow_data` is the PostgreSQL table targeted by documented Cash Settlement staging SQL performance tests and performance investigations. Queries select complete rows from the table and inspect nested values in its `cashflow` JSONB payload, commonly through `jsonb_extract_path_text(...)`.

The *SQL performance in different condition* source reports that `cashflow_data` contains 1,359,511 rows. That source alternates between `cashflow_data` and `cash_settlement_query_cn.cashflow_data` without defining whether they are the same relation.

## Referenced JSONB fields

Across the two sources, queries reference these JSONB paths:

- `Cashflow.Payment_Date`
- `Cashflow.Event_Date`
- `Cashflow.Payment_Amount`
- `Cashflow.Booking_System_Event`
- `Cashflow.Cashflow_State`
- `Cashflow.Is_Commodity`
- `Entity.Booking_Entity_SCI_FMID`
- `Entity.Counterparty_SCI_FMID`
- `Entity.Counterparty_SCI_FMCODE`
- `Instrument_Common.Murex_Product_Typology`
- `Instrument_Common.ISDA_Taxonomy`

The *SQL performance summary* source additionally states that the table's `created_at` column is used for descending result ordering.

## Documented performance observations

The *SQL performance summary* source reports the following behavior by predicate shape:

- A booking-entity-only query is fast.
- Multi-condition queries may use bitmap scans and may incur lossy bitmap rechecks.
- A payment-date-only range query is problematic on certain staging dates.
- Repeated `jsonb_extract_path_text(...)` expressions require suitable expression-index alignment to appear as index conditions rather than post-fetch filters.

More generally, because filter and sort attributes reside in JSONB rather than conventional typed columns, performance depends on exact expression matching, data distribution, query selectivity, and planner access paths. See [[jsonb-expression-indexed-query-performance]], [[postgresql-jsonb-expression-index-matching]], and [[cash-settlement-cashflow-read-model]].

## Source limitations and open details

The *SQL performance in different condition* source does not include index definitions. The relation-name ambiguity and missing index definitions are tracked in [[which-expression-indexes-support-cashflow-data-date-filters-and-sorts]].

The *SQL performance summary* source includes no table definition, index definition, row-count data, or execution plan. Its absence of row-count data applies to that summary source; the separate *SQL performance in different condition* source reports the 1,359,511-row figure above.

See also [[value-date-bounded-cashflow-queries]] and [[cashflow-blotter-query-performance]].