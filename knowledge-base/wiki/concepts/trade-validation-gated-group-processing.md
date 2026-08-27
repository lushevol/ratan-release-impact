---
type: concept
title: Trade-Validation-Gated Group Processing
tags: [trade-validation, group-blotter, manual-stp, cashflow-lifecycle]
related: [bulk-manual-stp-for-group-blotter, group-major-version-completion-rules, when-does-is-trade-validated-propagate-bulk-manual-stp-to-related-group-versions, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2025-changes--38-bulk--4160up]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md"]
---
# Trade-Validation-Gated Group Processing

The `is_trade_validated` flag appears to affect expected downstream processing of related group-major-version fixtures during bulk manual STP tests.

## Test Pattern

Cases 4.1 through 4.3 select `T1_G2_V2`, initially in `PENDING_TRADE_VALIDATION`, and vary the condition of `T1_G3_V3`:

- With `T1_G3_V3` in `PENDING_TRADE_VALIDATION` and `is_trade_validated=false`, only `T1_G2_V2` is expected to complete.
- With `T1_G3_V3` in `PENDING_TRADE_VALIDATION` and `is_trade_validated=true`, its child `C1` is expected to become `END`, while its parent remains pending.
- With `T1_G3_V3` in `PENDING_PRE_GROUP` and `is_trade_validated=true`, both parent records are expected to become `COMPLETED`.

## Qualification

The matrix does not identify the relationship between `T1_G2_V2` and `T1_G3_V3`, nor does it define the complete validation rule. The scenarios support a test expectation of status- and validation-dependent propagation, but not a general processing specification. See [[when-does-is-trade-validated-propagate-bulk-manual-stp-to-related-group-versions]].