---
type: query
title: What Are the Authoritative SCBML Paths for SSI Stamping Query Fields?
created: 2026-08-23
updated: 2026-08-23
tags: [query, scbml, xpath, xpath-2, ssi-stamping, data-mapping]
related: [scbml, ssi-stamping-service, ssi-stamping-product-mapping, scbml-trade-enrichment-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# What Are the Authoritative SCBML Paths for SSI Stamping Query Fields?

The SSI Stamping design identifies legal-entity FMID and counterparty FMID paths, but the XPath expressions contain apparent syntax and namespace inconsistencies. CFI Code, Settlement Method, Settlement Type, and payment-currency extraction paths are not finalized.

## Fields requiring confirmation

- Legal Entity FMID.
- Counterpart FMID.
- Payment Currency.
- CFI Code.
- Settlement Method.
- Settlement Type.
- Debit/Credit derivation.
- SSI status selection.

The implementation should use validated XPath 2.0 expressions with explicit namespace bindings rather than copying the source expressions verbatim.

## Evidence to resolve

The source provides sample SCBML messages containing party FMIDs, product identifiers, exchanged currencies, and settlement instructions. The source does not state which field takes precedence when multiple product classification fields disagree.

Resolution should include executable XPath expressions, namespace declarations, representative XML fixtures, expected values, and ownership of future schema changes.