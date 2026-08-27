---
type: concept
title: Cashflow Status Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, lifecycle, projected, queued, netted, dead]
related: [cashflow-materialization, cashflow-netting-and-un-netting, ratan, cashflow-record]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# Cashflow Status Lifecycle

The CN Settlement demo specifies an individual-cashflow status model in [[Ratan]].

## Required transitions

- A VD-7 `New` cashflow is stored as `Projected`.
- A VD-5 or VD-4 `New` cashflow is stored as `Queued`.
- Materialization changes `Projected` to `Queued` on VD-5 in the documented scenario.
- Netting changes component cashflows from `Queued` to `Netted` and creates a resultant cashflow as `Queued`.
- Un-netting restores components from `Netted` to `Queued` and changes the resultant from `Queued` to `Dead`.

This model applies to individual cashflows and should not be conflated with [[Cashflow Group Lifecycle]] or [[Cashflow Group Blotter State Lifecycle]].