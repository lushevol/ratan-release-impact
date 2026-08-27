---
type: project
title: 2026 BRP Q3 RatanSett Product-Agnostic Aggregation
created: 2026-08-22
updated: 2026-08-22
tags: [2026-brp-q3, ratansett, cash-settlement, aggregation, fmrp]
related: ["ratan", "normalized-payment-schedule", "product-agnostic-cashflow-aggregation", "fmrp-flow", "what-are-the-normalized-payment-schedule-aggregation-keys", "how-will-normalized-payment-schedule-aggregation-coexist-with-irs-and-ccs-auto-netting", "what-is-the-historical-data-policy-for-normalized-payment-schedule-aggregation"]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
status: planned
owner: ""
start_date: 2026-08-22
target_date: ""
---
# 2026 BRP Q3 RatanSett Product-Agnostic Aggregation

## Brief

This planned enhancement corresponds to ADO Story 14618546, “[2026 BRP Q3 RatanSett Enhancement] Product Agnostic Aggregation based on Normalized Payment Schedule.”

It proposes introducing [[normalized-payment-schedule]] to support [[product-agnostic-cashflow-aggregation]] in [[ratan]].

## Business rationale

The source identifies that:

- [[murex-2-11]] is stated to aggregate cashflows under the same trade, while [[stella]] does not provide that behavior for [[fmrp-flow]].
- Existing IRS Netting and [[ccs-auto-netting]] are taxonomy-specific supplementary mechanisms.
- Further FMRP Flow taxonomies, including `InterestRate:LoanDeposit` as an example, create demand beyond IRS and CCS coverage.
- Current IRS Netting is stated not to support an IRS model with multiple cashflows in the second leg.

## Status and constraints

The project is recorded as planned because the source is a draft requirement and contains no implementation, approval, test, or deployment evidence.

Detailed user cases are referenced through an unavailable `analysis.xlsx` attachment and screenshots. Key functional rules therefore remain unverified.

## Key open requirements

- [[what-are-the-normalized-payment-schedule-aggregation-keys]]
- [[how-will-normalized-payment-schedule-aggregation-coexist-with-irs-and-ccs-auto-netting]]
- [[what-is-the-historical-data-policy-for-normalized-payment-schedule-aggregation]]

## Risks

- Unspecified matching keys may lead to incorrect aggregation.
- Concurrent legacy and new aggregation paths may create duplicate or inconsistent outputs.
- Historical-data handling is undefined.
- Initial taxonomy coverage and exclusions are not stated.
- Downstream impacts on settlement, SWIFT generation, accounting, and operational workflows are not documented.