---
type: concept
title: Cashflow Aggregation Lineage
tags: [cashflow, aggregation, lineage, audit, idempotency, irs]
related: [irs-cashflow-aggregation, cashflow-aggregation-state-model, cashflow-lineage-and-amendment-correlation, what-is-the-authoritative-irs-leg-correlation-and-aggregation-eligibility-rule, what-is-the-authoritative-unaggregate-state-and-lineage-behavior]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# Cashflow Aggregation Lineage

Cashflow aggregation lineage is the relationship between the two source IRS cashflow legs and any resulting aggregated settlement cashflow.

The proposed IRS aggregation process requires a reversible and auditable relationship model, but the source does not specify one.

## Required design decisions

A complete lineage design must establish:

- The authoritative key used to identify the two related IRS legs.
- Eligibility checks for product, currency, value date, direction, account, and SSI compatibility.
- Validation that exactly two eligible legs are combined.
- Idempotency and duplicate-prevention behavior.
- Whether aggregation modifies source cashflows, creates a new cashflow, or creates a parent-child relationship.
- Audit history for aggregation, reversal, amendment, cancellation, and failed processing.
- The lifecycle behavior of each linked object during `UnAggregate`.

The existing [[cashflow-lineage-and-amendment-correlation]] material is relevant as a lineage pattern, but it does not establish rules for IRS aggregation. The unresolved pairing and reversal requirements are tracked in [[what-is-the-authoritative-irs-leg-correlation-and-aggregation-eligibility-rule]] and [[what-is-the-authoritative-unaggregate-state-and-lineage-behavior]].