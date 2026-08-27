---
type: concept
title: SSI Stamping Retry Contract
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, cdups, ratan, retry, timeout, error-handling]
related: [trade-ssi-stamping, ssi-exception-state-model, cdups, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# SSI Stamping Retry Contract

The SSI stamping retry contract defines CDUPS recovery behavior for transient RATAN failures.

## Retryable conditions

CDUPS retries when:

- RATAN returns HTTP `500`.
- RATAN times out.
- RATAN provides no response.

The retry uses the same trade ID and major version, at least three times, with three-minute intervals.

## Non-retryable condition

HTTP `400`, including `VALIDITION_FAILED` or trade-not-found cases, is a validation failure rather than a retryable infrastructure failure.

## Unresolved contract details

The source does not specify:

- Whether the original `trackingId` must be preserved.
- A formal idempotency key.
- The final state after the third retry.
- The maximum elapsed retry duration.
- Whether `DEFAULT_NOSTRO` is a usable success state or requires review.
- A precise RATAN timeout value.