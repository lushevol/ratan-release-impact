---
type: query
title: What Is the v1/v2 Cashflow STP Blocking Rule?
created: 2026-08-24
updated: 2026-08-24
tags: [query, v1, v2, stp, cashflow, group-blotter, ratan]
related: [ratan, murex-211, trade-validation-cashflow-gating, cashflow-business-and-message-versioning, non-economic-cashflow-amendment-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--g0i06l]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# What Is the v1/v2 Cashflow STP Blocking Rule?

## Question

What is the authoritative rule that prevents STP of a v1 cashflow while v2 cashflows remain in RATAN’s Group Blotter?

## Requirement Gap

The source states the requirement as “To Be Enriched” but does not define:

- how v1 and v2 are identified;
- whether versions refer to trade versions, payment generations, business versions, or message versions;
- which v1 actions are blocked;
- whether the block applies to one currency leg, a trade, a batch, or an entire Group Blotter;
- what conditions release or cancel the block;
- how non-economic amendments and reversal cashflows are treated;
- what Operations should do when a blocking version remains pending.

The scenarios contain payment generations such as `p1` through `p5`, but these identifiers do not by themselves establish the formal v1/v2 control.

## Evidence Boundary

The UAT cases demonstrate validation-based release and several complex amendment paths, including manual handling of predecessor or reversal payments. They do not include an attempted v1 STP while a v2 cashflow remains pending, nor do they record a pass/fail assertion for that behavior.

A dedicated functional requirement, data model, and executable UAT scenario are needed before this can be considered an implemented or validated control.