---
type: source
title: Actions on Hold
authors: []
year: 2025
url: ""
venue: ""
tags: [cash-settlement, cashflow, hold, reinstatement, functional-requirement]
related: [cash-settlement-home-page, held-cashflow-reinstatement, release-cutoff-risk-for-unhold, what-is-the-reinstate-exception-lifecycle-for-held-cashflows, what-are-the-authorization-controls-for-send-to-waiting, does-send-to-waiting-scenario-four-require-swift-or-cashflow-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Actions on Hold.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Actions on Hold

This functional requirement defines actions available for a cashflow in `HOLD` status in the [[cash-settlement-home-page]]. It introduces **Send to WAITING** as a controlled alternative to `Unhold`.

`Unhold` restores the cashflow to its status before `HOLD`—`QUEUED`, `WAITING`, or `READY`. Restoring a cashflow to `READY` can allow the release-cutoff job to release it downstream before an operator can amend SSI or suppress the cashflow.

**Send to WAITING** returns the cashflow to the main flow in `WAITING` status, creates a `Reinstate` exception, and records `Reinstate` in action history. It creates an operational checkpoint for [[adhoc-ssi-workflow]], suppression, or netting before release.

## Specified hold-status actions

|  |  | User profile | Comment |
| --- | --- | --- | --- |
| Unhold (send to previous status) | revert back to the previous status before HOLD |  |  |
| **Send to WAITING** | **resend the cashflow back to main flow and will be hold in WAITING status with "<u>*Reinstate*</u>" exception** | ** ** |  |

## Access and UI requirements

- The user profile for both actions is the same as for the `HOLD` action.
- A user who performed the hold cannot select `Unhold`, but can select `Send to WAITING`.
- `Unhold` validates the cashflow amount limit; `Send to WAITING` follows reinstatement behavior and does not require amount-limit validation.
- The `Unhold` menu tooltip and popup information icon must state: `Unhold action will send cashflow to previous status(QUEUED/WAITING/READY)`.
- The `Unhold` popup must display: `Warning: Unhold action can auto release payment to downstream`.
- The `Send to WAITING` confirmation popup requires a comment.
- The action-history label for `Send to WAITING` is `Reinstate`.

## Acceptance scenarios

|  | AC-No | Function | Scenario | Expected Result |
| --- | --- | --- | --- | --- |
| 1 |  | Unhold action | 1. book cashflow STP to READY status, current time < release cut off 2. user hold the cashflow 3. user unhold the cashflow 4. trigger the release cutoff job | 1. cashflow state ='READY', cashflow sub state type = 'NA' 2. cashflow state ='HOLD' 3. cashflow state ='READY' 4. cashflow state = RELEASED/SETTLED |
| 2 |  | Send to WAITING + Adhoc SSI | 1. book cashflow STP to READY status, current time < release cut off 2. user hold the cashflow 3. user select "Send to WAITING" action 4. user perform adhoc SSI and release the cashflow | 1. cashflow state ='READY', cashflow sub state type = 'NA' 2. cashflow state ='HOLD' 3. cashflow state ='WAITING' with "Reinstate" exception 4. cashflow SSI updated and cashflow state = RELEASED/SETTLED |
| 3 |  | Send to WAITING + cashflow suppress | 1. book cashflow STP to READY status, current time < release cut off 2. user hold the cashflow 3. user select "Send to WAITING" action 4. user perform cashflow suppress | 1. cashflow state ='READY', cashflow sub state type = 'NA' 2. cashflow state ='HOLD' 3. cashflow state ='WAITING' with "Reinstate" exception 4. cashflow state = CASHFLOW_SUPPRESSED |
| 4 |  | Send to WAITING + swift suppress | 1. book cashflow STP to READY status, current time < release cut off 2. user hold the cashflow 3. user select "Send to WAITING" action 4. user perform cashflow suppress | 1. cashflow state ='READY', cashflow sub state type = 'NA' 2. cashflow state ='HOLD' 3. cashflow state ='WAITING' with "Reinstate" exception 4. cashflow state = SWIFT_SUPPRESSED |
| 5 |  | Send to WAITING + Net | 1. book cashflow STP to READY status, current time < release cut off 2. user hold the cashflow 3. user select "Send to WAITING" action 4. user perform net | 1. cashflow state ='READY', cashflow sub state type = 'NA' 2. cashflow state ='HOLD' 3. cashflow state ='WAITING' with "Reinstate" exception 4. cashflow state = NETTED |

## Open specification points

The source does not define the lifecycle of the `Reinstate` exception, including whether it blocks release, when it is cleared, or how repeated hold/reinstate cycles behave. It also does not identify the technical service or event used to resend a cashflow to the main flow.

Scenario 4 is internally inconsistent: its function and expected outcome describe SWIFT suppression, while its final scenario step says the user performs cashflow suppression. See [[does-send-to-waiting-scenario-four-require-swift-or-cashflow-suppression]].