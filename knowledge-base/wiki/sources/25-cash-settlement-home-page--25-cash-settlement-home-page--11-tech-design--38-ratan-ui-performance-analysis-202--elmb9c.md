---
type: source
title: Ratan UI Performance Analysis (2022 Dec)
authors: []
year: 2022
url: ""
venue: "Cash Settlement Home Page technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, ui-performance, cash-settlement, graphql, restful-api, lighthouse]
related: [ratanone, ratanone-ui-performance, ui-performance-metrics, frontend-configuration-loading, iframe-micro-frontend-loading-priority, graphql-vs-restful-cashflow-querying, graphql, lighthouse, postman, single-spa, cashflow-blotter, static-configuration-management, config-server]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# Ratan UI Performance Analysis (2022 Dec)

## Summary

This December 2022 technical-design document analyzes [[ratanone]] UI loading performance and compares GraphQL with RESTful API access for the CN Cash Settlement cashflow blotter. It combines Lighthouse measurements, browser performance timings, local concurrency tests, staging comparisons, and architectural proposals.

The source identifies three major performance concerns:

1. RatanOne interactivity degrades as more blotters are composed.
2. Synchronous loading of multiple configuration JSON files delays JavaScript execution and first meaningful paint.
3. iFrame-based micro-frontend composition does not provide deterministic loading priority.

It also evaluates GraphQL as a request-shaping and response-size optimization. The results are mixed locally but substantially favor GraphQL for the tested staging queries.

## UI performance metrics

The source distinguishes generic browser metrics from workflow-specific metrics. The proposed custom targets are:

| Metric | Description | Target |
| --- | --- | --- |
| Cashflow Loaded | Time from cashflow blotter initialization to display of the first data table | < 3 sec |
| Cashflow Table Loaded | Time from cashflow table initialization to display of the first data table | < 300 ms |
| Cashflow Quick Search Interaction | Time from clicking search to display of the result | < 500 ms |
| Cashflow Custom Search Interaction | Time from changing custom search or view to display of the result | < 1000 ms |

The reference thresholds included in the source are:

| Metric | Good | Needs improvement | Poor |
| --- | --- | --- | --- |
| FCP | < 1.8 sec | 1.8–3.0 sec | > 3 sec |
| LCP | < 2.5 sec | 2.5–4.0 sec | > 4 sec |
| FID | < 100 ms | 100–300 ms | > 300 ms |
| TTI | Reduce the gap between FCP and TTI | — | — |
| TBT | Reduce TBT | — | — |

See [[ui-performance-metrics]] for definitions and interpretation.

## RatanOne benchmark

The benchmark used UAT Office Network workspace configurations:

| Case | Description |
| --- | --- |
| I | Workspace 1: Cashflow Blotter; Workspace 2: none |
| II | Workspace 1: Cashflow Blotter, Suppression Rules, and Validation Exception in the first screen; Workspace 2: none |
| III | Workspace 1: Cashflow Blotter and Trade Blotter in the first screen; Validation Exception and Settlement Exceptions in the second screen |
| IV | Workspace 1: Cashflow Blotter and Trade Blotter in the first screen; Validation Exception and Settlement Exceptions behind the first screen |

| Case | FCP | TTI | TBT | LCP | Performance score |
| --- | ---: | ---: | ---: | ---: | ---: |
| I | 1.9 sec | 8.8 sec | 2000 ms | 3.1 sec | 27 |
| II | 1 sec | 9.2 sec | 4350 ms | 2.2 sec | 27 |
| III | 1.9 sec | 13.7 sec | 5340 ms | 3.1 sec | 17 |
| IV | 1.7 sec | 19.8 sec | 14100 ms | 3.3 sec | 13 |

TTI increased from 8.8 seconds to 19.8 seconds, while TBT increased from 2,000 ms to 14,100 ms as the composed workspace became more complex. The source cautions that the absolute Lighthouse scores were affected by a poorly performing notebook; the relative degradation across cases is therefore more useful than the absolute scores.

