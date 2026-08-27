---
type: source
title: Cashflow Dedicated Nostro Stamping Design (like RFI STRATEGY etc.)
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, nostro, rfi, ssi, static-data, amendment]
related: [dedicated-nostro-stamping, portfolio-currency-nostro-selection, nostro-selection-economic-change-detection, dedicated-nostro-static-data-model, rfi-dedicated-nostro-stamping, 001-implement-rfi-selection-in-ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# Cashflow Dedicated Nostro Stamping Design (like RFI STRATEGY etc.)

## Summary

This functional requirement introduces dedicated Nostro selection for RFI cashflows. Existing production selection uses `entity + ccy + settlementMeans + settlementAccount`; the RFI path instead uses portfolio plus currency. The stated current scope is RFI portfolios and the KOR currency leg only. Non-qualifying legs, including USD or GBP legs of RFI trades, retain standard selection.

The design is intended to be extensible to later dedicated types such as Strategy, but each new type still requires code changes and mapping configuration. The document proposes implementing the RFI decision in [[ratan-cash-settlement-ssi-stamping-service]] rather than a rule-engine.

## Required behavior

- RFI dedicated selection is based on portfolio and currency, without Vostro information, `settlementMeans`, or `settlementAccount`.
- RFI and standard Nostro selection are intended to be exclusive.
- An eligible RFI cashflow with no matching dedicated configuration raises the existing missing-Nostro exception; it does not fall back to normal selection.
- Multiple matching RFI configurations raise the existing multi-Nostro exception.
- Vostro stamping is not changed and must not overwrite Nostro stamping.
- A changed returned `nostroId` between paired new and withdrawal cashflows is an economic change.

The amendment correlation assumption is:

```text
bookingEntityId
counterpartyFmId
paymentCurrency
paymentAmount
ValueDate
Direction
settlementMethod
```

For a matching new/withdrawal pair, these seven factors are assumed unchanged. If an amendment group currently classified as `NonEcoAmend` has different selected Nostro accounts, it must instead follow economic-change processing.

## Design and deployment

Dedicated-type identification ultimately selects a memory-plus-database approach: identify the type in memory for each request while keeping authoritative data in the database. The document notes a prior preference for memory-only logic, creating ambiguity about the precise final caching and consistency behavior.

The storage discussion includes JSONB, a child table, and a child table with JSONB. The stated preferred storage choice is a child table with JSONB, while the requirement also proposes `nostroType`, `nostroKey`, and `dedicated_info`. No final DDL or lookup query is supplied.

Planned go-live actions are:

1. Deploy `51358-ratanone-static-data-service`, `51358-ratan-cash-settlement-ssi-stamping-service`, `51358-ratan-cash-settlement-group-management-service`, `51358-ratanone-swift-service`, and `51358-ratan-cash-settlement-query-service`.
2. Execute `51358-ratanone-db-repository` and migrate Nostro static data.
3. Check logs for errors and correct behavior.

## Open implementation issues

The source alternates between `KOR` and `KRO`; one canonical value is required. It also distinguishes no historical cashflow migration from required partial static-data migration: existing records default to `nostroType='DEFAULT'`, while identified RFI records become `RFI` and receive dedicated attributes.

The final duplicate key is stated as:

```text
EntityFmId + currency + settlementMeans + settlementAccount + nostroType
```

This conflicts with portfolio-based RFI selection because it excludes the portfolio/`nostroKey` discriminator. Ad hoc, split, accounting, and trade stamping are listed as entry points requiring consideration, but trade stamping is explicitly not currently in scope because product XML portfolio paths are inconsistent.