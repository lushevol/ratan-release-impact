---
type: query
title: What Are the Idempotency, Retry, and Ordering Rules for NSTP Auto-Close?
tags: [nstp, idempotency, retry, event-ordering, exception-handling]
related: [confirmation-driven-nstp-exception-auto-closure, cashflow-reinstatement-and-replay, what-is-the-canonical-replay-and-reinstate-procedure, what-is-the-canonical-cash-settlement-exception-state-machine, ratan-cash-settlement-orchestration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# What Are the Idempotency, Retry, and Ordering Rules for NSTP Auto-Close?

## Question

How should the confirmation-driven NSTP auto-close consumer behave for duplicate, late, replayed, concurrent, or out-of-order `MATCHED` and `Confirm`/`Affirm` events, and for failures returned by the Camunda API?

## Evidence

[[confirmation-driven-nstp-exception-auto-closure]] defines the trigger and the `mutiException/syncSummary` invocation but defines no deduplication key, transactional boundary, retry policy, DLQ behavior, concurrency control, or reconciliation process.

The documented `RATAN-201050003` response means that the expected Cashflow fixing task was absent. The source does not specify whether this is retriable, terminal, stale-event handling, or a technical exception.

## Needed Decisions

- Define the idempotency key, such as an exception ID, `trackingId`, or versioned cashflow tuple.
- Define ordering and stale-event handling across trade and cashflow versions.
- Define retry classification and backoff for `RATAN-201050003`.
- Define DLQ, alerting, and reconciliation ownership.
- Establish how replay procedures in [[cashflow-reinstatement-and-replay]] apply to auto-close submissions.