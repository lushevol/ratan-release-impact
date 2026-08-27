---
type: concept
title: Cashflow Retrieval Concurrency Bottleneck
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, performance, concurrency, lifecycle, cash-settlement, api]
related: [bulk-exception-processing-performance, camunda-task-completion-bottleneck, ratan-cashflow-lifecycle-service, rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result.md"]
---

# Cashflow Retrieval Concurrency Bottleneck

Cashflow retrieval is a separate performance constraint in RATANONE Cash Settlement bulk processing. The checker flow retrieves cashflow information before completing workflow tasks.

## Observed latency

The source reports approximately 30 seconds to retrieve 1,000 `cashflowId` values through:

```text
GET /api/ratan/stmcn/v1/cashflows
```

An endpoint-level test measured 34.87 seconds for the same general workload. In the detailed checker breakdown, `checkUserLimitBasedProfileAccess`, including `cashFlowApiClient.getCashFlows`, accounted for 829 ms for one checker operation. These measurements represent different scopes and should not be combined as though they were the same request.

## Concurrency sensitivity

The source states that cashflow retrieval from Lifecycle becomes slower as concurrency increases. This indicates that improving Camunda completion alone may not remove the end-to-end bottleneck.

Potential investigation areas include:

- More efficient bulk query and pagination behavior.
- Smaller response projections.
- Reuse or preloading of cashflow data.
- Lifecycle database connection and query capacity.
- Request fan-out and application thread-pool behavior.
- Cache effectiveness and data freshness requirements.

## Scope boundary

Cashflow retrieval should be analyzed separately from profile limitation checking and Camunda task completion. The reported batch limitation-check latency was 657.41 ms in one 1,000-cashflow endpoint test, whereas cashflow retrieval and checker completion took tens or hundreds of seconds.
