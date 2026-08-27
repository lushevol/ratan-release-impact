---
type: concept
title: Cashflow-Versioned Exception Orchestration
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, versioning, Camunda, orchestration, auditability, SCBML]
related: [multiple-cashflow-exception-handling, cashflow-status-change-event-contract, ratan, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# Cashflow-Versioned Exception Orchestration

Cashflow-versioned exception orchestration correlates maker/checker tasks and domain-service actions using a cashflow identifier, business version, cashflow version, minor version, and tracking identifier.

## Correlation fields

The proposed request metadata includes:

- `cashflowId`
- `businessVersion`
- `cashflowVersion`
- `minorVersion`
- `exceptionId`
- `exceptionStatus`
- `trackingId`
- Optional action `requestBody`

The version fields provide a way to associate each exception action with the cashflow state against which it was submitted. The example flow increments the minor version as SSI stamping, payment-date updates, and manual affirmation occur.

## Benefits

Version-aware correlation supports:

- Workflow-to-cashflow traceability.
- Exception audit history.
- Detection of actions associated with a particular cashflow state.
- Reconstruction of the sequence leading to `READY`, `RELEASED`, and `SETTLED`.

## Missing safeguards

The design does not define optimistic-locking behavior for stale versions, concurrent maker and checker requests, task locking, duplicate submissions, or retries after an uncertain downstream result. These safeguards are necessary before versions can serve as a reliable concurrency contract.