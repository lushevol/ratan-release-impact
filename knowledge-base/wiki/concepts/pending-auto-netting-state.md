---
type: concept
title: Pending Auto Netting State
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, auto-netting, lifecycle, state-management]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-resultant-cashflow-lifecycle, netting-un-net-lifecycle, netting-static-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Business user case testing.md"]
---
# Pending Auto Netting State

`Pending Auto Netting` is the cashflow sub-state used while an eligible cashflow is waiting for the configured auto-netting execution time.

## Observed representation

The source consistently represents the state as:

```text
state = 'WAITING'
cashflow sub state type = 'Pending Auto Netting'
```

This state is observed before the scheduled job in bilateral, CCIL, BIC, single-cashflow, post-netting-time, cross-rule, withdrawal, and refresh scenarios.

## Transitions observed in testing

- At the configured execution time, multiple eligible cashflows can become `NETTED` and produce a resultant.
- A single eligible cashflow remains `WAITING` but can become affirmed and receive the configured NSTP exception.
- Withdrawal before execution changes the withdrawn cashflow to `CANCELLED`; remaining eligible cashflows can still be netted.
- Withdrawal after a resultant has been created can return surviving source cashflows to `WAITING / Pending Auto Netting`.
- Creating a new rule can move existing cashflows from `Pending Netting`, `Pending Exception`, or `READY` into `Pending Auto Netting`.
- Disabling a rule is expected to remove this sub-state, but the destination state is not defined and one test observed an unexpected `Pending Exception`.

The complete authoritative state machine remains unresolved; this page records test evidence rather than a formal implementation contract.