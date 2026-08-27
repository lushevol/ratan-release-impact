---
type: query
title: What Is the Authoritative IRS Leg Correlation and Aggregation Eligibility Rule?
tags: [irs, cashflow, aggregation, correlation, eligibility, idempotency]
related: [irs-cashflow-aggregation, cashflow-aggregation-lineage, interest-rate-swap, cashflow-lineage-and-amendment-correlation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# What Is the Authoritative IRS Leg Correlation and Aggregation Eligibility Rule?

## Question

What authoritative key identifies the two IRS cashflow legs that may be aggregated, and what validation rules prevent incompatible or duplicate pairings?

## Why this matters

The source requires the combination of two IRS legs but provides no correlation key or eligibility contract. Without this definition, aggregation cannot be made reliably deterministic or idempotent.

## Evidence

[[irs-cashflow-aggregation]] states that the upstream system does not provide a pre-merged cashflow and that two IRS legs must be combined for settlement. The source does not specify product confirmation, value-date alignment, currency compatibility, direction, account or SSI compatibility, amendment behavior, or duplicate prevention.

## Required resolution

Define the authoritative relationship identifier and all required eligibility checks, including behavior for missing, late, amended, cancelled, or already-aggregated legs.