---
type: concept
title: SWIFT Entity Configuration
created: 2026-08-22
updated: 2026-08-22
tags: [swift, settlement, bic, configuration, entity-onboarding]
related: [manual-entity-settlement-onboarding, ratan, entity-routing-and-cashflow-suppression, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/00 Manual Entities Onboarding Checklist.md"]
---
# SWIFT Entity Configuration

SWIFT entity configuration is the set of entity-specific settlement-message settings required during manual-entity onboarding.

## Configuration inputs

The source labels the following as mandatory for each entity:

- Booking Entity FMID.
- Booking Entity SWIFT BIC used as sender BIC.
- Field 53 SWIFT BIC for LCY and Over Account.
- Field 58 SWIFT BIC for Flip MT202.
- Branch-code mapping.

It also calls for assessment of MT604/MT605 receiver BICs and any branch-specific SWIFT customization.

## Currency-specific processing

For new precious-metal entities or currencies, the source says that a PM list replicated from Murex 2.11 drives MT604, MT605, and MT692 template generation. It identifies `UDF_Strategy` and `UDF_SWF_LS` as additional copied UDF tables and states that a Change Request is required for a new PM entity to be released to production.

The exact applicability of individual BIC fields, receiver BIC configuration, PM templates, and accounting treatment remains unresolved. See [[which-manual-entity-configuration-fields-are-mandatory-by-message-and-currency]].