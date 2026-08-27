---
type: source
title: "Trade SSI Stamping — Product Templates"
authors: []
year: 2025
url: ""
venue: "FMRP Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, trade-settlement, rat an, cdups, scbml, fpml, functional-requirement]
related: [cdups, fmrp, ratan, ssi, stella, trade-lake, trade-ssi-stamping, trade-cashflow-ssi-linkage, ssi-best-match-rule, ssi-product-template-mapping, ssi-swift-field-enrichment, ssi-stamping-retry-contract, fixing-notice-ssi-override]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# Trade SSI Stamping — Product Templates

## Scope

This functional requirement specifies the trade SSI stamping flow in the [[fmrp]] context. [[cdups]] queries [[ratan]] for confirmation-oriented trade SSI stamping. The design covers Vostro and Nostro lookup, product-specific trade extraction, SCBML enrichment, response result states, retry behavior, and Fixing Notice handling.

The document is a design-level specification agreed with Product Owners. It is not a production performance study or operational validation report.

## Architectural intent

Trade SSI stamping and cashflow SSI stamping are linked, but cashflow SSI does not inherit the trade SSI. Cashflow stamping remains an independent process. [[ratan]] is intended to provide the central SSI stamping service so that the two flows remain aligned while preserving their separate data and lifecycle boundaries.

The confirmation model is primarily pull-oriented:

- Vostro refresh is not automatically published to CDUPS.
- RATAN Nostro refresh is not automatically published to CDUPS.
- Settlement Ops ad-hoc stamping is not automatically published to CDUPS.
- CDUPS may request confirmation or the latest cashflow SSI on an ad-hoc, call-based basis.
- A Fixing Notice response returns the latest cashflow SSI result before the general SSI result.
- Following a trade event, CDUPS calls again rather than relying on automatic publication.

## CDUPS request contract

| Field | Mandatory | Nullable | Data type | Example or rule |
|---|---:|---:|---|---|
| `trackingId` | Yes | No | String | `STELLA.1728376554435.c641406d-7e94-4b29-b8f7-fab1bab19f8d` |
| `tradeId` | Yes | No | String | `{ "key": "Trade_Id", "value": "4354367341" }` |
| `majorVersion` | Yes | No | String | `{ "key": "Trade_Lake_Trade_Major_Version", "value": "5" }` |
| `asOf` | Yes | No | String | Trade Lake transaction-from timestamp |
| `effective` | Yes | No | String | Trade Lake valid-from timestamp |
| `requestDate` | Yes | No | String | `YYYY-MM-DD` |
| `bookingEntityFmId` | Yes | No | String | Booking entity FMID |
| `counterpartyFmId` | Yes | No | String | Counterparty FMID |
| `cfiCode` | Yes | No | String | Financial instrument code |
| `settlementMethod` | Yes | No | String | Trade settlement method |
| `settlementType` | Yes | No | String | Specified as hardcoded `Cash` |
| `legs.currency` | Yes | No | String | Product-specific currency |
| `legs.payerPartyReference` | Yes | No | String | Product-specific party reference |

For `tradeId`, the key and value are used for validation, `Trade_Id` is used for linkage, and the value is used in the stamping query.

## SSI stamping response

The response is leg-oriented and includes lookup outcomes plus enriched settlement-instruction fields.

| Field | Required | Nullable | Meaning |
|---|---:|---:|---|
| `legs.currency` | Yes | No | Settlement currency |
| `legs.payerPartyReference` | Yes | No | Direction and party reference |
| `legs.vostroResult` | Yes | No | `SUCCESS`, `MULTI_VOSTRO_ERROR`, or `MISSING_VOSTRO_ERROR` |
| `legs.nostroResult` | Yes | No | `SUCCESS`, `MISSING_NOSTRO_ERROR`, `DEFAULT_NOSTRO`, or `MULTI_NOSTRO_ERROR` |
| `Settlement_Instruction.Account.Beneficiary_BIC_code` | Yes | No | SWIFT Field 58 beneficiary customer |
| `Beneficiary_Account_Name` | Yes | Yes | Beneficiary name |
| `Beneficiary_Street_Address` | Yes | Yes | Beneficiary address |
| `Beneficiary_City` | Yes | Yes | Beneficiary city |
| `Beneficiary_Account_Number` | Yes | Yes | Beneficiary account |
| `Beneficiary_Bank_BIC_code` | Yes | Yes | SWIFT Field 57 account-with-institution |
| `Intermediary_BIC_code` | Yes | Yes | SWIFT Field 56 intermediary institution |
| `Booking_Entity_Correspondent_BIC_code` | Yes | No | SWIFT Field 53 sender’s correspondent |
| Corresponding name, address, city, and account fields | Yes | Usually yes | Enriched SSI details |

## Error and retry contract

| Code or condition | Meaning | CDUPS behavior |
|---|---|---|
| `200` | Success or `DEFAULT_NOSTRO` | No downstream action is defined |
| `400` | `VALIDITION_FAILED` or trade not found | Treat as validation failure |
| `500` | `INTERNAL_ERROR` | Retry with the same trade ID and major version at least three times, at three-minute intervals |
| RATAN timeout or no response | Infrastructure failure | Apply the same retry behavior as `500` |

The specification does not define the final state after retries, an idempotency key beyond trade ID and major version, timeout duration, authentication, endpoint, or whether `DEFAULT_NOSTRO` is operationally acceptable.

