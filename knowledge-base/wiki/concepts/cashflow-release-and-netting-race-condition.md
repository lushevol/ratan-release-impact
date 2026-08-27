---
type: concept
title: Cashflow Release and Netting Race Condition
created: 2026-08-24
updated: 2026-08-24
tags: [concurrency, cash-settlement, netting, duplicate-payment, RATAN]
related: [ratan, ratan-cashflow-lifecycle-service, release-time-cashflow-status-gating, cash-settlement-release-cutoff-controls, is-ratan-release-status-validation-atomic-with-downstream-dispatch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/OPS Allowed Actions Post Pending Release.md"]
---
# Cashflow Release and Netting Race Condition

A cashflow release and netting race condition occurs when automatic payment release and an Operations netting action can concurrently act on the same cashflow before either action prevents the other.

In the documented RATAN incident, a gross cashflow in `READY` was being automatically released while an Operations user performed ad-hoc netting within a reported 55-second interval. Both the gross amount and the resulting net amount were released.

## Control requirement

A safe design must ensure that eligibility validation, state transition, outgoing-instruction creation, and dispatch are serialized or otherwise protected by a concurrency mechanism. A status rule alone does not demonstrate this property unless the implementation prevents a stale `READY` read from authorizing a concurrent downstream dispatch.

This incident concerns RATAN’s intra-application actions and should not be generalized to data-centre failover or unrelated messaging races. See [[ratan]] and [[ratan-cashflow-lifecycle-service]].