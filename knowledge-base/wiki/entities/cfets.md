---
type: entity
title: CFETS
created: 2026-08-22
updated: 2026-08-23
tags: [market-infrastructure, external-system, cn-ccs, trade-booking-system, clearing, CFETS, trade-source, confirmation, stella, deprecated-evidence]
related: [cash-settlement-2025-roadmap, ratan, fmrp, murex, clearing-trade-payment-risk, clearing-status-propagation, stella, confirmation-source-routing, comp-status-driven-stp, what-is-the-current-fmrp-and-cfets-confirmation-status-source-and-eligibility-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Clearing Trades & Payment Risk.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# CFETS

CFETS is an external system or market-infrastructure dependency associated with the CN CCS workstream in the [[cash-settlement-2025-roadmap]].

The [[clearing-trade-payment-risk]] source additionally identifies CFETS as a trade-booking source system included in the clearing-trade scope matrix.

## Recorded Milestones

The [[cash-settlement-2025-roadmap]] associates the CN CCS CFETS go-live with 8 March 2025. It separately associates CN CCS trade migration with August 2025.

These are distinct events and should not be represented as a single undifferentiated go-live.

## Clearing Status Scope

According to the [[clearing-trade-payment-risk]] source, the first version has clearing status for CHINA HO and HONGKONG flows. These flows are marked for novation to a Clearing House.

## Historical Confirmation-Status Evidence

A deprecated requirement identifies CFETS as a trade population for which confirmation status should be sourced from [[stella]] rather than [[cdu-lake]].

The historical statement says that CFETS confirmation status includes `COMP`. It does not define `COMP` semantics, status transitions, implementation state, asset-class scope, or whether a CDU Lake fallback exists.

This CFETS-specific historical observation must not be generalized to the Korea COMP-driven STP model without independent evidence.

## Evidence Boundaries

The [[cash-settlement-2025-roadmap]] source does not explain the CFETS interface, message flow, operating model, ownership, or production-validation evidence.

The [[clearing-trade-payment-risk]] source does not define the full product population, interface behavior, or whether the clearing status is available to [[ratan|RATAN]] before payment release.

The deprecated confirmation requirement provides historical confirmation-source and `COMP`-status information only; it does not establish current implementation behavior or a general CFETS confirmation-processing model.