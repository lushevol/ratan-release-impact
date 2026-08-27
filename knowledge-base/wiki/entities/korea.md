---
type: entity
title: Korea
created: 2026-08-22
updated: 2026-08-22
tags: [korea, onboarding, cashflow-migration, cash-settlement]
related: [cashflow-migration, korea-ssi-onboarding, kro-to-krw-currency-mapping, korea-swift-mx-message-generation, korea-settlement-accounting, korean-character-reporting, krx, tds3]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# Korea

## Role

Korea is the onboarding jurisdiction and entity scope for the checklist documented in sources/26-auto-netting-page-md-files--216-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-04--lpgtrq.

The source treats Korea primarily as a **cashflow-migration and cash-settlement onboarding** scope, not as a broad Murex-to-FMRP trade-migration scope.

## Confirmed or indicated requirements

- Add Korea to the dashboard.
- Map `KRO` to `KRW` for payment and accounting.
- Enable or validate NDS, IRS, and CCS auto-netting behavior.
- Net ND CCS and ND IRS in [[entities/ratan]].
- Add [[entities/krx]] as a netting counterparty.
- Integrate with [[entities/tds3]] for trade-confirmation status.
- Generate MX messages for all listed flows except MT210.
- Support Korean characters in the SSDR report.

## Dependencies requiring confirmation

The source does not define Korea’s final settlement means, settlement accounts, SSI hierarchy position, agent structure, MT210 treatment, EBBS accounting configuration, or detailed NSTP and suppression rules.

The source also records an unresolved question about integration between Korea and [[entities/murex]] using Solace.