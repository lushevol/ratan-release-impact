---
type: source
title: Ratan Common Compensation Solution
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, exception-handling, compensation, dead-letter-queue, lock-contention, trade-validation]
related: [retry-exhaustion-compensation, dead-letter-queue-recovery, what-is-the-ratan-wide-retry-exhaustion-and-dlq-recovery-contract, how-should-trade-id-lock-contention-be-handled-for-large-payment-groups, cashflow-group-management-service, trade-validation-gating, ratan-distributed-lock-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan common Compensation Solution.md"]
---
# Ratan Common Compensation Solution

## Summary

This source is a problem statement advocating a common Ratan mechanism for handling messages that have exhausted their retry limit. It reports a Group Management failure scenario in which more than 400 payments under one trade ID cause cashflow processing and trade-status processing to compete for a trade-ID lock.

The source does not propose an architecture, recovery contract, state machine, API, ownership model, or approved compensation action. It should therefore be treated as incident motivation rather than as an approved technical design.

## Reported scenario

> Ratan need a common exception handling and compensation mechanism. Main ask is how to handle those messages reached out to the max retry times on any cases.
>
> One case we found that in group management, 400+ payments exist under same trade id and the processing competing with the trade status flow from another topic on the trade id lock authorization.
>
> While the cashflows are being processed, trade status cannot obtain the lock authorization after 5 times retry and eventually moved to dead letter queue and dropped, which caused the payments pending trade validation.
>
> Though manual STP can solve the problem, but we need a graceful way of handling it.

## Implications

The reported sequence connects lock acquisition failure to an operationally unresolved business state:

1. Cashflow processing holds or competes for a trade-ID lock.
2. A trade-status flow cannot acquire the lock after five retries.
3. The event is sent to a dead letter queue and described as dropped.
4. Payments remain pending trade validation.
5. Manual STP is used as a workaround.

The meaning of “dropped” is not defined. It is unclear whether the DLQ message is retained for manual replay, automatically discarded, or otherwise unavailable for recovery.

## Design gaps identified

A Ratan-wide recovery design needs to establish:

- retry eligibility, retry count, backoff, jitter, and time limits;
- DLQ retention, monitoring, ownership, and replay authorization;
- idempotency and business-state validation before replay;
- the distinction between event replay, state reconciliation, technical compensation, and business compensation;
- lock ownership, lock scope, lease duration, and release behavior;
- identification and recovery of payments stranded in pending trade validation;
- audit evidence for automated and manual recovery actions.

The reported incident is relevant to [[cashflow-group-management-service]], [[trade-validation-gating]], and [[group-level-trade-validation-hold]]. Its lock-contention aspect should be investigated alongside [[ratan-distributed-lock-ownership]], [[cross-service-lock-validation]], and [[synchronized-process-lock-scope]].

## Follow-up

- [[retry-exhaustion-compensation]]
- [[dead-letter-queue-recovery]]
- [[what-is-the-ratan-wide-retry-exhaustion-and-dlq-recovery-contract]]
- [[how-should-trade-id-lock-contention-be-handled-for-large-payment-groups]]
- [[which-ratan-distributed-lock-ownership-model-is-approved]]