---
type: concept
title: Utilization Status Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-status, lifecycle, fx-utilization]
related: [ratan, stella, blade, cashflow-status-lifecycle, fx-utilization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Utilization Status Lifecycle

The proposed utilization lifecycle distinguishes full utilization, partial utilization, and PastDue state.

- `UTILIZED` means the full amount is utilized and remaining amount is zero.
- Partial utilization is variously written as `PARTIALLY-UTILIZED`, `PARTIALUTILIZED`, and `PARTIALUTIL`.
- `PASTDUE` is described as a main status, while `Pastdue` is also described as a sub-status.

RATAN is intended to publish utilization status to [[stella]], enabling [[blade]] to hard-block market events for cashflows that are utilized or partially utilized. Partial and PastDue states are marked out of MVP scope, and the source does not define canonical codes or valid transitions. See [[what-is-the-canonical-fx-utilization-status-and-sub-status-model]].