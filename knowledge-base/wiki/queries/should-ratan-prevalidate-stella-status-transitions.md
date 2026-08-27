---
type: query
title: Should Ratan Prevalidate Stella Status Transitions?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, stella, validation, state-machine]
related: [stella-cashflow-status-synchronization, ratan-cashflow-lifecycle-service, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Should Ratan Prevalidate Stella Status Transitions?

A development test indicates that Stella rejects a direct `PROJECTED` to `SETTLED` update as a cross-status update.

Determine whether `ratan-cashflow-lifecycle-service` must prevent invalid transitions before calling Stella, or whether Stella is the sole validator. This source alone does not resolve the complete Ratan state machine.