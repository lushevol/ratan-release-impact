---
type: concept
title: New-Currency Onboarding Static-Data Readiness
created: 2026-08-23
updated: 2026-08-23
tags: [currency-onboarding, static-data, ratan, settlement, bau]
related: [legal-entity-currency-cutoff-control, precious-metal-currency-classification, booking-currency-to-iso-code-mapping, currency-rounding-configuration-readiness, nostro-records, ratan, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
---
# New-Currency Onboarding Static-Data Readiness

New-currency onboarding static-data readiness is the BAU control that ensures RATAN can safely process a currency newly introduced by a TP system.

The required RATAN review areas are:

- a cutoff configuration keyed by legal entity and currency;
- mandatory Nostro static data;
- precious-metal classification for relevant SWIFT generation;
- booking-currency-to-ISO-code conversion for SWIFT and Accounting;
- availability in the applicable rounding configuration.

The source establishes the need for these checks but does not define owners, approval gates, field-level completeness criteria, evidence requirements, or production rollout controls. Those gaps are tracked in [[what-is-the-complete-new-currency-onboarding-acceptance-checklist]].

This is distinct from a historic static-data migration such as [[nostro-static-data-migration]]: it concerns ongoing BAU onboarding.