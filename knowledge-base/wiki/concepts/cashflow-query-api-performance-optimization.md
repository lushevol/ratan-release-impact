---
type: concept
title: Cashflow Query API Performance Optimization
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, api, performance, batching, concurrency, ratan]
related: [ratan-cashflow-lifecycle-service, cashflow-migration-readiness, lien-aware-netting-and-auto-unnetting, trade-lien-notification-reconciliation, what-are-the-validated-production-latency-and-capacity-results-for-cashflow-query-optimization, what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Cashflow query api optimization.md"]
---
# Cashflow Query API Performance Optimization

Cashflow query API performance optimization reduces latency and resource consumption for high-volume cashflow retrieval while preserving the response data and consistency requirements of each downstream workflow.

In the [[ratan-cashflow-lifecycle-service]] context, three proposed techniques are:

1. **Category-based fetching:** retrieve only table-backed data categories required by a request.
2. **Batch querying:** retrieve multiple cashflow IDs through grouped operations rather than repeated per-ID work.
3. **Multithreaded request processing:** use bounded parallelism for independently retrievable work.

## Compatibility requirements

The service has heterogeneous consumers. A safe design must ensure that selective retrieval does not omit fields required by accounting, affirmation, LMS, SSI stamping, lifecycle processing, or netting operations.

Netting workflows can require data across lifecycle history, Stella event-source records, and SCBML messages. Unnetting and lien-related processing additionally depend on version, status, value-date, and `nettingId` data; see [[lien-aware-netting-and-auto-unnetting]] and [[trade-lien-notification-reconciliation]].

## Validation requirements

Optimization should be evaluated using end-to-end latency and capacity metrics rather than per-cashflow averages alone. Evidence should include:

- p50, p95, and p99 latency by batch size;
- supported maximum `cashflowIds` per request;
- throughput, error rate, timeout rate, and partial-result behavior;
- database-query count and database execution time;
- connection-pool, thread-pool, CPU, and memory saturation;
- ordering, duplicate-ID, retry, and transaction-consistency behavior;
- regression coverage for locking and state-sensitive netting operations.

The source records high absolute latency for large batches but does not provide enough observability or post-deployment evidence to establish a root cause or measured benefit. This remains relevant to [[cashflow-migration-readiness]].