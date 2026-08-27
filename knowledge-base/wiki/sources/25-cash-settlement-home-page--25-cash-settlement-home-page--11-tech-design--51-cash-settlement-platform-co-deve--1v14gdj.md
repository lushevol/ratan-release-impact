---
type: source
title: Cash Settlement Platform Co-development Guideline
authors: [Cash Settlement platform development team]
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/Foundation+Service+Mesh+Platform"
venue: Internal technical design and meeting-minutes document
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, co-development, foundation-services, FSM, Camunda, architecture]
related: [foundation-service-mesh-platform, cash-settlement-shared-platform-architecture, ratan-camunda-starter, cash-settlement-cluster-topology-options, camunda, ratan, kafka, redis, postgresql, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Platform - Co-development Guideline.md"]
---
# Cash Settlement Platform Co-development Guideline

## Summary

This internal guideline defines the proposed technical and organizational model for co-developing the Cash Settlement platform. It aligns domain services with the Foundation Service Mesh Platform (FSM), promotes shared infrastructure and foundation services, and recommends reuse or enhancement of Ratan’s Camunda workflow component.

The document records agreements, meeting discussions from 8–19 August, and an action register. It distinguishes agreed architectural direction from unresolved questions about topology, ownership, availability, and future business requirements.

## Agreed platform model

All Cash Settlement domain services should follow the FSM 1.0 design and share infrastructure and foundation services.

### Shared infrastructure

```text
- Kafka
- Redis
- ELK
- Servers
- PostgreSQL
```

### Foundation services

```text
- Consul, for service registration and configuration
- Spring Cloud API Gateway
- Authentication Server
```

### Domain-service archetype and starters

```text
- API registration starter
- Distributed lock starter
- Duplication check starter
- Camunda workflow starter
- Logging starter
- Kafka starter
- Redis starter
- Actuator starter
```

The intended delivery model also includes a common CI/CD pipeline for building infrastructure, installing foundation services, and building and deploying domain services. Development should use Spring Boot and Spring Cloud native components.

## Workflow component reuse

The guideline proposes that the Camunda workflow currently used by [[ratan]] should be reused or enhanced. The meeting record states that Ratan had three workflows live in production for approximately two years. The Ratan Camunda Starter was demonstrated using [[bcs]] settlement and was considered a candidate for the China Settlement workflow.

The evidence supports technical feasibility for the demonstrated workflow patterns, but does not establish that every China Settlement requirement is covered. New or unsupported business requirements must be identified before enhancements are finalized.

The starter is described as a technical component for orchestrating domain services through Camunda workflow diagrams. Its demonstrated development mode focuses on creating BPMN diagrams and starting a Spring Boot application with limited application coding. The source does not specify the implementation model for complex business rules, retries, compensation, idempotency, workflow versioning, or migration.

## Deployment topology options

The 8 August meeting recorded two possible implementations of the shared-platform model:

1. A single cluster hosting shared infrastructure, foundation services, and domain services.
2. A topology in which the Ratan VM cluster hosts infrastructure services while Razor physical servers host domain services.

The second option raises unresolved availability and synchronization concerns. VM patching may cause downtime, while physical servers may require hard reboots. The document does not record a final topology decision.

The meeting also identifies unresolved responsibility questions concerning how two PSS groups would jointly operate the platform.

## MIEX discussion

The 10 August meeting described MIEX as differing mainly in its API Gateway architecture. The record states that migration to Spring Cloud API Gateway should require limited effort. This remains an unvalidated assessment because the source contains no interface inventory, compatibility analysis, migration plan, proof of concept, or effort estimate.

## Action register

| # | Action | Status | Owner | Update |
|---:|---|---|---|---|
| 1 | FSM-foundation to be created containing all dependencies and starters | Not specified | Eric | Not specified |
| 2 | Archetype to be created on open source repository | Not specified | Eric | Not specified |
| 3 | Shared library to be created for infrastructure setup and application installation | Not specified | Not assigned | Not specified |
| 4 | Testing environment on cluster to be created for verification | Not specified | Geoffrey | 4 CPU + 8 G memory + 70 Disk |
| 5 | Infrastructure services installation on testing environment using Ansible scripts | Not specified | Not assigned | Not specified |
| 6 | Foundation services installation on testing environment | Not specified | Not assigned | Not specified |
| 7 | Demo domain-service build | Not specified | Not assigned | Not specified |

The action register does not define deadlines, acceptance criteria, or explicit statuses. Four actions have no named owner.

## Meeting chronology

### 8 August

Rich, Eric, Zikai, Lina, and Geoffrey discussed FSM 1.0 and FSM 2.0. The group agreed that Cash Settlement domain services should share infrastructure and foundation services according to FSM 1.0. The group also agreed that the Ratan Camunda workflow should be reused or enhanced. The next agenda items were Ratan’s Camunda practice and MIEX architecture.

### 10 August

Rich, Eric, Karl, Lina, and Geoffrey reviewed Ratan’s Camunda usage. The meeting recorded no key blocker to supporting the new business flow. Rich described MIEX and identified API Gateway as its main architectural difference.

### 15 August

Rich, Eric, Karl, Zikai, Wayne, and Geoffrey reaffirmed the agreements and instructed the team to work strictly to them, communicate changes, and avoid redundant development.

### 17 August

Rich, Lu, Krishna, Zikai, Lina, Wayne, Eric, and Geoffrey reviewed the Ratan Camunda Starter. It was demonstrated for BCS settlement and considered a suitable candidate for China Settlement, subject to identifying additional business requirements.

### 19 August

Liam, Zikai, Eric, Lina, Wayne, and Geoffrey reviewed the agreements. Camunda workflow definition was identified as a topic for the next session.

## Open questions and risks

- Which cluster topology was ultimately approved?
- How will PSS groups divide ownership and operational responsibility?
- What availability, patching, and disaster-recovery targets apply?
- Which China Settlement requirements have been tested against the Ratan Camunda Starter?
- How will workflow retries, compensation, idempotency, versioning, migration, and auditability work?
- What repository, licensing, security, dependency-management, and release policies apply to the archetype?
- What completion criteria and deadlines apply to each action?
- The original document contains sensitive infrastructure details and a plaintext credential. Those details are intentionally omitted here and should be removed from source control; the credential should be rotated or revoked.

## Related context

This guideline provides upstream architectural context for [[cash-settlement-shared-platform-architecture]], [[ratan-camunda-starter]], [[camunda]], [[ratan]], [[kafka]], [[redis]], [[postgresql]], and [[razor]].