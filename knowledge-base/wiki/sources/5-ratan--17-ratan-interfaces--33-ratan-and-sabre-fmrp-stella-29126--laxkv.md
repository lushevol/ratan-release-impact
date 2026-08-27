---
type: source
title: RATAN and SABRE (FMRP STELLA) Interface 29126
authors: [Yunzhe Ta, Junying Jiang, Pengpeng Li]
year: 2026
url: ""
venue: "RATAN interface documentation"
tags: [ratan, sabre, fmrp-stella, settlement, trade-control, interface-29126]
related: [ratan, sabre, stella, fmrp-stella, sabre-booking-api, ratan-fmrp-stella-interface, scbml-kafka-stella-event-flow, trade-lock-status-for-mo-validation, what-is-the-authoritative-ratan-fmrp-stella-29126-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# RATAN and SABRE (FMRP STELLA) Interface 29126

## Summary

This source documents interface **29126-FMRP STELLA** between FMRP STELLA/SABRE and **51358-RATAN**. It covers two related but distinct integration areas:

- Settlement processing, including spot-rate retrieval, BCS fixed/floating-leg netting checks, cashflow status write-back, and trade-status updates.
- Trade control, including trade-lock status retrieval, trade validation, rejection, affirmation, and Economic Affirmation (`E0`) events.

The documented integration uses the `sabre-booking-api` SDK. Its named components are `StellaBookingApi` for cashflow and trade-status write-back and `StellaBookingRestApi` for trade-lock status retrieval.

## Document metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
|---|---|---|---|---|
| @Yunzhe Ta @Junying Jiang | 2026-02-04 | @Yunzhe Ta @Pengpeng Li | 2026-03-18 | |

The source states that status should be updated to `Published` after review, but the status field is blank.

## Settlement processing flow

1. RATAN retrieves the **Spot Rate** from the Stella API to comply with settlement-processing profile constraints.
2. In the **BCS flow**, RATAN calls the Stella API to check fixed/floating legs for netting.
3. RATAN writes calculated cashflow status and updated trade status back to Stella.
4. RATAN publishes continuous, real-time confirmation events and settlement workflow events to the SABRE/STELLA SDK Booking API.
5. RATAN posts an SCBML message to a dedicated Kafka topic.
6. Stella reads the message from Kafka and pushes it into the trade booking engine.
7. The Stella booking engine returns an ACK or NACK based on processing success.

The source does not specify whether the ACK/NACK is returned synchronously, published as a Kafka event, or delivered through another callback mechanism.

## Trade control flow

1. RATAN queries trade-lock status from the Stella SDK Booking REST API through the **Ratan Stella Ambassador** service.
2. Middle Office (MO) users use the lock information to determine whether a trade or trade package is locked before initiating manual intervention.
3. When a lock exists, Stella provides the identity of the user or system holding the lock and the lock duration or expiry time.
4. The **RSA microservice** acts as a secure integration gateway between RATAN and Stella for trade validation, rejection, and affirmation.
5. RATAN publishes Economic Affirmation (`E0`) events directly to Stella through an API.

## Connection details

| API Provider | Consumer | Data type | Connection Detail | Version | METHOD | Query/Parameter | Query Frequency | API limitation | API timeout |
|---|---|---|---|---|---|---|---|---|---|
| 29126-FMRP STELLA | 51358-RATAN | confirmation events and settlement workflow events | `https://sabre-prod-cloud-global.gdc.standardchartered.com/fmrp-stella-ep/prod` | `version would update to 2025.10.23-1-cfda1ef9` |  |  | real-time |  |  |
| 29126-FMRP STELLA | 51358-RATAN | trade validation status | `https://sabre-prod-cloud-global.gdc.standardchartered.com/fmrp-stella-ep/prod` StellaBookingApi, `/v1/stella/{type}/{operation}/{action}` |  |  |  | real-time |  |  |
| 29126-FMRP STELLA | 51358-RATAN | trade lock status | StellaBookingRestApi PROD URL: `https://sabre-prod-cloud-global.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/{contract_id}`; example: `https://sabre-prod-cloud-1.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/5028387294` |  | Trade validation change the channel to: `RATAN_VALIDATION` |  | real-time |  |  |

## Named SDK components

```text
SDK: sabre-booking-api

Cashflow/trade status write back:
  StellaBookingApi

Trade lock status:
  StellaBookingRestApi
```

## API signatures and examples

```text
/v1/stella/{type}/{operation}/{action}
```

```text
https://sabre-prod-cloud-1.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/5028387294
```

## Referenced documentation

- [Process Model - Contract Matching Service (from CDU/RATAN) - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=1702274658)
- [MO Validation - Design - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/MO+Validation+-+Design)
- [Trade and Lifecycle Events - Workflows - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/Trade+and+Lifecycle+Events+-+Workflows)
- [FMRP STELLA Booking API - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/FMRP+STELLA+Booking+API)
- [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)
- [Ratan -> FMRP Stella API integration - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Ratan+-%3E+FMRP+Stella+API+integration)
- [Trade Lock/Unlock for MO Validation Tech Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3263145506)

## Evidence boundaries and unresolved details

The source documents the functional scope at a high level but does not provide a complete production interface contract. The following details are absent or require validation:

- Actual API ownership versus runtime producer and consumer direction.
- HTTP methods and payload schemas.
- Authentication and authorization requirements.
- API versions for validation and lock-status operations.
- Retry, timeout, rate-limit, and idempotency policies.
- Error mappings and ACK/NACK correlation.
- The expansion of `{type}/{operation}/{action}`.
- The canonical production hostname and path for `StellaBookingRestApi`.
- The precise distinction between the Ratan Stella Ambassador and RSA microservice.
- Whether `RATAN_VALIDATION` is the canonical channel for all trade-validation changes.

The connection table labels the interface provider as FMRP STELLA and the consumer as RATAN, while the narrative describes RATAN writing and publishing data to Stella. API ownership and runtime data direction should therefore be recorded separately until corroborated.

## Contacts

| Role | Name | Contact |
|---|---|---|
| SABRE PSS Manager | Brito, Paulo - 1547035 | +65 6981 3784 |
| PSS Change Contact | SABRE PSS | SABREPSS@sc.com |
