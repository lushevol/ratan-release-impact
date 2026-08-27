---
type: concept
title: SSI Product Template Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, scbml, fpml, xpath, product-mapping, trade-processing]
related: [trade-ssi-stamping, stella, cdups, ssi-best-match-rule, ssi-swift-field-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# SSI Product Template Mapping

SSI Product Template Mapping defines how trade products expose currencies, party references, and settlement attributes for Vostro and Nostro lookup.

## Product families

- FX Spot and Forward use `fxSingleLeg.exchangedCurrency1` and `exchangedCurrency2`.
- Bullion Spot and Forward use `commodityForward.fxSingleLeg`.
- FX Swap uses near-leg and far-leg `exchangedCurrency1` and `exchangedCurrency2`.
- Bullion Swap uses `strategy.fxSwap` with near and far legs.
- IRS, NDIRS, and NDCCS use the first two `swapStream` structures and may include a settlement currency.
- CCS and MTM CCS use two swap streams and may include a varying notional currency.
- Fixing uses settlement information from `fixingNoticePayload`.

## Direction and enrichment

For most products, the payer-party reference determines whether a currency is treated as Credit or Debit. The resulting lookup selects either client Vostro data, SCB Nostro data, or both.

The source contains implementation-sensitive inconsistencies:

- XPath examples compare both `Party1` and `party1`.
- FX Swap currency-2 direction examples repeat the currency-1 path in places.
- Bullion Swap far-leg direction uses receiver-party references rather than payer-party references.

These rules require confirmation before being treated as canonical.