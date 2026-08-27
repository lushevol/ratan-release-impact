---
type: entity
title: BCDF
created: 2026-08-23
updated: 2026-08-23
tags: [bcdf, file-format, accounting, integration]
related: [ebbs, aspire, cashflow-accounting-stamping, entity-based-eod-feeding, cashflow-accounting-eligibility, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# BCDF

## Role

BCDF is the proposed file format for accounting feeds in the Cash Settlement Home Page accounting scope.

The source associates BCDF with:

- Aspire accounting-entry generation.
- EBBS accounting-entry generation.
- Entity-based end-of-day integration.
- End-of-day feeding integration.

## Contract Status

The document establishes BCDF as an integration constraint but does not provide a complete interface contract. The following details remain unknown:

- Schema and version.
- Required fields.
- Record types.
- File naming convention.
- Delivery mechanism.
- Encryption and security controls.
- Acknowledgement and retry behavior.
- Error handling.
- Reconciliation and replay process.

BCDF should therefore not be treated as a validated enterprise-standard format based on this source alone.
