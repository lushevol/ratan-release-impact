---
type: concept
title: Settlement Accounting
created: 2026-08-22
updated: 2026-08-24
tags: [settlement, accounting, integration, static-data, ratan, source-unavailable]
related: [ebbs, ratan, solace, vietnam-ifc-branch, entity-branch-onboarding, ratan-settlement, post-trade-orchestration, 5-ratan--25-ratan-core-function-copy--28-ratan-settlement-7accounting--1dr53iw]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md", "RATAN/RATAN -Core Function copy/RATAN-Settlement  7_Accounting.md"]
---
# Settlement Accounting

Settlement accounting is the generation and routing of accounting entries associated with settlement cashflows.

## Entity-Onboarding Inputs

A new entity may require:

- Accounting branch code.
- Transaction code or transaction type.
- Bridge-account number.
- Booking-currency-to-ISO-code mapping.
- Entity- or currency-specific suppression.
- Messaging topic or queue.
- Accounting-service routing and transformation support.

For the [[vietnam-ifc-branch]], these values must support [[ebbs]]. The entity-onboarding source also anticipates a new [[solace]] topic or queue and accounting-service adaptation.

## Scope Classification

According to the entity-onboarding source, the accounting work is mandatory and classified as `Config/Dev`. It is estimated at 15 person-days. Although the overall proposal says there are no customized features, reusable development may still be required to enable a standard onboarding path for a new entity.

## RATAN Source Status

The filename of [[5-ratan--25-ratan-core-function-copy--28-ratan-settlement-7accounting--1dr53iw]] indicates that settlement accounting is its apparent subject.

However, the source content for `RATAN-Settlement 7_Accounting.md` was unavailable. Therefore, that source does not define a RATAN-specific accounting process or establish that [[ratan-settlement]] creates, transmits, reconciles, or owns accounting records.

### Unverified RATAN Scope

The unavailable RATAN document may address:

- Accounting treatment.
- Posting.
- Ledger integration.
- Reconciliation.
- Reporting.
- Controls.
- Exception handling.

Each item requires confirmation from the source text.

### Related RATAN Context

[[ratan-settlement]] is the contextual settlement capability, and [[post-trade-orchestration]] is a potentially related broader process category. Their precise relationship to settlement accounting remains unverified.

## Open Question

See [[what-is-the-authoritative-ratan-settlement-accounting-contract]].