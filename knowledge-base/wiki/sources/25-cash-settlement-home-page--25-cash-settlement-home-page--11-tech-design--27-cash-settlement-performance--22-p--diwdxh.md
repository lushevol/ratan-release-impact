---
type: source
title: SQL Performance Summary
authors: []
year: 2025
url: ""
venue: "Cash Settlement PostgreSQL performance documentation"
tags: [cash-settlement, postgresql, sql-performance, jsonb, query-optimization]
related: [cash-settlement-query-cn-cashflow-data, postgresql, postgresql-lossy-bitmap-scan, postgresql-jsonb-expression-index-matching, postgresql-index-cond-vs-filter, cashflow-blotter-query-performance, value-date-bounded-cashflow-queries, value-date-query-performance-guardrail, does-cashflow-payment-date-search-require-an-ordering-or-index-policy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md"]
---

# SQL Performance Summary

## Scope

This summary documents PostgreSQL query-performance observations for `cash_settlement_query_cn.cashflow_data`. The source compares four query shapes involving JSONB field extraction, filtering, `created_at` ordering, and a 1,000-row limit.

The observations are based on `EXPLAIN ANALYZE` investigations, Kibana slow-query categories, staging behavior, and daily-database data-distribution observations. The source does not include the actual execution plans, timings, index definitions, row counts, or the contents of the referenced charts.

## Referenced material

- [SQL performance using bitmap](https://confluence.global.standardchartered.com/display/DSP/SQL+performance+using+bitmap)
- [SQL performance in different condition](https://confluence.global.standardchartered.com/display/DSP/SQL+performance++in+different+condition)
- [SQL performance with daily database](https://confluence.global.standardchartered.com/display/DSP/SQL+performance+with+daily+database)

## Query categories

### 1. Multiple conditions with `NOT IN`

This query filters by booking entity and excludes several cashflow states, counterparties, product typologies, and an ISDA taxonomy. Each exclusion explicitly permits `NULL`. Results are ordered by descending `created_at`.

The source categorizes this shape as slow and reports that translating the exclusion-oriented predicates into an inclusion-oriented shape moves it toward category 2. That claim requires validation because the rewrite must preserve PostgreSQL `NULL` semantics and the business meaning of the exclusions.

```sql
explain analyse
select
      *
   from
       cash_settlement_query_cn.cashflow_data cfd1_0
   where
        jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID') = '10075222'
  and 
 (
           jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State')  not in ('READY','RELEASED','SETTLED','CASHFLOW_SUPPRESSED','SWIFT_SUPPRESSED','CANCELLED','ERROR','DEAD','FAILED','NETTED', 'NOSTROMATCH')
           or jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Cashflow_State') is null
       )
       and jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Is_Commodity')='false'
       and (
           jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMID')  not in ('40083122', '10037537')
           or jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Counterparty_SCI_FMID') is null
       )
       and (
           jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology') not in ('STL-Cust', 'NDF')
           or jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'Murex_Product_Typology') is null
       )
       and (
           jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy') not in ('Credit:Loans:TermLoan')
           or jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy') is null
       )
 
   order by
        cfd1_0.created_at desc
   offset
       0 rows
   fetch
       first 1000 rows only
```

### 2. Multiple indexed conditions

This query filters by booking entity, a payment-date range, and ISDA taxonomy. The source associates this shape with bitmap-scan behavior and notes that a large bitmap can become lossy. Increasing `work_mem` is presented as a possible optimization, with an operational limit of approximately 30 MB in the Ratan business context.

This should be treated as a plan-dependent hypothesis. Validation requires checking the actual plan for bitmap usage, lossy pages, heap rechecks, latency, and the effect of changing `work_mem`.

```sql
explain analyse
select
   *
    from
       cash_settlement_query_cn.cashflow_data cfd1_0
   where
        jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID')='10075222' 
  and
        jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') between ('2025-04-01') and ('2025-05-07') 
  and
        jsonb_extract_path_text(cfd1_0.cashflow, 'Instrument_Common', 'ISDA_Taxonomy')='InterestRate:IRSwap:FixedFloat'
  order by
        cfd1_0.created_at desc
   offset
       0 rows
   fetch
       first 1000 rows only
```

### 3. Single booking-entity condition

This query filters only by booking entity, orders by descending `created_at`, and returns the first 1,000 rows. The source reports that it is fast in practice and is not considered a SQL issue.

The finding is limited to this query shape and observed environment. It does not establish that all single-condition queries are fast.

```sql
explain analyse
select
      *
   from
       cash_settlement_query_cn.cashflow_data cfd1_0
   where
  jsonb_extract_path_text(cfd1_0.cashflow, 'Entity', 'Booking_Entity_SCI_FMID') = '10075222'  
   order by
        cfd1_0.created_at desc
   offset
       0 rows
   fetch
       first 1000 rows only
```

### 4. Single payment-date range condition

This query filters only by payment date, orders by descending `created_at`, and returns the first 1,000 rows. The source reports that the issue occurs only on certain dates in staging. It proposes replacing `created_at` in the `ORDER BY` clause with a column used by the filter or an appropriate index.

That change may alter the user-visible ordering contract. It should not be adopted without confirming that payment-date ordering or another predicate-aligned ordering is acceptable.

```sql
explain analyse
select
      *
 from
       cash_settlement_query_cn.cashflow_data cfd1_0
   where
       jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date') between ('2025-04-01') and ('2025-05-07')
   order by
       cfd1_0.created_at desc
   offset
       0 rows
   fetch
       first 1000 rows only
```

## Recorded conclusions and qualifications

- PostgreSQL can choose among available execution plans, but adding more indexed predicates is not universally better. Indexes also impose write, storage, maintenance, and planning costs.
- Multi-condition queries may use bitmap scans. A bitmap may become lossy when it is too large, causing additional heap-page rechecks. `work_mem` changes should be measured and considered against concurrent-session memory consumption.
- An `ORDER BY` aligned with a selective predicate or suitable index may improve performance, but changing from `created_at DESC` can change result semantics.
- Expression indexes require immutable expressions, and the query expression must match the indexed expression sufficiently for the planner to use it. The source's statement that immutable functions cannot be used by indexes is too broad.
- Conditions represented as `Index Cond` can reduce the rows fetched from the table. Conditions represented as `Filter` are evaluated after row or page retrieval and may require more data to be fetched and discarded.
- Query performance depends jointly on selectivity, data distribution, index definitions, ordering, cache state, concurrency, and planner choice.

## Evidence limitations

The source does not provide:

- Actual `EXPLAIN ANALYZE` output
- Query latency or percentile measurements
- Table and index definitions
- Estimated and actual row counts
- Lossy bitmap indicators or heap recheck counts
- `work_mem` values before and after testing
- Data-volume values represented by the attached charts
- Confirmation that changing `ORDER BY` preserves product requirements

The staging-only observation for the payment-date query should not be treated as a production acceptance result without comparable data volume and distribution.

## Validation questions

1. Which expression and ordering indexes exist on `cash_settlement_query_cn.cashflow_data`?
2. Do the plans for category 2 contain a lossy bitmap and heap rechecks?
3. What latency change results from each tested `work_mem` value?
4. What exact rewrite converts category 1 into the proposed category-2 shape?
5. Are `NULL` values intentionally included by every exclusion predicate?
6. Can `created_at DESC` be replaced without changing the API or UI ordering contract?
7. Should payment-date searches require a booking-entity predicate or a maximum date range?
8. Would generated columns or normalized relational fields be preferable for frequently queried JSONB attributes?

## Related wiki pages

- [[concepts/postgresql-sequential-scan-triage]]
- [[concepts/postgresql-lossy-bitmap-scan]]
- [[concepts/postgresql-jsonb-expression-index-matching]]
- [[concepts/postgresql-index-cond-vs-filter]]
- [[concepts/cashflow-blotter-query-performance]]
- [[concepts/value-date-bounded-cashflow-queries]]
- [[comparisons/cashflow-query-indexing-options]]
- [[queries/does-cashflow-payment-date-search-require-an-ordering-or-index-policy]]