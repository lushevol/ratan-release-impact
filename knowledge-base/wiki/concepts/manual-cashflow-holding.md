---
type: concept
title: Manual Cashflow Holding
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, manual-hold, cashflow-status, workflow-control]
related: [cashflow, cashflow-status-restoration, holding-release-precheck, cashflow-precheck-validation, manual-hold-representation-options, what-is-the-authoritative-manual-hold-status-transition-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Manual Holding Process Tech Design.md"]
---
# Manual Cashflow Holding

Manual cashflow holding is an operator-controlled capability that prevents a cashflow from proceeding through in-progress settlement processing. The technical design selects representation through the cashflow's main status.

## Intended processing effect

While held, a cashflow must be blocked from the following operations or states identified by the design:

- Pending Exception, including pending operator or verification work
- Pending Netting
- Ready
- Queued
- Projected

Unhold is intended to return the cashflow to its original pre-hold status, eliminating duplicated work.

## Separation from exceptions

Manual holding is explicitly intended to remain separate from ordinary exception remediation. The rejected exception-based alternative would have created a checker-only exception, which would prevent users from resolving all exceptions while retaining a manual hold.

Manual hold should also not be conflated with [[cashflow-lifecycle-stamping]]. The source concerns operational workflow control, not lifecycle-event stamping.

## Release validation

[[holding-release-precheck]] remains relevant: the evaluated `isHeld` alternative would have required release checks to consider both queued-cutoff status and the new hold attribute. Since the selected design uses main status, the authoritative release predicate and status mapping remain unresolved.

## Limitations

The source does not specify a canonical held status, whether holding is idempotent, how a hold is persisted, or how concurrent processing requests are controlled. These gaps are tracked in [[what-is-the-authoritative-manual-hold-status-transition-contract]].