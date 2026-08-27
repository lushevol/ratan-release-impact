---
type: query
title: What Are the Authoritative Completion Rules for Group-Major-Versions?
tags: [open-question, group-blotter, completion, cashflow-lifecycle]
related: [group-major-version-completion-rules, bulk-manual-stp-for-group-blotter, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2025-changes--38-bulk--4160up]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md"]
---
# What Are the Authoritative Completion Rules for Group-Major-Versions?

The source creates an unresolved conflict between two expected outcomes:

- Cases 3.1–3.3 suggest that `T1_G1_V1` becomes `COMPLETED` after its final displayed pending child reaches `END`.
- Case 1.2 expects `T1_G1_V1` to become `COMPLETED` although displayed children remain `PENDING` and `ERROR`.

Clarification is needed on whether completion depends on all children, all eligible children, selected children, a separate parent workflow, or another terminal-status rule.

Required evidence: the functional requirement, completion-rule implementation, and confirmed test execution results for cases 1.2 and 3.1–3.3.