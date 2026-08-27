---
type: source
title: Trade Information Technical Design
authors: []
year: 0
url: ""
venue: ""
tags: [cash-settlement, trade-information, tds3, architecture]
related: [trade-information-sourcing-for-cash-settlement, tds3, data-ambassador, which-trade-information-sourcing-option-is-approved-for-cash-settlement]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md"]
---
# Trade Information Technical Design

## Summary

This design note examines how Cash Settlement should obtain trade information for two use cases:

- LMS feed generation, requiring Entity LEID and Trader ID.
- A potential Cashflow Blotter Query, requiring Instrument data associated with BCS.

The note compares querying TDS3 directly through Data Ambassador for each cashflow event with continuing to use the existing trade service that consumes all trades from TDS3. It records an architectural options analysis, not an approved decision. The concrete identities of the generic “Cashflow service” and “trade service” are not established.

## Architectural Options

The source presents the following comparison:

| Options | Option 1 Cashflow service query TDS3 directly through Data Ambassador on each cashflow event | Option 2 Continue with the trade service currently we are using to consume all trades from TDS3 |
| --- | --- | --- |
| PROs | 1. Only partial data will be within Payment world, no silver copy issue | 1. Independent with payment processing |
| CONs | 1. New dependency | 1. Silver copy of trade data 2. Large data storage |

### Option 1: Direct TDS3 Query

Under Option 1, the Cashflow service would query TDS3 through Data Ambassador on each cashflow event and retrieve the required trade information. The stated advantage is that only partial trade data would be held within the Payment domain, avoiding a silver copy. The stated disadvantage is a new runtime dependency.

### Option 2: Existing Trade Service

Under Option 2, Cash Settlement would continue using the existing trade service that consumes all trades from TDS3. The stated advantage is independence with payment processing. The stated disadvantages are maintaining a silver copy of trade data and the associated large storage requirement.

## Required Information

| Use case | Required information | Stated source or context |
| --- | --- | --- |
| LMS feed generation | Entity LEID; Trader ID | Trade information from TDS3 |
| Potential Cashflow Blotter Query | Instrument | BCS |

The note does not define field semantics, lookup keys, formats, freshness requirements, or an API response contract.

## Limitations and Open Questions

The source does not select an option or identify an approving authority. It also does not specify:

- The concrete Cashflow service or trade service.
- Whether Data Ambassador is a synchronous API, event interface, cache, or another access mechanism.
- TDS3 API signatures, schemas, lookup keys, or service-level requirements.
- Availability, latency, timeout, retry, fallback, authorization, audit, or observability requirements.
- Trade-data volume, retention, replication latency, or storage sizing for Option 2.
- The meaning and ownership of BCS.
- Whether the Cashflow Blotter Query is a production requirement or only a potential use case.

See [[trade-information-sourcing-for-cash-settlement]] for the architectural abstraction and [[which-trade-information-sourcing-option-is-approved-for-cash-settlement]] for the unresolved decision.
