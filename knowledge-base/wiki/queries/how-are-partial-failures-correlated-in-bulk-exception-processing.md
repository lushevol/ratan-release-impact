---
type: query
title: How Are Partial Failures Correlated in Bulk Exception Processing?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, bulk-processing, partial-failure, idempotency, error-handling]
related: [bulk-exception-processing, backend-batch-partitioning, exception-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# How Are Partial Failures Correlated in Bulk Exception Processing?

Partitioning a logical bulk request into multiple backend batches introduces the possibility that some batches complete while others fail. The source does not define how a caller receives and reconciles individual outcomes.

Establish the contract for:

- Correlating results and errors to input cashflows or exceptions.
- Representing completed, failed, skipped, and in-progress items.
- Retrying only failed items without duplicating successful workflow actions.
- Transaction and compensation boundaries.
- Audit records and operator recovery.
- Reconciliation after timeouts or client disconnects.

Related source: [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--11yr784]].