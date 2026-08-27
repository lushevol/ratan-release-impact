---
type: query
title: What Validations Restrict Swift Value Date Selection During Failed Cashflow Reprocessing?
created: 2026-08-23
updated: 2026-08-23
tags: [swift-value-date, date-validation, cashflow, settlement, open-question]
related: [failed-cashflow-reinstatement, swift-value-date-maker-checker-control, payment-date-override, cashflow-netting-and-un-netting-state-transitions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Re-Process - New Swift Value Date.md"]
---
# What Validations Restrict Swift Value Date Selection During Failed Cashflow Reprocessing?

## Question

What business and technical validations constrain a user-selected `Settlement_Instruction.Value_Date` during failed-cashflow reinstatement?

## Known evidence

The requirement allows the Maker and Checker to select either:

- the existing `Cashflow.Payment_Date`, copied to `Settlement_Instruction.Value_Date`; or
- a new date, described as any date.

No explicit restrictions are provided.

## Validation areas to confirm

The implementation or authoritative requirements should clarify whether the selected date is checked against:

- currency and market business-day calendars;
- holidays and settlement calendars;
- payment-generation and release cutoffs;
- dates earlier than the current processing date;
- the original cashflow payment date;
- settlement-instruction validity;
- payment status or already-generated instructions;
- netting cycles, netting groups, and cashflow maturity;
- duplicate reinstatement or repeated failure history.

## Field authority

The source does not establish whether `Settlement_Instruction.Value_Date` becomes the authoritative payment date or whether `Cashflow.Payment_Date` remains unchanged and authoritative elsewhere. It only specifies a one-way copy when the existing cashflow Value Date is selected.

This question should be resolved before treating the workflow as a general [[payment-date-override]] model.