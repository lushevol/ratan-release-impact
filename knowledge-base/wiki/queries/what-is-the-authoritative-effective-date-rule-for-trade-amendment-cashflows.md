---
type: query
title: What Is the Authoritative Effective-Date Rule for Trade Amendment Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [trade-amendment, effective-date, cashflow-generation, stella, uat]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-trade-cashflow-events--1p4c878, stella, cashflow-lifecycle-state-model, cashflow-business-and-message-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/Drop 2 UAT Open Issues and test cases.md"]
---
# What Is the Authoritative Effective-Date Rule for Trade Amendment Cashflows?

For a Stella trade amendment, what is the required treatment of cashflows with value dates before, equal to, and after the amendment effective date?

## Evidence

The Drop 2 UAT register records critical open defect 423 for `MTC17`: cashflows with `VD<effective date` are touched, while cashflows with `VD>effective date` do not generate a new cashflow. The issue is tracked in Azure DevOps work item `3875467` with an ETA of 23rd Apr.

The source is sufficient evidence that the issue was open and critical at the time of the register. It does not define the expected state transition, versioning rule, generation rule, or closure result.

## Information Needed

- The approved Stella amendment functional specification.
- Expected outcomes for value dates before, equal to, and after the effective date.
- Resolution and regression evidence for Azure DevOps work item `3875467`.
- Confirmation of the outcomes for trades `4330350484` and `4354404271`.

## Related Pages

- [[stella]]
- [[cashflow-lifecycle-state-model]]
- [[cashflow-business-and-message-versioning]]
- [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-trade-cashflow-events--1p4c878]]