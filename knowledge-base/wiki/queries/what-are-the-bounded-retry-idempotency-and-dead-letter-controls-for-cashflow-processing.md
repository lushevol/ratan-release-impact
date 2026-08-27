---
type: query
title: What Are the Bounded Retry, Idempotency, and Dead-Letter Controls for Cashflow Processing?
tags: [cash-settlement, retry, idempotency, dead-letter, observability]
related: [cashflow-locking-and-retry-policy, camunda, netting-service, nstp, swift-service, accounting-service, adaptor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Are the Bounded Retry, Idempotency, and Dead-Letter Controls for Cashflow Processing?

The documented behavior is repeatedly “auto retry until succeeded” for new cashflow events and selected status updates. No operational controls are specified.

## Evidence Needed

- Retry intervals, backoff strategy, and maximum-attempt policy.
- Idempotency keys and duplicate-event handling for every participating service.
- Ordering guarantees and handling of stale events.
- Dead-letter, expiry, replay, alerting, and operator-remediation processes.
- Metrics and ownership for persistent processing failures.