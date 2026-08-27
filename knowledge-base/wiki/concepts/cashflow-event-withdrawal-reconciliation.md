---
type: concept
title: Cashflow Event Withdrawal Reconciliation
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, events, withdrawal, reconciliation, expiry, controls]
related: [stella, ratan, non-trade-event-cashflow-updates, cashflow-lifecycle-state-machine, cashflow-technical-failure-recovery, how-should-stella-expiry-and-withdrawal-events-reconcile-in-ratan, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--28-02-issue-tracking-tec--1uz12d6]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Stella Inbond cashflow filter.md"]
---
# Cashflow Event Withdrawal Reconciliation

Cashflow event withdrawal reconciliation is the control that determines which prior cashflow event or events a withdrawal offsets, using an authoritative correlation key and event-precedence policy.

## Reported mismatch

A reported [[stella]] production sequence contains:

- two new events; and
- one withdrawal event.

The withdrawal can offset only one new event under the described processing, leaving one new event unmatched.

## Undetermined policy

The source does not establish the intended reconciliation policy. It remains unclear whether:

- both new events are valid;
- one new event is a duplicate;
- expiry should supersede or cancel a prior event;
- expiry should create a replacement rather than a new event; or
- one withdrawal should offset multiple events.

The required matching identifier, lifecycle result, version treatment, and ownership between Stella and [[ratan]] are also unspecified.

This concern is related to [[cashflow-technical-failure-recovery]], but the source does not classify the condition as a technical failure. The governing question is tracked in [[how-should-stella-expiry-and-withdrawal-events-reconcile-in-ratan]].