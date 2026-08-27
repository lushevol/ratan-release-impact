---
type: query
title: Should RATAN Long-Running Batch Jobs Use Asynchronous Execution?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, batch-jobs, asynchronous-execution, api-gateway]
related: [ratan, long-running-batch-job-api-execution, cash-settlement-batch-job-performance, what-idempotency-controls-protect-ratan-ready-state-retries, is-ratan-release-status-validation-atomic-with-downstream-dispatch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
---
# Should RATAN Long-Running Batch Jobs Use Asynchronous Execution?

The source reports multi-minute execution times for tested jobs and states that the API gateway circuit breaker activates after 65 seconds. It leaves a choice between a 30-minute synchronous timeout and asynchronous execution.

## Decision criteria

- Confirm the gateway circuit-breaker configuration and whether route-specific changes are permitted.
- Define workload completion SLOs and concurrent-run limits.
- Compare capacity, failure visibility, and retry behavior for both approaches.
- If asynchronous execution is selected, define job identifiers, durable state transitions, authorization, status retrieval, cancellation, retries, idempotency, monitoring, alerting, audit, and reconciliation.
- Ensure that release correctness remains intact, especially where group locks and downstream dispatch are involved.

No selected or validated mitigation is present in the source.