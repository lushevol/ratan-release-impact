---
type: concept
title: Normalized Payment Schedule
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, payment-schedule, data-modeling, aggregation, fmrp]
related: [product-agnostic-cashflow-aggregation, 2026-brp-q3-ratansett-product-agnostic-aggregation, ratan, fmrp-flow, cashflow-logical-model, scbml-cashflow-ingestion-and-persistence, what-are-the-normalized-payment-schedule-aggregation-keys]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
---
# Normalized Payment Schedule

Normalized Payment Schedule is a proposed upstream data-model mechanism intended to enable [[product-agnostic-cashflow-aggregation]] in [[ratan]] across cashflow taxonomies in [[fmrp-flow]].

The draft presents it as the strategic alternative to extending separate, taxonomy-specific aggregation mechanisms such as IRS Netting and [[ccs-auto-netting]].

## Known intent

The stated purpose is to provide a normalized basis on which eligible cashflows can be aggregated without restricting the solution to IRS or CCS taxonomies.

## Undefined design details

This source does not define:

- The schedule schema, identifiers, or owning system.
- The schedule granularity and source-to-schedule cardinality.
- Aggregation and eligibility keys.
- Conflict resolution when schedule attributes differ.
- Product scope, exclusions, and rollout sequencing.
- Historical-data, replay, idempotency, or reconciliation behavior.
- Downstream effects on settlement, SWIFT, accounting, or blotter workflows.

These unresolved requirements are tracked in [[what-are-the-normalized-payment-schedule-aggregation-keys]] and [[what-is-the-historical-data-policy-for-normalized-payment-schedule-aggregation]].