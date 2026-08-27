---
type: query
title: How Are Stella Cashflow Versions Correlated With Ratan Versions?
created: 2026-08-24
updated: 2026-08-24
tags: [stella, versioning, correlation, cashflow]
related: [cashflow-status-result-events, strategic-cashflow, stella-cashflow-status-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# How Are Stella Cashflow Versions Correlated With Ratan Versions?

The source contains `cashflowVersion`, `businessVersion`, transaction-version transitions, and `stellaCashflowVersion`, but does not define their respective domains or consistency rules.

Establish the authoritative meaning of each counter, expected increments, validation behavior, and the correlation behavior when a failure result omits Ratan identifiers.