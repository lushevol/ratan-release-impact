---
type: query
title: What Are the Canonical Fee and AsGross Exclusion Semantics for Auto-Aggregation?
created: 2026-08-24
updated: 2026-08-24
tags: [fee, asgross, aggregation, cashflow, payment-schedule]
related: [normalized-payment-schedule-completeness-check, normalized-payment-schedule, netting-service, cashflow, product-agnostic-cashflow-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# What Are the Canonical Fee and AsGross Exclusion Semantics for Auto-Aggregation?

The draft uses different descriptions for exclusions on the expected-leg and received-cashflow sides:

- Fee schedule entries are excluded from `expected_num`.
- Cashflows with `payment_type` Fee bypass aggregation.
- `"AsGross"` cashflows are excluded from `cf_count`.

## Questions to Resolve

- Does `*Fee` mean a suffix wildcard, a glob, a regular expression, or a literal value?
- Is Fee matching case-sensitive, and which payment-type taxonomy is authoritative?
- Does Fee exclusion apply before or after schedule-to-cashflow grouping?
- Are Fee cashflows excluded from `cf_count` in addition to bypassing their own aggregation processing?
- Are `"AsGross"` records always excluded, and should an equivalent exclusion apply to expected schedule legs?
- How should unrecognized or null payment types be handled?

A single, testable eligibility predicate is required to prevent expected and actual leg counts from being calculated under incompatible rules.