## Supported products and events

The intended testing scope includes:

- `ForeignExchange:Forward`, `ForeignExchange:Spot`, `ForeignExchange:NDF`, and `ForeignExchange:Swap`: New, Amendment, Cancel, Novation, Terminations, Undo.
- `ForeignExchange:VanillaOption`: New, Amendment, Cancel, Novation, Terminations, Exercice, Expire, Undo.
- `InterestRate:IRSwap:FixedFloat`, `OIS`, `FloatFloat`, `Basis`, and `FixedFixed`: New, Amendment, Cancel, Novation, Terminations, Undo.
- `InterestRate:CrossCurrency:FixedFloat`, `FloatFloat`, `Basis`, and `FixedFixed`: New, Amendment, Cancel, Novation, Terminations, Undo.
- `Commodity:Metals:Precious:SpotFwd:Cash` and `Commodity:Metals:Precious:SpotFwd:Physical`: New, Amendment, Cancel, Novation, Terminations, Undo.
- `InterestRate:LoanDeposit` is struck through and has no supported event list in the source.

## Lookup and enrichment rules

Initial CFI selection is product-dependent:

- FX spot, forward, and swap use hardcoded `*F****`.
- IRS, CCS, bullion spot/forward/swap, MTM CCS, NDIRS, and NDCCS use the SCBML value.
- Fixing uses an API value.

The CFI is refactored using wildcards for sequence `213456`. Lookup considers the requested CFI, parent patterns, and the wildcard `******`, selecting the best available Vostro in this order:

1. Exact CFI.
2. Parent CFI.
3. `******`.

Settlement-method normalization follows the cashflow SSI lookup:

| Trade settlement method | Vostro query method |
|---|---|
| `CASH` | `(CASH,FEDWIRE)` |
| `GROSS` | `(CASH,FEDWIRE)` |
| Any other value | `(Other Value, CASH,FEDWIRE)` |

Common enrichment maps settlement data to SWIFT fields:

- SCB Buy/Debit currency uses SCB Nostro and enriches Field 53.
- Client Sell/Credit currency uses client Vostro plus SCB Nostro and enriches Fields 58, 56, 57, and 53.
- Some Fixing templates also identify Field 54 as a receiving correspondent.

## Product extraction summary

| Product family | Extraction model | Lookup shape |
|---|---|---|
| FX Spot/Forward | `fxSingleLeg.exchangedCurrency1` and `exchangedCurrency2` | Two currencies; payer reference derives direction |
| Bullion Spot/Forward | `commodityForward.fxSingleLeg` | Two currencies, including precious-metal currencies such as `XPD` |
| FX Swap | `fxSwap.nearLeg` and `fxSwap.farLeg` | Four lookup legs |
| Bullion Swap | `strategy.fxSwap.nearLeg` and `farLeg` | Four lookup legs, including currencies such as `XAU` |
| NDIRS/IRS/NDCCS | `swap.swapStream[1]` and `[2]` | Two streams; both Credit and Debit Vostro queries |
| CCS/MTM CCS | Two swap streams plus possible `varyingNotionalCurrency` | Two stream currencies and a potentially varying MTM currency |
| Fixing | `fixingNoticePayload` | Settlement currency and payer-party reference from the Fixing Notice |

## Sample multi-leg API response

```js
{
  "trackingId": "MX_FXCXXXXXX",
  "tradeId": "111",
  "message": "<Base64 trade ssi enriched scbml>",
  "nearLegResult": [
    {
      "direction": "Buyer",
      "code": "700400325",
      "message": "SCB_RECEIVE_UNIQUE_NOSTRO",
      "vostroResult": "SUCCESS",
      "nostroResult": "SUCCESS"
    },
    {
      "direction": "Seller",
      "code": "700400323",
      "message": "SCB_PAY_UNIQUE_VOSTRO_UNIQUE_NOSTRO",
      "vostroResult": "SUCCESS",
      "nostroResult": "SUCCESS"
    }
  ],
  "farLegResult": [
    {
      "direction": "Buyer",
      "code": "700400325",
      "message": "SCB_RECEIVE_UNIQUE_NOSTRO",
      "vostroResult": "SUCCESS",
      "nostroResult": "SUCCESS"
    },
    {
      "direction": "Seller",
      "code": "700400323",
      "message": "SCB_PAY_UNIQUE_VOSTRO_UNIQUE_NOSTRO",
      "vostroResult": "SUCCESS",
      "nostroResult": "SUCCESS"
    }
  ]
}
```

Single-leg products use `singleLegResult` with the same direction, code, message, Vostro result, and Nostro result pattern.

## Source limitations

The document contains design examples rather than canonical, versioned schemas. Several areas require confirmation before implementation:

- The request hardcodes `settlementType` as `Cash`, while SCBML examples contain `Physical`.
- Direction rules use both `Party1` and `party1`.
- FX Swap currency-2 XPath rules appear to repeat `exchangedCurrency1`.
- Bullion Swap far-leg direction uses `receiverPartyReference`, unlike the ordinary FX Swap rule.
- The CCS/MTM CCS outbound template is empty.
- The Fixing outbound example is structurally incomplete and includes mock values.
- The endpoint, HTTP method, authentication, content type, timeout, payload limit, and formal versioning contract are unspecified.

See [[trade-ssi-stamping]] and [[ssi-product-template-mapping]] for the extracted implementation concepts.