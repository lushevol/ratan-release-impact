---
type: query
title: What Is the Authoritative Uber Withdrawal and Cancellation Semantics?
created: 2026-08-24
updated: 2026-08-24
tags: [uber-message, withdrawal, cancellation, idempotency, duplicate-payment]
related: [uber-message, non-economic-cashflow-amendment-handling, non-economic-cashflow-suppression, trade-event-undo-semantics, undo-revive-cashflow-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# What Is the Authoritative Uber Withdrawal and Cancellation Semantics?

## Question

Should a withdrawn cashflow be emitted as an explicitly stamped withdrawal, directly cancel the prior item, or support both representations?

## Evidence

The non-economic amendment example shows new cashflows followed by withdrawal events and replacement cashflows. One withdrawal is flagged as a possible duplicate-payment exception.

## Required resolution

Define event history, idempotency, ordering, retry, cancellation state, settlement blocking, audit evidence, and the control that prevents payment when a withdrawal or replacement is delayed.