## Configuration-loading benchmark

Each blotter application synchronously loads separate configuration JSON files, delaying `main.js` execution. The reported timings are:

```text
| Action | Duration | Total Time |
| load-config-start | 0 | 0 |
| load-ratanConfig-done | 315.60 | 315.60 |
| load-cashflowDetailsConfig-done | 276.20 | 591.80 |
| load-cashflowDetailsConfig-done | 274.60 | 866.40 |
| load-tradeDetailsConfig-done | 276.30 | 1142.70 |
| load-tradesConfig-done | 265.50 | 1408.20 |
| load-exceptionConfig-done | 267.70 | 1675.90 |
| load-cashflowConfig-done | 0.00 | 1675.90 |
| set-config-done | 0.20 | 1676.10 |
| mount-app | 2170.60 | 3846.70 |
| FMP: mount-cashflow-grid | 610.70 | 4457.40 |
```

A second unzipped benchmark reported:

```text
| Action | Duration | Total Time |
| load-config-start | 0 | 0 |
| load-ratanConfig-done | 314.60 | 314.60 |
| load-cashflowDetailsConfig-done | 285.20 | 599.80 |
| load-cashflowDetailsConfig-done | 290.00 | 889.0 |
| load-tradeDetailsConfig-done | 288.30 | 1178.10 |
| load-tradesConfig-done | 285.20 | 1463.30 |
| load-exceptionConfig-done | 286.70 | 1750.00 |
| load-cashflowConfig-done | 0.00 | 1750.00 |
| set-config-done | 0.10 | 1750.10 |
| mount-app | 435.30 | 2185.40 |
| FMP: mount-cashflow-grid | 708.60 | 2894.00 |
```

The zipped configuration benchmark reported:

```text
| Action | Duration | Total Time |
| load-config-start | 0 | 0 |
| load-zippedConfig-done | 257.60 | 257.60 |
| load-config-all-done | 0.20 | 257.80 |
| set-config-done | 0.00 | 257.80 |
| mount-app | 343.90 | 601.70 |
| FMP: mount-cashflow-grid | 424.30 | 1026.00 |
```

The zipped approach reduced the configuration phase from approximately 1.68–1.75 seconds to 0.26 seconds and reduced the reported time to cashflow-grid FMP to 1.03 seconds. The proposed [[frontend-configuration-loading]] solution also includes HTTP and server-side caching, synchronization, versioning, auditability, DEVOPS hooks, and policy-based access control.

## iFrame loading

The source reports that a blotter in the first screen can load after a blotter in the second screen or behind it. The shell does not arrange loading priority among iFrame applications, and adding more blotters makes progress slower and harder to interpret.

Proposed remedies are:

- Render skeleton layouts before embedded applications load.
- Add explicit loading-priority control.
- Share loading status through `ratan-message`.
- Load applications on demand where possible.

See [[iframe-micro-frontend-loading-priority]].

## GraphQL and RESTful API comparison

The tested CN Cash Settlement query-service request used 10,000,000 database records and requested the same logical result through GraphQL and RESTful APIs.

### GraphQL request

```json
{
  "variables": {},
  "query": "{\n cashflowsNew(\n filter: [{ field: \"Cashflow.Cashflow_State\", operator: NOTIN, values: [\"NETTED\",\"DEAD\"]}]\n page: 0\n size: 100\n) {\n pageInfo {\n totalHits\n pageNo\n pageSize\n lastPage\n }\n results {\n FMO_Comments {\n FMO_Comment\n FMO_Comment_Timestamp\n FMO_Comment_Updater\n }\n Cashflow {\n Cashflow_Business_Version\n Cashflow_Version\n Cashflow_State\n Cashflow_Affirmation_Status\n Cashflow_Event_Type\n Cashflow_Minor_Version\n Payment_Currency\n Payment_Date\n Payment_Type\n Payment_Cutoff_Time\n Pay_Receive_Indicator\n Payment_Amount\n Netting_Id\n Payment_Receiver_Party_Reference\n Payment_Payer_Party_Reference\n Cashflow_Sub_State\n Cashflow_Sub_State_Type\n Cashflow_Sub_State_Updater\n Status_Event_Type\n Event_Date\n }\n Entity {\n Booking_Entity_SCI_FMID\n Booking_Entity_SCI_FMCODE\n Counterparty_SCI_FMID\n Counterparty_SCI_FMCODE\n }\n Portfolio {\n Booking_Entity_Trade_Portfolio_Name\n }\n }\n }\n}\n"
}
```

