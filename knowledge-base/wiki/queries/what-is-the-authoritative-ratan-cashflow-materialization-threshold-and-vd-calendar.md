---
type: query
title: What Is the Authoritative RATAN Cashflow Materialization Threshold and VD Calendar?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, materialization, value-date, lifecycle]
related: [cashflow-materialization, ratan, cashflow-record]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md"]
---
# What Is the Authoritative RATAN Cashflow Materialization Threshold and VD Calendar?

The Sprint 13 requirement expects a Stella cashflow at VD-7 to be `Projected`, while VD-5 and VD-4 cashflows are `Queued`; it also expects a materialization run on VD-5 to transition a VD-7 cashflow to `Queued`.

The authoritative definition remains unknown.

## Questions to Resolve

- Does VD represent calendar days, business days, or settlement-calendar days?
- Which holiday calendar, time zone, and cut-off time apply?
- What are the expected states at VD-6, VD-3 through VD0, and for past-due cashflows?
- Is materialization scheduled automatically, and what are its retry, failure, and rerun rules?
- Is the Sprint 13 threshold still valid for current RATAN processing?

## Evidence Boundary

The available source is a demo specification with expected results only. It does not demonstrate test execution or establish an enduring production contract.