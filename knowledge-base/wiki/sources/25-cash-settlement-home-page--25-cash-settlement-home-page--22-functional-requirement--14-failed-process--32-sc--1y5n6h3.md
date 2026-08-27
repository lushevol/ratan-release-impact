---
type: source
title: Scheduled Failed Job Manual Fail
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-status, scheduled-job, manual-operation, cn-settlement]
related: [scheduled-failed-cashflow-job, manual-cashflow-failure, failed-cashflow-status-eligibility, currency-specific-failed-cutoff, aspire, what-is-the-authoritative-failed-cashflow-transition-contract, what-is-the-post-failed-cashflow-processing-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Scheduled Failed Job Manual Fail.md"]
---
# Scheduled Failed Job Manual Fail

This functional requirement fragment defines scheduled and manual paths for moving selected cashflows to `FAILED` status. It distinguishes an initial CN Day 1 operating model from a longer-term currency-specific model, but leaves timing, configuration ownership, and post-failure processing incomplete.

## Scheduled Failed Job

CN Day 1 requires a daily job, including weekends and holidays, at a fixed time before Razor accounting EOD. The exact time is marked TBC.

The longer-term strategy assigns [[ratan]] responsibility for moving cashflows to `FAILED` at different times by currency. Settlement Accounting generation must align with Aspire, which generates trade accounting at one time across currencies.

## Scheduled Eligibility

Cashflows are in scope only when their value date is the current system date. The source states that the failed cutoff must have passed for the currency, but also says that this rule does not need to run for CN Day 1.

| Cashflow Status | Can move to Failed? |
| --- | --- |
| PROJECTED | Y |
| QUEUED | Y |
| WAITING | Y |
| READY | Y |
| ONHOLD | Y |
| CANCELLED | N |
| NETTED | N |
| SPLIT | N |
| DEAD | N |
| SUPPRESSED | N |
| PAYMENT SUPPRESSED | N |
| RELEASED | N |
| SETTLED | N |
| NOSTRO MATCHED | N |

## `FAILED` Cutoff Static

For CN Day 1, the cutoff is a fixed time for an SCB Legal entity across all currencies.

The proposed long-term static data is:

| Attributes | Value |
| --- | --- |
| Currency | CNY/CNO/CNH |
| Time | 10:00 am |
| Time Zone | GMT |
| Entity? | |

The blank `Entity?` value does not establish whether the long-term cutoff is keyed by currency only, by legal entity and currency, or by an optional entity dimension.

## Manual Failed

FMO can right-click a cashflow in the Cashflow Blotter and select `Manual Fail`. The same eligibility matrix applies. For an eligible cashflow, its status moves to `FAILED` immediately after the user action.

The requirement does not specify permissions, maker-checker controls, audit data, a reason code, confirmation behaviour, or rejection feedback for this action.

## Unspecified Post-`FAILED` Processing

The source ends at the heading “Post 'FAILED' process” without defining any downstream behaviour. It does not establish recovery or retry rules, accounting consequences, notifications, reconciliation, event publication, or whether `FAILED` is terminal.

See [[scheduled-failed-cashflow-job]], [[manual-cashflow-failure]], and [[failed-cashflow-status-eligibility]].