---
type: concept
title: Kafka Persistent Retry and DLT Recovery
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, retry-topics, dead-letter-topic, resilience, recovery]
related: [tdsx-uber-message-listener, uber-inbound-message-idempotency-and-error-state, does-tdsx-uber-retryabletopic-work-correctly-with-consumererrorhandler, what-is-the-operational-recovery-process-for-uber-dlt-records, orchestration, database-to-kafka-exception-event-reliability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# Kafka Persistent Retry and DLT Recovery

Kafka persistent retry moves failed record processing through durable retry topics rather than relying only on repeated listener execution in memory. A Dead Letter Topic (DLT) receives records that exhaust the configured retry policy and establishes a terminal, operationally recoverable state.

## Project Application

For `TdsxUberMessageListener`, the source proposes `@RetryableTopic` with five configured attempts and exponential delays beginning at 15 seconds. The reported Dev result of four retries before DLT is consistent with an interpretation where the initial delivery is included in the attempt count, but the exact semantics depend on the deployed Spring Kafka version and configuration.

## Required Properties

A durable retry/DLT design requires more than topic routing:

- A failure must be propagated so retry-topic routing occurs reliably.
- Retry-topic naming, partitioning, concurrency, retention, and ACLs must be defined.
- Terminal DLT processing must persist an explicit business failure state.
- Reprocessing must be idempotent across database writes and downstream publication.
- Operators need alerts, ownership, replay authorization, and a documented recovery procedure.
- Offset acknowledgment and error-handler behavior must not bypass retry or DLT routing.

## DLT Is Not Successful Completion

For Uber group processing, DLT handling is intended to retain inbound and group records, mark incomplete work as `ERROR`, and leave the group record `PENDING`. Downstream cashflow must not be emitted for terminally failed processing.

This is distinct from [[database-to-kafka-exception-event-reliability]], which concerns reliable publication from database processing to Kafka. This concept concerns reliable Kafka inbound processing into database and business state.