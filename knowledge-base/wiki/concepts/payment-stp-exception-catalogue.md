---
type: concept
title: Payment STP Exception Catalogue
created: 2026-08-22
updated: 2026-08-22
tags: [payment-stp, exceptions, murex, settlement, nstp]
related: [murex, ratan-one, murex-to-ratan-exception-mapping, auto-netting-rule-check, what-is-the-ratan-payment-stp-exception-precedence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 Payment Non-STP Exception.md"]
---
# Payment STP Exception Catalogue

A Payment STP exception catalogue defines the eligibility checks that prevent automatic settlement and records why a cashflow was stopped.

For the documented Murex2.11 process, failed checks append one or more codes to the cashflow `REASON` column. A single exception is sufficient to stop STP, while multiple failures may be retained together.

## Rule groups

The source groups legacy Murex controls across several concerns:

- Netting and queue exclusions: `INTER NET`, `FIXING`, `NET`, and `CROSS-NET`.
- Static eligibility and counterparty controls: `AMOUNT`, `LIMIT TYPE`, `CP_EXCL`, `PROD`, `STRAT`, `CURR`, `ENTITY`, `STP_HOLD`, and `CORP`.
- Trade and clearing controls: `NDS`, `LIEN`, `PX_CAP`, `CLEARING STATUS`, `XIT`, and `STATUS`.
- Settlement-instruction controls: `SI`, `SI(AWI)`, and `SI(MUL)`.
- Lifecycle controls: `S&M`, `MOP`, and `REV`.
- Deferred or manual-flow controls: `COMMENT`, `XAU`, `XAG`, `XU5`, and `XS9`.

This catalogue describes Murex behavior. It must not be treated as a complete RATAN exception catalogue; the migration is selective and differs by entity, region, release scope, and lifecycle state.