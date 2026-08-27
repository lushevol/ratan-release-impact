---
type: entity
title: Camunda 7
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, workflow-engine, process-automation, legacy-platform]
related: [camunda, activiti-5, camunda-7-architecture, camunda-7-workflow-data-handling, camunda-persistence-schema, what-is-the-approved-camunda-7-to-8-migration-strategy-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda migration from 7.X to 8.X.md"]
---

# Camunda 7

Camunda 7 is the workflow-engine version family described in the source. It is characterized as being based on [[activiti-5]], using relational-database persistence, and handling workflow data through Java objects, workflow variables, and listeners.

The source describes Camunda 7.19 as the latest Camunda 7 version and associates it with Spring Boot 2.7.x compatibility. That version statement is historical and time-sensitive; current support status must be verified independently.

The source does not document Camunda 8 or establish a migration path from Camunda 7. Any migration assessment must identify the Cash Settlement process models, delegates, listeners, variables, persistence requirements, and treatment of active and historical workflow instances.
