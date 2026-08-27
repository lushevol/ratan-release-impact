---
type: query
title: What Are the Preconditions and Execution Mechanism for Trade-Event-Triggered Cashflow STP?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, stp, nstp, settlement-instructions, cdu, workflow]
related: [trade-event-triggered-cashflow-stp, stp-nstp-and-last-user-message-contract, cash-settlement-home-page, cdu, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Trade event trigger cashflow STP.md"]
---
# What Are the Preconditions and Execution Mechanism for Trade-Event-Triggered Cashflow STP?

Two validation scenarios show SI entry and verification before a CDU inbound completion event changes `Trade_State` and is followed by STP. The source does not distinguish prerequisites from the transition trigger or execution mechanism.

## Known Sequence

Both scenarios perform the following activities:

1. Enter SI in Settlement Exceptions.
2. Verify SI in Settlement Exceptions.
3. Confirm the “Trade/Cash not affirmed” NSTP condition.
4. Produce a qualifying CDU event.
5. Verify event persistence in RATAN.
6. Observe STP.

## Questions to Resolve

- Must SI be entered, verified, or both before the cashflow can reach STP?
- Does a qualifying CDU event directly invoke STP, or merely make the cashflow eligible for a later rule reevaluation?
- Which service, job, or event handler evaluates the NSTP predicate after the trade-state change?
- Can STP occur when `Cashflow__Cashflow_Affirmation_Status` remains other than `Affirmed`?
- What occurs if the trade is already `AFFIRMED` or `CONFIRMED` when the event arrives?

The source supports the ordered workflow but not a complete causal or operational contract. See [[trade-event-triggered-cashflow-stp]].