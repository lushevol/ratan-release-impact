---
type: query
title: What Is the Authoritative Fixing Flag State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, fixing-flag, state-machine, IRS]
related: [fixing-flag-notification-processing, pending-fixing-and-waiting-another-leg, fixing-notification-event-ordering, cashflow-status-change-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# What Is the Authoritative Fixing Flag State Machine?

The fixing-flag design uses `PendingFixing`, `WaitingAnotherLeg`, and example flags `X`, `Y`, and `N`, but does not define their canonical relationship.

## Questions

- Are `PendingFixing` and `WaitingAnotherLeg` persisted statuses or derived values?
- Are `X`, `Y`, and `N` production fixing-flag values or placeholders?
- Does flag `N` mean that no fixing is required, or only that the cashflow is no longer waiting for another leg?
- Which service owns the final state transition?
- How are cancelled, failed, and `techfailed` cashflows represented?
- Can fixing-flag data change while the lifecycle state remains cancelled?

The withdrawal scenario suggests that lifecycle state and fixing-flag data must be modeled separately, but this has not been confirmed.
