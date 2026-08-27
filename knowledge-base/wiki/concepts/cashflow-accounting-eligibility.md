---
type: concept
title: Cashflow Accounting Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, cashflow, eligibility, business-rules, cash-settlement]
related: [ebbs, aspire, cashflow-accounting-stamping, entity-based-eod-feeding, single-payment-realtime-accounting-feeding, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Cashflow Accounting Eligibility

## Definition

Cashflow accounting eligibility comprises the rules that determine which cashflows are included in Aspire and EBBS accounting feeds.

The source explicitly marks these rules as **TBC** for both accounting-entry generation scopes.

## Impact

Until eligibility is defined, the project cannot reliably determine:

- The complete accounting population.
- Expected feed volumes.
- Completeness checks.
- Exclusion behavior.
- Reconciliation coverage.
- Whether EOD and realtime feeding apply to the same population.

This is a material unresolved business rule rather than a minor implementation detail.

## Required Clarification

The authoritative rule should identify eligible and excluded cashflow types, relevant regional or entity conditions, treatment of cancellations and amendments, and how eligibility is represented in reconciliation outputs.
