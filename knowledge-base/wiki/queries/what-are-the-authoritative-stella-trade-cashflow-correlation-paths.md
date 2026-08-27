---
type: query
title: What Are the Authoritative Stella Trade-Cashflow Correlation Paths?
created: 2026-08-24
updated: 2026-08-24
tags: [stella, scbml, trade-correlation, cashflow, versioning]
related: [stella, tds3, ratan, trade-cashflow-correlation-by-trade-version]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# What Are the Authoritative Stella Trade-Cashflow Correlation Paths?

The source identifies `Trade_ID` and `Trade_Lake_Trade_Major_version` as shared Stella trade and cashflow correlation fields, but provides no SCBML paths.

Obtain the authoritative:

- Trade-side and cashflow-side SCBML paths.
- Logical and physical schema definitions.
- Uniqueness and matching-cardinality constraints.
- Rules for missing, mismatched, stale, duplicate, and out-of-order versions.
- Treatment for a single trade version associated with multiple cashflows.