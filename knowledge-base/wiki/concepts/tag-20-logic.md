---
type: concept
title: Tag 20 Logic
created: 2026-08-22
updated: 2026-08-22
tags: [swift, messaging, identifier, integration]
related: [vietnam-ifc-branch, lms, fmrp, ratan, stella, blade, cfets]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md"]
---
# Tag 20 Logic

Tag 20 logic defines how SWIFT field 20 identifiers are constructed or used to query messages across booking and processing flows.

## Documented Patterns

The source records several existing patterns:

- SABRE EQ through STELLA uses the `EQ` prefix.
- LOANIQ uses the `LQ` prefix.
- BLADE, S2BX, and CFETS through [[fmrp]] use the `DV` prefix in the source-system agreement table.
- BCS Stella GUI queries use `EQ + Branch Code + Cashflow ID`.
- Egypt, Nepal, and Saudi GUI queries use `FX + Branch Code + Cashflow ID`.
- LOANIQ GUI queries use `LQ + Branch Code + Cashflow ID`.
- Existing FMRP GUI queries for SG, MY, IN, and CN use the cashflow ID against [[ratan]] without a documented Tag 20 composition.

These patterns belong to their stated flows and entities. They are not interchangeable templates.

## Vietnam Decision

[[lms]] and Settlement Team must agree on the source-system designation and Tag 20 behavior for the [[vietnam-ifc-branch]]. The decision should identify:

- Authoritative message source.
- Prefix, if any.
- Branch-code inclusion.
- Cashflow identifier.
- Query condition.
- Uniqueness and length constraints.
- Compatibility with LMS and RATAN queries.