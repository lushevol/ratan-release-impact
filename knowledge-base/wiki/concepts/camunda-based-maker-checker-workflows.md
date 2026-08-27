---
type: concept
title: Camunda-Based Maker-Checker Workflows
tags: [camunda, maker-checker, workflow, ddd, process-orchestration]
related: [camunda, nstp, nstp-maker-checker-processing, adhoc-suppression-maker-checker-workflow, user-operation-audit-trail]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Camunda-Based Maker-Checker Workflows

Camunda-based maker-checker workflows place approval initiation, user tasks, task completion, and process progression in Camunda rather than implementing that workflow behavior directly in business microservices.

The intended boundary is that business services retain basic domain operations while the workflow engine owns process-domain coordination. Services participate through APIs for business actions, state changes, and persistence.

## Proposed benefits

The source expects this approach to make user-operation logic visible in BPMN workflows, reduce coupling between maker-checker logic and business code, and make workflow-focused changes more manageable.

These are intended architectural benefits, not verified operational results. A workflow change may still require service operations, data fields, authorization controls, audit changes, or changed status transitions.

## Trade-off

The proposal explicitly moves complexity rather than removing it: the current approach has high code complexity, while the proposed approach has high Camunda workflow complexity.

Workflow governance, BPMN versioning, testing, authorization, retry behavior, compensation, and observability are therefore material design concerns.