---
type: concept
title: Korea SSI Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [ssi, settlement-instructions, onboarding, korea, nostro, vostro]
related: [korea, ssi-stamping, ssi-selection-hierarchy, kro-to-krw-currency-mapping, cdups]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# Korea SSI Onboarding

## Existing SSI behavior

The checklist describes:

- An old SSI hierarchy covering `CN/SG/IN/MY/EG/SA/NP/AG/LOANIQ`.
- A new hierarchy for `UK & new onboarding`.
- CFI selection using only the first two characters, with special logic for IRS and CCS.
- `FEDWIRE` and `CASH` settlement methods.
- Support for single-agent and two-agent structures.
- No support for three-agent structures.
- Trade SSI stamping to [[entities/cdups]] through XML and product-based logic.

## Korea-specific behavior

Korea requires validation of a new onboarding path and the `KRO` to `KRW` transformation described in [[concepts/kro-to-krw-currency-mapping]]. Nostro stamping should follow the default behavior.

The source does not specify Korea’s hierarchy position, settlement method, agent structure, or final settlement means and accounts. These must not be inferred from the UK onboarding path.