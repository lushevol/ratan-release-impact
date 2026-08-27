---
type: source
title: "Failed Re-Process — New Swift Value Date"
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflow, failed-process, swift-value-date, maker-checker]
related: [cash-settlement-home-page, fmo-ops, failed-cashflow-reinstatement, swift-value-date-maker-checker-control, payment-date-override, cashflow-blotter-functional-scope, cashflow-netting-and-un-netting-state-transitions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Re-Process - New Swift Value Date.md"]
---
# Failed Re-Process — New Swift Value Date

## Scope

This functional requirement describes how FMO Ops reinstates a cashflow in `FAILED` status and how a Maker/Checker workflow selects a new Swift Value Date for reprocessing.

The Swift Value Date is the `Settlement_Instruction.Value_Date` field. The requirement describes the operational workflow in the Cashflow Blotter, but does not define underlying APIs, persistence structures, final approval statuses, or downstream SWIFT-generation behavior.

## Reinstatement workflow

1. FMO Ops right-clicks a cashflow with status `FAILED` in the Cashflow Blotter.
2. FMO Ops selects **Re Instate**.
3. The cashflow moves to `QUEUED`.
4. The cashflow runs through **Netting client Check** and **Exception Check**.
5. Exception Check generates a dedicated **Cashflow Re-Instate** exception.
6. The exception is initially assigned to the Maker with status `Pending Operator`.

This workflow is also summarized by [[failed-cashflow-reinstatement]].

## Swift Value Date selection

The Maker and Checker independently select the new `Settlement_Instruction.Value_Date` using one of two options:

- **Use the current cashflow Value Date:** select `Cashflow.Payment_Date`. The selected value is copied to `Settlement_Instruction.Value_Date`.
- **Select a new date:** choose any date as the Swift Value Date.

The requirement does not state whether selecting a new Swift Value Date changes `Cashflow.Payment_Date`. It also does not define date validation for holidays, currency calendars, cutoffs, past dates, payment state, or settlement-instruction constraints.

## Maker/Checker workflow

The Maker submits a Swift Value Date selection, after which the exception moves to the Checker’s page. The Checker independently selects and submits a date.

At Checker submission, the system compares the Maker’s and Checker’s inputs. If the values differ, the system displays a warning to the Checker. If the Checker considers the Checker-selected value correct, the Checker can reject the Maker’s input, returning the exception to the Maker’s page.

The requirement does not specify the positive completion path when values match, whether the Checker can explicitly approve a differing value, or which event resumes cashflow processing. See [[swift-value-date-maker-checker-control]].

## Explicit workflow states

| Subject | State or value | Requirement |
|---|---|---|
| Cashflow before reinstatement | `FAILED` | FMO Ops may select **Re Instate** from the Cashflow Blotter. |
| Cashflow after reinstatement | `QUEUED` | The cashflow runs through Netting client Check and Exception Check. |
| Reinstatement exception | `Pending Operator` | A dedicated Cashflow Re-Instate exception is initially assigned to the Maker. |
| Settlement instruction | `Settlement_Instruction.Value_Date` | Receives either the existing `Cashflow.Payment_Date` or a user-selected date. |

## Boundaries and unresolved behavior

The source does not specify:

- the final status after Maker/Checker completion;
- the event that resumes reprocessing after approval;
- whether the original or selected date is authoritative for payment generation;
- retention of Maker and Checker values for audit;
- duplicate or repeated reinstatement handling;
- netting membership, payment-instruction state, or payment-version behavior;
- the exception code, SLA, routing rule, or persistence model.

The requirement should therefore be treated as a scoped operational specification pending confirmation of the authoritative completion and validation rules.

## Related wiki pages

- [[cash-settlement-home-page]]
- [[fmo-ops]]
- [[cashflow-blotter-functional-scope]]
- [[payment-date-override]]
- [[cashflow-netting-and-un-netting-state-transitions]]
- [[suppression-maker-checker-workflow]]