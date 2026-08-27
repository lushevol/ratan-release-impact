---
type: concept
title: SGO Currency Handling
created: 2026-08-22
updated: 2026-08-22
tags: [sgo, currency-mapping, swift, accounting, nostro, vostro]
related: [swift-mt-mx-integration, cash-settlement-accounting-routing, nostro-configuration, ssi-stamping, f2b-hk-tw-milestone-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# SGO Currency Handling

SGO currency handling is the HK/TW configuration and processing behavior that maps `SGO` output to `SGD` for settlement messaging and accounting.

## Acceptance criteria

The checklist requires that:

- SGO generates SWIFT as `SGD`.
- SGO generates accounting as `SGD`.
- SGO produces no SWIFT or accounting failure.
- SGO Nostro is automatically attached.
- SGO Vostro is automatically attached.

The scenario should be tested independently from generic non-ISO-to-ISO and precious-currency mapping because the expected output currency and account attachments are explicit.

## Open implementation details

The source does not specify the mapping authority, validation rules, effective dates, message-field treatment, accounting transaction types, or exception handling for SGO.