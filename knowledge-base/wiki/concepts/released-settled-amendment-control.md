---
type: concept
title: Released and Settled Amendment Control
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, amendment, withdrawal-and-new, FO, MO, payment-correction]
related: [fmrp-stella, ratan, razor, cashflow-lifecycle-state-model, cashflow-version-concurrency-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# Released and Settled Amendment Control

The proposal establishes `Released` and `Settled` as an amendment-control boundary.

When the underlying cashflow is `Released` or `Settled`:

- FO amendment is blocked.
- MO is permitted to amend the trade.
- Stella emits a `Withdrawal` event for the original cashflow and a new cashflow for the amended trade.
- Ratan must process the withdrawal before the new event.
- Razor may issue `MT292/MT192` reversal messages and `MT202/MT103` replacement or original payment messages.

The source states:

```text
There's system control the Withdrawal event(C101) must be proceeded prior to the new event(C102)
```

The examples use inconsistent identifiers for the replacement cashflow. Identifier lineage, permission enforcement across all entry points, and the exact reversal state are not yet authoritative.