---
type: query
title: How Is Lien Removal or Zero Lien Processed in RATAN?
created: 2026-08-23
updated: 2026-08-23
tags: [lien, exception-lifecycle, ratan, nstp]
related: [ratan, tds3, lien-driven-cashflow-nstp, trade-lien-notification-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# How Is Lien Removal or Zero Lien Processed in RATAN?

The requirement defines lien placement and lien-amount update behavior but does not define how RATAN handles lien removal, a zero lien value, event correction, cancellation, or reversal.

This is particularly important because **“LIEN on Trade”** is system-defined and unavailable for Ops update or removal. Clarification is needed on:

- the authoritative condition that indicates a lien is no longer active;
- whether RATAN automatically resolves, supersedes, or retains the exception;
- reprocessing and un-netting implications for previously affected cashflows; and
- audit and maker/checker requirements for a system-led resolution.

The source document ends before providing its full function flow.