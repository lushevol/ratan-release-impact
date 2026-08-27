---
type: source
title: Cashflow Query API Optimization
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, api, performance, netting, optimization]
related: [ratan-cashflow-lifecycle-service, cashflow-query-api-performance-optimization, what-are-the-validated-production-latency-and-capacity-results-for-cashflow-query-optimization, what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query, what-data-does-ratan-cash-settlement-ssi-stamping-service-require-from-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Cashflow query api optimization.md"]
---
# Cashflow Query API Optimization

This source describes a proposed performance optimization for cashflow-detail retrieval in [[ratan-cashflow-lifecycle-service]], a component of [[ratan]]. It identifies the APIs, callers, table-backed data needs, selected production observations, and three proposed approaches: category-based fetching, batch query, and multithreaded request processing.

## APIs and implementation references

```text
Service: RATAN-CASHFLOW-LIFECYCLE-SERVICE

API:
- /v1/ratan/cashflow/query
- /v1/ratan/cashflow/query/cashflowIds

Controller:
com.scb.ratan.cashflow.lifecycle.lifecycle.entrypoint.CashflowLifecycleController#queryCashflowDataByCashflowIds
```

```text
Branch:
feature/cashflowDetailOptimization-0912

Repository URL:
https://dev.azure.com/sc-ado/777f0ba6-cfdf-4f44-99dd-ae1dc434f5c5/_git/51358-ratan-cashflow-lifecycle-service?version=GBfeature/cashflowDetailOptimization-0912

Branch comparison:
https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-cashflow-lifecycle-service/branchCompare?baseVersion=GBmain&targetVersion=GBfeature/cashflowDetailOptimization-0912&_a=files
```

The implementation references are hosted in [[ado]]. The source does not state whether the branch was merged, deployed, or validated in production.

## Related data sources

| No. | Table name | Field information |
|---:|---|---|
| 1 | `ratan_cashflow_scbml_history` | `15 fields` |
| 2 | `Ratan_Cashflow_Scbml_Message` | `message entity` |
| 3 | `ratan_cashflow_cutoff_info` | `queuedCutoff` |
| 4 | `ratan_cashflow_affirmation_status` | `affirmationDetails`: `String affirmedBy; String phone_email; Timestamp affirmedAt;` |
| 5 | `ratan_stella_message_event_source` | `41 fields` |

No DDL, index definitions, join conditions, query plans, or cardinality evidence is included. The source therefore does not establish the database-level cause of latency.

## Caller compatibility inventory

| Caller service | API and request pattern | Required response data |
|---|---|---|
| `ratan-cash-settlement-accounting-service` | `/v1/ratan/cashflow/query`; single `cashflowId` | `ratan_stella_message_event_source`: `murexStrategy`, `settlementType` |
| `ratan-cash-settlement-batch-service` | `v1/ratan/cashflow/query`; single `cashflowId` | `ratan_cashflow_scbml_history`: `cashflowStatus`, `subStatus`, `subStatusEventType`, `cashflowId`, `businessVersion`, `minorVersion`, `cashflowVersion` |
| `ratan-cash-settlement-group-management-service` | `/v1/ratan/cashflow/query` | `TradeConfirmedEventHandler#filterCashflows`: `cashflowStatus`, `subStatusEventType`, `cashflowId`; `TradeLienPlacementEventHandler#doHandle`: `cashflowStatus`, `subStatusEventType`, `cashflowId`, `businessVersion`, `minorVersion`, `nettingId` |
| `ratan-cash-settlement-lms-service` | `/v1/ratan/cashflow/query`; single `cashflowId` | `ratan_cashflow_scbml_history`; `Ratan_Cashflow_Scbml_Message` |
| `ratan-rule-service` | `/v1/ratan/cashflow/query`; single `cashflowId` | `ratan_cashflow_scbml_history`: `affirmationStatus`, `businessVersion`, `minorVersion` |
| `ratan-cash-settlement-query-service` | `/v1/ratan/cashflow/query`; multiple `cashflowIds` | `ratan_cashflow_affirmation_status`: `affirmedBy`, `phone_email`, `affirmedAt` |
| `ratan-cash-settlement-ssi-stamping-service` | `/v1/ratan/cashflow/query`; unspecified | Not specified |
| `ratan-cash-settlement-netting-service` | `/v1/ratan/cashflow/query/cashflowIds`; single or multiple `cashflowIds` | Lifecycle, event-source, and message data according to operation |

The varied requirements support [[cashflow-query-api-performance-optimization]], but they also make response-contract compatibility a critical constraint. In particular, netting and lien-related flows depend on lifecycle state, versions, and `nettingId`; see [[lien-aware-netting-and-auto-unnetting]] and [[trade-lien-notification-reconciliation]].

## Netting-service operations

| Operation | Request pattern | Required response data |
|---|---|---|
| `DefaultRsultantCompensateProcessor.process` | Single `cashflowId` | `ratan_cashflow_scbml_history.action`; `ratan_stella_message_event_source.tradeId`, `originatingTradeId`, `CaptureSystem (dataSourceSystem)`; `Ratan_Cashflow_Scbml_Message.message` |
| `com.cn.ratan.netting.application.service.UnNettingService#unNetCashflowWithLock` | Single `cashflowId` | `ratan_cashflow_scbml_history.businessVersion`, `cashflowVersion`, `minorVersion`, `nettingId`, `valueDate`; `ratan_stella_message_event_source.settlementCurrency` |
| `com.cn.ratan.netting.application.service.splitting.AmountAmendService#amendAmount(com.cn.ratan.netting.entrypoint.web.request.splitting.AmountAmendRequests, java.util.List<com.cn.ratan.netting.domain.splitting.SplittingCashflow>)` | Multiple `cashflowIds` | `ratan_cashflow_scbml_history.cashflowStatus`, `cashflowId`, `businessVersion`, `cashflowVersion`, `minorVersion`; `ratan_stella_message_event_source.settlementCurrency`, `settlementAmount`; `Ratan_Cashflow_Scbml_Message.message` |
| `com.cn.ratan.netting.application.service.splitting.SplittingService#splitCashflowWithLock` | Multiple `cashflowIds` | `ratan_cashflow_scbml_history.cashflowStatus`, `cashflowId`, `splittingId`; `ratan_stella_message_event_source.settlementAmount`, `payerParty` |

## Production timing observations

| Cashflow count | Total time | Stated average |
|---:|---:|---:|
| 1 | 34 ms | 34 ms |
| 2 | 58 ms | 29 ms |
| 5 | 91 ms | 18 ms |
| 13 | 395 ms | 30 ms |
| 57 | 757 ms | Not supplied |
| 107 | 3,973 ms | 37 ms |
| 1,487 | 9,624 ms | 6 ms |

The observations indicate material end-to-end latency at high request volumes. The stated per-cashflow averages do not establish a consistent linear cost model and should not be used alone to judge acceptability.

The source supplies no percentiles, repetition count, workload definition, payload size, service-level objective, database metrics, or resource-saturation measurements.

## Proposed optimization directions

1. Fetch by category.
2. Batch query.
3. Multithreaded request processing.

Development before-and-after screenshots exist for requests containing 1, 4, 50, 100, 150, and 300 cashflows, but their numeric results are not available as structured data in the source. They do not substantiate a quantified improvement.

## Constraints and follow-up

A selective or parallel implementation must preserve the data, ordering, error, consistency, and locking expectations of callers, especially for compensation, unnetting, splitting, amount amendment, and lien-placement workflows.

Open validation is tracked in:
- [[what-are-the-validated-production-latency-and-capacity-results-for-cashflow-query-optimization]]
- [[what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]]
- [[what-data-does-ratan-cash-settlement-ssi-stamping-service-require-from-cashflow-query]]