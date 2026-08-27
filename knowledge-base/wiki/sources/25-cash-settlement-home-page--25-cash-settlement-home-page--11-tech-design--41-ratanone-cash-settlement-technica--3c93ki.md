---
type: source
title: Uber Development Testing Questions
authors: []
year: 2025
url: ""
venue: "RATANONE Cash Settlement technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, RATANONE, Uber, integration-testing, Camunda, lifecycle, netting]
related: [uber, ratanone, camunda, ratan-cashflow-lifecycle-service, ratan-cash-settlement-netting-service, ratan-cash-settlement-orchestration, accounting-service, cash-settlement-cashflow-domain-events, process-in-topic, cashflow-action-time-format, process-in-publication-contract, reinstatement-domain-event-history, automatic-un-netting-error-handling, materialize-process-in-publication, cashflow-lifecycle-state-machine-restructuring, cashflow-status-restoration, kafka-persistent-retry-and-dlt-recovery, product-agnostic-cashflow-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---

# Uber Development Testing Questions

## Scope

This document records development-testing findings for the RATANONE Cash Settlement [[entities/uber|Uber]] integration. The notes cover cashflow lifecycle actions, Swift suppression and unsuppression, accounting updates, manual and automatic un-netting, bulk submission, reinstatement, Camunda orchestration, SettleAsGross, and Materialize.

The source contains a mixture of reported fixes, passed cases, unresolved requirements, and runtime failures. “Fixed” and “Passed” are preserved as reported statuses; the document does not consistently provide post-fix traces, acceptance criteria, message identifiers, or complete test evidence.

Testing references and screenshots indicate activity around 27–29 August 2025.

## Test findings

| Area | Identifier(s) | Reported result | Finding |
|---|---|---|---|
| FMO action time | `C06810140003` | Fixed; format awaiting confirmation | The `actionTime` implementation was reportedly fixed, but its authoritative format remains unspecified. |
| Lifecycle holding check | `C06810140004` | Failed | The holding-check endpoint returned HTTP 500 while parsing an ISO timestamp with a `Z` suffix. |
| Swift suppression and accounting | `C06810140005` | Fixed | Accounting-service SSI-stamp URL and parameters were updated; accounting-service version was updated to `2.0.0`. |
| Swift unsuppression approval | `C06810140005` | Unresolved | The lifecycle service did not publish to the `process-in` topic after approval. |
| Process-in publication | `N00000062629` | Fixed | A missing publication to the `process-in` topic was reported as fixed. |
| Manual un-netting | `N00000062629` | Fixed | The manual un-net path previously did not call Query Service. |
| UI un-netting call | `N00000062629` | Requirement/observation | The UI un-net operation calls the Swift suppress/unsuppress approval API. |
| Automatic un-netting endpoint | `N00000062630`, `C06810140005`, `C06810141005` | Failed | The orchestration call returned “No static resource” for the `autoUnNet` endpoint. |
| Automatic un-netting payload | `N00000062630`, `C06810140005`, `C06810141005` | Fixed | A separate failure reported `Payload must not be null`. |
| Bulk submit | `C06810142008`, `C06810142009` | Passed | Bulk-submit case 13 passed. |
| Reinstatement API and UI | `C06810142008`, `C06810142009` | Change recorded | The UI calls `/v2/ratan/cashflow/move/status/user`; the SCBML field should be removed. |
| Reinstatement failure and history | `C06810142009` | Fixed | The Camunda task-fail API was called, but UI history missed the event because of a message-format error. |
| SettleAsGross | `CH6800724464` | Requirement recorded | The action must publish to the `process-in` topic. |
| Camunda orchestration | Not specified | Passed | An “orchestration 1_1” Camunda modification was marked passed; the modified behavior is not described. |
| Materialize | `C07810140013` | Unresolved | A Materialize action error was recorded, together with an open question about whether lifecycle must publish to `process-in`. |

## Exact runtime errors

### Lifecycle holding-check parsing error

```text
Exception happened -- [http://ratan-cashflow-lifecycle-service/v1/cashflow/camunda/holding-check], ReplayTopic is [Settlement_Orchestration_Adhoc_Ssi], Exception reason is [[500 ] during [POST] to [[http://ratan-cashflow-lifecycle-service/v1/cashflow/camunda/holding-check]] [CommonServiceCaller#execute(URI,CamundaApiRequest)]: [{"status":500,"errorCode":"SERVICE_INTERNAL_ERROR","errorMessage":"Text '2025-09-19T18:00:00Z' could not be parsed, unparsed text found at index 19","metadata":null}]]
```

The parser rejected the observed timestamp at index 19, immediately after the seconds component. The evidence demonstrates the failure but does not establish whether the cause is rejection of the `Z` suffix, an expected local timestamp format, or another parser constraint.

The error identifies `Settlement_Orchestration_Adhoc_Ssi` as a replay topic. The source does not define whether replay is safe after payload correction or whether the event must be reconstructed.

### Automatic un-netting endpoint error

```text
ratan-cash-settlement-orchestration || STELLA.1755538990974.6b9cc4d8-5a42-4e02-8ef8-721306996a8c-1-1_1001 || Stella || RAZOR || null || Exception happened -- [http://ratan-cash-settlement-netting-service/v2/netting/camunda/autoUnNet], ReplayTopic is [null], Exception reason is [[500 ] during [POST] to [[http://ratan-cash-settlement-netting-service/v2/netting/camunda/autoUnNet]] [CommonServiceCaller#execute(URI,CamundaApiRequest)]: [{"status":500,"message":"No static resource v2/netting/camunda/autoUnNet.","data":null}]]
```

This is consistent with an unavailable, incorrectly routed, or incorrectly mapped endpoint. The evidence does not distinguish between an incorrect path, deployment mismatch, and gateway-routing problem.

### Automatic un-netting null-payload error

```text
com.cn.ratan.netting.domain.common.error.NettingServiceException: Payload must not be null
        at com.cn.ratan.netting.application.service.UnNettingService.unNetCashflow(UnNettingService.java:188)
        at com.cn.ratan.netting.application.service.UnNettingService.lambda$unNetCashflowWithLock$3(UnNettingService.java:146)
        at com.scb.ratan.service.template.ResourceLockManager.run(ResourceLockManager.java:72)
        at com.cn.ratan.netting.application.service.UnNettingService.unNetCashflowWithLock(UnNettingService.java:129)
        at com.cn.ratan.netting.application.service.UnNettingService.lambda$autoUnNet$1(UnNettingService.java:102)
```

The null-payload exception is distinct from the missing-resource error. It indicates that the netting service reached `UnNettingService` but received no usable payload.

### Reinstatement history message-format error

The reinstatement failure involved the following API:

```text
https://fmo-mfe-dev.uk.dev.net:8453/api/ratan/v1/camunda/task/fail
```

The source reports that the fail action called the API, but the UI history did not show the event because of a message-format error on:

```text
cash_settlement_cashflow_domain_events
```

## Integration behavior captured by the test notes

The test evidence distinguishes several side effects that should not be treated as equivalent:

1. A UI action can invoke a command API.
2. Camunda can accept or fail a task.
3. A lifecycle or orchestration service can publish a domain event.
4. A downstream service can process the event.
5. Query Service or UI history can project the resulting event.

The reinstatement result demonstrates that successful command invocation does not guarantee domain-event publication or UI-history visibility. Similarly, the process-in findings indicate that publication behavior must be specified per lifecycle action rather than inferred globally.

Manual and automatic un-netting are separate paths. Manual un-netting was associated with a missing Query Service call, whereas automatic un-netting exposed both endpoint/resource and null-payload failures.

## Open contract questions

- What is the authoritative `actionTime` format: local timestamp, UTC timestamp, or ISO-8601 with `Z`?
- Which lifecycle actions must publish to the `process-in` topic?
- Does Materialize publish to `process-in`, and under what conditions?
- What is the canonical API path and request payload for `autoUnNet`?
- Is the `cash_settlement_cashflow_domain_events` message schema versioned and validated?
- How should a successful Camunda task failure or reinstatement appear in UI history?
- What evidence is required before a defect is formally considered fixed?
- Is `Settlement_Orchestration_Adhoc_Ssi` the approved replay mechanism, and what recovery procedure governs it?

## Evidence limitations

The source does not provide a complete test environment, author, formal status, expected-versus-actual assertions, message IDs, timing measurements, or complete post-fix traces. Screenshot-only evidence is referenced by the original notes but is not independently interpreted here.

This document should be read alongside the broader [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1isntku|RATAN - Uber Integration Technical Design]] and the existing lifecycle, status-restoration, netting, and Kafka-recovery pages.