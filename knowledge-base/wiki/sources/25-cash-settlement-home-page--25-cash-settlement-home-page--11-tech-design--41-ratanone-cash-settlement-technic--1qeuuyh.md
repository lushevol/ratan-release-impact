---
type: source
title: UBER Precious Metals
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, uber, precious-metals, netting, swift, schema-evolution]
related: [ratanone, netting-service, opensearch, sabre-sdk, swift-service, precious-metals-cashflow-identification, product-specific-delivery-location-extraction, what-is-the-canonical-precious-metals-identification-rule-for-uber-cashflows, should-netting-read-precious-metals-attributes-from-raw-uber-messages-or-lifecycle-storage, what-is-the-authoritative-swift-26c-commodity-identity-mapping-for-precious-metals]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# UBER Precious Metals

This preliminary technical-change note describes FMRP 9.0 Precious Metals support for UBER-message cashflows in [[ratanone]]. It identifies four trade attributes intended to identify precious-metals cashflows and drive specialized processing:

- `Custodian_SCI_FMID`
- `Custodian_Name`
- `Delivery_Location`
- `Settlement_Method`

The stated downstream uses are resultant generation in [[netting-service]], custodian-name stamping in Group Service, Swift Field 26C generation in [[swift-service]], and CIS query APIs. The document does not define the predicate, qualifying values, null behavior, or precedence rules that formally classify a cashflow as precious metals.

## Requirements traceability

- [Story 14562333 [FMRP 9.0 Commodities] Precious Metals - Update relevant APIs for dowstream systems(CIS) 26C](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14562333)
- [Story 14449450 [FMRP 9.0 Commodities] Precious Metals - Swift Msg - Field_26_Commodity_Identity](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14449450)

## Core inbound fields

```text
Custodian_SCI_FMID: tradeRecord.Entity.Custodian_SCI_FMID
Delivery_Location: tradeRecord.Delivery_Location
Settlement_Method: tradeRecord.Settlement_Method
```

`Custodian_Name` is identified as an input to precious-metals processing, while the Group Service requirement says it must be stamped by calling DA with a custodian FMID. The document does not establish whether inbound `Custodian_Name` or FMID-based enrichment is authoritative.

## Dependency upgrades

```text
SABRE SDK current version: v7.23-RELEASE-20260130.2-17e9c9eb
SABRE SDK upgrade version: v7.46-RELEASE-20260805.2-1aaadb3e
Foundation upgrade version: 8.0.7
```

The impacted domain services are `message-bridge`, `orchestration`, `group`, `lifecycle`, `query`, `netting`, `swift`, `utilization`, `open-search`, and `ssi-stamping`.

The source calls the dependency both “SEBRA SDK” and “Sabre SDK.” This naming discrepancy remains unresolved; this wiki uses [[sabre-sdk]] for the explicitly versioned dependency.

## Service-specific requirements

- `message-bridge`, `orchestration`, and Lifecycle Service require Foundation `8.0.7`.
- Utilization Service requires Foundation `8.0.7`; a `Settlement_Method` update triggers cashflow stamping.
- Group Service requires Foundation `8.0.7` and stamps custodian name through DA using custodian FMID.
- SSI Stamping Service is associated with Xinmiao Huang.
- OpenSearch work is associated with zhang jiangnan.
- OpenSearch and Query Service must expose the required trade attributes, notably delivery location, for all listed product structures.
- [[swift-service]] is required to generate Field 26C / commodity identity, but its dedicated design section is empty.

## Delivery-location extraction scope

The source provides the following identical path list for OpenSearch and Query Service:

```text
- Trade.Structured_Instrument.Forward_Future_Instrument.Far_Leg.Delivery_Location
- Trade.Structured_Instrument.Forward_Future_Instrument.Near_Leg.Delivery_Location
- Trade.Loan_Deposit_Instrument.Delivery_Location
- Trade.Forward_Future_Instrument.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.First_Leg.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.Second_Leg.Delivery_Location
- Trade.Option_Instrument.Commodity_Leg.Delivery_Location
- Trade.Intent_To_Allocate
- Trade.Entity.Custodian_Name
- Trade.Entity.Custodian_SCI_FMID
- Trade.Delivery_Location
```

The list mixes delivery-location paths with `Trade.Intent_To_Allocate` and custodian fields. It should therefore be read as required attribute scope rather than an unambiguous delivery-location-only mapping. No type, normalization, null-handling, target API contract, OpenSearch mapping, or precedence rule is supplied. See [[product-specific-delivery-location-extraction]].

## Netting alternatives

[[netting-service]] needs `Custodian_SCI_FMID`, `Delivery_Location`, and `Settlement_Method`. The document presents alternatives without selecting one.

### Proposal A: Deserialize raw UBER messages

Deserialize every cashflow's raw UBER message in the trade layer to retrieve the three fields.

```text
15 KB × 10,000 cashflows = 150,000 KB ≈ 150 MB
```

This is a raw-payload-volume estimate, not a demonstrated runtime memory, latency, CPU, or garbage-collection result.

### Proposal B: Persist fields in Lifecycle DB

Persist the three fields in Lifecycle Service storage and support an API query by `cashflowIds`.

This avoids per-cashflow raw-message deserialization but requires an ownership model, schema change, persistence behavior, historical backfill, API design, and consistency rules. None is specified. The decision is tracked in [[should-netting-read-precious-metals-attributes-from-raw-uber-messages-or-lifecycle-storage]].

## Status and gaps

This is a requirement and preliminary design note, not a final architecture. It does not contain:

- a canonical precious-metals classification rule;
- a selected Netting data-access approach;
- a Swift Field 26C mapping or validation specification;
- OpenSearch mapping, reindexing, or compatibility details;
- Lifecycle schema or API definitions;
- DA integration and failure-handling semantics; or
- an SDK/Foundation rollout and regression-test plan.