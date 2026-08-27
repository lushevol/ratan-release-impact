---
type: query
title: How Are RATAN Payment-Level Validation Errors Retried and Reconciled?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, payment-validation, exception-handling, retry, reconciliation]
related: [ratan-batch-ack-nack-gating, fmrp-payment-insertion-eligibility, murex-ratan-cashflow-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# How Are RATAN Payment-Level Validation Errors Retried and Reconciled?

The source distinguishes non-blocking payment-level errors from stream-blocking file-level NACKs, but leaves payment-level behavior as TBC.

Required decisions include the rejected payment status, exception visibility, operational owner, correction route, retry mechanism, duplicate protection, ACK/NACK reporting, and reconciliation treatment.