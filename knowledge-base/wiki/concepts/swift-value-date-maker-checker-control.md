---
type: concept
title: Swift Value Date Maker/Checker Control
created: 2026-08-23
updated: 2026-08-23
tags: [swift-value-date, maker-checker, dual-control, cashflow, settlement-instruction]
related: [failed-cashflow-reinstatement, payment-date-override, suppression-maker-checker-workflow, cashflow-blotter-exception-panel-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Re-Process - New Swift Value Date.md"]
---
# Swift Value Date Maker/Checker Control

Swift Value Date Maker/Checker control is the dual-blind selection process used to determine `Settlement_Instruction.Value_Date` while resolving a Cashflow Re-Instate exception.

## Selection options

Both the Maker and Checker independently choose one of two options:

1. Select the current cashflow Value Date, represented by `Cashflow.Payment_Date`. The system copies this value to `Settlement_Instruction.Value_Date`.
2. Select a new date as the Swift Value Date.

The requirement describes the second option as allowing the user to select any date. It does not specify business-day, currency-calendar, cutoff, past-date, payment-state, or settlement-instruction validation.

## Comparison and rejection

After the Maker submits, the exception moves to the Checker’s page. The Checker independently selects a date and submits it. The system compares the Maker’s submitted value with the Checker’s value at Checker submission.

When the values differ, the system warns the Checker. If the Checker considers the Checker-selected value correct, the Checker can reject the Maker’s input. The exception then returns to the Maker’s page.

## Control boundary

This source establishes a mismatch warning and a rejection route, but not a complete approval protocol. It does not state:

- what happens when the values match;
- whether a Checker may approve a differing value;
- whether rejection resets or preserves the Maker’s selection;
- how both selections are recorded for audit;
- which event or status resumes cashflow processing.

This is a distinct use of Maker/Checker control from the suppression workflow in [[suppression-maker-checker-workflow]]. Suppression-specific statuses, rollback behavior, and approval semantics must not be inferred here.

The date-copy behavior is related to [[payment-date-override]], but this requirement supports only this scoped Cashflow Re-Instate use case and does not establish a universal payment-date authority model.