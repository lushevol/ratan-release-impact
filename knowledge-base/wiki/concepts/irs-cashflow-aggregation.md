---
type: concept
title: IRS Cashflow Aggregation
tags: [irs, cashflow, aggregation, settlement, lifecycle]
related: [interest-rate-swap, net-function, cashflow-aggregation-state-model, cashflow-aggregation-lineage, cash-settlement-home-page, what-is-the-authoritative-irs-leg-correlation-and-aggregation-eligibility-rule, is-irs-cashflow-aggregation-fully-automated-or-user-initiated]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# IRS Cashflow Aggregation

IRS cashflow aggregation is the proposed deterministic combination of the two cashflow legs of an [[interest-rate-swap]] into one settlement representation.

## Purpose

The upstream system does not send a pre-merged IRS cashflow. The proposed Aggregation function therefore addresses a settlement requirement rather than a discretionary operator netting activity.

Aggregation is explicitly distinct from the [[net-function]]:

- Net is described as allowing users to merge different cashflows.
- Aggregation is proposed specifically to combine the two IRS legs for settlement.
- The distinction is intended to make the business meaning of each function clear.

## Unspecified operational rules

The source does not define the authoritative pairing key, validation that exactly two eligible legs exist, idempotency behavior, timing of the trigger, or amendment and cancellation treatment.

It also does not establish whether aggregation is fully automated or can be initiated by users. These gaps are tracked in [[what-is-the-authoritative-irs-leg-correlation-and-aggregation-eligibility-rule]] and [[is-irs-cashflow-aggregation-fully-automated-or-user-initiated]].