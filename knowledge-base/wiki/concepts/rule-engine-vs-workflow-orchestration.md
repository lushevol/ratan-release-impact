---
type: concept
title: Rule Engine vs Workflow Orchestration
created: 2026-08-24
updated: 2026-08-24
tags: [architecture, rule-engine, workflow, orchestration, camunda]
related: [business-rule-engines, drools, liteflow, camunda-based-maker-checker-workflows, what-is-the-boundary-between-drools-camunda-and-domain-services]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# Rule Engine vs Workflow Orchestration

Rule engines evaluate conditions to derive decisions, while workflow orchestration coordinates ordered activities, participants, waits, retries, and process state. The boundary is important when a solution combines decision-making with multi-step processing.

The source characterizes [[drools]] as a decision and business-rules platform and [[liteflow]] as particularly suited to component-flow orchestration. This distinction may overlap with existing [[camunda-based-maker-checker-workflows]].

## Boundary principle

Use a rule engine for independently managed and explainable decisions that can be evaluated from facts. Use a workflow engine for process lifecycle and coordination. Keep domain-service code responsible for side effects, persistence, and integration unless an explicit architecture defines otherwise.

This is a proposed framing, not an approved project boundary. Cash Settlement needs concrete examples and integration contracts before assigning responsibilities.