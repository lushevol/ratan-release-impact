---
type: query
title: Is Auto Split Atomic Across Parent and Child Cashflows?
tags: [cashflow-splitting, auto-split, atomicity, techfail, lifecycle]
related: [cashflow-auto-split-failure, cashflow-splitting, camunda, techfail, split-cashflow-persistence-and-lineage]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# Is Auto Split Atomic Across Parent and Child Cashflows?

## Question

What consistency and recovery guarantee applies when automatic splitting changes the parent and creates or advances child cashflows?

## Evidence

Induced lifecycle timeouts in UAT produced three different outcomes:

- Pre-process timeout: parent `READY -> TechFail`; no children generated.
- Process-stage timeout: parent `READY -> SPLIT -> TechFail`; children generated but stuck in `Queue`.
- Post-process timeout: parent `READY -> SPLIT -> TechFail`; children generated successfully.

## Why It Matters

A parent `TechFail` status is insufficient to determine whether operational repair requires child creation, child resumption, reconciliation, or no action. The documented results show no all-or-nothing transaction boundary across parent and children.

## Needed Resolution

Define the authoritative parent/child state model, idempotency behavior, operator recovery path, and downstream accounting or SWIFT handling for each partial-completion state.