---
type: query
title: What Is the Authoritative Nigeria NGB-NGN Rounding and Mapping Sequence?
created: 2026-08-23
updated: 2026-08-23
tags: [nigeria, currency, rounding, ratan, open-question]
related: [non-iso-to-iso-currency-mapping, ratan, manual-entity-go-live-static-data-controls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md"]
---
# What Is the Authoritative Nigeria NGB-NGN Rounding and Mapping Sequence?

The checklist requires `NGB → NGN` mapping, records an earlier instruction to set NGN precision to `0`, and retains `NGB | 2 | ROUNDING_OFF` after later notes stating that NGN precision should be `2`.

Confirm:

1. Whether rounding occurs before or after `NGB → NGN` normalization.
2. The production-authoritative currency code and precision.
3. The deployed Ratan mapping and rounding records.
4. Evidence of settlement validation using the production sequence.