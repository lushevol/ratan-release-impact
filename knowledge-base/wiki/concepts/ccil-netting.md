---
type: concept
title: CCIL Netting
created: 2026-08-22
updated: 2026-08-23
tags: [ccil, india, settlement, netting, swift, accounting, cash-settlement, cross-counterparty]
related: [ratan, ratan-netting-rule-check, swift-network, swift-service, payment-and-cashflow-suppression-governance, ccil, ccil-cashflow-identification, netting-service, settlement-method-driven-netting]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# CCIL Netting

CCIL Netting is the stated India-market netting path for trades booked with CCIL counterparties. Settlement operations consolidate eligible trades into one cashflow against the CCIL central counterparty.

The Cash Settlement Home Page technical design describes CCIL netting as a proposed netting workflow for cashflows whose settlement method is `CCIL`.

> [!NOTE]
> The RATAN Settlement Netting Rule Check source describes the operational outcome for CCIL netting resultants. The CCIL Netting Design source describes proposed eligibility, isolation, cross-counterparty review, and resultant settlement-method behavior. Where the sources do not specify implementation or controls, no generalized conclusion is implied.

## Eligibility and Isolation

According to the CCIL Netting Design, frontend CCIL netting candidates should have:

- Settlement method `CCIL`
- The same entity
- The same value date
- The same currency
- A status described as `waiting+pending netting`

The design states that normal netting must not combine a normal `CASH` cashflow with a CCIL cashflow. This isolation should be represented in frontend filtering. The design also indicates that the backend should enforce the isolation, while not explicitly requiring or describing the backend validation mechanism.

The RATAN Settlement Netting Rule Check source does not identify eligible products or the controlling market configuration.

## Cross-Counterparty Processing

The CCIL Netting Design states that, unlike the normal netting restriction implied by that design, CCIL netting review should allow different counterparties to participate in one netting operation.

The design does not define the required authorization, legal-entity, settlement-account, reconciliation, or audit controls for this cross-counterparty exception.

## Resultant Cashflow and Downstream Processing

The CCIL Netting Design requires the resultant cashflow's settlement method to change from `CCIL` to `CASH`. It does not state whether a separate provenance field or audit event must preserve that the resultant originated from CCIL netting.

For the resulting net cashflow, the RATAN Settlement Netting Rule Check source states that SWIFT generation is bypassed while accounting remains required.

That source does not identify:

- The implementation mechanism for the SWIFT bypass
- The required accounting workflow

This SWIFT and accounting behavior is specific to CCIL netting resultants and must not be generalized to all RATAN auto-netting resultants.