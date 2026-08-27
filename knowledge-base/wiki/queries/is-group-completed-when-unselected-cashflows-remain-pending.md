---
type: query
title: Is a Group Completed When Unselected Cashflows Remain Pending?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, group-completion, cashflow-status, bulk-manual-stp]
related: [group-blotter-cashflow-state-lifecycle, bulk-manual-stp-group-blotter, allocation-cashflow-state-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# Is a Group Completed When Unselected Cashflows Remain Pending?

## Question

Does a group become `COMPLETED` when the selected cashflows finish, or only when every required cashflow in the group reaches a terminal state?

## Conflicting Evidence

Case 1.2 expects `T1_G1_V1` to become `COMPLETED` while `c1` remains `PENDING` and `c3` remains `ERROR`. Other scenarios imply that group completion follows processing of all relevant pending cashflows, including the final pending cashflow in case 3.3.

Case 1.3 also contains a likely typo: the selection refers to `c1` and `c2`, while the expected result refers to `c1` and `c3`.

## Required Resolution

Define the completion predicate separately from the selected-operation result. Confirm whether `PENDING` and `ERROR` cashflows are included in the predicate, and whether an unselected cashflow can prevent group completion.