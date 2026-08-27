---
type: concept
title: Non-Trade-Event Cashflow Updates
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, events, lifecycle, status-update, expiry, ratan]
related: [stella, ratan, cashflow-event-withdrawal-reconciliation, cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--28-02-issue-tracking-tec--1uz12d6]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Stella Inbond cashflow filter.md"]
---
# Non-Trade-Event Cashflow Updates

Non-trade-event cashflow updates are changes to a cashflow that do not originate from a trade event.

The documented normal model is that trade events create cashflow events, increase the cashflow major version, and cause [[ratan]] to consume a new cashflow as a business change. The source identifies two exceptions:

- a status update driven by RATAN; and
- cashflow expiry in [[stella]].

## Control implication

Consumers must not assume that every cashflow update has a one-to-one trade-event origin. Lifecycle processing needs explicit correlation and precedence rules for updates arising through status and expiry paths.

The reported Stella case demonstrates the risk: two new events and one withdrawal event may leave an unmatched event when withdrawal processing assumes one-to-one offsetting.

## Relationship to lifecycle and persistence

[[cashflow-lifecycle-state-machine]] should account for expiry and withdrawal transitions that occur without a corresponding trade event. [[business-versioned-cashflow-persistence]] is relevant because the source associates normal business changes with major-version increments, but does not establish how major versions identify or reconcile non-trade-driven updates.