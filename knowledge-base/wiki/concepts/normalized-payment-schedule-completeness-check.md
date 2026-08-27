---
type: concept
title: Normalized Payment Schedule Completeness Check
created: 2026-08-24
updated: 2026-08-24
tags: [payment-schedule, completeness, aggregation, cashflow, netting]
related: [normalized-payment-schedule, netting-service, product-agnostic-cashflow-aggregation, cashflow, what-is-the-authoritative-auto-aggregation-completeness-and-idempotency-contract, what-is-the-canonical-fee-and-asgross-exclusion-semantics-for-auto-aggregation, what-causes-duplicate-cashflow-ids-and-major-versions-in-uber-trades]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# Normalized Payment Schedule Completeness Check

A normalized payment schedule completeness check is the proposed comparison of expected payment legs from `NormalizedPaymentSchedule` with received eligible cashflows before automatic aggregation.

## Proposed Calculation

- `expected_num` is the count of schedule entries matching the candidate cashflow’s currency and `paymentDate`, excluding Fee entries.
- `cf_count` is the count of cashflows for the same `tradeId`, currency, and payment date, excluding `"AsGross"` records.
- If `expected_num > cf_count`, the source says the cashflow should be updated to “pending another leg.”
- Otherwise, the source says the cashflows should be auto-aggregated.

## Unresolved Correctness Conditions

The proposed comparison accepts `cf_count == expected_num` and `cf_count > expected_num` alike. An over-count may instead indicate duplicate delivery, a revision, or an incorrect grouping key. Count parity also cannot establish correspondence between individual schedule entries and cashflows.

The predicate must clarify whether Fee and `AsGross` exclusions apply consistently on both expected and received sides, and it must define idempotency, locking or concurrency behavior, status ownership, recovery, and reconciliation.