---
type: concept
title: Six-Attribute Cashflow Equivalence
created: 2026-08-24
updated: 2026-08-24
tags: [cashflows, matching, amendments, ratan, equivalence]
related: [non-economic-cashflow-amendment-handling, cashflow-lineage-and-operational-visibility, what-is-the-authoritative-matching-algorithm-for-non-economic-cashflow-amendments]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# Six-Attribute Cashflow Equivalence

[[ratan]] classifies a withdrawn cashflow and a newly generated cashflow as a non-economic replacement pair only if all six attributes are equal:

1. Booking Entity (FMID)
2. Counterparty (FMID)
3. Payment Currency
4. Payment Amount
5. Payment Value Date
6. Receive/Pay Direction

The test is applied per cashflow pair rather than per trade amendment. A mismatch in any attribute means the replacement is a new economic cashflow and must enter standard processing.

The functional requirement does not define deterministic pairing where multiple cashflows share the same six values, nor treatment of unequal withdrawal and replacement cardinalities. These gaps are tracked in [[what-is-the-authoritative-matching-algorithm-for-non-economic-cashflow-amendments]].