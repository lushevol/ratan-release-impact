---
type: concept
title: KRO to KRW Currency Mapping
created: 2026-08-22
updated: 2026-08-22
tags: [currency-mapping, kro, krw, korea, payment, accounting]
related: [korea, currency-code-transformation, ssi-stamping, korea-settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# KRO to KRW Currency Mapping

## Requirement

The Korea checklist explicitly requires transformation of `KRO` to `KRW` for both payment and settlement accounting.

## Processing boundaries

The requirement should be validated independently at:

1. SSI lookup and stamping.
2. Payment-message generation.
3. Settlement-accounting generation.
4. Downstream integrations and reports.

The source does not establish whether `KRO` is an inbound Murex code, an internal code, or a legacy code. It also does not state whether the mapping must appear in SSI, SCI, cashflow, or reporting data.

## Control risk

Applying the mapping at only one boundary could produce inconsistent SSI selection, payment messages, accounting entries, or reports. The authoritative source field and transformation point require confirmation.