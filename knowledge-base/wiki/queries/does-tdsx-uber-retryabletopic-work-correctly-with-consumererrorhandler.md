---
type: query
title: Does TdsxUberMessageListener RetryableTopic Work Correctly With consumerErrorHandler?
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, retry-topics, error-handler, offset-management, uber]
related: [tdsx-uber-message-listener, kafka-persistent-retry-and-dlt-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# Does TdsxUberMessageListener RetryableTopic Work Correctly With consumerErrorHandler?

The proposed listener retains `errorHandler = "consumerErrorHandler"` while adding `@RetryableTopic`. The source states that `MessageConsumerErrorHandler` rethrows as `RatanServiceException`, but does not establish the deployed Spring Kafka version, container factory settings, acknowledgment mode, `CommonErrorHandler` configuration, or offset-commit behavior.

## Evidence Needed

- Active `consumerErrorHandler` implementation and bean wiring.
- Spring Kafka and Spring Boot versions by environment.
- Listener container factory configuration, including acknowledgment mode and common error handler.
- Integration test proving original-topic failure, retry-topic transitions, DLT arrival, and expected committed offsets.
- Test proving no handler seeks, commits, or recoverer behavior bypasses retry-topic routing.

## Decision Impact

If the handler chain is incompatible, records may still bypass durable retry or reach DLT unexpectedly. The retry/DLT reliability claim for [[tdsx-uber-message-listener]] remains conditional until this integration contract is verified.