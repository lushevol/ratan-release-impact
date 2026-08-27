---
type: entity
title: SWIFT Network
created: 2026-08-22
updated: 2026-08-22
tags: [SWIFT, payment-network, outbound-payments]
related: [ratan, last-mile-payment-release-control, payment-release-concurrency-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# SWIFT Network

## Role

The SWIFT network is the external destination for outbound payment messages generated through RATAN’s release process.

The source proposes placing a final last-mile control immediately before payment is sent from RATAN to the SWIFT network. That control is intended to reconcile payment amounts and prevent duplicate or incorrect payments.

## Release Boundary

The proposed release sequence includes:

1. Workflow confirms the current state is `READY + NA + NA`.
2. The cashflow transitions toward `READY + NA + PendingAck`.
3. The SWIFT service confirms `READY + NA + PendingAck`.
4. A final outbound control performs the required checks before publication to the SWIFT network.

The source does not specify the SWIFT message standard, gateway implementation, or production status of the proposed gate.