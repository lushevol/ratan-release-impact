---
type: query
title: Does CDU Consolidate Structured-Product Trade Confirmations?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, CDU, confirmations, structured-products, SCBML]
related: [cdu, structured-product-package-trade-model, package-identifier-lineage, confirmation-status-normalization, confirmation-source-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md"]
---
# Does CDU Consolidate Structured-Product Trade Confirmations?

## Question

Was the proposed CDU behavior implemented, whereby individual trade `SCBML` documents with the same package ID are consolidated into one confirmation document for the full structured-product package?

## Historical evidence

The deprecated source describes package-level confirmation consolidation as a CDU plan and marks it `TBC`. It does not establish whether the plan was implemented, rejected, or superseded.

The same source leaves unresolved how CDU would return confirmation status to Stella.

## Required resolution

A current source should establish:

- Whether consolidation occurs.
- The package grouping key.
- Whether individual confirmations remain available.
- How component-level status contributes to package-level status.
- The authoritative status owner.
- The CDU-to-Stella message or API contract.
- Retry, duplicate, and exception handling.

Until this question is resolved, the proposed behavior must be treated as historical design intent rather than current functionality.