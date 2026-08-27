---
type: query
title: What Is the Authoritative RFR Payment-Type Mapping?
created: 2026-08-22
updated: 2026-08-22
tags: [rfr, payment-type, uat, murex, business-rule]
related: [rfr-payment-type-classification, swap-agent, murex-2-11, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# What Is the Authoritative RFR Payment-Type Mapping?

The document contains an initial mapping and marks it as incomplete following UAT findings on 2025-01-07. The latest mapping broadens the coupon strategy condition from `SWAP_AGENT` to `SWAP_AGENT` or `RECALC`, while narrowing coupon typology to `Vanilla X-ccy swap`.

## Confirmation needed

- Confirm that the 2025-01-07 mapping is effective for all environments and interfaces.
- Confirm expected handling of `RECALC` cashflows with blank typology, `FWD_START_SWAP`, or another typology.
- Confirm whether source attribute values and comparison behavior are case-sensitive.