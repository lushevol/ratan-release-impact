---
type: query
title: Are INR, INO, and INY the Authoritative Cashflow Currency Scope for India LEI Enrichment?
created: 2026-08-23
updated: 2026-08-23
tags: [LEI, India, currency, INR, INO, INY, SWIFT]
related: [india-payment-lei-swift-enrichment, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md"]
---
# Are INR, INO, and INY the Authoritative Cashflow Currency Scope for India LEI Enrichment?

The requirement describes the currency condition in two ways:

- The ISO currency in SWIFT is INR.
- The cashflow currency is in `(INR, INO, INY)`.

The source does not define whether `INO` and `INY` are internal variants that must map to INR for SWIFT, or whether they represent separate eligibility values.

Clarification should establish:

- The authoritative source field for the currency decision.
- Whether `INO` and `INY` are valid qualifying values.
- The mapping from each internal value to outgoing SWIFT currency.
- Whether the INR 500,000,000 threshold applies directly to all three values.
- Boundary behavior for exactly INR 500,000,000 and any conversion or normalization process.