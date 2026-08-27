---
type: concept
title: Value-Date-Based Cashflow Materialization
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, materialization, value-date, settlement-status, ratan]
related: [ratan, stella, cashflow-blotter, auto-netting-job, what-is-the-authoritative-cashflow-materialization-horizon-and-calendar]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md"]
---
# Value-Date-Based Cashflow Materialization

Value-date-based cashflow materialization is the expected RATAN behavior that makes a cashflow operationally eligible by moving it from `PROJECTED` to `QUEUED` when its value date falls within an applicable processing window.

## Sprint 17 Expected Boundary

The documented acceptance cases specify:

- T+2 CCS initial exchange: `QUEUED`;
- one-year CCS final exchange: `PROJECTED`;
- T+5 Stella forward: `QUEUED`;
- T+6 Stella forward: `PROJECTED`;
- T+7 Stella forward before the stated window: `PROJECTED`;
- the same T+7 cashflow after a materialization job runs at T+2, described as VD-5: `QUEUED`.

This indicates an intended boundary around five days before value date. The source does not establish that this is a universal RATAN rule.

## Distinction from Auto-Netting

The materialization job changes settlement eligibility/status. It is not the [[auto-netting-job]] and the source does not state that materialization performs netting.

## Open Parameters

The governing date calendar, business-day treatment, timezone, cutoff time, scheduler configuration, and product/source applicability remain unresolved. See [[what-is-the-authoritative-cashflow-materialization-horizon-and-calendar]].