---
type: source
title: Failed Process
authors: []
year: 0
url: ""
venue: ""
tags: [cash-settlement, cashflow, failed-processing, ratan, stella, swift]
related: [cash-settlement-home-page, ratan, stella, cashflow-status-lifecycle, cashflow-blotter-functional-scope, payment-date-override, failed-cashflow-status, failed-cashflow-reprocessing, reinstated-from-failed-exception, currency-calendar-based-system-date]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process.md"]
---
# Failed Process

## Summary

This functional requirement describes the handling of cashflows that are not settled before their due date, cutoff, or required processing time. The settlement platform moves these cashflows to `FAILED`, after which Settlement Ops give them additional attention through a separate failed re-processing flow.

The document identifies two entry paths into `FAILED`:

1. A scheduled job applies predefined rules.
2. FM Ops manually move a cashflow to `FAILED` from the Cashflow Blotter, subject to Maker/Checker control.

A `FAILED` cashflow cannot receive further direct Ratan actions, including ordinary exception handling. The only stated Ratan action is `Re-Instate`. New cashflow events from Stella may overwrite a failed cashflow, although the document does not define event precedence, field-level behavior, or versioning.

## Reinstatement and Swift Value Date

Reinstatement creates the dedicated `Re-Instated from Failed` exception. This exception is included in multi-exception handling and is grouped with the `Back value date` exception because both update `Swift Value Date`.

FMO Ops must manually update `Swift Value Date`, which is used for Swift message generation. The permitted choices are:

- Current System Date, defined as the latest business day calculated using the currency calendar.
- The current cashflow value date.
- A manually selected new date.

The source examples are reproduced below.

| Currency | Cashflow Value Date | FAILED Date | User Action Date | System Date | Comment |
| --- | --- | --- | --- | --- | --- |
| USD | 20th April | 20th April EOD | 21th April(Fri) | 21th April | |
| USD | 21th April | 21th April | 22th April(Sat) | 24th April | 22th - Sat 23th - Sun 24th - next working day |
| CNY | 21th April | 21th April | 23th April(Sat) | 23th April | 22th - Sat 23th - working day |

The source uses `FAIELD` once, but the intended status is `FAILED`.

## Accounting

The document introduces an accounting requirement for `FAILED` cashflows but does not provide the accounting rules or examples. The referenced **Failed Cashflow Accounting** requirement is therefore necessary before accounting entries, reversals, holds, or reinstatement treatment can be documented.

## Referenced Requirements

- [Failed Cashflow Accounting](https://confluence.global.standardchartered.com/display/DSP/Failed+Cashflow+Accounting)
- [Failed Re-Process - New Swift Value Date](https://confluence.global.standardchartered.com/display/DSP/Failed+Re-Process+-+New+Swift+Value+Date)
- [Scheduled Failed Job/Manual Fail](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2730027165)

## Open Points

The source does not specify the scheduled-job eligibility rules, execution time, timezone, or race conditions between scheduled and manual failure. It also does not establish whether `Re-Instate` creates a new cashflow version, how Stella overwrites are correlated, or which currency-calendar service is authoritative.

This source extends the broader [[cashflow-status-lifecycle]] and [[cashflow-lifecycle-supersession-and-audit-history]] models with a recoverable failed state and an explicit operational recovery path.