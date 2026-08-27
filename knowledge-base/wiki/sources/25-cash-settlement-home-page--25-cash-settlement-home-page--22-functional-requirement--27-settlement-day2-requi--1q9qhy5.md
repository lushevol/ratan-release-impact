---
type: source
title: Manual Rounding API Design
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, manual-rounding, api-design, camunda, maker-checker]
related: [camunda, camunda-task-bulk-amend-rounding-api, manual-rounding-amendment, maker-checker-rounding-workflow, cashflow-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md"]
---
# Manual Rounding API Design

## Summary

This functional-requirement document specifies a Camunda task API for manual rounding changes to cashflows. The same endpoint supports three actions:

1. A maker submits a manual rounding amendment with `AmendRounding`.
2. A checker approves the amendment with `Approve`.
3. A checker rejects the amendment with `Reject`.

The document provides request and response examples but does not provide deployment evidence, execution logs, authentication requirements, validation rules, or confirmed post-action cashflow behavior.

## API endpoint

All three operations use:

```text
POST /v1/camunda/task/bulk/AmendRounding
```

The `/bulk/` path accepts a `cashflows` array. The examples contain one cashflow only, so multi-cashflow, atomicity, and partial-success behavior are not established.

## Documented API data

The source documents the following API entries:

| | method | url | request | response | comment |
| --- | --- | --- | --- | --- | --- |
| 1 | `POST` | /v1/camunda/task/bulk/AmendRounding | `{ "action": "**AmendRounding**", "comment": "1", "cashflows": [ { "cashflowId": "M00000049915", "businessVersion": "0", "cashflowVersion": "0", "minorVersion": "5", "amendAmount": "100.01", "currency": "USD", } ] }` | `{ "status": 200, "errorCode": "200", "errorMessage": "SUCCESS" }` or `{ "status": 500, "errorCode": "100500001", "errorMessage": "Connection refused: /10.198.199.166:25057", "metadata": null }` | maker manual change rounding |
| 2 | `POST` | /v1/camunda/task/bulk/AmendRounding | `{ "action": "**Approve**", "comment": "2", "cashflows": [ { "cashflowId": "M00000049915", "businessVersion": "0", "cashflowVersion": "0", "minorVersion": "6" } ] }` | `{ "status": 200, "errorCode": "200", "errorMessage": "SUCCESS" }` or `{ "status": 500, "errorCode": "100500001", "errorMessage": "Connection refused: /10.198.199.166:25057", "metadata": null }` | checker approve |
| 3 | `POST` | /v1/camunda/task/bulk/AmendRounding | `{ "action": "**Reject**", "comment": "2", "cashflows": [ { "cashflowId": "M00000049915", "businessVersion": "0", "cashflowVersion": "0", "minorVersion": "6" } ] }` | `{ "status": 200, "errorCode": "200", "errorMessage": "SUCCESS" }` or `{ "status": 500, "errorCode": "100500001", "errorMessage": "Connection refused: /10.198.199.166:25057", "metadata": null }` | checker reject |

## Request examples

The following examples preserve the documented request structures, with trailing commas removed so that they are valid standard JSON.

### Maker manual rounding amendment

```json
{
  "action": "AmendRounding",
  "comment": "1",
  "cashflows": [
    {
      "cashflowId": "M00000049915",
      "businessVersion": "0",
      "cashflowVersion": "0",
      "minorVersion": "5",
      "amendAmount": "100.01",
      "currency": "USD"
    }
  ]
}
```

### Checker approval

```json
{
  "action": "Approve",
  "comment": "2",
  "cashflows": [
    {
      "cashflowId": "M00000049915",
      "businessVersion": "0",
      "cashflowVersion": "0",
      "minorVersion": "6"
    }
  ]
}
```

### Checker rejection

```json
{
  "action": "Reject",
  "comment": "2",
  "cashflows": [
    {
      "cashflowId": "M00000049915",
      "businessVersion": "0",
      "cashflowVersion": "0",
      "minorVersion": "6"
    }
  ]
}
```

## Response examples

### Success

```json
{
  "status": 200,
  "errorCode": "200",
  "errorMessage": "SUCCESS"
}
```

### Connection failure

```json
{
  "status": 500,
  "errorCode": "100500001",
  "errorMessage": "Connection refused: /10.198.199.166:25057",
  "metadata": null
}
```

The same success and failure alternatives are documented for all three actions. The source does not identify the service expected at `10.198.199.166:25057`; the address may be environment-specific.

## Observed workflow and versioning

The maker payload includes `amendAmount` and `currency`, while the checker payloads do not. This indicates that the amendment value is supplied during maker submission and that approval or rejection acts on an existing workflow item.

The example uses:

- `minorVersion: "5"` for the maker request.
- `minorVersion: "6"` for both checker requests.
- `businessVersion: "0"` and `cashflowVersion: "0"` throughout.

This suggests a minor revision transition between submission and review, but the document does not define whether the transition is mandatory, automatic, or calculated by another service.

## Limitations and implementation cautions

- The source does not define authentication or authorization.
- It does not establish that maker and checker users must be different.
- It does not define required fields, data types, amount precision, or currency validation.
- It does not describe the effect of approval or rejection on the cashflow.
- It does not specify whether bulk requests are atomic, independently processed, or partially successful.
- The maker example contains trailing commas and is not valid standard JSON if copied literally.
- The document is an interface specification, not evidence that the endpoint is deployed or operational.
- No relationship to `Murex`, `LMS`, `FMSGW`, or `RATAN` is established by this source.

See [[manual-rounding-amendment]], [[maker-checker-rounding-workflow]], and [[cashflow-versioning]] for the business and technical concepts extracted from this document.
