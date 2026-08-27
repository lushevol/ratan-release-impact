---
type: concept
title: Package Identifier Lineage
created: 2026-08-23
updated: 2026-08-23
tags: [identifier-lineage, package-correlation, RFQID, trade-identifiers, cashflow-identifiers]
related: [blade, stella, cdu, structured-product-package-trade-model, trade-event-id-lineage, trade-cashflow-reference-linkage, confirmation-source-routing, confirmation-status-normalization, cashflow-event-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md"]
---
# Package Identifier Lineage

## Definition

Package identifier lineage is the propagation and correlation of a package identity across booking systems, trade messages, confirmations, and cashflow records.

The deprecated [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--18-st--tn9c1x|Structure Products]] requirement describes at least two package-level identifiers:

- Blade's source package ID, identified as `RFQID`.
- Stella's system-generated package ID.

It also references individual `Trade ID`, `Cashflow ID`, trade and cashflow `SCBML` documents, and `Tracking Version`.

## Proposed lineage

```text
Blade RFQID
    ↓
Individual trade SCBML
    ↓
Stella package ID enrichment
    ↓
Trade ID and related cashflow IDs
    ↓
Potential CDU package confirmation
```

This is a conceptual lineage, not a confirmed interface contract. The source does not state whether `RFQID` or Stella's package ID is the authoritative cross-system correlation key, whether the identifiers are immutable, or how they behave during amendments, rebooking, or cancellation.

## Identifier responsibilities

| Identifier | Apparent scope | Evidence status |
| --- | --- | --- |
| `RFQID` | Blade structure-booking or source package | Directly stated in the source |
| Stella package ID | Stella package correlation | Directly stated in the source |
| Trade ID | Individual trade | Present in the source example; lifecycle rules are undefined |
| Cashflow ID | Individual cashflow | Present in the source example; linkage rules are undefined |
| `Tracking Version` | Unspecified trade, package, confirmation, or cashflow version | Present as `0`; semantics are undefined |

## Control requirements

A current implementation would need to define:

1. The authoritative package correlation key.
2. The mapping and uniqueness rules between `RFQID` and Stella package ID.
3. Whether package identifiers remain stable across trade amendments and rebookings.
4. The relationship between package, trade, and cashflow identifiers.
5. The scope and increment rules for `Tracking Version`.
6. The identifier and status fields used by CDU if package-level confirmation consolidation is implemented.

These controls connect to [[concepts/trade-event-id-lineage]], [[concepts/trade-cashflow-reference-linkage]], and [[concepts/confirmation-source-routing]].