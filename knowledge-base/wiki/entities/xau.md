---
type: entity
title: XAU
created: 2026-08-22
updated: 2026-08-23
tags: [currency, reference-configuration, gold-settlement, XAU, gold, precious-metal, settlement, configuration-baseline]
related: [hau, hau-currency-onboarding, hong-kong-physical-gold-settlement, release-cutoff-configuration, non-iso-to-iso-currency-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# XAU

## Role in HAU and HKCS Configuration

`XAU` is the existing currency identifier used as a configuration reference during [[hau]] onboarding.

The newly generated version describes `XAU` as the existing gold booking code and comparative baseline for the HKCS `HAU` configuration. This characterization applies to the HKCS requirement source and does not establish broader equivalence between `HAU` and `XAU`.

## Referenced Configuration Baselines

The HKCS requirement source states or proposes that:

- HAU approval limits should use the same limits as XAU.
- Existing XAU release-cutoff data may be copied for HAU, pending extraction and confirmation.
- The HAU rounding question references existing XAU data; the recorded answer is three decimals with rounding off.

That source does not provide the actual XAU limit or cutoff values and does not prove that all XAU configuration should be copied to HAU.

The onboarding source states that HAU rounding should attach to existing XAU configuration. It raises, but does not answer, whether HAU should inherit XAU holiday-calendar and currency cut-off data.

## Scope and Limitations

No broader equivalence or conversion rule between HAU and XAU is established. In particular, the references to XAU limits, release-cutoff data, rounding, holiday calendars, or currency cut-offs should not be generalized into a conclusion that HAU inherits all XAU configuration.