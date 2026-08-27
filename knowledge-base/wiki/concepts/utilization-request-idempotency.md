---
type: concept
title: Utilization Request Idempotency
created: 2026-08-23
updated: 2026-08-23
tags: [idempotency, messaging, solace, api, fx-utilization]
related: [fxu, ratan, scpay, utilization-remaining-amount]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Utilization Request Idempotency

Utilization Request Idempotency is the required ability to ensure that retries and duplicate responses do not apply a utilization more than once.

The source requires FXU to retry after a timeout using the same utilization ID, process a late RATAN ACK/NACK, and handle multiple RATAN responses for one utilization ID. It suggests processing an ACK regardless of response sequence.

No definitive idempotency key, state machine, timeout policy, duplicate-request rule, correlation key, or ACK/NACK precedence is defined. The requirement is therefore an unresolved interface contract. See [[what-is-the-fxu-ratan-utilization-api-and-idempotency-contract]].