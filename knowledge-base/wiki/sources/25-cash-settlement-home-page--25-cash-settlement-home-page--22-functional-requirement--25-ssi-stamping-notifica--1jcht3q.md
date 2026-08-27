---
type: source
title: SSI Stamping Tech Design — Egypt
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page / Functional Requirement / SSI Stamping Notification / FMRP - SSI Stamping Flow"
created: 2026-08-23
updated: 2026-08-23
tags: [ssi-stamping, scbml, fmrp, settlement-instructions, ratan, technical-design]
related: [ssi-stamping-service, fmrp, scbml, ssi-stamping, vostro-nostro-ssi-matching, scbml-trade-enrichment-api, ssi-stamping-product-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# SSI Stamping Tech Design — Egypt

## Scope

This technical design describes an SSI Stamping service that accepts a Base64-encoded SCBML trade or confirmation message, resolves Vostro and Nostro settlement instructions, and returns an enriched SCBML message with leg-level resolution results.

The filename identifies Egypt, but the concrete confirmation sample contains `countryCode` `KE` and the legal entity `SCBLKEN*NBO`. The country scope therefore requires confirmation before this document is treated as Egypt-specific.

The endpoint shown is a UAT endpoint. The document does not establish production availability or production operational behavior.

## Enrichment endpoint

| Environment | URL |
| --- | --- |
| UAT | `https://ratan-api.uk.dev.net:8453/v1/stampings/trade/enrich` |

```http
POST /v1/stampings/trade/enrich
Authorization: Basic base64encode(username+":"+password）
```

The source contained a concrete Basic-auth credential. It is intentionally omitted from this summary. Credentials should be stored in an approved secret-management system and rotated or revoked if the source value remains valid.

## Request body

```js
{
  "trackingId": "MX_FXCASH_CONF_XXXX",
  "tradeId": "111",
  "productType": "spot",
  "message": "<Base64 trade scbml>"
}
```

The `message` field contains a Base64-encoded SCBML message.

## Response body: single-leg products

The single-leg response model applies to Spot, Forward, Bullion Spot, Bullion Forward, IRS, NDIRS, and NDCCS.

```js
{
  "trackingId": "MX_FXCXXXXXX",
  "tradeId": "111",
  "message": "<Base64 trade ssi enriched scbml>",
  "singleLegResult": [
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

## Response body: multi-leg products

The multi-leg response model applies to Swap, CCS, Bullion Swap, and MTM CCS.

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

## Response-code catalogue

| HTTP status | SCB Pay / sell result | SCB Receive / buy result |
| --- | --- | --- |
| `200` | `SCB_PAY_UNIQUE_VOSTRO_UNIQUE_NOSTRO` (`700400323`) | `SCB_RECEIVE_UNIQUE_NOSTRO` (`700400325`) |
| `400` | `SCB_PAY_BLANK_VOSTRO_DEFAULT_NOSTRO` (`700400320`); `SCB_PAY_BLANK_VOSTRO_BLANK_NOSTRO` (`700400321`); `SCB_PAY_UNIQUE_VOSTRO_BLANK_NOSTRO` (`700400322`); `CLIENT_DATA_INVALID_EXCEPTION` (`700400001`); `NOT_DEFINED_SCENARIO_ERROR` (`700400326`) | `SCB_RECEIVE_BLANK_NOSTRO` (`700400324`); `CLIENT_DATA_INVALID_EXCEPTION` (`700400001`); `NOT_DEFINED_SCENARIO_ERROR` (`700400326`) |
| `500` | `STAMPING_SERVICE_IO_EXCEPTION` (`700500002`) | Not specified |

Allowed `vostroResult` and `nostroResult` values are:

```text
SUCCESS
MISSING_VOSTRO_ERROR
MULTI_VOSTRO_ERROR
MISSING_NOSTRO_ERROR
MULTI_NOSTRO_ERROR
DEFAULT_NOSTRO
```

## Query parameters

### CDU-provided trade parameters

| Query parameter | Data source or rule | Path status |
| --- | --- | --- |
| Legal Entity FMID | `/scb:SCBML/scb:payload/scb:FPMLPayload/conf:party[1]/conf:partyId[1]][partyIdScheme="http://www.sc.com/coding-scheme/partyId/FMID"]` | Yes |
| Counterpart FMID | `/sc:SCBML/scb:payload/scb:FPMLPayload/conf:party[2]/conf:partyId[@partyIdScheme="http://www.sc.com/coding-scheme/partyId/FMID"]` | Yes |
| Payment Currency | Parsed as a list from the XML and identified by SSI Stamping service logic | Partially specified |
| Product type / CFI Code | Product mapping is defined below; source path remains open | Open |
| Settlement Method | Intended query parameter | Wait for confirmation |
| Settlement Type | Intended query parameter | Wait for confirmation |
| Debit/Credit | Derived from SCBML by SSI Stamping service logic; `Credit: SCB (Payer)`, `Debit: SCB (receiver)` | Not applicable |
| SSI Status | Hard-coded as `"Active"`, `"New"`, or `"Update"` | Selection rule open |

### Vostro query parameters

| Query parameter | Data source or rule |
| --- | --- |
| Counterpart FMID | `/scb:SCBML/scb:payload/scb:party[@id='party2']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` |
| Branch FM Code | Obtained from SSI Stamping service query logic |
| Currency | Parsed from XML and identified by SSI Stamping service logic |
| CFI Code | Default `*F****`; confirmation pending |
| Settlement Method | Default `cash`; confirmation pending |
| Settlement Type | Default `cash`; confirmation pending |
| Debit/Credit | Derived by SSI Stamping service logic; `Credit: SCB (Payer)`, `Debit: SCB (receiver)` |
| SSI Status | Hard-coded as `"Active"`, `"New"`, or `"Update"` |

### Nostro query parameters

| Query parameter | Data source or rule |
| --- | --- |
| Legal Entity FMID | `/scb:SCBML/scb:payload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` |
| Payment Currency | Parsed from XML |
| Settlement Means | Obtained from Vostro query result |
| Settlement Account | Obtained from Vostro query result |
| Default Nostro | `Currency + MAIN` |

The XPath expressions in the source contain apparent syntax and namespace inconsistencies. They require validation before implementation.

## Matching scenarios

For SCB Pay / sell currency:

| Vostro result | Nostro result | API result | Confirmation enrichment |
| --- | --- | --- | --- |
| Missing or multiple Vostro | Default Nostro | Blank Vostro + Default Nostro | Enrich SCB account details; counterparty account information is `Please advise` |
| Missing or multiple Vostro | Missing Nostro | Blank Vostro + Blank Nostro | SCB account information is `To Be Advise`; counterparty account information is `Please advise` |
| Unique Vostro | Missing or multiple Nostro | Unique Vostro + Blank Nostro | SCB account information is `To Be Advise`; enrich counterparty account details |
| Unique Vostro | Unique Nostro | Unique Vostro + Unique Nostro | Enrich both parties' account details |

For SCB Receive / buy currency:

| Nostro result | API result | Confirmation enrichment |
| --- | --- | --- |
| Missing or multiple Nostro | Blank Nostro | SCB account information is `To Be Advise` |
| Unique Nostro | Unique Nostro | Enrich SCB account details |

`To Be Advise` and `Please advise` are retained as source-system text and should not be grammatically normalized without domain-owner confirmation.

## Product-to-CFI mapping

| Product type | CFI Code |
| --- | --- |
| FX Spot | `I-F-X-X-X-X` |
| FX Forward | `J-F-X-X-X-X` |
| FX Swap | `S-F-X-X-X-X` |

The source marks the product mapping as closed, while the SCBML field paths for CFI Code, Settlement Method, and Settlement Type remain open.

## Technical implementation direction

The design retains the existing implementation for existing products and uses a refactored implementation for new products such as Bullion Spot and Bullion Forward.

The stated reasons for refactoring are:

- SCBML XPath expressions were upgraded to XPath 2.0, while the existing expressions use XPath 1.0.
- The existing SCBML generation uses product-specific templates, which limits reuse.

The source does not define product-routing controls, parity tests, ownership, rollout criteria, reconciliation controls, or legacy-path retirement criteria.

## Data model

The source includes an image for `trade_stamping_service`. No reliable SQL DDL, fields, keys, indexes, or constraints are available for transcription.

## Open questions and risks

- Confirm whether the design is Egypt-specific or whether the Kenyan sample is intentional.
- Define authoritative XPath 2.0 expressions and namespace bindings.
- Define canonical product classification precedence across `productType`, `productId`, subtype, and typology fields.
- Confirm production endpoint, authentication, credential rotation, timeout, retry, idempotency, logging, and monitoring behavior.
- Clarify whether enriched SCBML is returned for business-match outcomes represented by HTTP `400`.
- Establish governance for default Vostro values and SSI status values.
- Obtain the underlying `trade_stamping_service` schema.
- Define parity and migration controls for legacy and refactored implementations.
- Confirm the stated debit/credit terminology, which is counterintuitive in common accounting usage.

## Related pages

- [[entities/ssi-stamping-service]]
- [[entities/ratan]]
- [[entities/razor]]
- [[entities/fmrp]]
- [[entities/scbml]]
- [[concepts/ssi-stamping]]
- [[concepts/vostro-nostro-ssi-matching]]
- [[concepts/scbml-trade-enrichment-api]]
- [[concepts/ssi-stamping-product-mapping]]
- [[queries/what-are-the-authoritative-scbml-paths-for-ssi-stamping-query-fields]]
- [[queries/what-is-the-canonical-ssi-stamping-product-classification-precedence]]
- [[queries/what-is-the-production-security-and-operational-contract-for-the-ssi-stamping-api]]