---
type: comparison
title: Cashflow Data Provider Large-Volume Query Implementations
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, performance-testing, api, streaming, comparison]
related: [cashflow-data-provider, streaming-large-cashflow-query-responses, cashflow-query-connection-pool-capacity, cash-settlement-performance-and-stress-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/PT for big volume query.md"]
---
# Cashflow Data Provider Large-Volume Query Implementations

## Comparison

| Implementation | Retrieval strategy | Response construction | Documented behavior |
|---|---|---|---|
| V1 | Entire result set in one query | Entire response retained and returned together | OOM for documented 300k tests at 4 GB, 8 GB, and 12 GB maximum heap |
| V2 Draft | 10k-row loop queries | All loop results aggregated into one large list | Near maximum JVM memory or OOM; ten-query pool-size-10 case also had JDBC failures |
| V2 Final | 5k-row loop queries | Each chunk converted to bytes and streamed iteratively through Spring MVC | Listed tests reached 1,200k rows without a documented OOM outcome; pool size and query method remained material |

## Trade-offs

V1 is operationally simple but does not scale for the tested response sizes. V2 Draft reduces individual database fetch size but preserves the fundamental heap-retention problem. V2 Final changes the response lifecycle and is the strongest design among the three for server-memory behavior.

V2 Final does not remove database or concurrency constraints. Five simultaneous 500k-row tests had connection-acquisition failures with pool maximum 10 and were recorded as successful with pool maximum 20. At 1,200k rows, the reported `created_at` case took 3,357 seconds, while `cashflow_Ids` cases took 320–334 seconds; the comparison is confounded by different pool sizes and incomplete query-plan information.

## Decision-Relevant Caveats

The source does not define formal latency or throughput acceptance criteria, the test-column meanings, exact loop SQL, response completeness validation, or streaming behavior across proxies and clients. These must be resolved before selecting a production capacity baseline.

See [[what-controls-govern-data-provider-querycondition-sql]] and [[why-is-created-at-ordered-cashflow-query-slower-at-1200k]].