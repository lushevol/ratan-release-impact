---
type: query
title: What Correlation Key and Version-Ordering Rules Trigger Ratan Auto Un-Netting?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, netting, correlation, event-versioning, idempotency]
related: [automatic-un-netting-on-trade-market-events, ratan, stella, murex, cashflow-event-versioning, what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Auto Un-Net - Trade market event.md"]
---
# What Correlation Key and Version-Ordering Rules Trigger Ratan Auto Un-Netting?

## Question

What identifiers and ordering rules allow Ratan to determine that an incoming trade-market event belongs to a component of an existing netting group and therefore must trigger automatic un-netting?

## Evidence

The source requires Ratan to identify new market events on netted cashflows. Its only worked case shows Stella sending Amendment version `2` for cashflow `C103`, previously a component in netting group `N101`.

The source does not specify whether correlation uses `Cashflow ID`, source-system identity, trade ID, an upstream event identifier, `Netting ID`, an economic composite key, or another identifier.

## Decisions required

Define:

- The authoritative component-to-netting-group correlation key.
- Whether event versions must be strictly increasing.
- Duplicate-message and idempotency behavior.
- Treatment of late, stale, or out-of-order events.
- Concurrency handling when multiple components receive events.
- Behavior when the prior resultant has progressed beyond `Queued`.

This question is related to [[cashflow-event-versioning]] and [[what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule]].