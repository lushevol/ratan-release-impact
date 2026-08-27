---
type: concept
title: FX Cashflow Status Write-Back
tags: [fx, cashflow, status-write-back, duplicate-payment-control, fmrp, status, write-back, integration]
related: [razor, ratan, stella, fmrp, cashflow-status-lifecycle, cashflow-netting-and-un-netting-state-transitions, stella-suspended-matured-hard-block, six-economic-field-cashflow-matching, scbml, cashflow-status-change-event-contract, cash-settlement-platform, denormalized-cashflow-query-read-model, cashflow-notification-and-auto-refresh]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FX Cashflow Status Write Back - Razor to Stella.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md"]
---
# FX Cashflow Status Write-Back

The functional-requirement source describes FX cashflow status write-back as a proposed [[razor]] → [[ratan]] → [[stella]] feedback process for in-scope FX Spot, Forward, and Swap cashflows. Its purpose is to reduce duplicate-payment risk where Razor, rather than Stella, processes settlement.

The technical-design source provides a single [[scbml]] `CashflowStatusChange` sample from [[razor]], whose tracking ID includes `FXCASH`. It characterizes the flow as the return of a cashflow outcome from an originating system into the Cash Settlement domain. This sample is not evidence that every FX write-back follows the sample values or that a distinct FX replication service exists.

## Functional-requirement behavior

According to the functional-requirement source, RATAN changes the matched latest-version Stella cashflow to `SUSPENDED-MATURED` when it receives an eligible Razor event. This state is used for Stella hard-block control; it is not a generic payment, SWIFT, or settlement-completion status.

### Eligibility

A Razor event is eligible only when all of the following apply:

- Validation status is `Released`, `Settled`, `Netted`, `Split`, or `CCPNetted`.
- Reverse status is `None` or `Correction`.
- The Razor cashflow ID has not previously completed successfully.
- The message is not withdrawal-only.
- The event can be matched to a latest-version Stella cashflow through [[six-economic-field-cashflow-matching]].

If the Stella cashflow is already `SUSPENDED-MATURED`, the design prefers no redundant update.

### Lifecycle exclusions

`Netted` and `Split` are qualifying source states, but cashflows resulting from a netting or splitting transformation are not written back. Un-net and un-split events are also explicitly excluded. The stated rationale is continued duplicate-payment risk, even if the resulting Stella view is not a complete representation of Razor's lifecycle.

### Amendment behavior

For a Stella non-economic amendment, RATAN compares the prior and new cashflows using six economic fields. If the prior cashflow was `SUSPENDED-MATURED`, RATAN immediately propagates that state to the latest cashflow. If the prior cashflow was `SUSPENDED`, RATAN waits for Razor.

For a new cashflow or an economic amendment, RATAN waits for an eligible Razor event. Razor is assumed to make only non-economic amendments and not send those amendments to RATAN, but Razor provides no explicit economic-amendment indicator.

## Technical-design event sample

The technical-design source's single Razor event sample:

- Reports one cashflow as `Settled`.
- Marks `isPaymentReversal` as `false`.
- Provides a payment date.
- Supplies settled currency `CNH`.

The sample labels its process event type `Insert` while conveying a status change. This is materially ambiguous: a recipient may insert an immutable event, insert a status-history record, update a current cashflow state, or perform more than one of these actions. The technical-design source does not select among these interpretations.

No specific Query Service, blotter, or Cash Settlement persistence target is established by the sample.

## Control limitations and unresolved requirements

The functional-requirement source identifies material control limitations:

- Razor does not provide a trade version, so RATAN targets the latest Stella version.
- Correlation intentionally permits non-exact currency and amount comparisons.
- Reconciliation is not in place.
- ACK and NACK behavior is internally inconsistent.

Separately, the technical-design source states that operational use of this flow requires defined identity matching, idempotency, version ordering, allowed transitions, replay behavior, and reconciliation controls.

See [[what-is-the-authoritative-ack-nack-and-reconciliation-model-for-razor-stella-fx-status-write-back]] and [[how-does-ratan-prevent-stale-or-ambiguous-razor-events-from-updating-the-wrong-stella-cashflow-version]].