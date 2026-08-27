---
type: entity
title: ratanone_stamping_service
created: 2026-08-24
updated: 2026-08-24
tags: [database-schema, ssi-stamping, bcs, cash-settlement]
related: [bcs, dormant-ssi-processing, what-stamping-states-count-as-ssi-use-for-dormancy, what-is-the-authoritative-meaning-and-design-of-ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md"]
---
# ratanone_stamping_service

`ratanone_stamping_service` is the database schema used by the BCS SSI-use extraction described in the dormant SSI design.

## Relevant tables

- `cashflow_stamping` supplies `cashflow_id`, `payment_date`, `state`, `created_at`, and the join key `id`.
- `stamped_vostro_account` supplies `ssi_id` and joins through `cashflow_stamping_id`.

The BCS daily lookup joins these tables, excludes empty SSI IDs, filters on a requested payment date, and accepts only `STP_STAMPING_SHIPPED` records.

## Dormancy-use interpretation

The design operationally treats a stamping record in `STP_STAMPING_SHIPPED` state as evidence that the linked SSI has been used. This is an extraction rule, not a documented business definition of every valid SSI-use state. Its correctness is tracked in [[what-stamping-states-count-as-ssi-use-for-dormancy]].

A proposed B-tree index on `cashflow_stamping(payment_date)` supports the payment-date lookup, but the source provides no plan analysis or production validation.