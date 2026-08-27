---
type: entity
title: TIS
created: 2026-08-23
updated: 2026-08-25
tags: [tis, manual-payment, api, cash-settlement, korea, settlement, downstream-system, integration, ola, payment-processing, ratan, payment-information, cashflow, consumer-system]
related: [korea-cash-settlement-migration, ratan, operational-level-agreement-for-settlement-interfaces, korea-ratan-settlement-migration, oltp, ratan-tis-payment-query, korea-kro-non-kro-payment-routing, ratanone, tis-cashflow-eligibility-rules, withdrawal-cashflow-query-exclusion, what-is-the-authoritative-ratan-tis-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md", "RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# TIS (Total Information System)

## Role and Integration Context

TIS is identified as the downstream system for the RATAN manual-payment API in the Korea cash-settlement migration. It is also identified as a consumer of payment and cashflow information in the RATAN interface documentation.

The stated business objective in the RATAN interface documentation is to obtain some payment information through an API rather than requiring daily manual key-in through the [[oltp|OLTP]] UI. The documented high-level topology is:

```text
TIS <> RESTFUL API <> RATANONE
```

[[ratanone|RATANONE]] is named as the API-side system in that documentation, but the source does not define its role or relationship to RATAN.

The Korea RATAN processing guide describes TIS as the payment and receipt information interface used in the Korea RATAN migration flow. According to that guide, RATAN APIs are used with TIS to reduce daily manual payment entry in [[oltp]].

The Korea migration sources list TIS operational and development contacts.

## Documented Consumption and Processing Scope

### Korea Migration Scope

According to the Korea RATAN processing guide, the documented TIS scope applies to unreversed cashflows that meet all of the following conditions:

- Status is `Released` or `Settled`
- `STTL_MEANS = NOX`
- Entity FMID is `10036645`

The guide states that KRO payments are manually handled through TIS, while RATAN generates SWIFT messages for non-KRO payments. The exact KRO routing boundary remains unresolved; see [[what-is-the-authoritative-korea-kro-payment-routing-matrix]].

### RATAN Interface Documentation Scope

The RATAN interface documentation limits intended TIS consumption to cashflows described by [[tis-cashflow-eligibility-rules]]. It additionally states that withdrawal cashflows are unavailable for TIS query; see [[withdrawal-cashflow-query-exclusion]].

These statements come from different source documents and should not be treated as a single authoritative eligibility or routing matrix.

## OLA Status

The RATAN-to-TIS operational-level agreement (OLA) is pending PSS review and sign-off.

The Korea migration sources provide no version identifier, approval record, named owner, or deployment evidence for the OLA.

## Limits of Available Evidence

The RATAN and TIS interface source is unreviewed and contains no formal API contract. It does not define TIS authentication, access controls, endpoints, request parameters, response schemas, schedule, error handling, or operational ownership. These details remain tracked in [[what-is-the-authoritative-ratan-tis-api-contract]].

The Korea migration sources do not define the API contract, payment lifecycle, ownership boundaries, retry behavior, or reconciliation controls.