---
type: source
title: Trade Event Trigger Cashflow STP
authors: []
year: 2025
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, stp, nstp, cdu, bcs, ratan, settlement-instructions]
related: [trade-event-triggered-cashflow-stp, which-trade-state-results-from-each-cdu-inbound-completion-status, what-are-the-preconditions-and-execution-mechanism-for-trade-event-triggered-cashflow-stp, bcs-cdu-match-status-confirmation, stp-nstp-and-last-user-message-contract, cash-settlement-home-page, bcs, cdu, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Trade event trigger cashflow STP.md"]
---
# Trade Event Trigger Cashflow STP

This functional-validation document records two BCS cashflow scenarios in which a qualifying CDU confirmation event follows settlement-instruction entry and verification, changes trade state, and is reported to trigger STP.

## Stated CDU Status Rule

The document states that these `Confirmation_Message_Inbound_Status` values trigger a `Trade_State` change:

- `Inbound Completed - Match Completed`
- `Inbound Completed - Inbound Not Required`
- `Inbound Completed - Match Outside CDU`

The document does not specify the destination `Trade_State` for any status.

## NSTP Rule

The tested cashflows first meet the following “Trade/Cash not affirmed” NSTP condition:

```text
Trade_State != "AFFIRMED" && Trade_State != "CONFIRMED" && Cashflow__Cashflow_Affirmation_Status != "Affirmed"
```

## Scenario: Match Outside CDU

For BCS trade `BCS_3297952` and cashflow `6257787319`, the documented procedure is:

1. Locate the trade and cashflow in the Cashflow Blotter for FX & Equity.
2. Input SI in Settlement Exceptions.
3. Verify SI in Settlement Exceptions.
4. Confirm that the cashflow hits the NSTP rule.
5. Produce a CDU event with `Confirmation_Message_Inbound_Status` set to `Inbound Completed - Match Outside CDU`.
6. Verify the persisted event in RATAN.
7. Trigger STP.

The referenced inbound-message fixture is `Dispatched_IBOutsideCDU.json`.

```sql
select * from ratanone.event_record er where row_id in (select body_event_rowkey from ratanone.ratan_minor_version_history rmvh where cashflow_id ='6257787319')
```

## Scenario: Inbound Not Required

For BCS trade `BCS_3719646` and cashflow `6261288851`, the documented procedure is:

1. Locate the trade and cashflow in the Cashflow Blotter for FX & Equity.
2. Input SI in Settlement Exceptions.
3. Verify SI in Settlement Exceptions.
4. Confirm that the cashflow hits the NSTP rule.
5. Produce a CDU event with `Confirmation_Message_Inbound_Status` set to `Inbound Completed - Inbound Not Required`.
6. Verify the persisted event in RATAN.
7. Trigger STP.

The referenced inbound-message fixture is `Dispatched_IBsuppressed.json`.

```sql
select * from ratanone.event_record er where row_id in (select body_event_rowkey from ratanone.ratan_minor_version_history rmvh where cashflow_id ='6261288851')
```

## Observed Integration Chain

The scenarios provide test-level evidence for this chain:

[[bcs]] trade and cashflow → SI entered and verified in [[cash-settlement-home-page]] → qualifying [[cdu]] inbound confirmation status → persisted event verification in [[ratan]] → reported STP outcome.

RATAN persistence is checked by resolving `cashflow_id` through `ratanone.ratan_minor_version_history.body_event_rowkey` and retrieving the corresponding `ratanone.event_record` row.

## Evidence Boundaries

The two end-to-end examples cover only `Inbound Completed - Match Outside CDU` and `Inbound Completed - Inbound Not Required`. Although `Inbound Completed - Match Completed` is listed as trade-state-changing, this source provides no equivalent STP scenario, fixture, or persistence check for it.

The source documents an ordered sequence, but does not establish whether verified SI is a mandatory STP precondition, whether the CDU event directly invokes STP, or whether an asynchronous rule reevaluation performs the transition. It also does not provide the resulting `Trade_State`, event payloads, or duplicate and out-of-order event behavior.