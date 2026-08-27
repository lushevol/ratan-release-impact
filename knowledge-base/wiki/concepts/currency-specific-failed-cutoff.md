---
type: concept
title: Currency-Specific Failed Cutoff
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-status, cutoff, currency, static-data]
related: [scheduled-failed-cashflow-job, ratan, razor, aspire, what-is-the-authoritative-failed-cashflow-transition-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Scheduled Failed Job Manual Fail.md"]
---
# Currency-Specific Failed Cutoff

Currency-Specific Failed Cutoff is the proposed long-term timing model for automated movement of cashflows to `FAILED`.

[[ratan]] is expected to process cashflows at different times for each currency. The process must be aligned with settlement accounting and with [[aspire]], which generates trade accounting at one common time across currencies.

## Proposed Static Data

| Attributes | Value |
| --- | --- |
| Currency | CNY/CNO/CNH |
| Time | 10:00 am |
| Time Zone | GMT |
| Entity? | |

The requirement does not identify the owner of this static data or define the blank entity attribute.

## Relationship to CN Day 1

The CN Day 1 model instead uses a fixed time for an SCB Legal entity across all currencies, and indicates that failed-cutoff validation need not run. The source does not define the transition between this model and the currency-specific model.

Questions about configuration keying, currency validity, and activation are tracked in [[what-is-the-authoritative-failed-cashflow-transition-contract]].