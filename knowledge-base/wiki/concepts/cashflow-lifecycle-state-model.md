---
type: concept
title: Cashflow Lifecycle State Model
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, lifecycle, state-machine, Ratan, NSTP, settlement]
related: [ratan, fmrp-cashflow-responsibility-split, nstp-rule-routing, cash-settlement-home-page, released-settled-amendment-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# Cashflow Lifecycle State Model

The proposed post-trade lifecycle is:

```text
Projected → Queued → Pending → Validated → Released → Settled
```

## Transition ownership

- `Projected → Queued`: Ratan materializes the cashflow, normally on VD-5.
- `Queued → Pending`: Ratan identifies NSTP Review, CPN, SSI Exception, or another review criterion.
- `Pending → Validated`: FMO resolves the applicable criteria through maker/checker processing.
- `Validated → Released`: Ratan generates and sends the Swift message to FMSRE.
- `Released → Settled`: the Swift message has been sent to the Swift network and the settlement outcome is returned through downstream processing.

`Pending Operator` and `Pending Verification` are operational sub-statuses associated with NSTP processing.

## Unresolved state semantics

The source also names `Failed`, `Netted`, `Suppressed`, and direct transitions such as `Projected → Released` and `Netted → Settled`. It does not state whether these are formal states, exceptional transitions, or replicated status views. A canonical state-machine contract is therefore still required.