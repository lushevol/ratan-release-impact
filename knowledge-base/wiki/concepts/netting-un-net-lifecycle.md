---
type: concept
title: Netting Un-Net Lifecycle
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-netting, un-netting, lifecycle, workflow, trade-amendment]
related: [netting-resultant-cashflow, cashflow-lifecycle-versioning, ratan, maker-checker-settlement-control, adhoc-cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Settlement Netting Validation Generation.md"]
---
# Netting Un-Net Lifecycle

Netting un-netting reverses the operational effect of a netting request without deleting its history. It terminates the resultant and restores the components to settlement workflow.

## Ordinary checker un-net

For a checker review, the expected state transition is:

```text
Resultant: Pending / Netting / Pending Verification -> DEAD
Components: Netted -> Queued
```

The resultant becomes an end state and is removed from the GUI and settlement workflow. Components are pushed back to workflow and may participate in a later netting round.

A resultant cannot be netted directly. It must first be un-netted.

## Approval path

Approval is distinct in outcome:

```text
Resultant: Pending / Netting / Pending Verification -> Validated -> Released
Components: remain Netted and hidden
```

The checker must be a different FMO user from the maker. The shared Netting ID provides access to the component details.

## Trade-amendment reversal

A trade amendment after netting is more complex than ordinary un-netting. The source describes:

- Withdrawal of the amended original component.
- Creation of a successor component.
- Cancellation or withdrawal of the existing resultant.
- A withdrawn component potentially becoming `Suppressed`.
- Successor flows entering `Pending / Netting / Pending Reversal`.
- A requirement that the resultant be cancelled before FMO proceeds with successor components.

This path introduces business-version, cashflow-version, and Ratan minor-version changes. It should not be implemented as a simple alias for checker un-net.

## Unresolved state semantics

The source uses `Dead`, `DEAD`, `Suppressed`, `Netted`, `Pending Netting`, and `Netting` without defining whether each belongs to a cashflow status, workflow status, sub-status type, sub-status, or terminal-state enum. A canonical transition matrix is required.

The source also refers to both `Reject Netting` and `Un-Net`. It does not state whether rejection always performs the un-net transition or follows a separate resubmission path.