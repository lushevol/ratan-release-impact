---
type: query
title: What Is the Canonical Bulk Exception API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, bulk-processing, api-contract, exceptions]
related: [bulk-exception-processing, orchestration, exception-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# What Is the Canonical Bulk Exception API Contract?

The source references maker and checker Camunda task endpoints under `NSTPSSI`, but does not include request or response schemas. The Reject URL is malformed in the source.

Resolve the canonical endpoint ownership and contracts for Submit, Approve, Reject, and checker verification, including:

- Request identifiers and maximum item counts.
- Per-cashflow or per-exception result correlation.
- Response status and error schema.
- Idempotency, retry, and timeout behavior.
- Authorization scope and partial-success semantics.
- Whether `/v2/camunda/task/NSTPSSI/checker` is the authoritative checker endpoint.

Related source: [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--11yr784]].