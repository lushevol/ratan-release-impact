---
type: query
title: Is Expiry Processing Intentionally Excluded from Refixing Workflows?
created: 2026-08-24
updated: 2026-08-24
tags: [refixing, expiry, cashflow-processing, test-coverage, uat]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-trade-cashflow-events--1p4c878, stella, cashflow-lifecycle-state-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/Drop 2 UAT Open Issues and test cases.md"]
---
# Is Expiry Processing Intentionally Excluded from Refixing Workflows?

Is the statement that expired items are not processed an intended design restriction, an unimplemented capability, a defect, or a UAT test-environment limitation?

## Evidence

The Drop 2 UAT action for “Refixing (After released) +Expire test” records that manual refixing is done, automatic refixing is still to be booked, and expired items are not processed.

The source does not identify the affected system, define expected expiry semantics, or provide a defect identifier. It therefore establishes incomplete test coverage rather than an approved product limitation.

## Information Needed

- Functional requirements for expiry processing after release and refixing.
- Whether automatic refixing has been scheduled and executed.
- The intended status and operational treatment of expired cashflows.
- Defect, backlog, or design-decision evidence explaining the exclusion.

## Related Pages

- [[stella]]
- [[cashflow-lifecycle-state-model]]
- [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-trade-cashflow-events--1p4c878]]