---
type: query
title: Are Settled Cashflows Intentionally in Scope for Korea TIS Query?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, tis, cashflow-state, eligibility, korea-migration]
related: [ratan-tis-payment-query-integration, korea-settlement-account-routing, scfb-seoul, ratan, tis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# Are Settled Cashflows Intentionally in Scope for Korea TIS Query?

## Question

Should the RATAN-to-TIS payment and receipt APIs return `Settled` cashflows, or should they return only `Released` cashflows?

## Evidence

Both documented API filters select:

```text
Cashflow.Cashflow_State in ('Released','Settled')
```

The static-data matrix, however, describes the `UISUS`, `UIBOK`, and `UIDD` TIS/OLTP routes with post-cutoff status `Released`.

## Why it matters

Returning settled cashflows may create duplicate or late operational items in TIS. Excluding them may omit an intended recovery or historical-query population.

## Needed decision

Define the state eligibility independently for pay-side and receipt routes, identify the operational rationale, and provide acceptance-test cases for `Released`, `Settled`, reversed, and subsequently cancelled cashflows.