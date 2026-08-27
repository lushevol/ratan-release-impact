---
type: concept
title: Long-Running Batch-Job API Execution
created: 2026-08-24
updated: 2026-08-24
tags: [batch-jobs, api-gateway, circuit-breaker, asynchronous-execution]
related: [ratan, cash-settlement-batch-job-performance, should-ratan-long-running-batch-jobs-use-asynchronous-execution, what-idempotency-controls-protect-ratan-ready-state-retries]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
---
# Long-Running Batch-Job API Execution

The reported Cash Settlement batch jobs run for multiple minutes at 50k volume, while the source states that the API gateway circuit breaker activates after 65 seconds. A synchronous request lifecycle is therefore incompatible with the observed execution durations unless the relevant route timeout is changed.

The source leaves two alternatives unresolved:

1. Extend the timeout to 30 minutes.
2. Change job invocation to an asynchronous mechanism.

A longer synchronous timeout must be assessed for connection retention, gateway capacity, client retry ambiguity, and failure handling. Asynchronous execution requires an explicit job-state model, authenticated submission and status access, retry and idempotency controls, cancellation semantics, auditability, monitoring, and reconciliation.

The stated 65-second gateway behavior should be confirmed against the deployed route configuration before a design decision is made.