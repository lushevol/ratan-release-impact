---
type: query
title: Does created_at Filtering Correctly Implement the SSI Last-Used-Date Window?
created: 2026-08-24
updated: 2026-08-24
tags: [ssi, dormancy, date-semantics, data-quality, sql]
related: [dormant-ssi-processing, cash-settlement-query-cn-cashflow-data, ratanone-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md"]
---
# Does created_at Filtering Correctly Implement the SSI Last-Used-Date Window?

## Question

Does filtering source rows by `created_at` while calculating last use as `MAX(payment_date)` correctly implement the intended rule for SSIs unused for 24 months?

## Evidence

The retrospective report restricts all four source CTEs to rows created from `2024-07-18` inclusive through `2026-07-18` exclusive. It then derives each SSI's last-used value from the maximum payment date.

This can include a cashflow created during the window but paid outside it, while excluding a cashflow paid during the window that was created outside it.

## Why it matters

If dormancy is defined by payment-date use, the source-selection window may omit relevant evidence or include dates outside the intended two-year period. The hard-coded interval also does not define how a rolling cutoff is calculated for subsequent executions.

## Needed decision

Confirm the authoritative effective date for SSI use, the rolling-window calculation, late-arriving or amended cashflow treatment, and whether all historical sources apply the same date semantics.