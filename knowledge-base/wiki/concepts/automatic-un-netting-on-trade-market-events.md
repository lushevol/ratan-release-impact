---
type: concept
title: Automatic Un-Netting on Trade Market Events
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, trade-market-event, un-netting, ratan]
related: [ratan, stella, murex, cashflow-event-versioning, does-auto-un-netting-place-cashflows-in-nstp-or-queued, what-market-event-correlation-key-triggers-ratan-auto-un-netting, what-is-the-ratan-auto-un-netting-contract-for-cancellation-and-termination, what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Auto Un-Net - Trade market event.md"]
---
# Automatic Un-Netting on Trade Market Events

Automatic un-netting is Ratan's group-level reversal of an existing FMRP strategy-netting arrangement when a later trade-market event affects a netted component.

In the documented case, a new Stella Amendment version for component `C103` causes Ratan to release all components in netting group `N101`, including Murex 2.11 components `C101` and `C102`, and to retire Ratan-generated resultant `C104`.

## Illustrated transition

| Record role | Before event | After automatic un-netting |
| --- | --- | --- |
| Existing component `C101` | `Netted` | `Queued` |
| Existing component `C102` | `Netted` | `Queued` |
| Amended component `C103` | `Projected` on Amendment version `2` | `Queued` |
| Ratan resultant `C104` | `Queued` | `Dead` |

The source retains `N101` in the post-un-net table, but does not define whether this is an active association, a persisted audit reference, or merely illustrative lineage.

## Scope boundary

The source names Amendment, Cancellation, and Termination as possible incoming market events, but demonstrates only Amendment. It does not establish that Murex 2.11 or MXCash can independently trigger the same action, nor does it require automatic re-netting after release.

The operational status is ambiguous: narrative text says un-netted cashflows are held as `NSTP`, while the example records `Queued`. This is tracked in does auto un netting place cashflows in nstp or queued.

## Required but unspecified controls

A production contract requires rules for:

- Correlating an incoming event to a previously netted component and group.
- Version sequencing, late events, duplicate delivery, and idempotency.
- Concurrent events affecting several components of the same group.
- Handling a resultant that has progressed beyond `Queued`.
- Subsequent user review and potential re-netting.

See what market event correlation key triggers ratan auto un netting and what is the ratan auto un netting contract for cancellation and termination.