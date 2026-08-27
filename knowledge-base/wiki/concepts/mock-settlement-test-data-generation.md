---
type: concept
title: Mock Settlement Test-Data Generation
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, test-data, message-replay, UAT, identifier-uniqueness]
related: [akhq, fmo-post-trade-portal, sabre-trade-admin-tool, bcs, cdu, kafka-settlement-test-topics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md"]
---

# Mock Settlement Test-Data Generation

Mock settlement test-data generation is the practice of creating test cashflows and trade-related events by replaying representative messages through test interfaces and Kafka topics.

## Documented flows

### Cashflow creation

An existing message from `Cash_Settlement_Group_Message_Inbound` is copied, modified with new `trackingId` and `cashflowId` values, and produced through [[akhq]]. The new `cashflowId` is then searched in the [[fmo-post-trade-portal]].

### BCS trade replay

A trade sample is submitted through the [[sabre-trade-admin-tool]] with `BCS` selected as the source system. The `tradeId` and `trackingId` must be changed. The resulting cashflow is searched in the FMO Cashflow Blotter using the documented `BCS_` prefix convention.

### CDU confirmation status

A CDU sample is aligned to an existing cashflow by replacing `legalEntityFmId`, `counterpartFmId`, `tradeId`, and `tradeVersion`. The modified message is produced to `CDU_Trade_Confirmation_Process_In`.

## Controls

- Select and align the target environment before producing or replaying messages.
- Generate new identifiers to avoid duplicate records.
- Record identifiers, especially `cashflowId`, for downstream lookup.
- Keep cashflow, BCS trade, and CDU confirmation flows separate because their fields and validation steps differ.
- Use independent verification after message acceptance where test evidence requires proof of booking, cashflow creation, or event processing.

## Boundaries

The procedure documents test-data creation, not complete settlement processing. It does not establish that a producer notification, transformed replay result, or portal search proves successful downstream settlement. Cleanup, isolation, identifier-format rules, and complete message contracts remain unspecified.
