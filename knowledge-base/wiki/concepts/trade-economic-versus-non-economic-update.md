---
type: concept
title: Trade Economic Versus Non-Economic Update
tags: [trade, economic-update, non-economic-update, cashflow, Reference-ID]
related: [trade-cashflow-reference-linkage, trade-event-id-lineage, cashflow-amendment-supersession, scbml]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md"]
---
# Trade Economic Versus Non-Economic Update

The deprecated design distinguishes trade updates by whether they affect cashflows.

## Economic update

An economic update changes cashflow economics and generates amended cashflows. Under the proposed model, it changes the Reference ID shared by the trade and its resulting cashflows.

## Non-economic update

A non-economic amendment does not change the cashflow economics. Under the proposed model, its Reference ID remains unchanged, although its Event ID may change.

This distinction is important because Event ID behavior is not uniform: an economic update can retain the same Event ID while producing new cashflow versions, whereas a non-economic amendment can receive a new Event ID. The source does not provide a complete classification catalogue for all trade actions.