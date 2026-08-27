---
type: concept
title: Bilateral Netting Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, eligibility, validation, static-data]
related: [bilateral-netting, netting-static-blotter, ccil, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Bilateral Netting Eligibility

Bilateral netting requires both a live manual netting rule and a matching eligibility key.

## Required netting key

The selected cashflows must have the same:

- Booking entity
- Counterparty
- Value date
- Currency

If any attribute differs, the operation must be rejected with:

> `Validation failed ,Cash flow selected are not eligible for netting as either the same booking entity, counterparty,value date,currency`

The source does not define precedence when multiple attributes differ.

## State requirement

Before netting, eligible components are expected to be:

```text
state = 'WAITING'
cashflow sub state type = 'Pending Netting'
```

Cashflows in `Released` or `Settled` state are not eligible for netting. The requirement does not specify whether this restriction applies to resultant cashflows, component cashflows, or both in every context.

## CCIL scenario

The guaranteed CCIL scenario covers cashflows with:

```text
Settlement Method = CCIL
Counterparty FMID = 400021949
```

These cashflows are expected to produce an affirmed bilateral-netting resultant. The source does not establish whether `400021949` is required for every CCIL netting case.

## Rule ownership

Manual netting rules are created and maintained in the [[netting-static-blotter]]. The behavior of disabling or updating a rule after cashflows have entered `Pending Netting` remains unresolved.