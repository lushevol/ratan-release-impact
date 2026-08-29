---
type: entity
title: TDSX
created: 2026-08-22
tags: [tdsx, payment-schedule, cash-settlement, api, IRS, cashflow-schedule, Stella, uber, publisher, release-operations, trade-data, api-layer, tds2, tds3, sabre]
related: ["stella", "tds2", "tds3", "delivery-versus-payment", "dvp-nstp", "blade", "irs-fixed-floating-leg-netting", "pending-another-leg-status", "tdsx-uber-message-listener", "sabre-pss", "upstream-cashflow-replay-for-group-completion", "ratan-tdsx-integration", "sabre", "solace", "what-is-the-authoritative-ratan-tdsx-interface-contract", "what-is-the-authoritative-stella-tdx-tdsx-schedule-lookup-contract"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
updated: 2026-08-25
---

# TDSX

## Identity and documented architecture

TDSX, or Trade Data Store X, is described by the RATAN/SABRE interface source as a unified API layer over TDS2 and [[tds3|TDS3]]. That source places TDSX within the Trade Store Convergence Program and states that it is intended to hide the physical-store split from consumers.

The same source does not define:

- Request routing between TDS2 and TDS3.
- TDSX API or message schemas.
- Ownership boundaries between TDSX and SABRE.

The 2024-changes source states that TDS2 provides the TDSX API for Drop2/Drop3 and separately identifies [[tds3]] as a source of COM status and trade information for other flows. It does not define whether TDS2 owns TDSX, consumes it, or delivers an adjacent API. These statements should therefore remain source-specific rather than being treated as a fully documented ownership model.

The IRS fixed/floating-leg payment-handling source uses the lineage `Blade->Stella->TDS3→Ratan` and inconsistently refers to TDX, TDSX, and TDS3. It does not define the authoritative service identity, endpoint, response contract, availability handling, or exact date-match condition. These gaps are tracked in what is the authoritative stella tdx tdsx schedule lookup contract.

## RATAN interface

For the documented RATAN interface, the RATAN/SABRE source states that TDSX:

- Provides Payment Schedule data for RATAN trade control and Trade Blotter display.
- Exposes a REST API called by RATAN for trade validation.
- Publishes Uber messages delivered to RATAN through Solace.

The functional and netting requirements further identify TDSX as an API or data dependency for payment-schedule information used by Stella-related cash-settlement functions.

The IRS fixed/floating-leg payment-handling source describes TDSX as the schedule-information API dependency used by [[ratan]] for Stella/FMRP IRS cashflows. RATAN queries it by trade ID to retrieve scheduled interest-payment dates for both legs of an IRS.

The authoritative RATAN/TDSX interface contract, including the precise endpoint, request and response schemas, and related interface details, is not established here. See ratan tdsx integration and what is the authoritative ratan tdsx interface contract.

## Payment-schedule requirements and uses

The 2024-changes source assigns Stella/TDSX payment-schedule dependencies to:

- Fixing/floating netting.
- DVP NSTP.

The DVP NSTP requirement includes the unresolved note “only for CN booking?” This is not confirmed as a CN-only restriction.

For the `Blade->Stella->TDS3→Ratan` booking lineage, the IRS fixed/floating-leg payment-handling source states that RATAN compares the SCBML cashflow payment date with the first- and second-leg payment-date schedules. The intended purpose is to avoid holding a valid standalone coupon in `Pending Another Leg` when no matching coupon is expected for that schedule.

## Uber publishing and rollout operations

The RATAN/SABRE source states that TDSX publishes Uber messages and that RATAN receives them through Solace.

Separately, the Uber rollout runbook identifies TDSX as the publisher-management team or system responsible for the Uber flow. This is an operational reference and does not establish that the Uber publisher role is the same interface or component as the payment-schedule API dependency.

According to the Uber rollout runbook, the planned country-specific TDSX publisher stop and restart were struck through after selective suspension for EG, NP, and SA was reported as infeasible.

The runbook does not define a replacement control or establish whether TDSX publishing was stopped during the release. These rollout statements concern the publisher-management role or system described by that runbook and should not be generalized into the payment-schedule API behavior described by the functional and netting requirements.