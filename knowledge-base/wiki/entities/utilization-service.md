---
type: entity
title: Utilization Service
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, utilization, service, settlement-method, dlq]
related: [fxu, fxu-utilization-response-contract, utilization-dlq-retry-and-failure-semantics, gross-util-settlement-method-transition, past-due-accounting-reversal, cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# Utilization Service

Utilization Service is the proposed FXU entry point for utilization response processing and manual settlement-method changes between `GROSS` and `UTIL`.

## Proposed responsibilities

- Return enriched utilization responses containing processing outcome and request context.
- Return automatic-utilization amounts and remaining amounts for two exchanged currencies.
- Distinguish malformed JSON from Ratan internal processing failures.
- Retry Ratan internal-error messages through a DLQ at most five times.
- Expose `POST /v1/utilization/cashflow/settlementMethod/stamping`.
- Validate `SettlementMethod=UTIL`.
- Apply `UTIL ↔ GROSS` settlement-method changes at trade level.
- Handle immediate past-due accounting reversals when moving from `UTIL` to `GROSS`.

The proposed batch endpoint returns results per trade, including partial failures. The draft does not assign transactional boundaries, idempotency ownership, retry scheduling, or final DLQ disposition.

The source says Group Service must forbid `UTIL` restamping, making Utilization Service the intended owner of this specific manual change flow.