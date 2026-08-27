---
type: entity
title: Camunda Task Bulk AmendRounding API
created: 2026-08-23
updated: 2026-08-23
tags: [api, camunda, manual-rounding, cashflow, bulk-processing]
related: [camunda, manual-rounding-amendment, maker-checker-rounding-workflow, cashflow-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md"]
---
# Camunda Task Bulk AmendRounding API

## Endpoint

```text
POST /v1/camunda/task/bulk/AmendRounding
```

## Supported actions

| Action | Workflow role | Documented purpose |
| --- | --- | --- |
| `AmendRounding` | Maker | Submit a manual change to the rounding amount |
| `Approve` | Checker | Approve the submitted amendment |
| `Reject` | Checker | Reject the submitted amendment |

Each request contains a `cashflows` array. The source demonstrates one cashflow per request and does not establish the behavior of multiple cashflows.

## Payload distinction

`AmendRounding` includes `amendAmount` and `currency`. `Approve` and `Reject` omit these fields and identify the cashflow and version to be reviewed.

The example changes `minorVersion` from `"5"` in the maker request to `"6"` in checker requests, while `businessVersion` and `cashflowVersion` remain `"0"`. The version transition requires confirmation before it is treated as an API invariant.

## Responses

Success:

```json
{
  "status": 200,
  "errorCode": "200",
  "errorMessage": "SUCCESS"
}
```

Documented connection failure:

```json
{
  "status": 500,
  "errorCode": "100500001",
  "errorMessage": "Connection refused: /10.198.199.166:25057",
  "metadata": null
}
```

The source does not define authorization, validation, idempotency, retry behavior, or the business result of approval and rejection.
