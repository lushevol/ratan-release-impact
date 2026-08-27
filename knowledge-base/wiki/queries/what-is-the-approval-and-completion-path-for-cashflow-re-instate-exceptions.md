---
type: query
title: What Is the Approval and Completion Path for Cashflow Re-Instate Exceptions?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, reinstatement, maker-checker, exception, open-question]
related: [failed-cashflow-reinstatement, swift-value-date-maker-checker-control, cashflow-lifecycle-supersession-and-audit-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Re-Process - New Swift Value Date.md"]
---
# What Is the Approval and Completion Path for Cashflow Re-Instate Exceptions?

## Question

What event, status transition, and downstream processing occur after the Maker and Checker complete Swift Value Date selection for a Cashflow Re-Instate exception?

## Known evidence

The source defines the following partial path:

- A `FAILED` cashflow is reinstated to `QUEUED`.
- Netting client Check and Exception Check run.
- Exception Check creates a Cashflow Re-Instate exception in `Pending Operator`, initially assigned to the Maker.
- The Maker and Checker independently select `Settlement_Instruction.Value_Date`.
- A mismatch produces a Checker warning.
- The Checker may reject the Maker’s input and return the exception to the Maker.

## Missing completion rules

The requirement does not state:

- whether matching values automatically complete the exception;
- whether the Checker explicitly approves the selection;
- whether a differing value can be accepted;
- which status follows approval;
- which event resumes reprocessing;
- whether the cashflow returns to a queue, proceeds to payment generation, or undergoes another check;
- how repeated failures or reinstatement attempts are handled.

## Why this matters

Without the completion contract, reinstatement can be described only as a controlled re-entry into validation. It cannot be treated as evidence of final settlement or SWIFT message generation.

## Investigation targets

The authoritative answer should be sought in the Cashflow Blotter exception state model, the reinstatement workflow implementation, audit-event definitions, and downstream payment-processing requirements.