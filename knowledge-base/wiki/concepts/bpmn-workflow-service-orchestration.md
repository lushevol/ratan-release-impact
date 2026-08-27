---
type: concept
title: BPMN Workflow Service Orchestration
created: 2026-08-24
updated: 2026-08-24
tags: [BPMN, Camunda, workflow, service-orchestration, Cash-Settlement]
related: [ratan-camunda-starter, camunda, camunda-7, synchronous-kafka-to-camunda-orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Platform - Co-development Guideline.md"]
---
# BPMN Workflow Service Orchestration

BPMN workflow service orchestration models interactions among domain services as workflow diagrams executed through Camunda. In the Cash Settlement guideline, this approach is represented by the [[ratan-camunda-starter]].

The described development mode emphasizes BPMN diagram creation and a Spring Boot application rather than extensive orchestration code. This can reduce repeated technical setup and make workflow structure visible to delivery teams.

The source does not establish that BPMN diagrams replace application code for complex business rules. Error handling, retries, compensation, idempotency, workflow versioning, migration, and auditability require separate design and validation.