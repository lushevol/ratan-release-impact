---
type: query
title: What Is the Authoritative Failed Cashflow State Machine?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, cashflow-status, failed-cashflow, state-machine, reprocessing]
related: [failed-cashflow-accounting, cashflow-event-versioning, cashflow-status-lifecycle, reversal-and-correction-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# What Is the Authoritative Failed Cashflow State Machine?

## Question

What are the authoritative transitions among `WAITING`, `FAILED`, and `READY`, and which transitions permit a cashflow to be sent to Razor?

## Evidence

The examples show:

- `FAILED` cashflows are sent to Razor for accounting and do not generate Swift.
- A normal re-process changes `FAILED` to `READY` and enables Swift generation.
- An amended cashflow may remain `WAITING` and not be sent to Razor.
- The amended cashflow later becomes `FAILED` and is sent to Razor.
- A subsequent re-process changes it to `READY`.

The source does not define the event, operational action, or validation that causes the `WAITING` → `FAILED` transition.

## Why It Matters

Without a state machine, systems cannot reliably determine whether a cashflow should be sent for accounting, Swift generation, or neither. It also remains unclear whether `READY` is sufficient for Swift eligibility or whether additional controls apply.

## Current Position

The observed sequence is `FAILED` → `WAITING` → `FAILED` → `READY` for the repeated-failure amendment case, but the complete state contract is unresolved.