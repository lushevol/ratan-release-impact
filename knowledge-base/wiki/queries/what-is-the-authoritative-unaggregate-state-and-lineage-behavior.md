---
type: query
title: What Is the Authoritative UnAggregate State and Lineage Behavior?
tags: [cashflow, aggregation, unaggregate, lifecycle, lineage, dead-status]
related: [cashflow-aggregation-state-model, cashflow-aggregation-lineage, irs-cashflow-aggregation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# What Is the Authoritative UnAggregate State and Lineage Behavior?

## Question

What cashflow object does `UnAggregate` affect, and under what conditions does it transition to `QUEUED` versus `DEAD`?

## Evidence

The proposed matrix contains two materially different `UnAggregate` outcomes:

- `AGGREGATED` transitions to `QUEUED`.
- `QUEUED`, `WAITING`, `HOLD`, `FAILED`, `SWIFT_SUPPRESSED`, `CASHFLOW_SUPPRESSED`, and `READY` transition to `DEAD`.

The source does not state whether these rules concern source legs, an aggregate-created cashflow, or separate cashflow roles. It also asks whether manual unaggregation is required without answering the question.

## Required resolution

Define the object model, restoration behavior, audit requirements, downstream notifications, permitted lifecycle stages, and the rationale for any `DEAD` transition.