---
type: concept
title: Group-Major-Version Completion Rules
tags: [cashflow-lifecycle, group-blotter, completion, status-management]
related: [bulk-manual-stp-for-group-blotter, group-blotter, allocation-cashflow-state-handling, what-are-the-authoritative-completion-rules-for-group-major-versions, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2025-changes--38-bulk--4160up]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md"]
---
# Group-Major-Version Completion Rules

A group-major-version has a parent lifecycle distinct from the lifecycle of its child cashflows. The test matrix uses parent statuses including `PENDING_TRADE_VALIDATION`, `PENDING_PRE_GROUP`, and `COMPLETED`, while child cashflows use statuses including `PENDING`, `END`, and `ERROR`.

## Observed Test Expectations

For fixture `T1_G1_V1`, cases 3.1 through 3.3 imply that:

1. Processing one selected pending child changes that child to `END`.
2. The parent may remain `PENDING_TRADE_VALIDATION` while other displayed children remain pending.
3. The parent becomes `COMPLETED` when the final displayed pending child, `C294`, becomes `END`.

This is evidence of an intended completion pattern, not a universally confirmed rule.

## Unresolved Exception

Case 1.2 expects `T1_G1_V1` to become `COMPLETED` while its displayed child states remain `c1:PENDING`, `c2:END`, and `c3:ERROR`. This conflicts with a simple all-children-terminal model.

Possible explanations include an eligibility-based completion rule, a display or hierarchy distinction, or a test-matrix defect. The source does not resolve which explanation is correct. See [[what-are-the-authoritative-completion-rules-for-group-major-versions]].