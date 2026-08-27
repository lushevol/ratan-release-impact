---
type: query
title: What Is the Authoritative BCS SWIFT Field 20 Format?
created: 2026-08-22
updated: 2026-08-22
tags: [bcs, swift, field-20, cashflow-id, stella]
related: [bcs, stella, tag-20-logic, swift-mt-mx-integration, ratan-cashflow-id-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md"]
---
# What Is the Authoritative BCS SWIFT Field 20 Format?

The requirement states that SWIFT Field 20 has a maximum length of 16 and gives the BCS example:

```text
EQ02003791883175
```

It describes the value as `EQ` for Equity, `02` for the booking-entity branch code, and `00379188317` for an FMRP Stella-generated cashflow ID.

## Ambiguity

The example and its described components total 15 characters. The document also says the FMRP Stella cashflow ID has a maximum length of 12, although the illustrated component is 11 digits.

## Questions to resolve

- Is the BCS example intended to be 15 or 16 characters?
- Is the embedded Stella cashflow ID 11 or 12 characters in production?
- Is any padding, truncation, or transformation applied before Field 20 construction?
- Does this composition apply only to BCS, or are there explicitly approved variants for other booking entities?

The current evidence supports this only as a BCS-specific example, not as a universal Field 20 rule.