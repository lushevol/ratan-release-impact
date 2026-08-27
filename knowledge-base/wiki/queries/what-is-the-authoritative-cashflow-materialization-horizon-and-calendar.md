---
type: query
title: What Is the Authoritative Cashflow Materialization Horizon and Calendar?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, materialization, value-date, calendar, open-question]
related: [value-date-based-cashflow-materialization, ratan, stella, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--26-cn-settlement-demo-se--10ylmrb]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md"]
---
# What Is the Authoritative Cashflow Materialization Horizon and Calendar?

Sprint 17 expects a Stella forward cashflow at T+5 to be `QUEUED` and one at T+6 to remain `PROJECTED`. It also expects a T+7 cashflow to become `QUEUED` when the materialization job runs at T+2, described as the VD-5 window.

The implied five-day boundary is not formally defined in the source.

## Questions to Resolve

- Does T+n use business days or calendar days?
- Which settlement calendar, timezone, and cutoff time govern the calculation?
- Is VD-5 the authoritative materialization threshold?
- Is the transition caused only by a scheduled job, or can it occur through another mechanism?
- Does the rule apply to all cashflow sources and products, or only to the Stella scenarios?

## Evidence Needed

Obtain the RATAN materialization configuration, scheduler definition, interface design, and executed test evidence for the cases summarized in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--26-cn-settlement-demo-se--10ylmrb]].