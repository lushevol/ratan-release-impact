---
type: source
title: Structure Products
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/FMRP/Key+Trade+Identifiers+and+Versions+-+Description+and+Scenarios"
venue: Confluence
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, structured-products, deprecated, Blade, Stella, CDU, SCBML]
related: [blade, stella, cdu, structured-product-package-trade-model, package-identifier-lineage, trade-event-id-lineage, trade-cashflow-reference-linkage, confirmation-status-normalization, confirmation-source-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md"]
---
# Structure Products

## Status and scope

This document is a deprecated functional requirement concerning structured-product package trades and identifier handling across [[entities/blade]], [[entities/stella]], and [[entities/cdu]]. It should be treated as historical or provisional evidence rather than as the current authoritative interface contract.

The source references **Key Trade Identifiers and Versions - Description and Scenarios** in the FMRP Confluence space.

## Requirements described

- Blade books the package trades as one contract.
- Blade generates an individual trade `SCBML` for each trade in the package.
- Blade populates the structure-booking link ID, `RFQID`, in each individual trade `SCBML`.
- Stella populates its own package ID and enriches each trade `SCBML` with that identifier.
- CDU has a plan to consolidate all individual trade `SCBML` documents with the same package ID into one confirmation document for the full package. This behavior is marked `TBC`.
- CDU will discuss with Stella how to update confirmation status back to Stella. This feedback approach is also marked `TBC`.

The design therefore distinguishes package-level booking from trade-level messages. It also introduces separate Blade and Stella package identifiers without defining which identifier is authoritative.

## Example data

The following table is preserved verbatim from the source. Its rows do not consistently align with the header, so it must not be treated as a complete schema or authoritative field mapping without validating the original Confluence formatting.

```markdown
| Blade Source Package ID(RFQID) | Stella package ID | Trade ID | Trade SCBML | CDU Confirmation | Tracking Version | Trade Type | Cashflow ID | Cashflow SCBML | Payment Type | Currency | Amount | Pay/Receive |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6c9a1f12-5899-490d-901b-036edbdfd75e | 65e2fda7-ef2d-48e2-93a7-0ad3073e67ce | 3375505333 | | TBC | 0 | NDF | 003375505334 | | Broker Fee | USD | 1000 | Pay |
| 3375505335 | | TBC | 0 | FX Swap | 003375505336 | | Broker Fee | USD | 1000 | Pay |
| TBC | 0 | FX Swap | 003375505337 | | Cashflow-NearLeg | JPY | 100190000 | Pay |
| TBC | 0 | FX Swap | 003375505339 | | Cashflow-NearLeg | GBP | 759357.96 | Receive |
| TBC | 0 | FX Swap | 003375505338 | | Cashflow-FarLeg | GBP | 759418.91 | Pay |
| TBC | 0 | FX Swap | 003375505340 | | Cashflow-FarLeg | JPY | 100190000 | Receive |
```

## Evidence assessment

The following points are directly stated:

- Blade books the package as one contract.
- Blade generates trade-level `SCBML` documents.
- `RFQID` is propagated into each individual trade message.
- Stella adds its own package ID to each trade message.

The following points are provisional:

- CDU consolidation of component trade confirmations into one package-level confirmation.
- The mechanism for CDU to return confirmation status to Stella.

The example contains an `NDF`, `FX Swap` near-leg and far-leg cashflows, broker-fee cashflows, multiple currencies, and both Pay and Receive directions. Package membership therefore does not imply a single trade type, cashflow type, currency, or payment direction.

## Open issues

- The authority and lifecycle of Blade's `RFQID` versus Stella's package ID are undefined.
- The source does not specify whether CDU retains component-level confirmations when producing a package confirmation.
- Confirmation-status ownership and the CDU-to-Stella feedback contract are unresolved.
- `Tracking Version` is shown as `0`, but its scope and increment rules are not defined.
- The malformed table prevents reliable interpretation of several package IDs, trade IDs, and message references.
- A newer, non-deprecated requirement may supersede this document.

See [[concepts/structured-product-package-trade-model]] and [[concepts/package-identifier-lineage]] for the derived model and unresolved correlation questions.