---
type: concept
title: Product-Agnostic SSI Stamping
created: 2026-08-24
updated: 2026-08-24
tags: [SSI-stamping, normalization, UBER, RATAN-Logic-Model, product-agnostic]
related: [trade-level-ssi-stamping, ratan-uber-integration-technical-design, ssi-stamping-reference-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# Product-Agnostic SSI Stamping

Product-agnostic SSI stamping is the proposed normalization of product-specific UBER and RATAN Logic Model fields into a common input for SSI stamping.

## Normalization objective

The RATAN Logic Model extends UBER while remaining compatible with it. Because different products expose currencies and settlement attributes in different structures, RATAN must extract and standardize those values before invoking common SSI logic.

The source identifies these relevant attributes:

- Product type
- Trade ID
- Trade major version
- Counterparty FMID
- CFI code
- Settlement method
- Settlement type
- Currency
- Debit/credit

## Mapping requirements

A complete mapping must define:

- UBER product taxonomy to RATAN product types such as IRS and BullionSwap.
- Trade and tracking identifiers.
- Booking and counterparty FMIDs.
- All currency-bearing product paths.
- Pay/receive or debit/credit semantics for every supported product.
- Settlement method and settlement type.
- Validation behavior for missing, repeated, or contradictory fields.

The source provides examples for `Instrument_Common.ISDA_Taxonomy`, `Entity.Booking_Entity_SCIFMID`, and an interest-rate swap currency path, but does not provide a complete product mapping appendix.