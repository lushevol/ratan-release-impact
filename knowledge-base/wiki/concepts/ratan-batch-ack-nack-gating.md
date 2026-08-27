---
type: concept
title: RATAN Batch ACK/NACK Gating
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, murex-211, batch-processing, acknowledgement, nack, operations]
related: [murex-ratan-batch-file-triplet, fmrp-cashflow-publication-lifecycle, murex-ratan-cashflow-reconciliation, ratan-batch-acknowledgement-confirm, ratan-payment-level-validation-errors-retried-and-reconciled]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# RATAN Batch ACK/NACK Gating

Murex must wait for RATAN's ACK or NACK before publishing the next UK CSV batch because Murex cannot automatically regenerate a batch.

RATAN returns one of the following response files to a separate folder:

```text
FMRP_Murex_Payments_YYYYMMDD_XXX_Ack.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Nack.csv
```

If Murex receives no response within 30 minutes, processing is held and [[murex-pss]] investigates. RATAN PSS escalates NACKs to Murex PSS. A file-level NACK blocks the subsequent batch stream; payment-level validation errors are intended to be non-blocking.

The source does not state whether ACK confirms receipt, validation, persistence, or complete processing. It also leaves replay idempotency, duplicate responses, and correlation semantics undefined.