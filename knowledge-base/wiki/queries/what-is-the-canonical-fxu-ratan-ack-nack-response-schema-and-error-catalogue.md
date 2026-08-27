---
type: query
title: What Is the Canonical FXU-RATAN ACK NACK Response Schema and Error Catalogue?
created: 2026-08-23
updated: 2026-08-23
tags: [fxu, ratan, utilization, ack, nack, api-contract, idempotency]
related: [fxu, ratan, fxu-ratan-utilization-response-contract, utilization-request-idempotency, what-is-the-fxu-ratan-utilization-api-and-idempotency-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Util Response ACK NACK.md"]
---
# What Is the Canonical FXU-RATAN ACK NACK Response Schema and Error Catalogue?

The source specifies a minimal response envelope—`Utilization.Utilization_Id`, `Utilization.Response`, and `Utilization.Error_Reason`—and a broad free-text NACK catalogue. It does not establish a fully typed response model.

## Open Contract Questions

- Is `Error_Reason` required for every `NACK`, absent for `ACK`, or optional in both cases?
- Is `Utilization_Id` solely an idempotency key, a business identifier, or both?
- Does a duplicate request receive “Duplicate utilizeId found” or replay the original response?
- What payload equality and retention rules apply to duplicate detection?
- Are error reasons stable codes, display strings, or both?
- Which field paths are canonical where the source uses variants such as `Trade.Util_Id`, `FXU.Utilization_Id`, and `Original_Util_Id`?