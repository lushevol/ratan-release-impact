---
type: query
title: What Is the Approved Withdrawal and Accounting Behavior After Split-Child Release?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, withdrawal, accounting, lifecycle, irs]
related: [cashflow-splitting, ratan-cashflow-lifecycle-state-machine, netting-resultant-cashflow-lifecycle, is-manual-splitting-of-irs-aggregation-resultants-in-day-1-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
---
# What Is the Approved Withdrawal and Accounting Behavior After Split-Child Release?

The source specifies that a withdrawal received after one or more split children are released is held in `WAITING` for manual action. However, it does not provide an approved end-to-end resolution.

For IRS aggregation-resultant scenarios, a proposed approach would generate reversal accounting for a withdrawal manually moved to `SWIFT_SUPPRESSED` or `FAILED`. A subsequent internal design review recorded concerns and recommended disabling the option.

Clarification is needed for:
- Gross versus netting-resultant and IRS aggregation-resultant parents.
- The lifecycle outcome of the withdrawal after manual suppression or failure.
- Whether and how accounting reversals are generated.
- The relationship between parent, component, and child status updates.
- Whether the documented “Ready status with swift error” is an approved target outcome or a test-observed defect.