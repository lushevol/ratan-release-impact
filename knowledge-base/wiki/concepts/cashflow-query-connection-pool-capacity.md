---
type: concept
title: Cashflow Query Connection-Pool Capacity
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, jdbc, connection-pool, capacity-planning, performance-testing]
related: [cashflow-data-provider, database-connection-pool-saturation, streaming-large-cashflow-query-responses, postgresql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/PT for big volume query.md"]
---
# Cashflow Query Connection-Pool Capacity

JDBC connection-pool capacity is a demonstrated reliability boundary for the tested Cashflow Data Provider workload.

## UAT Evidence

For five simultaneous 500k-row V2 Final queries:

- `created_at` ordering with pool maximum 10 had three loop queries fail to obtain JDBC connections.
- The same `created_at` scenario with pool maximum 20 was recorded as all successful.
- `cashflow_Ids` with pool maximum 10 had two loop queries fail to obtain JDBC connections.
- `cashflow_Ids` with pool maximum 20 was recorded as all successful.

The source also records a V2 Draft ten-query test in which pool maximum 10 caused JDBC timeout and connection-acquisition failures, while pool maximum 30 changed the observed failure to OOM. This illustrates that increasing the pool can expose or amplify heap pressure when request handling still aggregates complete responses.

## Interpretation

Pool maximum 20 is UAT evidence for the listed conditions, not an approved universal production setting. The appropriate value depends on database capacity, service-instance count, request concurrency, query duration, connection timeout, other pool consumers, and workload mix.

Pool expansion should be paired with bounded response handling, concurrency limits, database-capacity testing, and monitoring. See [[database-connection-pool-saturation]] and [[streaming-large-cashflow-query-responses]].