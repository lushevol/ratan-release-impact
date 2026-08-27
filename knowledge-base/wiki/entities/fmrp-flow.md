---
type: entity
title: FMRP Flow
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, cashflow-generation, fmrp]
related: [ratan, stella, murex-2-11, normalized-payment-schedule, product-agnostic-cashflow-aggregation]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
---
# FMRP Flow

FMRP Flow is described in this draft as the processing flow for which [[stella]] generates cashflows.

The document identifies a functional difference relevant to aggregation: same-trade cashflow aggregation is stated to occur in [[murex-2-11]] but not in Stella-generated FMRP Flow cashflows. [[ratan]] currently supplements that gap through taxonomy-specific mechanisms, while [[normalized-payment-schedule]] is proposed as an upstream dependency for a broader aggregation approach.

The source cites `InterestRate:LoanDeposit` as an example of an additional taxonomy entering FMRP Flow. It does not provide a complete taxonomy inventory or confirm product coverage.