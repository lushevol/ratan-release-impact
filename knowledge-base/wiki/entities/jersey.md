---
type: entity
title: Jersey
created: 2026-08-22
updated: 2026-08-22
tags: [legal-entity, tranche-3, onboarding, static-data, cash-settlement, swift]
related: [zhengzhou, taeyuan, lms, fmrp, ebbs, entity-onboarding-static-data-controls, is-jersey-tranche-3-go-live-a-static-data-onboarding-or-a-full-settlement-activation, ratan, tranche-3-entity-onboarding, payment-and-cashflow-suppression-governance, cashflow-suppression-vs-swift-suppression, what-is-the-authoritative-jersey-bridge-and-ebbs-nostro-account-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3 Onboarding.md"]
---
# Jersey

Jersey is a Tranche 3 entity. The static-data go-live checklist identifies Jersey as its primary entity, while the Tranche 3 onboarding source describes Jersey as being configured in [[ratan]].

## Entity and messaging attributes

The Tranche 3 onboarding source records the following attributes:

| Attribute | Value |
|---|---|
| FMID | `400910415` |
| Branch code | `05` |
| Sender BIC | `SCBLJESHXXX` |
| Field 53 BIC | `SCBLJESHXXX` |
| Field 58 BIC | `SCBLJESHXXX` |

The static-data go-live checklist requires entity-level SWIFT static data.

## Static-data and operational configuration

The static-data go-live checklist requires the following:

- Refer to the confirmed Jersey SSI workbook for SSI and nostro setup.
- Retain the existing currency list because users are not settling Jersey trades at this point.
- Configure the branch bridge-account arrangement described as equivalent to EBBS bridge suspense.
- Configure Jersey as a manual entity in the blotter under ADO work item `9905654`.
- Exclude Jersey from [[lms]] routing.

The Tranche 3 onboarding source separately states that Jersey must not flow to [[lms]], requires Cashflow Blotter country configuration, and requires a CPT Control update at go-live.

## Bridge and nostro accounts

The Tranche 3 onboarding source records:

| Account purpose | Account number |
|---|---|
| Branch suspense bridge account | `123613180028890791098` |
| EBBS nostro account | `123613180028881491098` |

Final confirmation of these account details remains open in [[what-is-the-authoritative-jersey-bridge-and-ebbs-nostro-account-configuration]].

## Suppression, NSTP, and netting

The static-data go-live checklist requires FMID `400910415` to be added to the existing `Non FMRP entities` cashflow-suppression rule. It specifically directs that `SAUDI` remain unchanged.

The Tranche 3 onboarding source records distinct UAT suppression configuration for Jersey:

- SWIFT suppression for listed deliverable currencies.
- Cashflow suppression for listed metal currencies.
- Membership in the `Non FMRP entities` cashflow-suppression rule.

That source also states that Jersey requires neither NSTP nor netting. This is checklist evidence rather than a formal architecture decision.

## Scope and readiness

The static-data go-live checklist establishes requirements and UAT rule references; it does not establish production readiness or full settlement activation. See [[is-jersey-tranche-3-go-live-a-static-data-onboarding-or-a-full-settlement-activation]].