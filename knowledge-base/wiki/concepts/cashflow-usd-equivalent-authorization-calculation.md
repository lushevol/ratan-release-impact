---
type: concept
title: Cashflow USD-Equivalent Authorization Calculation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, usd-conversion, fx-rates, authorization, stella, ratan]
related: [ratan, stella, profile-based-usd-authorization-limits, profile-limit-static-data-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# Cashflow USD-Equivalent Authorization Calculation

## Definition

This calculation converts a cashflow payment into a USD-equivalent amount so that Ratan can compare payments in different currencies against a profile's USD authorization limit.

## Inputs

The source identifies these logical-model fields:

```text
Cashflow.Payment_Currency
Cashflow.Payment_Amount
```

## Calculation

```text
If Cashflow.Payment_Currency == USD:
    USD authorization amount = Cashflow.Payment_Amount

Otherwise:
    Retrieve Stella spotRate where:
      baseCurrency = Cashflow.Payment_Currency
      quoteCurrency = USD

    USD authorization amount = Cashflow.Payment_Amount × spotRate
```

The Stella endpoint is:

```text
API fx/rates/date/eodTag/baseCurrency/quoteCurrency
```

Example response:

```js
Response Payload : { "status":"SUCCESS", "data": [ { "date": "2021-03-15", "eodTag": "OFFICIAL_EOD_UK", "baseCurrency": "GBP", "quoteCurrency": "USD", "spotRate": "1.356" } ] }
```

## Unspecified operational rules

The requirement does not define:

- Which business, booking, payment, or approval date populates `date`.
- How `eodTag` is selected.
- Fallback behavior when Stella has no rate or returns an error.
- Precision and rounding rules.
- Handling of stale rates, negative amounts, or multiple returned rates.
- Whether the selected rate and calculated amount are persisted with the authorization decision.

These rules are required for deterministic and auditable authorization.
