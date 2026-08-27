---
type: concept
title: Currency Transformation
created: 2026-08-22
updated: 2026-08-22
tags: [currency, non-ISO, SSI, Nostro, netting, settlement]
related: [f2b, fmrp, stella, ratan, nostro-configuration, nostro-static-management, ssi-stamping, auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md"]
---
# Currency Transformation

Currency transformation is the conversion of a received currency code into another code for settlement processing, account lookup, or related downstream logic.

## F2B onboarding use case

The checklist repeatedly uses SGO-to-SGD as the example:

- When SGO is received, SGD may be used for Vostro lookup.
- When SGO is received, SGD may be used for Nostro lookup.
- SSI and Nostro static data may need to be maintained for the non-ISO currency.
- Netting may fail when Murex produces SGD cashflows and Stella produces SGO cashflows.

## Control questions

Onboarding should establish:

1. Which system performs the transformation.
2. Whether the original and transformed codes are both retained.
3. Whether transformation occurs before SSI stamping, Nostro stamping, suppression, and netting.
4. How non-ISO and precious-metal currencies are represented downstream.
5. Which system owns the mapping and its change approval.

The source marks currency transformation as not supported yet in SSI and Nostro auto-stamping sections, so implementation status requires confirmation.
