---
type: concept
title: Cashflow Split and Un-Split
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, split, un-split, withdrawal, lifecycle]
related: [cashflow-withdrawal-and-new, cashflow-status-lifecycle, cashflow-event-versioning, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md"]
---
# Cashflow Split and Un-Split

Cashflow split and un-split describe the relationship between a gross parent cashflow and its child cashflows in [[entities/ratan]].

## Split lifecycle

The draft models a gross cashflow such as `C101` and two children:

```text
Gross parent: C101 -> PROJECTED -> QUEUED -> WAITING -> SPLIT
Child S101:        PROJECTED -> QUEUED -> WAITING
Child S102:        PROJECTED -> QUEUED -> WAITING
```

The example divides a USD 200 pay cashflow into two USD 100 pay children.

## Withdrawal-driven un-split

When the gross parent is withdrawn, the draft proposes:

- The parent moves from `SPLIT` to `CANCELLED`.
- Children still in Ratan move to `DEAD`.
- Children outside Ratan receive withdrawal events with updated business versions.

This is a relationship-level operation rather than an independent cancellation of each child. It is analogous to automatic un-netting described in [[concepts/cashflow-netting-and-un-netting-state-transitions]].

## Limitations

The draft does not define:

- The parent-child correlation key.
- Whether children may be partially released or settled.
- The result when only some children are available in Ratan.
- The financial reversal behavior for released children.
- Whether a replacement parent or replacement children are generated automatically.

Accordingly, the described behavior is historical design intent and not an authoritative lifecycle contract.
