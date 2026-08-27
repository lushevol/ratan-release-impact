---
type: source
title: Stella Inbond Cashflow Filter
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page / Functional Requirement / Issue Tracking & Tech Debt"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, ratan, stella, cashflow, issue-tracking, event-reconciliation]
related: [stella, ratan, non-trade-event-cashflow-updates, cashflow-event-withdrawal-reconciliation, how-should-stella-expiry-and-withdrawal-events-reconcile-in-ratan, cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Stella Inbond cashflow filter.md"]
---
# Stella Inbond Cashflow Filter

## Summary

This source records an unresolved production issue involving [[stella]], [[ratan]], and the handling of cashflow events that are not driven by trade events.

Under the stated normal flow, a trade event generates new cashflow events and increments a cashflow major version. RATAN interprets the resulting new cashflow as a business change. The source identifies exceptions in which cashflows are updated without a trade event:

1. A status update driven by RATAN.
2. A Stella cashflow expiry.

## Reported production case

The reported sequence is:

> New cashflow + Expiry + Withdrawal

The source states that this sequence produces two new events but only one withdrawal event. Consequently, the withdrawal can offset only one of the new events, leaving another new event unmatched.

This is evidence of an event-cardinality mismatch, but the source does not establish whether either new event is invalid, whether expiry should produce a different event type, or whether a withdrawal is expected to offset more than one event.

## Unspecified implementation details

Although the title refers to an inbound cashflow filter, the source does not define an approved filter or reconciliation design. In particular, it does not specify:

- a Stella-to-RATAN correlation key;
- event precedence among new, expiry, and withdrawal events;
- the intended cardinality of withdrawal offsets;
- ownership of filtering or reconciliation;
- required lifecycle or major-version behaviour; or
- financial and accounting consequences for the unmatched event.

The referenced image `attachments/image2024-11-13_10-30-26.png` is not available in the supplied document text.

## Related knowledge

The issue extends [[non-trade-event-cashflow-updates]] and may expose a lifecycle gap in [[cashflow-lifecycle-state-machine]]. It also raises whether the versioning model described by [[business-versioned-cashflow-persistence]] is sufficient for correlating events that do not originate from a trade amendment.

The unresolved design question is tracked in [[how-should-stella-expiry-and-withdrawal-events-reconcile-in-ratan]].