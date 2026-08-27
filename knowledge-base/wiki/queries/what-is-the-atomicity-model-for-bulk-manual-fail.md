---
type: query
title: What Is the Atomicity Model for Bulk Manual Fail?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-fail, atomicity, maker-checker, open-question]
related: [bulk-cashflow-manual-fail, cashflow-manual-fail-maker-checker, cashflow-pre-fail-state-restoration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# What Is the Atomicity Model for Bulk Manual Fail?

## Question

Does checker approval or rejection apply atomically to the complete bulk-fail request, or can individual cashflows in the request produce different outcomes?

## Evidence

The requirement describes bulk approval as moving multiple cashflows to `FAILED`, while rejection requires each cashflow to return to its own pre-fail state. It does not define:

- Whether one checker decision covers the entire request.
- Whether individual cashflows can be approved or rejected separately.
- What happens when one item becomes ineligible after maker submission.
- Whether a technical failure rolls back all items or only the affected items.
- How partial results are displayed and audited.

## Why it matters

The answer determines transaction boundaries, state persistence, UI behavior, retry handling, audit records, and the meaning of the mandatory checker comment.

## Required decision

The product and operations owners should define the bulk request model before implementation: atomic all-or-nothing processing, per-cashflow decisions, or a hybrid model.
