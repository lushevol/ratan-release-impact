---
type: query
title: What Is the Approved Camunda 7-to-8 Migration Strategy for Cash Settlement?
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, camunda-7, camunda-8, migration, cash-settlement, architecture]
related: [camunda-7, camunda-7-architecture, camunda-7-workflow-data-handling, camunda-persistence-schema, destructive-workflow-data-purge, what-camunda-history-retention-and-audit-requirements-apply-to-ratanone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda migration from 7.X to 8.X.md"]
---

# What Is the Approved Camunda 7-to-8 Migration Strategy for Cash Settlement?

## Question

What migration strategy, target architecture, and operational plan are approved for moving Cash Settlement from Camunda 7.x to Camunda 8.x, if Camunda 8.x is the approved target?

## Current Evidence

The source documents only a Camunda 7 baseline: Activiti 5 lineage, relational persistence, and workflow data handling through Java objects, workflow variables, and listeners. It does not contain Camunda 8-specific evidence or a migration conclusion.

## Information Required

The decision should address:

- Whether Camunda 8.x is an approved target or remains under investigation.
- The target deployment and operating model.
- BPMN process-definition conversion and feature compatibility.
- Java delegate, execution-listener, and task-listener replacement.
- External-task and job-worker changes.
- Variable serialization, mapping, and historical-data treatment.
- Handling of in-flight process instances.
- Retention, audit, legal-hold, and reconciliation requirements.
- Testing, rollback, cutover, and coexistence arrangements.
- The Camunda 7.19 and Spring Boot 2.7.x versions actually used in Cash Settlement.
- Database migration, archival, and purge implications.

## Related Questions

Historical records and variable data may be subject to the requirements tracked in [[what-camunda-history-retention-and-audit-requirements-apply-to-ratanone]]. Existing persistence and purge material should be treated as operational context rather than migration approval evidence.
