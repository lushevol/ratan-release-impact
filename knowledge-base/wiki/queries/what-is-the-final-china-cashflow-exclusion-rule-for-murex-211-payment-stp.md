---
type: query
title: What Is the Final China Cashflow Exclusion Rule for Murex 2.11 Payment STP?
created: 2026-08-24
updated: 2026-08-24
tags: [china-settlement, murex-211, payment-stp, routing-rule]
related: [china-cashflow-payment-stp-exclusion, cn-settlement-murex-211-integration, cashflow-suppression-rules, nstp-rule-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# What Is the Final China Cashflow Exclusion Rule for Murex 2.11 Payment STP?

## Question

What rule identifies a China cashflow, at which processing layer is the exclusion enforced, and what is the resulting disposition of an excluded cashflow?

## Evidence

The delivery plan schedules “Exclude China Cashflow from Murex2.11 Payment STP” twice, in Q4 Sprint 15 and Q1 2023 Sprint 1. It also schedules disabling or excluding China cashflows from the BAU payment queue.

## Unknowns

- Whether the repeated Payment STP task is rework, environment-specific scope, or a later release.
- The matching fields and source of the China classification.
- Whether exclusion occurs during extraction, queueing, RATAN ingestion, or multiple layers.
- The precedence against other STP and cashflow-suppression rules.

## Needed evidence

Obtain the functional specification, `RATAN-10678` history, implementation configuration, and test evidence defining eligibility and processing outcomes.