---
type: entity
title: TdsxUberMessageListener
created: 2026-08-24
updated: 2026-08-24
tags: [kafka-listener, uber, group-service, spring-kafka, cash-settlement]
related: [kafka-persistent-retry-and-dlt-recovery, uber-inbound-message-idempotency-and-error-state, does-tdsx-uber-retryabletopic-work-correctly-with-consumererrorhandler, what-is-the-operational-recovery-process-for-uber-dlt-records, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# TdsxUberMessageListener

`TdsxUberMessageListener` is the group-service Spring Kafka listener for TDSX Uber messages. It creates inbound processing state, publishes `UberValidatedEvent` under a resource lock, and initiates downstream group processing.

## Failure History

Before the described enhancement, a downstream exception could lead to deletion of the listener's newly persisted `VALIDATED` inbound record. The exception was rethrown through `consumerErrorHandler`; after container-level retry exhaustion and offset progression, neither the inbound evidence nor an automatically consumable message remained.

The source identifies this behavior as contributing to a message-loss incident for trade `7153008753`.

## Intended Reliability Model

The proposed design applies `@RetryableTopic` with:

- `attempts` defaulting to `5`;
- exponential backoff beginning at 15 seconds with multiplier `2.0`;
- indexed retry-topic suffixes;
- configurable retry partitions and listener concurrency; and
- terminal handling through `@DltHandler`.

Terminal failure must retain an auditable state in `ratan_inbound_message`, `ratan_cashflow_group`, and `ratan_cashflow_group_message`; it must not emit downstream cashflow.

## Important Integration Constraint

The listener annotation retains `errorHandler = "consumerErrorHandler"` while adding `@RetryableTopic`. The active behavior of `MessageConsumerErrorHandler`, container error handling, seek behavior, and acknowledgment/offset commits must be tested together before treating retry-topic routing as confirmed.

See [[kafka-persistent-retry-and-dlt-recovery]] and [[uber-inbound-message-idempotency-and-error-state]].