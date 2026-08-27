---
type: concept
title: RATAN–TDS3 Trade Lake Integration
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tds3, sabre, trade-data, settlement-data, blotter, integration]
related: [ratan, tds3, sabre, razor, ratan-fx-replication, trade-validation, ratan-settlement, ratan-interface-architecture, what-is-the-authoritative-ratan-tds3-interface-contract, what-are-the-ratan-tds3-cache-refresh-and-outage-behaviors, what-is-the-authoritative-fx-rate-and-conversion-rule-for-ratan-settlement]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDS3)-29126.md"]
---
# RATAN–TDS3 Trade Lake Integration

[[tds3]] is described as SABRE's FM Trade Lake and as an immediate upstream data source for [[ratan]]. The documented integration supplies RATAN with trade, fixing, cashflow, trade-identifier, instrument-reference, and spot-rate data.

## Trade Processing

RATAN uses TDS3 in several trade-related functions:

- It intermediates FX replication in the route `TDS3 → RATAN → RAZOR`; RATAN is responsible for filtering so only intended trades reach [[razor]].
- It retrieves TDS3 trade data for database storage and trade-blotter population.
- It also queries TDS3 APIs in real time for trade-blotter display.
- It obtains rate-fixing data through the `ratanone rule service` for FM COO exception management.
- During manual [[trade-validation]], it directly retrieves the latest trade version from TDS3.

The concurrent persisted and real-time trade-blotter patterns indicate a hybrid data-access model. The source does not state whether these modes serve different trade populations, fields, user actions, or freshness requirements.

## Settlement Processing

For the documented settlement route, TDS3 supplies cashflows for RATAN processing. RATAN also consumes TDS3 data for enrichment and display:

- `trade_external_id`
- `clearing_organization_trade_id`
- *Parent Trade Instrument*
- *Equity Instrument Reference*
- Spot rates used to convert cashflow amounts to USD for OPS per-amount limitations

The document says that the two identifier fields are cached but does not define the cache lifecycle. It also does not establish that TDS3 is the authoritative business producer of every cashflow; it establishes TDS3 as RATAN's stated immediate source in this interface.

## Stated Lineage

```text
Trade flow: Blade → FMRP Stella → TDS3 → RATAN
Settlement flow: BCS Stella/Blade → FMRP Stella → TDS3 → Solace → Ratan → Razor/FMSGW
```

This lineage complements [[ratan-interface-architecture]] and [[ratan-fmsgw-settlement-messaging]], but it does not specify protocols, schedules, event timing, schemas, or delivery and recovery semantics.

## Contract Gaps

This source is not an authoritative interface contract. Outstanding details include:

- API endpoint, request, response, authentication, and versioning definitions.
- Trade-filter selection criteria for the RAZOR route.
- Data ownership and authoritative-source boundaries.
- Cache refresh, invalidation, freshness, and TDS3-outage behaviour.
- Latest-version consistency rules for manual validation.
- Spot-rate timestamp, precision, currency conventions, missing-rate handling, and reconciliation.
- Error handling, retry, monitoring, and operational service levels.

These gaps are tracked in [[what-is-the-authoritative-ratan-tds3-interface-contract]], [[what-are-the-ratan-tds3-cache-refresh-and-outage-behaviors]], and [[what-is-the-authoritative-fx-rate-and-conversion-rule-for-ratan-settlement]].