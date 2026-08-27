---
type: query
title: What Is the Canonical Rule-Maintenance Maker-Checker State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-maintenance, maker-checker, authorization]
related: [ratan-rule-engine, camunda-based-maker-checker-workflows, nstp-maker-checker-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# What Is the Canonical Rule-Maintenance Maker-Checker State Machine?

## Question

Which statuses, transitions, roles, approval rules, segregation-of-duties controls, and audit requirements govern rule CRUD operations?

## Evidence

The source lists `SAVE_CONFIRMED` and `DELETE_PENDING` as running statuses, but its “Not Running status” statement is incomplete. Maintenance UML, maker actions, checker actions, and event treatment are headings without substantive design.

This requirement must not be assumed to use the [[camunda-based-maker-checker-workflows]] or [[nstp-maker-checker-processing]] state machines.