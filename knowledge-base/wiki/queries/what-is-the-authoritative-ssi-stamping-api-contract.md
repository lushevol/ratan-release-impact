---
type: query
title: What Is the Authoritative SSI Stamping API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, API, SCBML, cashflow, open-question]
related: [ssi-stamping-and-best-match, cdups, scbml, cashflow, ssi-stamping-reference-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# What Is the Authoritative SSI Stamping API Contract?

The source describes separate trade and cashflow SSI-stamping APIs with shared matching logic, but does not provide their endpoint paths, request schemas, response schemas, error contracts, retry semantics, or versioning rules.

## Evidence

- CDUPS invokes trade stamping with SCBML and receives enriched SCBML.
- Camunda triggers cashflow stamping.
- Cashflow failures generate SSI exceptions.
- Trade and cashflow responses differ, and SCBML XPath locations vary by trade type.

## Questions to resolve

- What are the canonical endpoints and schemas?
- Which fields are mandatory for each trade type?
- How are missing and multiple matches represented?
- Is trade-stamping failure returned as an error, an unenriched SCBML response, or another result?
- Which component owns retries and idempotency?