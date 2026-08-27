---
type: concept
title: Last-Mile Payment Release Control
created: 2026-08-22
updated: 2026-08-22
tags: [payment-release, SWIFT, RATAN, reconciliation, controls]
related: [ratan, payment-release-concurrency-control, auto-release, clearing-resultant-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# Last-Mile Payment Release Control

## Definition

A last-mile payment-release control is a planned final gate before a payment leaves RATAN for the SWIFT network. Its purpose is to prevent duplicate or incorrect outbound payments after upstream lifecycle, workflow, and release processing has completed.

The source proposes that the gate include proper internal reconciliation of payment amounts. It is described as future work to be tracked under Market Efficiency, not as an approved or deployed production control.

## Intended Checks

The source does not define a complete implementation specification, but the control is expected to address:

- Confirmation that the cashflow remains eligible for release.
- Reconciliation of the payment amount against the internally expected amount.
- Duplicate detection before outbound publication.
- Protection against status-write-back failures that could otherwise leave a cashflow in an operationally constrained state.
- Coordination with the SWIFT service’s existing or proposed duplicate checks.

## Relationship to Other Controls

The last-mile gate complements, rather than replaces:

- Workflow validation that the current cashflow state is `READY + NA + NA`.
- SWIFT-service validation that the current state is `READY + NA + PendingAck`.
- Cache-based concurrency locks.
- Business-version and minor-version validation.
- Message Bridge tracking-ID deduplication.
- SWIFT duplicate detection using cashflow ID and business version.

See [[payment-release-concurrency-control]] for the broader layered control pattern.

## Ownership and Status

The source identifies Market Efficiency as the tracking area but does not name an implementation owner, define the reconciliation algorithm, or confirm approval, deployment, monitoring, or test evidence.