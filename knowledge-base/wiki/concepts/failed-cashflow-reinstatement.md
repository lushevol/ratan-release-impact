---
type: concept
title: Failed Cashflow Reinstatement
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, reinstatement, failed-process, reprocessing, cash-settlement]
related: [cash-settlement-home-page, cashflow-blotter-functional-scope, cashflow-blotter-exception-panel-visibility, fmo-ops, swift-value-date-maker-checker-control, cashflow-netting-and-un-netting-state-transitions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Re-Process - New Swift Value Date.md"]
---
# Failed Cashflow Reinstatement

Failed cashflow reinstatement is the operator-triggered process for returning a cashflow in `FAILED` status to a controlled reprocessing path.

## Defined process

FMO Ops initiates **Re Instate** from the Cashflow Blotter by right-clicking the failed cashflow. The cashflow then moves to `QUEUED` and runs through:

1. **Netting client Check**
2. **Exception Check**

Exception Check generates a dedicated **Cashflow Re-Instate** exception. The exception is initially a Maker exception with status `Pending Operator`. The Maker and Checker then resolve the exception through the [[swift-value-date-maker-checker-control]] workflow.

## Operational meaning

Reinstatement is not specified as direct approval, settlement, or SWIFT transmission. It reopens processing for validation and exception-controlled remediation. The source confirms the `FAILED` → `QUEUED` movement and the invocation of the two checks, but does not define the resulting status after the exception is completed.

## Unspecified lifecycle behavior

The requirement does not define:

- the successful completion event after Maker/Checker review;
- the status reached after approval;
- whether the cashflow retains its original identifiers or netting group;
- payment-instruction, payment-version, or audit-history behavior;
- handling of another failure after reinstatement;
- duplicate or repeated reinstatement attempts.

These gaps distinguish this concept from broader lifecycle material such as [[cashflow-lifecycle-supersession-and-audit-history]] and [[cashflow-netting-and-un-netting-state-transitions]], which should not be assumed to supply the missing rules for this process.