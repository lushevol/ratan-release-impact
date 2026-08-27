---
type: concept
title: Cashflow Event Control
tags: [cashflow, event-sequencing, deduplication, lifecycle-control, ratan, cashflows, trade-events, settlement, uat]
related: [ratan, stella, murex-211, cashflow-batch-control, cashflow-business-and-message-versioning, cashflow-version-concurrency-control, undo-revive-cashflow-control, cashflow-lifecycle-state-model, released-settled-amendment-control, trade-event-undo-semantics, cashflow-netting-and-auto-un-netting, cn-settlement-murex-211-integration]
created: 2026-08-24
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# Cashflow Event Control

Cashflow event control governs how booking, amendment, cancellation, withdrawal, early termination, expiry, novation, and portfolio reassignment affect payment obligations and their lifecycle states.

In the Ratan control model described by the primary requirement, cashflow event control is the second-level control, applied after [[cashflow-batch-control]] has established trade-event ordering. It manages repeated messages for the same cashflow ID and protects settlement processing from invalid replay or lifecycle patterns.

## Release and lifecycle control

The CN Drop 2 UAT catalogue treats payment release as the principal control boundary. Its scenarios are repeatedly divided into actions performed before or after release of the original payment, cancellation, termination fee, or net payment.

According to that catalogue:

- Before payment release, an event may generally modify, cancel, or revive the original cashflow.
- After release, the original cashflow generally remains released while the event is blocked, discarded, or represented by a separate cancellation or reversal flow.

The catalogue tests the following target behaviors:

- Amendments and cancellations for single, BTB3/5/7, inter-entity, and intra-entity trades
- Portfolio reassignment before and after payment release
- Novation before and after payment release
- Cancellation and amendment after net payment release
- Expiry gated by cashflow settlement status
- Undo behavior for cancellation, early termination, and expiry

These are target behaviors in a UAT scenario catalogue, not evidence that every scenario passed.

## Defined event sequences

The primary requirement defines the following repeated-event sequences:

- `New → Withdrawal` is a normal business sequence.
- `New → Withdrawal → New` is an allowed sequence associated with trade Undo/Revive and is processed in order.
- `New → New → New` retains the first `New` and discards subsequent `New` events.

Cashflow major version increases across successive trade lifecycle events in the examples. Business version and source message version must remain distinguishable from this major version.

## Event-specific overrides

The generic sequence rule does not override business-event rules. In particular, Stella expiry events are non-economic and are discarded, including later revive messages.

Undo cases must also respect release, settlement, netting, and cancellation state before a new event can be accepted. The UAT catalogue separately tests undo behavior for cancellation, early termination, and expiry, including the effect of payment and cashflow settlement status.

## Related controls

Cashflow event control is implemented or investigated alongside [[fo-hard-block-mo-soft-block]], [[trade-event-undo-semantics]], [[cashflow-netting-and-auto-un-netting]], and [[cashflow-suppression-rules]]. Detailed status synchronization and release-processing context is documented in [[fmrp-cashflow-status-synchronization]] and [[ratan-cashflow-acknowledgement-and-release-processing]].

See also [[undo-revive-cashflow-control]] and [[stella-trade-event-to-settlement-control]].

## Limits of the stated rule

The primary requirement does not specify:

- Idempotency keys
- Deduplication windows
- `Withdrawal → Withdrawal` handling
- Out-of-order delivery treatment
- How to compare economically different duplicate `New` messages

The UAT scenarios describe target behaviors and coverage areas, but do not establish that every scenario passed.