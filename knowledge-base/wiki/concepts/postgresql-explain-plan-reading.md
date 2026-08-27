---
type: concept
title: PostgreSQL EXPLAIN Plan Reading
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, explain, query-plans, performance-diagnostics]
related: [explain, postgresql-query-lifecycle, postgresql-index-bitmap-sequential-scan-selection, postgresql-sequential-scan-triage, cashflow-blotter-query-performance, value-date-query-performance-guardrail]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL Explain.md"]
---
# PostgreSQL EXPLAIN Plan Reading

## Plan-tree structure

A PostgreSQL query plan is a tree of plan nodes. Scan nodes at the bottom commonly retrieve rows from tables or indexes. Higher nodes perform operations such as joins, aggregation, sorting, limits, and other transformations.

`EXPLAIN` usually reports one summary line per node with:

- Node type
- Startup cost
- Total cost
- Estimated output rows
- Additional properties and conditions

## Cost interpretation

- **Startup cost:** Estimated work before the first tuple is returned.
- **Run cost:** Estimated work required to fetch all tuples.
- **Total cost:** Startup cost plus run cost.

Costs are relative planner units, conventionally anchored by `seq_page_cost = 1.0`. They are not milliseconds and should not be read as elapsed time. Parent-node costs include child-node costs, while client-side result transmission is excluded. The `rows` estimate describes rows emitted by the node, not necessarily rows physically scanned.

Planner cost constants include `seq_page_cost`, `random_page_cost`, `cpu_tuple_cost`, `cpu_index_tuple_cost`, and `cpu_operator_cost`. Their relative values influence plan selection. `random_page_cost` is not a direct measurement of current cache state; it is a configurable model of expected random-access cost and caching behavior.

## `Index Cond` and `Filter`

Conditions shown as `Index Cond` constrain index-driven retrieval. Conditions shown as `Filter` are evaluated after candidate rows have been retrieved. A filter may reduce the number of emitted rows while leaving much of the scan work unchanged.

When reviewing a slow query, check:

1. Whether the predicate is usable by the chosen index.
2. Whether estimated rows are plausible.
3. Whether a large candidate set is discarded by a post-retrieval filter.
4. Whether the index order can satisfy `ORDER BY`.
5. Whether `LIMIT` changes the desirable startup-cost trade-off.

## Estimated versus actual behavior

Plain [[explain]] displays estimates. For controlled diagnosis, use `EXPLAIN (ANALYZE, BUFFERS)` to compare:

- Estimated rows with actual rows.
- Estimated costs with measured execution time.
- Planned scan behavior with buffer hits, reads, and temporary activity.

Large estimate errors may indicate stale or insufficient statistics, data skew, correlated predicates, an unsuitable query shape, or configuration assumptions that do not match the workload.

## Safety and limitations

`EXPLAIN (ANALYZE)` executes the statement. It should therefore be used with appropriate safeguards for writes, production traffic, locks, and returned data volume. A plan observed in development is not proof of production behavior.

This guidance supports [[postgresql-sequential-scan-triage]], [[cashflow-blotter-query-performance]], and [[value-date-query-performance-guardrail]] but does not validate any particular production index or service-level objective.