---
type: concept
title: Cashflow Locking and Retry Policy
tags: [cash-settlement, locking, retry, concurrency, idempotency]
related: [force-complete-next-batch-concurrency, camunda, netting-service, adaptor, nstp, swift-service, accounting-service, how-do-cashflow-id-and-original-trade-id-locks-coordinate, what-are-the-bounded-retry-idempotency-and-dead-letter-controls-for-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Cashflow Locking and Retry Policy

The documented cash-settlement design uses locking to prevent concurrent processing of the same business item. Most flows use `Cashflow Id`; an unspecified Adaptor retry flow uses `Original Trade Id`.

## Interaction Modes

Manual UI actions—suppression, netting, fail, reinstate, comment, and business-exception submission or approval—return an alert when another process is handling the cashflow. The user must retry.

Background processing automatically retries until success for new cashflow workflow events and for SWIFT and Accounting status updates. The identified participants are [[camunda]], [[netting-service]], [[nstp]], SSI service, Lifecycle, [[swift-service]], and [[accounting-service]].

## Key-Granularity Risk

`Cashflow Id` and `Original Trade Id` are different synchronization scopes. The source does not describe their coordination when a trade produces multiple cashflows or when cashflows are grouped, netted, split, or unnetted. This gap is tracked in [[how-do-cashflow-id-and-original-trade-id-locks-coordinate]].

## Unspecified Controls

“Auto retry until succeeded” has no stated retry interval, backoff, maximum attempt count, expiry, idempotency key, ordering rule, dead-letter path, operator visibility, or alerting policy. These omissions are tracked in [[what-are-the-bounded-retry-idempotency-and-dead-letter-controls-for-cashflow-processing]].

The source does not identify the locking implementation or establish atomicity between lock acquisition, status validation, state transition, and downstream dispatch.