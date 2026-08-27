---
type: concept
title: Allocation Cashflow State Handling
created: 2026-08-22
updated: 2026-08-22
tags: [allocation, cashflows, suspended, projected, stella, ratan, settlement]
related: [stella, ratan, mw, vpa, cashflow-lifecycle-state-machine, fmrp-to-ratan-migration-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# Allocation Cashflow State Handling

Allocation cashflow state handling governs how block-trade and child-trade cashflows are represented and admitted to settlement processing after an allocation event.

## Documented flow

The source identifies the following processing path:

```text
MW → VPA → Stella
```

The explicit state behavior is:

| Flow | Cashflow status |
|---|---|
| Allocation block trade | `SUSPENDED` |
| Allocation child trade | `PROJECTED` |

The source also states that RATAN should filter out cashflows from allocation events.

## Settlement interpretation

The requirements imply that technically generated cashflows are not automatically eligible for normal settlement processing. Block-trade cashflows are held in `SUSPENDED`, while child-trade cashflows are forward-looking in `PROJECTED`.

The source does not establish:

- Whether RATAN filters by event type, allocation flag, status, or all three.
- When a `PROJECTED` child cashflow becomes settlement-eligible.
- Whether the block cashflow is replaced, cancelled, or retained for lineage.
- How allocation re-entry, amendment, reversal, or failure is handled.
- Whether these states map to existing RATAN lifecycle states.

`SUSPENDED` and `PROJECTED` must therefore remain distinct from `PendingAutoNetting`, payment suppression, cashflow suppression, and cashflow failure until an authoritative mapping is approved.