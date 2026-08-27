---
type: query
title: What Is the Canonical Uniqueness Key for Vostro SSI Records?
created: 2026-08-24
updated: 2026-08-24
tags: [vostro-ssi, uniqueness, static-data, ssi-plus, murex]
related: [vostro-ssi-redundancy-and-product-scoping, ssi-plus, murex-2-11, ratan-10123, vostro-data-sourcing-from-ssi-plus]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI.md"]
---
# What Is the Canonical Uniqueness Key for Vostro SSI Records?

Must `Security` or Murex product classification be part of the canonical Vostro SSI uniqueness and selection key? Which variations in `SwiftType` and `AccountRef` are valid product-specific configurations?

## Why this is open

RATAN-10123 labels several SSI+ China records as duplicate or totally the same, but every displayed pair or group includes a different `Security` value. Several groups also differ in `SwiftType` or `AccountRef`.

The source contains no database constraint, lookup implementation, precedence rule, or business policy defining which fields are material.

## Evidence needed

- The SSI+ Vostro SSI schema, constraints, and lookup implementation.
- Murex-to-SSI+ product/security selection rules.
- The treatment and resolved value of `SwiftType: Default`.
- Business approval for retaining, consolidating, or prioritising records that differ by product classification.
- Representative selection tests for `MXG IRD`, `MXG IRD IRS`, `MXG IRD CS`, and `MXG SCF`.

## Decision impact

The answer governs whether apparent matching records can be safely consolidated and whether an SSI selection can use a product-specific record without ambiguity.