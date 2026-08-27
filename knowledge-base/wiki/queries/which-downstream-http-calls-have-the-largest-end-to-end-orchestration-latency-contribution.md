---
type: query
title: Which Downstream HTTP Calls Have the Largest End-to-End Orchestration Latency Contribution?
tags: [http, latency, orchestration, camunda, profiling, cash-settlement]
related: [downstream-http-limited-workflow-throughput, synchronous-kafka-to-camunda-orchestration, orchestration, cashflow-lifecycle-service, group-service, camunda]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Orchestration Stg.md"]
---
# Which Downstream HTTP Calls Have the Largest End-to-End Orchestration Latency Contribution?

The staging study identifies consistent HTTP hotspots but reports per-call measurements rather than the full weighted contribution of each endpoint to end-to-end processing.

## Calls to Investigate

- `/v1/ratan/camunda/lifecycle/msgEventCheck`
- `/v2/ratan/camunda/cashflow/stamp`
- `/v2/ratan/camunda/lifecycle/status/move`
- `/v1/netting/camunda/checkPaymentDateForIRS`
- `/v1/netting/camunda/netForIRS`
- `/v2/ratan/camunda/cashflow/preCheck`

`status/move` was called 136 times in STG-C, compared with 68 calls for each other listed endpoint. Its cumulative impact should be calculated from invocation count, latency distribution, concurrency, and retry behavior rather than from average latency alone.

## Required Evidence

Collect an end-to-end trace or call graph that records:

1. Invocation count per workflow and per cashflow.
2. P50, P95, P99, maximum, timeout, and retry metrics for each endpoint.
3. Aggregate latency contribution and critical-path contribution.
4. Service-side CPU, database, and dependency diagnostics.
5. Whether duplicated checks or `status/move` operations can be merged, cached, moved earlier, or made asynchronous without violating ordering, idempotency, or consistency.

This investigation supports [[concepts/downstream-http-limited-workflow-throughput]].