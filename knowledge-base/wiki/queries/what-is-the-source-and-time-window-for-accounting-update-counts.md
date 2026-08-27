---
type: query
title: What Is the Source and Time Window for AccountingUpdate Counts?
tags: [open-question, AccountingUpdate, production-data, provenance, testing]
related: [accounting-update, accounting-update-production-volume-baseline, uber, fxu, ratanone, uber-scbml-performance-regression-testing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan/Production Existing Data Testing Cases.md"]
---
# What Is the Source and Time Window for AccountingUpdate Counts?

## Question

What query, environment, extraction date, measurement period, counting unit, and business scope produced the `AccountingUpdate` counts in the production testing inventory?

## Why this matters

The counts are being considered as a [[accounting-update-production-volume-baseline]] for production-like testing. Without provenance, they cannot be converted into rates or used to define representative test volumes, latency targets, failure rates, or go-live acceptance thresholds.

The parent path references both [[uber]] and [[fxu]], but the source does not identify how records are allocated between them. It is also unclear whether the categories are mutually exclusive or whether they represent multiple updates for the same [[cashflow]].

## Evidence currently available

The source provides category-level counts, including high-volume values for `CashflowStamped`, `New`, `Materialize`, `Net`, `Settle`, `GenerateSwift`, `Suppress`, and `Release`. It also includes rare recovery or manual categories such as `ResendToRazor`, `ManualAffirmed`, `UnSplit`, and `ReGenerateSwift`.

No query text, timestamp, environment identifier, denominator, or test-case mapping is included.

## Resolution criteria

Resolve this question when the team confirms:

1. The producing database query or export.
2. The environment from which the data was collected.
3. The extraction date and covered time window.
4. Whether counts represent rows, events, transitions, messages, or distinct cashflows.
5. Whether category counts overlap.
6. Whether the scope is Uber, FXU, or a combined population.
7. The mapping from each selected category to test cases and acceptance criteria.