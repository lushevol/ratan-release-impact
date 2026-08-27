---
type: concept
title: FXU-RATAN Utilization Response Contract
created: 2026-08-23
updated: 2026-08-23
tags: [fxu, ratan, utilization, ack, nack, api-contract]
related: [fxu, ratan, fxu-utilization-type-taxonomy, fxu-ratan-utilization-exception-routing, utilization-request-idempotency, what-is-the-fxu-ratan-utilization-api-and-idempotency-contract, what-is-the-canonical-fxu-ratan-ack-nack-response-schema-and-error-catalogue]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Util Response ACK NACK.md"]
---
# FXU-RATAN Utilization Response Contract

[[ratan]] responds to an [[fxu]] utilization request with a mandatory `Utilization.Utilization_Id` and `Utilization.Response`, where the response is `ACK` or `NACK`. The source provides `Utilization.Error_Reason` as the rejection explanation but does not formally specify its type, mandatory status for `NACK`, or allowed behavior for `ACK`.

## Validation Coverage

The documented NACK catalogue covers:

- missing request, utilization, trade, identifier, maker/checker, payment-reference, currency, amount, and leg data;
- utilization scope, trade cancellation, trade-major-version mismatch, cashflow errors, accounting information, and product cashflow-count checks;
- action eligibility, remaining and reversal amount comparisons, payment-currency matching, settlement-account eligibility, and value-date timing;
- duplicate `Utilization_Id` detection; and
- RATAN internal service failures.

A trade-major-version mismatch is documented as “Trade is amended” for `UTIL` and `REVERSE` requests. The source lists economic fields associated with amendment—booking entity FMID, counterparty FMID, currency, amount, payment date, and pay/receive direction—but does not state whether RATAN directly compares those fields.

## Limitations

This is not a complete implementation-level API specification. Field-path variants, the numeric example for a `String` utilization ID, error-code semantics, validation ordering, correlation, and retry/idempotency behavior are unresolved. See [[what-is-the-canonical-fxu-ratan-ack-nack-response-schema-and-error-catalogue]].