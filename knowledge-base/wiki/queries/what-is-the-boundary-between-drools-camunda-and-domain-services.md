---
type: query
title: What Is the Boundary Between Drools, Camunda, and Domain Services?
created: 2026-08-24
updated: 2026-08-24
tags: [architecture, drools, camunda, workflow, domain-services]
related: [drools, liteflow, rule-engine-vs-workflow-orchestration, camunda-based-maker-checker-workflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# What Is the Boundary Between Drools, Camunda, and Domain Services?

The source proposes Drools for business rules and describes LiteFlow as flow-oriented, while existing Cash Settlement material documents [[camunda-based-maker-checker-workflows]]. It does not define responsibility boundaries among a rule engine, workflow engine, and domain services.

## Questions to resolve

- Which decisions are pure evaluations that should return a decision result?
- Which processes require workflow state, human tasks, retries, timers, or compensation?
- Which component owns persistence, external calls, and idempotency?
- How are rule versions and decision evidence associated with workflow instances?
- Can workflow processes invoke decision services without embedding business policy in process definitions?