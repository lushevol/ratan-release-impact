---
type: query
title: What Is the Canonical Non-Economic Amendment Matching and Pairing Rule?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, non-economic-amendment, matching, data-quality]
related: [non-economic-cashflow-amendment, cashflow-replacement-mapping, group-management-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# What Is the Canonical Non-Economic Amendment Matching and Pairing Rule?

The source requires matching Booking Entity ID, Counterparty FM ID, Payment Currency, Payment Amount, Value Date, and Direction, plus opposite `Withdrawal` and `New` events.

It does not define amount precision or rounding, null handling, matching where multiple candidate events qualify, event-order behaviour, late delivery handling, or whether source system forms part of the matching key. An authoritative rule is needed before the classification can be safely implemented or reconciled.