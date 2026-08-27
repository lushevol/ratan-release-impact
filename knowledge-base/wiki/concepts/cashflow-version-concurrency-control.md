---
type: concept
title: Cashflow Version Concurrency Control
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, optimistic-concurrency, versioning, stale-update, integration-control]
related: [ratan, fmrp-stella, cashflow-business-and-message-versioning, cashflow-netting-and-auto-un-netting, released-settled-amendment-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# Cashflow Version Concurrency Control

The integration uses version fields to detect stale Ratan actions when Stella changes a cashflow concurrently.

## Release concurrency

Ratan may validate a cashflow and begin release while Stella creates an amendment. The source states that Ratan’s status update can fail because Stella has advanced the business or cashflow version. The proposed recovery sends the original and amended payment information to Razor for correction and reversal.

## Netting concurrency

Ratan may read current versions for component cashflows, but Stella can amend one component before Ratan submits the `Netted` update. The submission is then rejected because the latest cashflow version has increased. The source proposes considering transactional netting and automatic reversal.

## Required contract

The source does not specify:

- Compare-and-swap or equivalent concurrency semantics.
- The authoritative version store.
- Transaction boundaries across Ratan and Stella.
- Retry and idempotency behavior.
- Recovery ownership and exception-ticket requirements.
- Whether status replication is part of the same transaction as the Ratan state change.

These omissions remain design risks.