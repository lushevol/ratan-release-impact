---
type: query
title: What Is the Authoritative RATAN Lifecycle Transition Matrix?
tags: [ratan, lifecycle, state-machine, governance, data-quality]
related: [ratan-cashflow-lifecycle-state-machine, cashflow-lifecycle-versioning, what-are-the-canonical-cashflow-state-and-sub-state-values, what-is-the-canonical-unhold-and-suppression-reject-behavior]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# What Is the Authoritative RATAN Lifecycle Transition Matrix?

The imported lifecycle requirements contain 267 transition rows but do not state an approval status, release owner, or production applicability. Several rows are incomplete, malformed, or struck through.

An approved, machine-readable source of truth is needed before using the matrix for application validation, workflow orchestration, reporting dimensions, or regression tests.

## Evidence needed

- A current versioned transition specification with owner and approval status.
- Explicit treatment of deprecated struck-through `SPLIT` rows.
- A definition of wildcard semantics for `ALL`.
- Confirmation that documented APIs and actions remain supported.