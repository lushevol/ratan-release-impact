---
type: entity
title: Foundation Service Mesh Platform
created: 2026-08-24
updated: 2026-08-24
tags: [FSM, platform-architecture, cash-settlement, foundation-services]
related: [cash-settlement-shared-platform-architecture, ratan-camunda-starter, consul, spring-cloud-api-gateway]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Platform - Co-development Guideline.md"]
---
# Foundation Service Mesh Platform

The Foundation Service Mesh Platform (FSM) is the architectural standard referenced for Cash Settlement co-development. The guideline favors the FSM 1.0 design for sharing servers, infrastructure, and foundation services across domain services.

FSM-related platform capabilities named in the source include [[consul]], Spring Cloud API Gateway, Authentication Server, Kafka, Redis, ELK, and PostgreSQL. The source also records that FSM 1.0 and FSM 2.0 were presented for comparison, but does not provide a complete technical specification for either version.

The Cash Settlement team is expected to create an FSM-foundation package containing dependencies and starters, together with an archetype and common CI/CD process. Ownership, release governance, and operational responsibility across PSS groups remain unresolved.