### Local single-request test

| Measure | GraphQL | RESTful |
| --- | ---: | ---: |
| Before query data | 77 ms | 119 ms |
| Fetch data | 3819 ms | 3619 ms |
| Response | 3860 ms | 3720 ms |
| Response size | 9.93 KB | 60.66 KB |

GraphQL substantially reduced response size, but the data-fetch duration was similar and total response time was slightly slower in this test.

### Local concurrency test

| Requests | Workers | GraphQL | RESTful |
| ---: | ---: | ---: | ---: |
| 10 | 10 | 5.05 sec | 5.06 sec |
| 50 | 10 | 18.19 sec | 18.14 sec |
| 100 | 20 | 41.34 sec | 44.4 sec |
| 300 | 20 | 130.08 sec | 143.22 sec |

The local results show broadly similar behavior, with GraphQL somewhat faster at higher request counts.

### Staging single-request test

| Measure | Index GraphQL | Index RESTful | Cashflow ID GraphQL | Cashflow ID RESTful |
| --- | ---: | ---: | ---: | ---: |
| Parse params duration | 176 ms | 190 ms | 180 ms | 183 ms |
| Response size | 89.27 KB | 658.77 KB | 2.08 KB | 13.43 KB |
| Total duration | 1883 ms | 3580 ms | 271.45 ms | 500.62 ms |

### Staging concurrency test

| Requests | Workers | Index GraphQL | Index RESTful | Cashflow ID GraphQL | Cashflow ID RESTful |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 10 | 6.09 sec | 9.06 sec | 1.04 sec | 2.04 sec |
| 50 | 10 | 26.23 sec | 49.52 sec | 2.07 sec | 3.09 sec |
| 100 | 20 | 56.42 sec | 77.85 sec | 2.04 sec | 3.04 sec |
| 300 | 20 | 174.59 sec | 217 sec | 3.05 sec | 5.06 sec |
| 300 | 150 | — | — | 2.11 sec | 2.23 sec |
| 300 | 300 | — | — | 2.10 sec | 2.49 sec |
| 500 | 100 | — | — | 3.14 sec | 4.21 sec |

The staging tests favored GraphQL for the tested query shapes, with smaller response sizes and lower total durations. These results should not be generalized to all GraphQL or RESTful systems. GraphQL does not remove downstream data-fetching costs; its performance remains constrained by the slowest microservice or resolver dependency.

## Long-term direction

The source recommends:

- Evaluating a possible migration from iFrame composition to [[single-spa]].
- Adding custom performance tracking for important user journeys.
- Introducing continuous performance monitoring.

The source does not establish an approved migration decision, production baseline, repeatable test protocol, or acceptance criteria.

## Limitations

The document does not specify a formal test harness, browser and operating-system versions, hardware beyond the notebook qualification, sample counts, repeated-run statistics, cache conditions for every test, or controlled CPU and network throttling. It therefore provides directional evidence and useful hypotheses rather than a production-grade benchmark.

## Related pages

- [[ratanone-ui-performance]]
- [[ui-performance-metrics]]
- [[frontend-configuration-loading]]
- [[iframe-micro-frontend-loading-priority]]
- [[graphql-vs-restful-cashflow-querying]]
- [[graphql]]
- [[lighthouse]]
- [[single-spa]]
- [[cashflow-blotter]]