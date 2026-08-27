---
type: source
title: High Value Exception Scenario Analysis
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, exceptions, high-value, multi-exception, stp]
related: [high-value-exception-dependency, multi-exception-resolution-handling, does-a-maker-only-exception-trigger-or-only-retain-high-value-exception, what-is-the-authoritative-auto-versus-manual-exception-resolution-attribute, what-exactly-closes-when-a-checker-resolves-a-multi-exception-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/High Value Exception Scenario Analysis.md"]
---
# High Value Exception Scenario Analysis

## Summary

This functional requirement defines High Value as a dependent exception in a cashflow multi-exception workflow. High Value must not be triggered when it is the only exception; in that case, the cashflow should proceed through STP. Its retention and automatic removal depend on companion exceptions, whether they still require Checker action, and whether they were resolved automatically or manually.

The source specifies that automatic resolution of the relevant companion exception can remove High Value and allow STP. A Maker's manual resolution leaves High Value visible to Checker, while a Checker's manual resolution is stated to close all exceptions under multi-exception handling. The exact closure scope is not defined.

## Requirement

- High Value exception must be triggered only if there are exceptions which require a manual action by Checker
- If there are no other exceptions, then High Value exception should not be triggered and STPd
- If there was an exception previously which got auto resolved (example: Confirmation Match resolving 'Pending Affirmation' exception) system must auto remove the High Value Exception so that the cashflow can STP
- For pending affirmation exception, If manually affirmed, then high value exception still visible to checker; if auto affirmed, then high value exception will not be visible to checker.
- High value exception should be triggered as long as there is at least one other exception that requires checker action

## When Exception Generated

| # | Scenario | High Value Exception |
| --- | --- | --- |
| 1 | High Value Exception Only | Not Triggered |
| 2 | High Value Exception + Checker exception | Triggered |
| 3 | High Value Exception + Maker only Exception | Triggered |

## When Any Exception Is Resolved

| # | High Value + Other Exception Scenario | Expected System Behavior for High Value Exception | Example |
| --- | --- | --- | --- |
| 1 | Maker only Exception | If manually resolved, then still visible to checker; If auto resolved, If no other checker exception (other than high value exception), then auto resolve. Else Still visible to checker. | Pending Affirmation + High Value when manual affirm, checker can see High Value when auto affirm, checker can see cashflow STPed Pending Affirmation + Missing Vostro + High Value when manual affirm, checker can see Missing Vostro + High Value when auto affirm, checker can see Missing Vostro + High Value |
| 2 | Exception Auto Resolved | If no other checker exception (other than high value exception) /pending affirmation exception, then auto resolve. Else Still visible to checker. | Missing Nostro + Net Cashflow + High Value when Missing Nostro auto resolved, check can see Net Cashflow + High Value Missing Nostro + High Value when Missing Nostro auto resolved, checker can see cashflow STPed |
| 3 | Exception Manually Resolved | If maker manually fix exception Still visible to checker If checker manually fix exception All exception closed as multi exception handling | |

## Technical Parameters

| # | Business term | Tech Parameter | Sample Value |
| --- | --- | --- | --- |
| 1 | Checker exception | operationLevel in (CHECKER_ONLY, MAKER_CHECKER) | CHECKER_ONLY/MAKER_ONLY/MAKER_CHECKER |
| 2 | Exception Auto/Manually resolved | TBD | |
| | | | |

## Interpretation Boundaries

The examples involving Pending Affirmation, Missing Vostro, Missing Nostro, and Net Cashflow illustrate the requirement but do not define an exhaustive exception taxonomy.

The source conflicts internally: it says High Value is triggered only with an exception requiring Checker action, while its generation table also states that High Value is triggered with a Maker-only exception. The intended distinction between generation, Checker visibility, and retention remains unresolved in [[does-a-maker-only-exception-trigger-or-only-retain-high-value-exception]].

The technical parameter for distinguishing automatic from manual resolution is explicitly TBD. See [[what-is-the-authoritative-auto-versus-manual-exception-resolution-attribute]]. The meaning of “All exception closed as multi exception handling” is tracked in [[what-exactly-closes-when-a-checker-resolves-a-multi-exception-cashflow]].