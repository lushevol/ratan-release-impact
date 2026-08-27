---
type: source
title: Cashflow Status Sync with FMSGW Deletion
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6090337"
venue: "Functional Requirement — Settlement Day2 Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, settlement, swift, fmsgw, ratan, functional-requirement]
related: [fmsgw, fmsgw-deletion-driven-cashflow-settlement, what-is-the-authoritative-cov-swift-status-display-rule, what-is-the-post-settlement-fmsgw-status-correction-and-idempotency-contract, what-accounting-events-are-suppressed-by-using-settled-instead-of-swift-suppressed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow status sync with FMSGW deletion.md"]
---
# Cashflow Status Sync with FMSGW Deletion

This functional requirement defines a scoped [[entities/ratan|Ratan]] status-synchronization rule for SWIFT messages sent to [[fmsgw|FMSGW]]. When downstream deletion or release statuses are received, an interim `RELEASED` cashflow must move to `SETTLED`.

The requirement is tracked in [ADO 6090337](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6090337).

## Required Cashflow Transition

Ratan must set the related cashflow to `SETTLED` when a received SWIFT status is in this allowlist:

- `FMSGW Deleted`
- `FMSRE Deleted`
- `Manual Delete`
- `Released by SCPAY`
- `Released by AMH`

The rule applies after Ratan has generated and sent SWIFT. The requirement specifically selects `SETTLED`, rather than `SWIFT_SUPPRESSED`, because `SWIFT_SUPPRESSED` may trigger duplicate accounting. This decision is limited to the FMSGW deletion-related flow; it does not define the use of `SWIFT_SUPPRESSED` in other workflows.

## MT103/202 COV Rule

For an MT103/202 COV pair, Ratan must transition the cashflow to `SETTLED` only when both component messages have a status in the allowed terminal-status set. The component statuses may differ.

Examples stated by the requirement:

- MT103: `FMSGW Deleted`; MT202 COV: `Manual Delete` → `SETTLED`
- MT103: `Released by AMH`; MT202 COV: `Manual Delete` → `SETTLED`
- MT103: `Released by AMH`; MT202 COV: `Released by SCPAY` → `SETTLED`

If one component receives a deletion response and the other receives an error response, the cashflow remains `RELEASED`.

`Check in FMSGW` is described as the SWIFT-status display used when the two COV message values differ. It is not, by itself, a settlement blocker: settlement depends on both message statuses being members of the allowlist.

## Open Questions Recorded in the Requirement

| | Raised Date | Description | Comment |
| --- | --- | --- | --- |
| 1 | 2025-10-09 | Currently these FMSGW deletion status are not involved in cashflow dashboard filter, what's the business impact without these function? | 2025-10-10 'RELEASED' is a interim status, so trying to move it to a final status to avoid user unnecessary attention |
| 2 | 2025-10-09 | Do we have to set the cashflow status to SWIFT_SUPPRESSED? this may trigger duplicate accounting Should these be moved to Settled status which is in sync with manual settle action | 2025-10-16 confirmed in teams group chat and OK to use settled instead of SWIFT_SUPPRESSED ![image-2025-10-16_16-52-53.png](attachments/image-2025-10-16_16-52-53.png) |
| 3 | 2025-10-22 | MT103/202Cov received deleted response but with different delete status for each message, what's the expectation? | ![image-2025-10-22_10-59-0.png](attachments/image-2025-10-22_10-59-0.png) |

## Business Use Cases

| Scenario | Test Steps | Expected result |
| --- | --- | --- |
| Mt103/MT202/MT210/MT202Flip/MT192/MT292 /MT604/MT605/MT692 | 1. cashflow processed in Ratan and swift generated 2. Swift sent to FMSGW and got deleted response | 1. Cashflow moved to Released status 2. Cashflow moved to Settled status and swift status reflect the downstream response |
| MT103/202Cov | 1. cashflow processed in Ratan and swift generated 2. Swift sent to FMSGW and both msg got deleted response | 1. Cashflow moved to Released status 2. Cashflow moved to Settled status and swift status show as Check in FMSGW |
| MT103/202Cov | 1. cashflow processed in Ratan and swift generated 2. Swift sent to FMSGW and one msg got deleted response, the other got error response | 1. Cashflow moved to Released status 2. Cashflow still in Released status and swift status show as Check in FMSGW |
| MT103/202Cov | 1. cashflow processed in Ratan and swift generated 2. Swift sent to FMSGW and one msg got deleted response, the other Released by SCPay | 1. Cashflow moved to Released status 2. Cashflow moved to Settled status and swift status show as Check in FMSGW |

## Unspecified Operational Behavior

The source does not define processing for absent, delayed, duplicated, corrected, or unrecognized downstream responses. It also does not provide an event schema, retry policy, settlement reversibility rule, or accounting-event contract. These gaps are tracked in [[what-is-the-post-settlement-fmsgw-status-correction-and-idempotency-contract]] and [[what-accounting-events-are-suppressed-by-using-settled-instead-of-swift-suppressed]].