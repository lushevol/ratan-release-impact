---
type: query
title: What Is the Authoritative Ratan Treatment for Non-Economic Amendment Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [Ratan, non-economic-amendment, cashflow-eligibility, settlement-controls, open-question]
related: [non-economic-cashflow-suppression, fmrp-payment-eligibility-and-suppression, fmrp-payment-insertion-eligibility, cashflow-version-concurrency-control, cashflow-lifecycle-state-model, stella, tds3, ratan, cdu]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Ratan Non Economic Cashflow Handling.md"]
---
# What Is the Authoritative Ratan Treatment for Non-Economic Amendment Cashflows?

## Question

When Stella creates replacement cashflows for a non-economic trade amendment and sends them through `TDS3` to `Ratan`, are those cashflows physically discarded, retained but marked ineligible, excluded only from the Cashflow Blotter, or allowed through receipt while being excluded from STP and settlement feeds?

## Evidence

The source proposes discarding replacement cashflows such as `C3` and `C4` so that they are not visible to Settlement Ops. It separately states that Ratan updates active cashflows and shows `C3` and `C4` progressing from `PROJECTED` to `PROJECTED->SETTELD`. These statements are not reconciled.

The source also shows inconsistent illustrative mappings between Stella and Ratan cashflow IDs. It does not define whether the examples represent record reuse, event correlation, or documentation errors.

## Decisions Required

Clarification is needed on:

1. The authoritative economic/non-economic amendment indicator.
2. The suppression point in the processing pipeline.
3. Persistence, audit, reconciliation, and error-handling requirements.
4. Treatment of withdrawal events for the previous trade version.
5. The canonical cashflow identity and event-correlation rule.
6. Status ownership and valid transitions for `PROJECTED`, `WAITING`, and `SETTLED`.
7. Whether suppressed cashflows are excluded from downstream settlement feeds as well as the Ratan blotter.
8. Handling of late, duplicated, or out-of-order amendment and confirmation messages.

## Related Controls

The answer must preserve the latest trade-version principle described for [[cdu]]: confirmation-status notifications use the latest trade ID and trade version for both economic and non-economic amendments. That principle should not be conflated with cashflow settlement eligibility.

This query draws on [[non-economic-cashflow-suppression]], [[cashflow-version-concurrency-control]], and [[fmrp-payment-insertion-eligibility]].