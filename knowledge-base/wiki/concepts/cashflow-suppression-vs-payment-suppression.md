---
type: concept
title: Cashflow Suppression versus Payment Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-suppression, payment-suppression, settlement-accounting, lifecycle]
related: [settlement-suppression-exceptions, clearing-resultant-swift-suppression, cashflow-fail-and-reinstatement, oscar, amh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# Cashflow Suppression versus Payment Suppression

Cashflow Suppression and Payment Suppression are distinct lifecycle controls.

## Cashflow Suppression

Cashflow Suppression applies when neither payment nor settlement accounting is required. It may be driven by a rules table or initiated manually under Maker–Checker control.

An incorrect suppression can be reversed only until value date. After value date, payment and accounting remediation is handled through [[entities/oscar]]. Trade amendments or cancellations create a new system version and lifecycle.

## Payment Suppression

Payment Suppression applies when payment is not required, while other settlement processing may remain relevant. It may be automatically applied to populations such as clearing deals or manually applied under Maker–Checker control.

An incorrect suppression can be reversed only until value date. After value date, payment remediation is handled through [[entities/amh]] or [[entities/oscar]].

The source does not specify whether both controls may coexist or which status takes precedence when their conditions overlap.
