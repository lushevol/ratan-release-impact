---
type: query
title: What Is the Authoritative Cashflow Netting and Un-Netting State Model?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, netting, un-netting, lifecycle, open-question]
related: [cashflow-netting-and-un-netting, cashflow-status-lifecycle, ratan, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# What Is the Authoritative Cashflow Netting and Un-Netting State Model?

The Sprint 14 demo specifies `Queued → Netted` for components, creation of a `Queued` resultant, restoration of components to `Queued` on un-netting, and transition of the resultant to `Dead`.

The authoritative model remains unresolved because the source does not state whether partial un-netting is supported, whether a resultant can be re-created after reversal, whether a netting ID is reusable, or how audit history is retained.