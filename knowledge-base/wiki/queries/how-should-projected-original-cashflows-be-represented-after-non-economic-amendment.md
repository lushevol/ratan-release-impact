---
type: query
title: How Should Projected Original Cashflows Be Represented After Non-Economic Amendment?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflows, projected-status, amendments, reconciliation, ratan]
related: [non-economic-cashflow-amendment-handling, cashflow-lineage-and-operational-visibility, fmrp-cashflow-status-synchronization, what-is-the-tlm-and-ratan-eod-reconciliation-treatment-for-suppressed-non-economic-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# How Should Projected Original Cashflows Be Represented After Non-Economic Amendment?

The requirement states that when original cashflows are Projected at the time of a fully non-economic amendment, subsequent Released, Netted, or Settled updates apply to replacement cashflows while the original cashflows remain Projected.

This leaves the operational representation unclear because original cashflows remain visible to Settlement Ops, while the active Stella replacement has a later lifecycle status.

## Questions

- What status should the cashflow blotter, Ratan EOD API, audit views, and reporting expose?
- How should the status mismatch be reconciled and explained to operational users?
- Are intermediate lineage records updated, or only the latest active replacement?
- What retry and failure behavior applies when propagation to Stella fails?