---
type: query
title: What Is the Complete Ratan Profile USD Limit Entitlement Matrix?
created: 2026-08-23
updated: 2026-08-23
tags: [query, ratan, authorization, profiles, entitlement-matrix, access-control]
related: [ratan, razor, fmo-ops, profile-based-usd-authorization-limits, profile-limit-static-data-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# What Is the Complete Ratan Profile USD Limit Entitlement Matrix?

## Question

What are the authoritative Ratan profile identifiers, RAZOR equivalents, monetary thresholds, settlement actions, and high-risk actions for every proposed profile?

## Evidence requiring resolution

The source narrative introduces profile 5, but the table omits it. The table also has incomplete rows and ambiguous column alignment. Profile 9 is especially unclear because both `FMO_OPS_BOL` and `GBL_BOL_ST` appear in the row.

Threshold boundaries are inconsistent because profiles 7–9 use `<` while profile 10 uses `<=`. The source also does not explain whether profile 10 inherits profile-9 high-risk actions.

## Desired resolution

Confirm:

- The complete profile-5 definition.
- Current versus new Ratan profile identifiers.
- Equivalent RAZOR mappings.
- Inclusive or exclusive threshold boundaries.
- Maker, submitter, checker, and approver rights.
- High-risk action entitlements by profile.
- Whether high-risk actions are independently limited by amount.
- Whether the matrix is approved for implementation.
