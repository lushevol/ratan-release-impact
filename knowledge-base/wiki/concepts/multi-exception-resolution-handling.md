---
type: concept
title: Multi-Exception Resolution Handling
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, exceptions, maker, checker, resolution]
related: [high-value-exception-dependency, what-is-the-authoritative-auto-versus-manual-exception-resolution-attribute, what-exactly-closes-when-a-checker-resolves-a-multi-exception-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/High Value Exception Scenario Analysis.md"]
---
# Multi-Exception Resolution Handling

Multi-exception resolution handling governs how a cashflow's co-existing exceptions change after one exception is resolved. In the documented High Value scenarios, the outcome depends both on the resolution origin and on whether another Checker-relevant exception remains.

## Resolution Rules

| Resolution mode | Documented effect |
| --- | --- |
| Automatic resolution | Remove High Value automatically when no other qualifying Checker exception remains; otherwise retain High Value for Checker. |
| Manual Maker resolution | Retain High Value as visible to Checker. |
| Manual Checker resolution | “All exception closed as multi exception handling.” |

Examples show that automatically resolving Pending Affirmation or Missing Nostro permits STP where no other relevant exception remains. Where Missing Vostro or Net Cashflow remains, High Value also remains visible to Checker.

## Open Implementation Questions

The source does not identify the field, event, or audit attribute that distinguishes automatic from manual resolution. It also does not define whether Checker resolution closes only High Value and the resolved exception, every co-existing exception, or a narrower eligible set. These questions are tracked in [[what-is-the-authoritative-auto-versus-manual-exception-resolution-attribute]] and [[what-exactly-closes-when-a-checker-resolves-a-multi-exception-cashflow]].