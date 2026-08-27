---
type: query
title: How Should Stella Expiry and Withdrawal Events Reconcile in RATAN?
created: 2026-08-22
updated: 2026-08-22
tags: [stella, ratan, cashflow, expiry, withdrawal, reconciliation, open-question]
related: [stella, ratan, non-trade-event-cashflow-updates, cashflow-event-withdrawal-reconciliation, cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--28-02-issue-tracking-tec--1uz12d6]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Stella Inbond cashflow filter.md"]
---
# How Should Stella Expiry and Withdrawal Events Reconcile in RATAN?

## Question

What identifier, event-precedence rule, and cardinality policy should [[ratan]] use to reconcile Stella new-cashflow, expiry, and withdrawal events?

## Evidence

The available source reports a production sequence of new cashflow, expiry, and withdrawal. It states that two new events exist while only one withdrawal event is emitted, so the withdrawal offsets only one new event.

The source also identifies [[non-trade-event-cashflow-updates]] as a relevant exception to normal trade-event-driven cashflow processing.

## Information needed

Resolution requires production evidence for the affected sequence, including:

- cashflow and event identifiers;
- event timestamps and processing order;
- major versions and lifecycle statuses;
- source payload fields;
- the expected post-withdrawal RATAN state; and
- financial or accounting impact of the unmatched event.

## Decisions required

A solution must define whether expiry is a new event, amendment, status update, cancellation, or replacement; whether withdrawal reconciliation is one-to-one or one-to-many; and whether control ownership lies with Stella, RATAN inbound processing, or downstream reconciliation.

The Murex-focused queries [[how-should-ratan-recover-missing-or-out-of-order-murex-payment-events]] and [[what-is-the-authoritative-ratan-correlation-key-for-murex-reversal-and-new-payments]] are conceptually analogous but do not provide a Stella-specific rule.