---
type: concept
title: Bulk Exception Processing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exceptions, bulk-processing, workflow, checker]
related: [backend-batch-partitioning, orchestration, exception-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# Bulk Exception Processing

Bulk exception processing performs workflow actions for multiple cashflows or exceptions in one logical request. The source references Submit through an `NSTPSSI` maker endpoint and checker verification through an `NSTPSSI` checker endpoint. It discusses Submit, Approve, and Reject, but does not provide complete payloads, response schemas, or a definitive mapping between action names and endpoints.

The source's performance evidence is limited to the `checker` API. A logical bulk request of 1,000 cashflows should be distinguished from one monolithic backend execution batch: the selected approach partitions that logical request into 20 batches of 50.

The following operational semantics are unspecified:

- Maximum supported logical bulk size and backend batch size.
- Per-cashflow result and error correlation.
- Partial-success and transaction behavior.
- Idempotency and duplicate-request handling.
- Retry, timeout, and authorization behavior.
- Whether the malformed Reject endpoint represents the intended checker endpoint.

See [[backend-batch-partitioning]].