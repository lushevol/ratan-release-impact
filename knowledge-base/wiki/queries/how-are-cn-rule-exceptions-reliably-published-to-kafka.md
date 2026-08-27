---
type: query
title: How Are CN Rule Exceptions Reliably Published to Kafka?
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, exceptions, transactional-outbox, reliability]
related: [database-to-kafka-exception-event-reliability, cn-rule-service, multiple-cashflow-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# How Are CN Rule Exceptions Reliably Published to Kafka?

The archived design identifies a failure case in which exception persistence succeeds but Kafka publication fails. It references Transactional Outbox as a possible pattern but does not record an implementation decision.

## Questions

- Does CN Rule Service use a Transactional Outbox, Kafka transaction, CDC publisher, or another delivery mechanism?
- How are publication failures retried and monitored?
- What event identifier makes consumer processing idempotent?
- How are event ordering, duplicate delivery, replay, and reconciliation handled?
- What operational process detects persisted exceptions that lack a corresponding Kafka event?

## Evidence needed

Current persistence and publisher code, topic contracts, outbox schema if applicable, retry policy, monitoring dashboards, and recovery runbooks.