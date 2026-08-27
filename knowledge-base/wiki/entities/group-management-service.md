---
type: entity
title: Group Management Service
created: 2026-08-23
updated: 2026-08-24
tags: [group-management, cashflow-grouping, CCY-Pair, service, cash-settlement, group-blotter, entitlement, backend-service]
related: [ssi-stamping-service, group-ready-ccy-pair-enrichment, ccy-pair-based-nostro-selection, ratan, query-service, static-data-service, cash-settlement-data-entitlement, how-are-production-data-entitlement-rules-governed-and-deployed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Option2  RATAN existing data entitlement implementation.md"]
---
# Group Management Service

## Role

According to the compatibility-design source, the Group Management Service manages grouped cashflows and is the proposed enrichment point for `CCY Pair` under Option 1.

According to the Option 2 data-entitlement source, Group Management Service is the component requiring new entitlement logic for the Cash Settlement Group Blotter.

## `CCY Pair` Enrichment Eligibility

Under Option 1 in the compatibility-design source, after a group is ready, the service should enrich `CCY Pair` only when:

1. The booking entity FM ID is `400991880`, `400007847`, or `401036553`.
2. Product taxonomy is `ForeignExchange:Forward`, `ForeignExchange:Swap`, or `ForeignExchange:Spot`.
3. The grouped cashflows contain exactly two payment currencies.

If any condition is not met, `CCY Pair` should not be enriched.

### Operational Considerations

The compatibility-design source notes that a manually delivered incomplete group may not contain all cashflows needed to derive the currency pair. Processing the currency pair may also generate an exception.

That source does not define the exact exception, replay, or configuration contract. No database change is expected in this service.

## Cash Settlement Group Blotter Entitlement Logic

The Option 2 data-entitlement source labels the entitlement change as new logic and assigns it an indicative effort of 3 units.

The source does not define:

- The Group Blotter interface.
- Entitlement inputs.
- The enforcement location.
- Failure behavior.
- Implementation ownership.

This work should use the same authoritative entitlement governance and rule contract as the wider Cash Settlement data-access design only after those contracts are confirmed. See [[how-are-production-data-entitlement-rules-governed-and-deployed]] and [[what-is-the-static-data-entitlement-rule-language-and-failure-contract]].