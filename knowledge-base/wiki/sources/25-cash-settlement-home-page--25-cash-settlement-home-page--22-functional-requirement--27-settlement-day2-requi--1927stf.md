---
type: source
title: Group Blotter Enhancement
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6472976"
venue: "Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, group-blotter, manual-stp, functional-requirement]
related: [cash-settlement-home-page, settlement-day-2, bulk-manual-stp, group-blotter-bulk-stp-eligibility, group-blotter-pagination, is-pending-pre-group-or-pending-prev-group-the-authoritative-bulk-stp-status, why-does-pending-pre-group-use-case-require-bulk-manual-stp-error, what-is-the-partial-success-contract-for-bulk-manual-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# Group Blotter Enhancement

This functional requirement proposes extending Group Blotter from single-record Manual STP to controlled multi-selection processing. It also specifies higher-volume record loading behavior modeled on Cashflow Blotter.

The enhancement is a requirement proposal, not evidence of implementation, testing, approval, or production deployment.

## Background

For exceptional cases, an operator can select a cashflow in Group Blotter and use Manual STP to push it to Cashflow Blotter. The existing action supports one record at a time, which is inefficient when multiple cashflows require manual handling.

The linked delivery record is Azure DevOps work item 6472976:

<https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6472976>

## Required Behavior

### Group Blotter loading

- Display 1,000 cashflows by default.
- Provide options to load the next 1,000 or 5,000 cashflows.
- Allow the user to change page size to 5,000.
- Use Cashflow Blotter as the behavioral reference.

The requirement does not specify whether loading is incremental or page-based, nor does it define ordering, filtering, maximum retrieval volume, or performance criteria. See [[group-blotter-pagination]].

### Bulk Manual STP

For multiple selected cashflows, Group Blotter should expose Manual STP in the context menu only when all selected cashflows' group statuses are `PENDING_TRADE_VALIDATION` or `PENDING_PRE_GROUP`.

Where selected cashflows have other statuses, the system should display an error.

The confirmation warning must begin with:

> Please only perform bulk manual STP when informed by support team  
> [count] cashflow selected

The warning should also include an existing warning message represented only by screenshots in the source. The complete canonical text, buttons, cancellation behavior, authorization model, and audit requirements are not available in accessible text.

## Existing and Proposed Eligibility

The source distinguishes the current single-record behavior from the proposed bulk behavior:

- Current single-record Manual STP: available when the cashflow status in Group Blotter is `PENDING` or `ERROR`.
- Proposed multi-record Manual STP: based on selected cashflows' **group statuses**, using `PENDING_TRADE_VALIDATION` or `PENDING_PRE_GROUP`.

The source does not establish whether the single-record rule remains unchanged, whether `ERROR` remains eligible, or whether both cashflow-level and group-level validation are required. See [[bulk-manual-stp]] and [[group-blotter-bulk-stp-eligibility]].

## Expected Successful Outcome

For successful eligible bulk processing:

- Selected cashflows transition from `PENDING` to `END`.
- Associated groups transition to `COMPLETED`.
- `bookingSystemEvent` is set to `ManualDeliver`.

The source includes all-processed and all-failed screenshots, but it does not define partial-success behavior, retry handling, idempotency, terminal states, audit records, or operator feedback. See [[what-is-the-partial-success-contract-for-bulk-manual-stp]].

## Open Question Record

| Raise Date | Description | Comment | Status |
| --- | --- | --- | --- |
| 2025-10-30 | Cashflows in `PENDING` status may create a risk of duplicate payment processing when manually STP-ed. | On 2025-11-04, the source says this was confirmed with Dinesh and bulk Manual STP was constrained to group statuses `PENDING_TRADE_VALIDATION` or `PENDING_PREV_GROUP`. | Closed |

The closed record uses `PENDING_PREV_GROUP`, while the requirement details and use cases use `PENDING_PRE_GROUP`. The authoritative identifier is unresolved. See [[is-pending-pre-group-or-pending-prev-group-the-authoritative-bulk-stp-status]].

## Business Use Cases

| Case | Function | Scenario | Expected result |
| --- | --- | --- | --- |
| 1 | One group in `PENDING_TRADE_VALIDATION` | Group 1 contains C1, C2, and C3. All are received and in `PENDING_TRADE_VALIDATION`; operations selects all and runs Manual STP. | Before action: C1, C2, and C3 are `PENDING`; G1 is `PENDING_TRADE_VALIDATION`. After action: C1, C2, and C3 are `END`; the group is `COMPLETED`; `bookingSystemEvent = 'ManualDeliver'`. |
| 2 | Two groups in `PENDING_PRE_GROUP` context | Group 1 has C1 received in `PENDING` and C2 not received. Group 2 has the same trade ID, contains C3 and C4, and is in `PENDING_PRE_GROUP`; operations selects C3 and C4 and runs Manual STP. | Before action: C1 and Group 1 are `PENDING`; C3 and C4 are `PENDING`; Group 2 is `PENDING_PRE_GROUP`. Expected result: system popup error. |
| 3 | One group in `PENDING_TRADE_VALIDATION` and another in `PENDING_PRE_GROUP` | Group 1 contains C1 and C2 in `PENDING_TRADE_VALIDATION`. Group 2 contains C3 and C4 in `PENDING_PRE_GROUP`. All are received; operations selects C1, C2, C3, and C4 and runs Manual STP. | Before action: C1–C4 are `PENDING`; group statuses are `PENDING_TRADE_VALIDATION` and `PENDING_PRE_GROUP`. After action: C1–C4 are `END`; groups are `COMPLETED`; `bookingSystemEvent = 'ManualDeliver'`. |

Use case 2 conflicts with the stated eligibility rule because it selects cashflows in `PENDING_PRE_GROUP` but expects an error. The same-trade relationship and incomplete first group may imply an additional constraint, but the requirement does not define one. See [[why-does-pending-pre-group-use-case-require-bulk-manual-stp-error]].

## Scope and Risk

The group-status restriction is intended to prevent duplicate payment processing for generic `PENDING` cashflows. Bulk Manual STP is explicitly framed as an exceptional, support-governed operation rather than routine processing.

This requirement belongs to [[cash-settlement-home-page]] and is located in the [[settlement-day-2]] functional-requirement area.