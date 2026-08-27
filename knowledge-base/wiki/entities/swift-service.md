---
type: entity
title: SWIFT Service
created: 2026-08-22
updated: 2026-08-24
tags: [SWIFT, service, payment-release, deduplication, cash-settlement, status-update, retry, precious-metals, messaging]
related: [ratan, swift-network, payment-release-concurrency-control, last-mile-payment-release-control, cashflow-locking-and-retry-policy, ratanone, precious-metals-cashflow-identification, what-is-the-authoritative-swift-26c-commodity-identity-mapping-for-precious-metals, what-controls-make-swift-generation-safe-without-a-distributed-lock]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# SWIFT Service

## Role in Cash Settlement

The SWIFT service generates outbound SWIFT messages for cashflows processed by RATAN’s release flow.

The design discussion in `Auto Release Process.md` proposes that the service generate SWIFT only after confirming that the current cashflow state is `READY + NA + PendingAck`.

## Duplicate Protection

`Auto Release Process.md` describes duplicate checks using cashflow ID and business version. It also identifies edge cases involving `ResendToRazor` and `ReGenerateSwift`, where SWIFT duplication checks are expected to provide protection.

The source does not confirm the exact persistence guarantee, message-header implementation, or production deployment status of these checks.

## Status Updates and Retry

`Cash Settlement Lock Process.md` identifies the Swift Service as automatically retrying SWIFT status updates until success. Its documented lock key is `Cashflow Id`.

That source does not specify retry timing, attempt limits, idempotency behavior, or the status-update message contract.

## Precious-Metals UBER Integration

The UBER Precious Metals design identifies Swift Service as the downstream service responsible for precious-metals commodity identity generation in Swift Field 26C for UBER-message cashflows.

The requirement is linked to Story 14449450. The Swift Service section of that source provides no technical design: it does not specify supported Swift message types, source-field mapping, Field 26C format, validation, fallback behavior, or test scenarios.

The unresolved data contract is tracked in [[what-is-the-authoritative-swift-26c-commodity-identity-mapping-for-precious-metals]].