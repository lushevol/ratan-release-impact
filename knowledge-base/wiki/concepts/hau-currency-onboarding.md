---
type: concept
title: HAU Currency Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [hau, currency-onboarding, settlement-day-2, static-data, swift]
related: [hau, xau, hong-kong-physical-gold-settlement, settlement-day-2, nostro-static, swift-entity-configuration, ebbs-settlement-accounting, manual-cashflow-netting, auto-netting-rule-check, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md"]
---
# HAU Currency Onboarding

HAU currency onboarding is the coordinated enablement of [[hau]] across RATAN ONE settlement static data, user workflow, settlement accounts, message publication, and rule assessment for [[settlement-day-2]].

## Confirmed or recorded configuration

- HAU is not required in the `holiday-currency-list (onshore|offshore)` configuration, where it is described as offshore like [[xau]].
- HAU rounding should attach to the existing XAU configuration.
- UAT1 included an HAU nostro record, PM-currency data, and SWIFT UDF data for `GOLD`, `FOZ`, `9950`, and `HONGKONG`.
- Razor publication for LoanIQ requires no HAU customization, according to the recorded confirmation from Carrie.
- The stated requirement is that HAU does not publish accounting entries.

## Open configuration and integration decisions

The source does not decide whether HAU needs dedicated holiday or cut-off static data, whether it must appear in the frontend currency dropdown, whether [[lms]] converts HAU to XAU, or whether HAU-specific SWIFT customization is needed.

The use of XAU as a configuration reference is limited. Rounding inheritance is recorded as selected; holiday and cut-off inheritance are questions, not approved design decisions.

## UAT boundary

The UAT1 workflow demonstrates that manually configured HAU data supported cashflow `M00127675004` through maker input, checker approval, and SWIFT-message generation. It does not demonstrate production deployment, downstream SWIFT acceptance, LMS behavior, accounting suppression, or netting eligibility.

## Rule assessment

`FMO UK Non X Currency Netting` and `Commodity Auto Netting – PM Currencies` are named as possible impacted rules. The source provides no match evaluation, priority outcome, or test evidence, so HAU eligibility must not be inferred.