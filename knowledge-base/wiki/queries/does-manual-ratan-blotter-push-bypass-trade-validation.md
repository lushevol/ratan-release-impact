---
type: query
title: Does Manual RATAN Blotter Push Bypass Trade Validation?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, RATAN, trade-validation, manual-control, exception-handling]
related: [trade-validation-cashflow-gating, manual-cashflow-blotter-push-exception, ratan-group-blotter-event-completeness, ratan, murex-211]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
---
# Does Manual RATAN Blotter Push Bypass Trade Validation?

## Question

When a trade is not validated on value date, does manually pushing the cashflow to the RATAN cashflow blotter bypass the normal validation gate, or does it place the cashflow into a separately controlled exception state?

## Evidence

The requirement says that SG, MY, and IN cashflows should enter the blotter only after validation from 10 August, but also instructs operators to monitor and manually push cashflows when validation is unavailable on value date. It does not define an override status, approval authority, audit trail, or reconciliation procedure.

## Information needed

- The exact state transition caused by a manual push.
- Whether the trade must subsequently be validated before payment release.
- Required approver and segregation-of-duties controls.
- Audit and reconciliation fields.
- Monitoring and escalation SLA.