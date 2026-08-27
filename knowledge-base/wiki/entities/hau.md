---
type: entity
title: HAU
created: 2026-08-22
updated: 2026-08-23
tags: [currency, gold-settlement, hkcs, settlement-day-2, HAU, gold, precious-metal, settlement]
related: [xau, hong-kong-physical-gold-settlement, hau-currency-onboarding, ratan, lms, settlement-day-2, hkcs, scb-hk, hau-gold-settlement-configuration, mt604-mt605-hau-message-customization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---

# HAU

## Role

`HAU` is the settlement-currency identifier and gold booking code required for SCB HK activity under the [[hong-kong-physical-gold-settlement]] initiative. It is used instead of [[xau]] for the stated HKCS flow.

## Configuration requirements

The HKCS initiative source states that:

- HAU approval limits should match existing XAU limits.
- HAU rounding should use three decimals with rounding off.
- A separate `HAU MAIN` Nostro should be configured.
- Vostros are expected to be configured as `HAU MAIN`.
- HAU cashflows must be sent to [[lms]].
- HAU holiday-calendar and release-cutoff configuration remains subject to confirmation.

The onboarding source records a Hong Kong HAU nostro record and UAT1 configuration for:

- HAU spot-rate lookup.
- PM currency recognition.
- SWIFT UDF data.

## Processing evidence

The onboarding source records a successful controlled path from HAU cashflow creation through checker approval to SWIFT-message generation.

This evidence documents the tested flow; it does not by itself confirm all production configuration or operational treatment.

## Relationship to XAU

The sources propose reuse of XAU configuration for selected functions:

- HAU approval limits should match existing XAU limits.
- HAU rounding should use three decimals with rounding off, reusing the recorded XAU rounding treatment.

Holiday-calendar and cut-off inheritance remain unresolved. The available evidence does not establish that HAU and XAU are semantically equivalent or interchangeable.

## ISO mapping and accounting scope

For the documented HKCS HAU flow, HAU-to-XAU ISO currency mapping is not required because:

- HAU accounting is not required in RATAN.
- The currency field is not used in precious-metal-related SWIFT.

This conclusion is limited to the documented HKCS HAU flow and must not be generalized to other systems or future accounting requirements.

## Unresolved operational treatment

The following remain unconfirmed:

- HAU’s canonical LMS representation.
- Confirmation that the documented LMS cashflow requirement is fully reflected in production configuration.
- Production SWIFT customization.
- Frontend visibility.
- Accounting-message treatment.
- Netting-rule eligibility.
- Final holiday-calendar and release-cutoff treatment.

See [[hau-currency-onboarding]] and the related open queries.