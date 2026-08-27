---
type: entity
title: CashflowGroup
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, domain-object, cashflow-groups, sequencing]
related: [ratan, cashflow-group-message, cashflow-group-lifecycle, trade-validation-group-advancement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# CashflowGroup

`CashflowGroup` is the RATAN domain object representing a grouped set of related cashflows. It is persisted as `ratan_cashflow_group`.

## Identification and initial state

The source describes group lookup using:

- `batchId`
- `tradeId`
- `majorVersion`

A newly built group has:

```text
status=PENDING
isLocked=true
```

The lock and earlier-group checks prevent a later group from advancing before its predecessor is complete.

## Lifecycle role

A `CashflowGroup` coordinates:

- Inbound message collection.
- Trade-validation propagation.
- Previous-group sequencing.
- Transition to `READY`.
- Downstream orchestration.
- Completion and unlocking.

See [[concepts/cashflow-group-lifecycle]] for the documented state transitions.