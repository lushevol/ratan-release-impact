---
type: concept
title: Retry-Exhaustion Compensation
created: 2026-08-24
updated: 2026-08-24
tags: [retry, exception-handling, compensation, asynchronous-processing, recovery]
related: [dead-letter-queue-recovery, what-is-the-ratan-wide-retry-exhaustion-and-dlq-recovery-contract, how-should-trade-id-lock-contention-be-handled-for-large-payment-groups, trade-validation-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan common Compensation Solution.md"]
---
# Retry-Exhaustion Compensation

Retry-exhaustion compensation is the controlled recovery process triggered when an asynchronous message cannot complete through its configured retry policy. It is not equivalent to simply increasing retry counts or repeating an operation indefinitely.

In the reported Ratan scenario, a trade-status event fails to acquire a trade-ID lock after five retries, resulting in payments remaining pending trade validation. The desired outcome is recoverability of the affected business state rather than reliance on manual STP.

## Recovery options

A recovery design should distinguish among:

- **Retry:** attempt the original operation again according to a bounded policy.
- **DLQ retention:** durably preserve the failed message and its diagnostic context.
- **Replay:** re-submit the original event after validating that it remains safe and relevant.
- **Reconciliation:** compare expected and actual business state, then repair missing processing.
- **Technical compensation:** correct partial technical side effects from a failed workflow.
- **Business compensation:** perform a domain-specific corrective action, potentially requiring approval.
- **Manual remediation:** an operator resolves the case using an auditable procedure.

These actions have different safety requirements. A generic recovery platform can coordinate routing, retention, auditability, and workflow controls, but business compensation must remain specific to the affected domain and state.

## Required controls

Before automated replay or compensation, the recovery path should establish:

- idempotency and duplicate-event behavior;
- the current business state and whether the event is still applicable;
- causal correlation between the failed event and affected payments;
- authorization for replay or corrective action;
- an immutable audit record of disposition and outcome;
- a terminal escalation path when automation is unsafe.

The source does not define these controls, so no particular recovery model is approved.

## Related Ratan case

The motivating case is documented in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--34-ratan-common-compensation-solutio--hjtzet]]. It should be considered with [[dead-letter-queue-recovery]] and [[trade-validation-gating]].