---
type: concept
title: Database-to-Kafka Exception Event Reliability
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, exceptions, transactional-outbox, reliability, consistency]
related: [cn-rule-service, multiple-cashflow-exception-handling, exception-operation-level, how-are-cn-rule-exceptions-reliably-published-to-kafka]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# Database-to-Kafka Exception Event Reliability

Database-to-Kafka exception event reliability concerns the consistency of persisting an exception and publishing its corresponding Kafka event.

The archived CN Rule Service note identifies a failure window: an exception can be successfully inserted into the database while publication to Kafka fails. It refers to the [Microservice Transactional Outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html) as a possible response.

The source does not confirm that an outbox, Kafka transaction, CDC publisher, retry process, or reconciliation mechanism exists. It also does not define idempotency keys, ordering, replay behavior, delivery monitoring, or dead-letter handling.

A reliable implementation requires an explicit contract for persistence, publication, retry, and consumer-safe duplicate handling. See [[how-are-cn-rule-exceptions-reliably-published-to-kafka]].