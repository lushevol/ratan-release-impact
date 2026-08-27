---
type: query
title: What Is the Authoritative LMS Message Behavior for Split Cashflows?
created: 2026-08-22
updated: 2026-08-22
tags: [lms, cashflow-splitting, integration, message-reconciliation]
related: [lms, split-cashflow-downstream-integration, cashflow-splitting, clearing-swift-suppression, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# What Is the Authoritative LMS Message Behavior for Split Cashflows?

The UAT marks LMS cases as `Pass`, but the evidence reports missing parent and netting-resultant messages, missing suppressed-child messages, and a released child received twice.

The open question is whether these outcomes reflect an intentional parent-versus-child message contract, LMS filtering defects, duplicate delivery, or inconsistent test reconciliation.

Resolution should define expected behavior for:

- Split parents.
- Released children.
- `SWIFT_SUPPRESSED` children.
- `CASHFLOW_SUPPRESSED` children.
- Threshold-generated replacement children.
- Withdrawal and reversal events.

See sources/26-auto-netting-page-md-files--159-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-se--bwywva and [[entities/lms]].