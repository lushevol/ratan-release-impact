---
type: concept
title: Fixing-Schedule-Cashflow Correlation
created: 2026-08-24
updated: 2026-08-24
tags: [fixing, re-fixing, schedule, cashflow, correlation]
related: [uber-message, cashflow-lineage-and-operational-visibility, cashflow-business-and-message-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Fixing-Schedule-Cashflow Correlation

## Definition

Fixing-schedule-cashflow correlation is the proposed use of a unique identifier to link a fixing notice, its schedule, and the underlying cashflow.

The requirement applies to fixing and re-fixing events carried in the [[uber-message]]. It is intended to make the affected cashflow unambiguous within a complete parent-trade snapshot.

## Required contract decisions

The source does not define:

- Identifier ownership or generation
- Uniqueness scope
- Persistence and retention
- Cardinality between fixing notices, schedules, and cashflows
- Behavior when a fixing is re-fixed or amended
- Whether the identifier is stable across cashflow versions

These questions are tracked in [[what-is-the-fixing-notice-schedule-cashflow-correlation-id-contract]].