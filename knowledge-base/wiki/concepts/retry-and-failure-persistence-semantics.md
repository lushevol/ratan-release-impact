---
type: concept
title: Retry and Failure Persistence Semantics
created: 2026-08-24
updated: 2026-08-24
tags: [retries, error-handling, failure-persistence, kafka, message-bridge]
related: [message-bridge, ratan-bridge-fail-message, message-bridge-deduplication-key-lifecycle, what-is-the-message-bridge-authoritative-retry-and-terminal-failure-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# Retry and Failure Persistence Semantics

Retry and failure persistence semantics define the boundaries between a retryable delivery failure, a terminal failure, and a record persisted for recovery.

For Message Bridge, the documented intended terminal path is:

```text
sendBody() exception
→ DispatchProducerRoute.onException (6 retries)
→ DIRECT_EXCEPTION_ROUTE
→ ExceptionProducerRoute.process()
→ DIRECT_RAW_MESSAGE_PERSISTENCE_ROUTE
→ RawMessagePersistenceProducerRoute.saveRawMessage()
→ ratan_bridge_fail_message
```

The incident does not establish the authoritative retry contract. It states both that `DispatchProducerRoute.onException` has six retries and that Kafka automatically retries up to six times, while the Kafka endpoint string contains `retries=10`.

The absence of an `ExceptionProducerRoute` log was used to infer that terminal handling had not occurred. This is insufficient by itself to prove the route was never entered.

A robust operational contract should identify the retry owner, attempt count, backoff, terminal condition, deduplication cleanup rule, persistence outcome, and possible duplicate-publication behavior for each failure state.

See [[what-is-the-message-bridge-authoritative-retry-and-terminal-failure-contract]].