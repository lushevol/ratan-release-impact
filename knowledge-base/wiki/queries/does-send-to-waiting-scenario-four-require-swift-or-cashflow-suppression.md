---
type: query
title: Does Send to WAITING Scenario Four Require SWIFT or Cashflow Suppression?
tags: [cashflow, swift, suppression, acceptance-criteria, reinstate]
related: [held-cashflow-reinstatement, cash-settlement-home-page, ssi-exception-state-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Actions on Hold.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Does Send to WAITING Scenario Four Require SWIFT or Cashflow Suppression?

Acceptance scenario 4 is titled **Send to WAITING + swift suppress** and expects final state `SWIFT_SUPPRESSED`. However, its final scenario step says that the user performs **cashflow suppress**.

## Required clarification

Confirm the authoritative action for scenario 4 and whether:

- SWIFT suppression alone produces `SWIFT_SUPPRESSED`;
- cashflow suppression can ever produce `SWIFT_SUPPRESSED`; or
- the scenario step is a documentation error.

The clarification should preserve the distinction between cashflow suppression, whose documented outcome is `CASHFLOW_SUPPRESSED`, and SWIFT suppression.