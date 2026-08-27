---
type: query
title: Is IRS Cashflow Aggregation Fully Automated or User-Initiated?
tags: [irs, cashflow, aggregation, automation, operations]
related: [irs-cashflow-aggregation, cashflow-aggregation-state-model, net-function, cash-settlement-home-page]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# Is IRS Cashflow Aggregation Fully Automated or User-Initiated?

## Question

Is IRS cashflow aggregation triggered automatically, initiated by an operator, or supported through multiple controlled mechanisms?

## Evidence

The source states that IRS legs must be combined automatically for settlement. However, it presents action-oriented names—`Aggregate`, `AggregateNew`, and `UnAggregate`—without defining the trigger, actor, permissions, timing, or exception workflow.

## Required resolution

Confirm:

- The triggering event or batch schedule.
- Whether users can invoke aggregation or only view its outcome.
- Authorization and maker-checker requirements for any manual intervention.
- Retry, failure, and duplicate-event handling.
- The relationship between automated aggregation and manual unaggregation.