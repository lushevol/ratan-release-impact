---
type: concept
title: DVP Exception Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [DVP, exception, cashflow, settlement, Ratan]
related: [auto-dvp-ebbs, cashflow-lineage-and-amendment-correlation, split-cashflow-dvp-handling, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md"]
---
# DVP Exception Lifecycle

A DVP exception is an exception state associated with an eligible Pay cashflow while the corresponding Receive-side settlement condition has not been satisfied.

## States and outcomes in the UAT specification

The source uses the following cashflow statuses:

- `Waiting`
- `Settled`
- `Cancelled`

It separately describes a DVP exception as present, retained, or automatically closed. Therefore, exception closure is not necessarily the same field or transition as the cashflow status.

The primary expected transition is:

```text
Receive cashflow: Waiting -> Settled
Pay-side DVP exception: open -> automatically closed
```

The UI indication for the positive case is a green `DVP Received` tag on the Pay cashflow in Cashflow Details.

## Negative and directional cases

The Pay-side exception remains open when:

- The booking entity is outside the tested scope.
- The product is not eligible CCS.
- The RTA amount does not match.
- The RTA value date is more than two business days after the payment date.
- The Receive-side relationship is replaced by an amendment with a changed trade ID.
- The relationship is an ordinary non-split one-to-many linkage.

A Pay-side RTA notification settles the Pay cashflow but does not automatically resolve the Receive-side exception relationship.

## Unresolved state semantics

The specification does not define whether closing an exception changes the `Waiting` status, records a separate resolution state, or only removes an exception flag and adds a UI tag. It also does not define the precise behavior of a withdrawn cashflow version.