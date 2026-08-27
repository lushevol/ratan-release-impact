---
type: concept
title: Non-Blocking Message Retry
tags: [kafka, spring-kafka, retry, dead-letter-topic, message-processing]
related: [kafka, solace, kafka-to-solace-semantic-migration, cash-settlement-platform]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Message Middleware DR Solution.md"]
---
# Non-Blocking Message Retry

Non-blocking message retry is a Spring Kafka pattern that redirects failed processing to retry topics rather than blocking the original topic partition. It supports higher consumption throughput where strict processing sequence is not required.

The Cash Settlement Platform uses retry topics and dead-letter topics for inbound cashflow, TDS3 trade, Murex trade, and lifecycle domain-event processing. The source describes `@RetryableTopic`, `@KafkaListener`, and `@DltHandler` as the current implementation pattern.

## Migration implication

The source states that Solace does not naturally provide Kafka's topic, offset, and seek model. A Kafka-to-Solace migration must therefore define functional equivalents for:

- Retry scheduling and backoff.
- Attempt counting and terminal failure handling.
- Dead-letter routing and operational remediation.
- Ordering expectations during retry.
- Idempotence and duplicate delivery.
- Monitoring equivalent to retry-topic depth and consumer lag.

The topic inventory recorded in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--11-2026-design--49-cash-settlement--1vzfqs8]] is evidence of specific existing dependencies, not proof that it is the complete platform retry inventory.