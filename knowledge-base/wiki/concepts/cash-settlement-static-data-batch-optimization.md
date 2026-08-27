---
type: concept
title: Cash Settlement Static-Data Batch Optimization
tags: [cash-settlement, static-data, batching, sql, database-performance, materialize, currency-cutoff]
related: [51358-ratanone-static-data-service, cash-settlement-batch-job-performance, paginated-cashflow-batch-processing, ratan]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Batch Group Stg.md"]
---
# Cash Settlement Static-Data Batch Optimization

## Definition

Cash Settlement static-data batch optimization replaces repeated single-parameter operations with interfaces that process multiple cashflows in one request or query.

The staging performance report identifies Materialize and Currency cutoff as single-parameter operations. The report associates this design with approximately twice as many cashflow calls per processing cycle and a large volume of SQL queries.

## Proposed change

The report recommends:

1. Add batch SQL-query interfaces for Materialize.
2. Add batch SQL-query interfaces for Currency cutoff.
3. Reduce repeated calls from group-management processing into `ratanone-static-data-service`.
4. Measure request count, database wait time, latency, CPU, and completed business messages separately.

This optimization is associated with the static-data dependency and the group-management processing path. It should not be generalized to all RATAN services.

## Reported results

The source compares production behavior, increased static-data database connections, and a combined optimized configuration:

| Topic count | Production behavior | Increased static-data DB connections | After batch optimization |
|---:|---:|---:|---:|
| 7 | 2 minutes 30 seconds; TPS 44.8 | 1 minute 35 seconds; TPS 70 | 16 seconds; TPS 420 |
| 2 | 2 minutes 32 seconds; TPS 44.2 | 2 minutes 27 seconds; TPS 45 | 21 seconds; TPS 320 |
| 1 | 6 minutes 30 seconds; TPS 17 | 2 minutes 36 seconds; TPS 43 | 35 seconds; TPS 192 |

The evidence section reports maximum latency of 2 seconds in the production-behavior observation, 1.2 seconds after increasing database connections, and 156 ms after batch optimization. It also states that the number of requests decreased significantly after batching.

Because the test rounds changed more than one variable, the final gains cannot be attributed to batching alone without controlled benchmarks.

## Constraints

Batch interfaces must preserve the semantic behavior of the original Materialize and Currency cutoff operations. Validation should confirm:

- Equivalent results between single-item and batch paths.
- Correct handling of partial failures.
- Idempotent retries.
- Transaction and consistency boundaries.
- Database connection usage under concurrent topic consumption.
- Business completion counts independent of retry-inflated consumption counts.

This page complements [[paginated-cashflow-batch-processing]] with evidence from Kafka-driven group-management processing.