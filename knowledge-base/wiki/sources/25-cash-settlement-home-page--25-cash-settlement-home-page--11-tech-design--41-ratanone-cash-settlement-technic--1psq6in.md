---
type: source
title: Batch Limitation Check API Doc
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, api-contract, profile-limitation, bulk-processing, validation]
related: [profile-limitation-api, batch-profile-limitation-validation, what-is-the-canonical-batch-limitation-check-identifier-field, what-does-top-level-success-mean-for-batch-limitation-checks, what-service-and-data-source-own-profile-limitations]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Batch Limitation Check API Doc.md"]
authors: []
year: 0
url: ""
venue: ""
---
# Batch Limitation Check API Doc

This draft specifies a proposed batch API for validating cashflow amounts against profile and currency limitations in support of bulk submit, approve, and reject operations.

## Endpoint

```http
POST /v1/profileLimitation/checkLimitationsBatch
```

## Request contract

```json
{
  "items": [
    {
      "referenceId": "MD100",
      "currency": "USD",
      "amount": 9999
    },
    {
      "referenceId": "MD101",
      "currency": "CNY",
      "amount": 4000
    },
    {
      "referenceId": "MD102",
      "currency": "EPT",
      "amount": 8888
    }
  ]
}
```

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `items` | List | Yes | List of check items |
| `items[].referenceId` | String | Yes | cashflowId |
| `items[].currency` | String | Yes | Currency code |
| `items[].amount` | BigDecimal | Yes | Amount to check |

## Response contract

```json
{
  "results": [
    {
      "referenceId": "MD100",
      "currency": "USD",
      "amount": 9999,
      "success": false,
      "reason": "cannot get limitation for profile: USER_A, currency: USD"
    },
    {
      "referenceId": "MD101",
      "currency": "CNY",
      "amount": 4000,
      "success": true,
      "reason": ""
    },
    {
      "referenceId": "MD102",
      "currency": "EPT",
      "amount": 8888,
      "success": true,
      "reason": ""
    }
  ],
  "success": true,
  "reason": ""
}
```

| Field | Type | Description |
| --- | --- | --- |
| `results` | List | List of check results |
| `results[].referenceId` | String | cashflowId |
| `results[].currency` | String | Currency code |
| `results[].amount` | BigDecimal | Amount to check |
| `results[].success` | Boolean | Whether check is passed |
| `results[].reason` | String | Failure reason (if any) |
| `success` | Boolean | Whether check is passed |
| `reason` | String | Failure reason (if any) |

For null request parameters, the documented response is:

```json
{
  "results": null,
  "success": false,
  "reason": "Request items cannot be empty"
}
```

## Supplied HTTP example

```http
POST /v1/profileLimitation/checkLimitationsBatch
Content-Type: application/json
```

```json
{
  "items": [
    {
      "cashflowId": "MD100",
      "currency": "USD",
      "amount": 9999
    },
    {
      "cashflowId": "MD101",
      "currency": "CNY",
      "amount": 4000
    },
    {
      "cashflowId": "MD102",
      "currency": "EPT",
      "amount": 8888
    }
  ]
}
```

```json
{
  "results": [
    {
      "cashflowId": "MD100",
      "currency": "USD",
      "amount": 9999,
      "success": false,
      "reason": "cannot get limitation for profile: USER_A, currency: USD"
    },
    {
      "cashflowId": "MD101",
      "currency": "CNY",
      "amount": 4000,
      "success": true,
      "reason": ""
    },
    {
      "cashflowId": "MD102",
      "currency": "EPT",
      "amount": 8888,
      "success": true,
      "reason": ""
    }
  ],
  "success": true,
  "reason": ""
}
```

## Findings

The documented mixed-result response shows that a batch can be processed successfully while individual limitation checks fail. Clients must therefore inspect every entry in `results`, rather than treating top-level `success: true` as evidence that all cashflows passed.

The draft contains an unresolved identifier mismatch. Its field tables and initial payloads use `referenceId`, whereas the HTTP example uses `cashflowId`. Both are described as the cashflow identifier, but the canonical external JSON member is not specified. See [[what-is-the-canonical-batch-limitation-check-identifier-field]].

The source does not identify the owning service, profile source, limitation data source, authentication context, batch-size limit, HTTP status codes, amount-validation rules, ordering guarantee, or retry and idempotency behavior. See [[what-service-and-data-source-own-profile-limitations]].

This API is a specific instance of [[batch-profile-limitation-validation]] exposed through the proposed [[profile-limitation-api]]. It is adjacent to [[cn-rule-prevalidation]], but this source does not establish that any CN rule component implements the check.