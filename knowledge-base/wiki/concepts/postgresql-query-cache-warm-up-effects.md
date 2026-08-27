---
type: concept
title: PostgreSQL Query Cache Warm-Up Effects
tags: [postgresql, performance-testing, caching, shared-buffers, benchmark-methodology]
related: [postgresql, cash-settlement-query-cn-cashflow-data, jsonb-expression-indexed-query-performance, postgresql-sequential-scan-triage]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md"]
---
# PostgreSQL Query Cache Warm-Up Effects

Repeated PostgreSQL query executions can be faster after relevant table and index pages enter PostgreSQL shared buffers or the operating-system page cache. This effect can materially alter elapsed-time comparisons between a first execution and subsequent executions.

The staging benchmark for [[cash-settlement-query-cn-cashflow-data]] reports multiple cases where later executions fall from seconds to tens or hundreds of milliseconds. The environment reports `shared_buffers: 15972MB`. This pattern is consistent with cache warm-up, but the source does not provide buffer hit/read statistics, cache-reset procedures, fixed execution order, or concurrent workload data.

## Interpretation rules

- Treat cold and warm timings as distinct observations, not interchangeable performance claims.
- Do not use warm timings alone as an application SLA.
- Alternate query variants or reset the test environment where practical to reduce execution-order bias.
- Record both elapsed time and `EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)` output.
- Preserve returned-row counts and plan shapes, because a different plan can explain timing changes independently of caching.

Cache effects may coexist with selectivity, sort cost, JSONB extraction cost, and I/O behavior. They do not establish that a specific index or sort order is superior.