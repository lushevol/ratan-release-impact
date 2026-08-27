---
type: concept
title: FX Utilization
created: 2026-08-23
updated: 2026-08-23
tags: [fx, utilization, cash-settlement, transaction-banking, fx-utilization, fxu, trade, cashflow]
related: [fxu, ratan, blade, stella, scpay, utilization-remaining-amount, utilization-status-lifecycle, partial-and-pastdue-utilization-accounting, fxu-utilization-validation, fxu-message-driven-integration, cashflow-version-tuple-comparison]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# FX Utilization

FX utilization is the application of an FX trade amount to one or more settlement cashflows. In the functional-requirement description, it is the process by which Transaction Banking applies a client's payment instruction against an eligible FX settlement amount before settlement.

The operation is trade-identified but cashflow-constrained:

- The request carries a trade identifier and currency amount.
- The query response supplies cashflow state, payment amount, remaining amount, payment date, settlement method, and settlement-account information.

## Proposed architecture

The functional-requirement source's proposed architecture places [[ratan]] in control of:

- Request validation
- Remaining amount
- Utilization status
- Settlement controls
- Accounting publication

[[fxu]] provides operational retrieval and instruction entry. [[blade]] and [[stella]] control booking and lifecycle effects.

## Utilization forms

The technical design names the following forms:

- **Full utilization:** represented by `VDATE-FULL-UTIL`.
- **Partial utilization:** represented by partial-utilization types and amounts less than the available amount.
- **Manual utilization:** initiated by a user or operational workflow.
- **Auto utilization:** system-triggered utilization.
- **Past-due utilization:** utilization after the value date.
- **Reverse utilization:** reversal of a previous utilization.

The permitted combinations of utilization type, value-date window, cashflow state, and amount are not fully specified by the technical design.

## Trade and cashflow relationship

A single FX trade can produce multiple currency cashflows. The technical-design example returns the following cashflows for the same trade:

- A `Pay` cashflow of `749.98` `SAR`
- A `Receive` cashflow of `200.0` `USD`

Both example cashflows are `PASTDUE`, use settlement method `UTIL`, and reference trade `7111011106`.

Swap-related requests may identify the `Far` or `Near` leg through `Swap_Leg_ID`. The request also carries `Trade_Lake_Trade_Major_Version`, which supports version-specific validation.

## MVP scope and lifecycle uncertainty

According to the functional-requirement source, MVP supports full utilization only on the value date. Partial utilization, reversal, post-value-date PastDue utilization, and early utilization are Phase 2 proposals and must not be treated as current functionality.

The technical-design source separately states that the MVP NACK catalogue does not currently allow reverse, early, past-due, or partial utilization. However, its response examples include `VDATE-PART-REV` and partial amounts. This conflict between the stated MVP restrictions and the technical-design examples is tracked in [[does-mvp-support-partial-fx-utilization]].
