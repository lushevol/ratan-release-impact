---
type: concept
title: Dead-Letter Queue Recovery
created: 2026-08-24
updated: 2026-08-24
tags: [dead-letter-queue, dlq, message-replay, operations, auditability, recovery]
related: [retry-exhaustion-compensation, what-is-the-ratan-wide-retry-exhaustion-and-dlq-recovery-contract, trade-validation-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan common Compensation Solution.md"]
---
# Dead-Letter Queue Recovery

Dead-letter queue recovery is the governed treatment of messages that cannot be processed through normal retry handling. A DLQ should preserve enough message payload, metadata, error context, and correlation information to enable a safe disposition.

The Ratan incident source describes a trade-status message being moved to a dead letter queue and “dropped” after five failed lock-acquisition retries. Whether the message is retained, deleted, or merely excluded from automated retries is not specified. That ambiguity must be resolved before selecting replay, reconciliation, or compensation behavior.

## Recovery lifecycle

A robust DLQ recovery lifecycle normally includes:

1. Capture the failed message with failure reason, attempt count, timestamps, and correlation identifiers.
2. Retain the message for a defined period under an accountable service or team.
3. Alert on backlog volume, backlog age, and business-impacting failure classes.
4. Triage whether the failure is transient, permanent, malformed, duplicate, or business-state dependent.
5. Validate idempotency and current business state before replay.
6. Execute an authorized replay, reconciliation, compensation, or manual disposition.
7. Record the operator or automation identity, decision, evidence, and final result.

## Design considerations

A DLQ is not itself a recovery strategy. Blind replay can duplicate side effects; automatic deletion can strand business records; and business compensation may require domain-specific validation and approval. Recovery controls should therefore be integrated with [[retry-exhaustion-compensation]] and the workflow's business-state model.

For the reported trade-status failure, recovery must identify affected payments that remain pending trade validation and determine whether event replay, state reconciliation, or another controlled action is safe.