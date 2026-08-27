---
type: concept
title: Trade-Event-Triggered Cashflow STP
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, stp, nstp, trade-state, cdu, settlement-instructions]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--zfjdgu, bcs-cdu-match-status-confirmation, stp-nstp-and-last-user-message-contract, which-trade-state-results-from-each-cdu-inbound-completion-status, what-are-the-preconditions-and-execution-mechanism-for-trade-event-triggered-cashflow-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Trade event trigger cashflow STP.md"]
---
# Trade-Event-Triggered Cashflow STP

Trade-event-triggered cashflow STP is the observed progression in which a CDU confirmation event changes `Trade_State` after a cashflow has met an NSTP condition, enabling the cashflow to reach STP.

## Source-Supported Sequence

The documented scenarios follow this order:

1. SI is entered and verified in Settlement Exceptions.
2. The cashflow meets the “Trade/Cash not affirmed” NSTP rule.
3. CDU produces an event with a qualifying `Confirmation_Message_Inbound_Status`.
4. `Trade_State` changes.
5. The cashflow is reported to trigger STP.

The directly evidenced statuses are:

- `Inbound Completed - Match Outside CDU`
- `Inbound Completed - Inbound Not Required`

`Inbound Completed - Match Completed` is asserted to change `Trade_State`, but has no worked STP example in the source.

## NSTP Condition

```text
Trade_State != "AFFIRMED" && Trade_State != "CONFIRMED" && Cashflow__Cashflow_Affirmation_Status != "Affirmed"
```

This predicate is a documented pre-event condition in two test cases. It should not be read as a complete STP eligibility specification.

## Scope and Limitations

The source establishes scenario-specific validation for BCS cashflows and CDU events. It does not establish:

- the destination state produced by each qualifying status;
- whether SI entry, SI verification, or both are mandatory prerequisites;
- whether event receipt directly executes STP or enables a later process;
- behavior for duplicate, delayed, conflicting, or non-qualifying events.

See [[which-trade-state-results-from-each-cdu-inbound-completion-status]] for the missing state mapping and [[what-are-the-preconditions-and-execution-mechanism-for-trade-event-triggered-cashflow-stp]] for the unresolved eligibility and execution model.