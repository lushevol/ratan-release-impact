---
type: concept
title: Netting Key Selection
created: 2026-08-22
updated: 2026-08-22
tags: [netting, identifiers, booking-model, ltid, nid]
related: [auto-netting, cross-product-netting, netting-over-netting, fmrp, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Netting Key Selection

Netting key selection determines which identifier groups cashflows for netting under a particular product or booking model.

## Booking-Model Associations

The FXO checklist records three explicit associations:

- RFR Booking Model: netting based on LTID.
- ND CCS and ND IRS: netting based on NID.
- Structures: netting based on Structure ID.

The [[cashflow-blotter]] must also accommodate LTID, NID, and Structure ID among the fields introduced by the Murex Flow.

## Scope Boundary

These mappings apply to the named booking models. They should not be interpreted as universal rules for all products or all netting performed in [[fmrp]] or [[ratan]].

## Missing Specifications

The source does not define:

- Identifier provenance and ownership.
- Field mapping from [[murex]] to FMRP.
- Null and duplicate handling.
- Fallback behavior.
- Collision detection.
- Identifier changes after amendment or migration.
- The relationship between these identifiers and other netting criteria.

These details are necessary before the associations can serve as executable netting rules.