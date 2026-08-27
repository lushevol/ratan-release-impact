---
type: concept
title: RATAN Cashflow Lifecycle State Machine
tags: [ratan, cashflow, lifecycle, state-machine, settlement]
related: [cashflow-lifecycle-versioning, ratan-external-and-internal-lifecycle-requests, cashflow-failure-and-reinstatement, cashflow-hold-unhold, ad-hoc-cashflow-netting, cashflow-splitting, swift-versus-cashflow-suppression, maker-checker-settlement-control, utilization-pilot, what-is-the-authoritative-ratan-lifecycle-transition-matrix]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# RATAN Cashflow Lifecycle State Machine

The RATAN lifecycle model represents a cashflow with a three-part state index: main status, sub-status, and sub-status type. It is an intended functional design for routing STP and manual cashflow actions, not evidence that every documented transition is live.

The standard non-netted progression is:

```text
PROJECTED → QUEUED → WAITING or READY → RELEASED → SETTLED
```

`PROJECTED` is materialized into `QUEUED`, normally by a VD-5 job or early user action. Validation can route a queued cashflow to `READY`, to a `WAITING` workflow, to a suppression state, to `NETTED`, or to `FAILED`. A `READY` cashflow can be released, settled directly, held, netted, failed, or returned to workflow.

## Workflow states

`WAITING` expresses responsibility and cause, rather than one common processing condition. Documented examples include:

- `Pending Operator / Pending Netting` for FMO Maker netting.
- `Pending Verification / Pending Exception` for FMO Checker exception resolution.
- `NA / Pending Another Leg` for a related-leg dependency.
- `NA / Auto Netting` for scheduled netting processing.
- `Pending Verification` with suppression, unsuppression, manual-settlement, reversal/rebook, or netting-review types.

These controls connect to [[maker-checker-settlement-control]], [[ad-hoc-cashflow-netting]], and [[pending-another-leg]].

## Settlement, suppression, and recovery

`RELEASED` follows publication to the FM Swift Gateway or Razor legacy processing; `SETTLED` follows acknowledgement from AMH/SCPAY or a direct-settlement action. `NOSTRO_MATCHED` is specified for TLM reconciliation but was explicitly out of scope in this source.

The model distinguishes [[swift-versus-cashflow-suppression]]:

- `CASHFLOW_SUPPRESSED` excludes settlement and accounting.
- `SWIFT_SUPPRESSED` retains accounting eligibility but excludes SWIFT generation.

Failure, netting, splitting, holds, and utilization introduce recovery paths and non-linear transitions. Their detailed behavior is documented in [[cashflow-failure-and-reinstatement]], [[cashflow-hold-unhold]], [[cashflow-splitting]], and [[utilization-pilot]].

## Reliability limitations

The source matrix is not yet safe as an unqualified implementation contract. It has undefined targets for `UnHold` and suppression rejection actions, malformed labels, inconsistent enum spellings, and deprecated struck-through transitions. Use an approved machine-readable transition source before generating validations or orchestration rules; see [[what-is-the-authoritative-ratan-lifecycle-transition-matrix]].