---
type: query
title: What Is the Idempotency and Concurrency Contract for Multiple Exception Fixing?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, idempotency, concurrency, retry, exception-handling, Camunda]
related: [partial-success-exception-resolution, cashflow-versioned-exception-orchestration, multiple-cashflow-exception-handling, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# What Is the Idempotency and Concurrency Contract for Multiple Exception Fixing?

The design requires successful exception actions to remain fixed when another action fails, while allowing only unresolved actions to be retried. It correlates requests using `cashflowId`, business version, cashflow version, minor version, exception ID, and `trackingId`.

## Questions to resolve

- What is the idempotency key for each exception action?
- Are actions executed sequentially or in parallel?
- Is each action independently committed?
- How are downstream timeouts and unknown outcomes reconciled?
- How are stale `cashflowVersion` and `minorVersion` requests rejected?
- How are simultaneous maker or checker submissions locked?
- How are duplicate Camunda callbacks handled?
- Should business failures be represented by structured application errors or HTTP 500?
- How is payment-regeneration prevention enforced after a payment has been sent?

Until these questions are answered, the version fields provide correlation and audit context but should not be treated as a complete concurrency or retry contract.