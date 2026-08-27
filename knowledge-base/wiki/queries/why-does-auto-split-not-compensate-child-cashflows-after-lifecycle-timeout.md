---
type: query
title: Why Does Auto Split Not Compensate Child Cashflows After Lifecycle Timeout?
tags: [cashflow-splitting, auto-split, compensation, timeout, lifecycle]
related: [cashflow-auto-split-failure, ratan-cashflow-lifecycle-service, ratan-cash-settlement-netting-service, camunda]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# Why Does Auto Split Not Compensate Child Cashflows After Lifecycle Timeout?

## Question

Is the absence of child compensation after an automatic-split lifecycle timeout intentional, or is it an implementation defect?

## Evidence

In manual-split UAT, a lifecycle timeout was followed by successful lifecycle processing and consumption of the parent domain event to continue child processing.

In the automatic process-stage timeout scenario, children were generated but remained in `Queue`, and the source reports that no compensation was triggered. Camunda then moved the parent to `TechFail`.

## Needed Resolution

Establish whether automatic splitting should consume the same parent event, use a separate retry process, or transition partial children to a repairable exception state. The solution must define duplicate-event protection and ownership between lifecycle, netting, orchestration, and Camunda.