---
type: concept
title: Release-Time Cashflow Status Gating
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-status, release-control, duplicate-payment, RATAN]
related: [ratan, cashflow-release-and-netting-race-condition, cash-settlement-release-cutoff-controls, what-idempotency-controls-protect-ratan-ready-state-retries]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/OPS Allowed Actions Post Pending Release.md"]
---
# Release-Time Cashflow Status Gating

Release-time cashflow status gating is the intended RATAN control invariant that only cashflows in `READY` status can be sent downstream. When a cashflow transitions to another status, the release process must stop.

The source applies this stated control to actions that move `READY` cashflows to `WAITING`, `DEAD`, `HOLD`, `UTILIZED`, `PARTIALLY_UTILIZED`, `NETTED`, or `SPLIT`.

## Limitation

The documented rule does not specify whether status validation is atomic with outgoing-message creation and dispatch. It also does not distinguish safe retries from duplicates for actions that retain `READY`, including `Early Release`, `Resend To Razor`, and `Regenerate Swift`.

The unanswered implementation question is tracked in [[is-ratan-release-status-validation-atomic-with-downstream-dispatch]]. Retry safeguards are tracked in [[what-idempotency-controls-protect-ratan-ready-state-retries]].