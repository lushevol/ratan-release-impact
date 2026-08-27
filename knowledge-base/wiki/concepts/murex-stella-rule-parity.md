---
type: concept
title: Murex-to-STELLA Rule Parity
created: 2026-08-22
updated: 2026-08-22
tags: [murex, stella, business-rules, nstp, suppression, migration]
related: [fmrp-prime-uk-uat-drop-2, murex, stella, ratan, straight-through-processing, cashflow-suppression, settlement-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---
# Murex-to-STELLA Rule Parity

Murex-to-STELLA rule parity is the requirement that rules originally applied to Murex cashflows produce the intended equivalent outcomes for STELLA cashflows processed through the FMRP and RATAN settlement flow.

The checklist covers:

- NSTP rules for SCB entities acting as counterparties or booking entities.
- Replication of Murex rules for STELLA cashflows.
- SWIFT suppression for expected cases such as auto-debit by agent or shared Nostros.
- RATAN suppression rules replacing Murex-to-RATAN interface filters that STELLA does not have.
- Automatic suppression of the `CLIENT_CLRG_LCH_STL` and `CLIENT_CLR_HKEX_ST` clearing portfolios.

Rule parity is a design and testing requirement, not evidence that all rules, identifiers, attributes, and outcomes have been compared or validated.