---
type: source
title: SSI Stamping Design
authors: []
year: 2022
url: ""
venue: Internal technical design
tags: [cash-settlement, ssi, stamping, adhoc-ssi, camunda, historical-design]
related: [ssi-stamping-service, adhoc-ssi-maker-checker-workflow, adhoc-ssi-exception-lifecycle, ssi-stamping-message-contract, what-is-the-authoritative-adhoc-ssi-api-contract, how-does-adhoc-ssi-maintain-query-service-and-blotter-consistency, what-are-the-two-new-ssi-exception-categories]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md"]
---
# SSI Stamping Design

This partial technical design describes the Adhoc SSI path of the SSI Stamping Service. It references external Confluence designs for the baseline SSI Stamping Flow and Adhoc Exception Design; those materials were not included in this ingest.

The illustrated calls use `localhost` and payload timestamps from 2022. They should be treated as historical contract examples, not as evidence of current production routing.

## Documented requirements

- A user may right-click a cashflow in `READY` status in the [[cashflow-blotter]] and select “Adhoc SI” to enter settlement instructions.
- If no SSI exception exists before a successful Maker submission, the service generates an exception and moves its sub-status to `PENDING_VERIFICATION`.
- If no SSI exception exists before Checker rejection, the service generates an exception and moves its sub-status to `PENDING_OPERATOR`.
- For CN, only Camunda is stated to call the SSI API, following the exception-fix processing pattern.

## API inventory

| API Name | Interface | Method |
| --- | --- | --- |
| Stamping cashflow | `http://{domain}/v1/stamping/cashflow/enrich` | Post |
| Stamping cashflow for accounting | `http://{domain}/v1/stamping/cashflow/accounting/enrich` | Post |
| Marker fix exception | `http://{domain}/v1/stamping/exception/{exception id}/fix` | Post |
| Query marker input data | `http://{domain}/v2/stamping/query/makerInput` | Post |
| Marker adhoc input data | `http://{domain}/v2/adhoc/ssis/makerInput/{cashflowId}` | Post |
| Checker approve exception fix data | `http://{domain}/v1/stamping/exception/{exception id}/approve` | Post |
| Checker reject exception fix data | `http://{domain}/v1/stamping/exception/{exception id}/reject` | Post |
| Checker adhoc reject stamping data | `http://{domain}/v2/adhoc/ssis/checker/reject/{cashflowId}` | Post |

## Adhoc Maker input contract

`POST /v2/adhoc/ssis/makerInput/{cashflowId}` accepts a versioned cashflow envelope. `metadata.requestBody` is a JSON-encoded string containing `fitVostro` and `fitNostro`, rather than a native nested JSON object.

```json
{
  "metadata": {
    "cashflowId": "String",
    "businessVersion": "String",
    "cashflowVersion": "String",
    "minorVersion": "String",
    "requestBody": "vostro and nostro info"
  },
  "trackingId": "String",
  "message": "cashflow xml"
}
```

The documented response shape is:

```json
{
  "trackingId": "String",
  "message": "cashflow xml",
  "metadata": {
    "exceptionStatus": "String",
    "cashflowId": "String",
    "minorVersion": "String",
    "cashflowVersion": "String",
    "businessVersion": "String"
  },
  "metadataList": [
    {
      "exceptionId": "ADHOC_SSI_EXCEPTION",
      "commonExceptionStatus": "PENDING_VERIFICATION"
    }
  ],
  "data": null,
  "camundaResponseCode": "SUCCESS/FILTERED",
  "description": null
}
```

The supplied Maker example uses `cashflowId` `888690236388` and the version tuple `businessVersion=2`, `cashflowVersion=1`, `minorVersion=1`. It returns `ADHOC_SSI_EXCEPTION` in `PENDING_VERIFICATION` with `camundaResponseCode` `SUCCESS`.

## Adhoc Checker rejection contract

`POST /v2/adhoc/ssis/checker/reject/{cashflowId}` uses the same identifying version tuple and transports the full SCBML cashflow XML.

```json
{
  "metadata": {
    "cashflowId": "String",
    "businessVersion": "String",
    "cashflowVersion": "String",
    "minorVersion": "String",
    "requestBody": null
  },
  "trackingId": "String",
  "message": "cashflow xml"
}
```

The documented response shape is:

```json
{
  "trackingId": "String",
  "message": "cashflow xml",
  "metadata": {
    "exceptionStatus": "String",
    "cashflowId": "String",
    "minorVersion": "String",
    "cashflowVersion": "String",
    "businessVersion": "String"
  },
  "metadataList": [
    {
      "exceptionId": "ADHOC_SSI_EXCEPTION",
      "commonExceptionStatus": "PENDING_OPERATOR"
    }
  ],
  "data": null,
  "camundaResponseCode": "SUCCESS/FILTERED",
  "description": null
}
```

The concrete rejection example instead returns `stampingId`, `cashflowBusinessVersion`, and `cashflowMinorVersion`, and reports `camundaResponseCode` `FILTERED` while creating `ADHOC_SSI_EXCEPTION` with `PENDING_OPERATOR`.

## Differences from BAU

| Num | Diff Part | Note |
| --- | --- | --- |
| 1 | Exception categories | Add two new exception |
| 2 | Exception generation processing | Exception generation timing |
| 3 | Cashflow status update event mechanism | not send notice to query service |
| 4 | Adhoc SSI handling | only call SSI API from camunda and same with fix exception processing |
| 5 | Get FM code | get FM code logic is change, and add `" ****** "` |
| 6 | only camunda call SSI API for CN | |
| 7 | SSI+ notifcation handling processing | |
| 8 | Vostro -> Nostro stamping processing | try best to stamping cashflow |

## Limitations and unresolved issues

The source does not define authentication, authorization, segregation of duties, audit, idempotency, concurrency, retry, timeout, failure, rollback, or approval-path behavior. It also does not explain the notification-suppression consistency mechanism for [[query-service]].

The stated `READY` eligibility conflicts with the supplied SCBML fixture’s `QUEUED` workflow state. The API inventory and concrete examples also disagree on use of ports `50001` and `60001`. These issues are tracked in [[what-is-the-authoritative-adhoc-ssi-api-contract]].