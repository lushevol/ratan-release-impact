---
type: source
title: Cashflow Blotter Page Size Performance
authors: []
year: 2025
url: "https://uklvadrtn006a.pi.dev.net:8081/performance-test/1744185925071/report/index.html"
venue: Internal technical design documentation
tags: [cash-settlement, cashflow-blotter, performance-testing, pagination, value-date, staging]
related: [cashflow-blotter, cashflow-blotter-query-performance, value-date-bounded-cashflow-queries, ultra-cashflow-query, legacy-cashflow-query, what-cashflow-blotter-queries-are-covered-by-the-performance-sla, what-evidence-validates-ultra-cashflow-query-performance-against-legacy]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Page Size Performance.md"]
---
# Cashflow Blotter Page Size Performance

This internal performance report evaluates [[cashflow-blotter]] query latency for 1,000- and 5,000-record pages, the impact of value-date (VD) bounds, and a Staging comparison between [[legacy-cashflow-query|Legacy]] and [[ultra-cashflow-query|Ultra]] query implementations.

## Page-Size and VD-Bounding Results

The source labels the measurements as “90% Response Time (ms).” Several cells contain multiple readings, but it does not specify whether they are independent runs, percentile outputs, or another aggregation. The source-reported overall scaling factors are 1.5 for 5,000 versus 1,000 records and 0.3 when a VD constraint is added; calculation methods are not provided.

| Queried Filter | Underlining Filters | Page Size 1000 | Page Size 5000 | 1000 vs 5000 Scaling Factor | Page Size 5000 + VD in [T, T+10] | + VD vs without VD Scaling Factor |
| --- | --- | --- | --- | --- | --- | --- |
| 90% Response Time (ms) | 90% Response Time (ms) | 90% Response Time (ms) |  |  |  |  |
| Default Filters | Cashflow State = WAITING VD between [T, T+5] | 195.00 | 161.00 | 0.82 |  |  |
| Only WAITING | Cashflow State = WAITING | 893.00 889.00 934.00 | 3418.00 3584.00 3510.00 | 3.9 | 116.70 118.50 105.30 | 0.033 |
| INDIA | Entity FMCODE in [....] VD = ... | 147.00 | 126.00 | 0.85 |  |  |
| NDF LONDON | Entity FMID = ... Murex Product Typology = ... Cashflow State NOTIN [...] | 851.00 1319.00 1337.00 | 923.00 1336.00 1351.00 | 1.14 | 291.10 435.90 440.10 | 0.315 |
| COMM CHECKER | Sub State = Pending Verification Is Commodity = true Entity FMID IN [...] | 237.00 69.00 99.00 | 175.00 115.00 100.00 | 1.5 | 88.60 81.70 101.40 | 0.502 |
| UK COMMODITY | Entity FMID = ... Cashflow State NOTIN [...] Is Commodity = true | 22305.00 22412.00 22481.00 | 25233.00 25393.00 26159.00 | 1.20 | 5352.30 11862.00 18592.90 | 0.4 |
| DRV KL LDN COM | Entity FMID = ... Cashflow State in [...] Is Commodity = true Counterparty FMID NOTIN [...] VD NOTIN [...] | 3376.00 3272.00 2415.00 | 2978.00 1791.00 1887.00 | 0.87 |  |  |
| PAYDOL UK | Entity FMID = ... Cashflow State NOTIN [...] Is Commodity = false Counterparty FMID NOTIN [...] Murex Product Typology NOTIN [...] ISDA Taxonomy NOTIN [...] | 6607.00 9372.00 26920.00 | 26927.00 9883.00 10179.00 | 4 | 6910.90 8411.40 3349.50 | 0.256 |
| UK NON COMMODITY | Entity FMID = ... Cashflow State NOTIN [...] Is Commodity = false Counterparty FMID NOTIN [...] Murex Product Typology NOTIN [...] ISDA Taxonomy NOTIN [...] | 45731.00 17463.00 34051.00 | 18604.00 35079.00 35221.00 | 2.05 | 6773.20 10910.80 10971.70 | 0.364 |
| DRV ASA SETTS | Entity FMID in [...] Cashflow State in [...] | 513.00 113.00 125.00 | 436.00 147.00 422.00 | 1.3 | 135.80 149.00 150.80 | 0.30 |
| WAITING + VD 15 | Cashflow State IN [WAITING] VD between [T, T+15] | 72.00 74.00 86.00 | 105.00 109.00 103.00 | 1.4 |  |  |
| Overall Scaling Factor |  |  |  | 1.5 |  | 0.3 |

## Proposed Loading SLA

The source proposes, rather than records approval of, the following targets for 5,000-record Cashflow Blotter loading:

- Maximum: 7.5 seconds, derived from a previous five-second target multiplied by 1.5.
- Average: three seconds, derived from a previous two-second target multiplied by 1.5.

The proposal does not define the percentile, workload, eligible filter profiles, environment, or approval authority. Unbounded and complex filter cases in the same results exceed 7.5 seconds.

## 2025-04-12 Legacy and Ultra Test Configuration

```text
Target Env: Staging
Total Volume: 1357121
VD: 0318
VD Volume: 84141
User Concurrency: 50
Target TPS: 1
```

## Legacy versus Ultra Results

| Queried Filter | Underlining Filters | Legacy Response | Ultra Response |
| --- | --- | --- | --- |
| 90% Response Time (ms) | 90% Response Time (ms) | 90% Response Time (ms) |  |
| Default Filters | Cashflow State = WAITING VD = 20250318 | 3212.00 | 2282.00 |
| INDIA | Entity FMCODE in [....] VD = 20250318 | 291.20 | 169.40 |
| NDF LONDON | Entity FMID = ... Murex Product Typology = ... Cashflow State NOTIN [...] VD = 20250318 | 2833.00 2384.10 3210.10 | 1235.60 2081.70 2027.40 |
| COMM CHECKER | Sub State = Pending Verification Is Commodity = true Entity FMID IN [...] VD = 20250318 | 129.70 1167.10 329.20 | 88.00 54.40 482.00 |
| UK COMMODITY | Entity FMID = ... Cashflow State NOTIN [...] Is Commodity = true VD = 20250318 | 1602.12 1230.00 2491.00 | 1504.40 1575.00 1626.00 |
| DRV KL LDN COM | Entity FMID = ... Cashflow State in [...] Is Commodity = true Counterparty FMID NOTIN [...] VD = 20250318 | 2013.01 2891.01 2931.00 | 1502.50 2713.50 2333.20 |
| PAYDOL UK | Entity FMID = ... Cashflow State NOTIN [...] Is Commodity = false Counterparty FMID NOTIN [...] Murex Product Typology NOTIN [...] ISDA Taxonomy NOTIN [...] VD = 20250318 | 1853.20 2930.11 2811.02 | 1777.40 3101.00 3195.10 |
| UK NON COMMODITY | Entity FMID = ... Cashflow State NOTIN [...] Is Commodity = false Counterparty FMID NOTIN [...] Murex Product Typology NOTIN [...] ISDA Taxonomy NOTIN [...] VD = 20250318 | 1823.10 3419.22 3519.01 | 1701.70 3304.00 3427.00 |
| DRV ASA SETTS | Entity FMID in [...] Cashflow State in [...] VD = 20250318 | 1230.11 3952.11 2699.35 | 196.00 4232.20 2456.80 |
| WAITING + VD 15 | Cashflow State IN [WAITING] VD = 20250318 | 1911.01 3920.51 2501.30 | 2318.10 4105.20 2336.80 |
| ACCOUNTING ERROR + VD+-1 | Cashflow Accounting Status in ["SENT", "REJECTED", "MISSING_INFO"] and VD in [T-1, T+1] | 90.22 | 38.50 |
| ERROR + VD+2 | Cashflow State = "Error" and VD in [T, T+2] | 120.23 | 63.00 |
| FAILED + VD Today | Cashflow State = "FAILED" and VD = T (CURRENT_DATE) | 901.65 | 648.50 |
| HOLD + VD+2 | Cashflow State = "HOLD" and VD in [T, T+2] | 90.77 | 77.80 |
| QUEUED + VD+2 | Cashflow State = "QUEUED" and VD in [T, T+2] | 125.60 | 54.40 |
| SWIFT ERROR + VD+-1 | Cashflow Swift Status in [ "Ratan Internal Error", "FMSGW Error", "AMH Error", "MX Generation Error", "FMSRE Error", "SCPAY Error"] and VD in [T-1, T+1] | 157.33 | 77.50 |
| WAITING + VD Today | Cashflow State = "WAITING" and VD = T (CURRENT_DATE) | 952.23 | 56.90 |
| GROUP ERROR | Dashboard Status = "ERROR" | 305.55 | 248.00 |
| GROUP PENDING | Dashboard Status = "PENDING" and Dashboard Group Status in ["PENDING", "PENDING_PRE_GROUP"] | 302.22 | 207.60 |
| GROUP PENDING VALIDATION + VD Today | Dashboard Status = "PENDING" and Dashboard Group Status = "PENDING_TRADE_VALIDATION" and VD <= T+1 | 196.88 | 139.50 |

## Interpretation and Limitations

The source concludes that Ultra has no performance shortcoming and reports an overall scale factor of around 5%. The row-level results show Ultra faster in many cases but slower in some readings. This supports only a Staging-specific conclusion for the stated volume, concurrency, TPS, and unspecified page size.

The report references `RATAN_ADVANCED_SEARCH_PT.jmx` as the JMeter test script. The Legacy report is marked `TODO`. No SQL, indexes, execution plans, warm-up procedure, duration, error-rate threshold, response-time aggregation method, or acceptance threshold is supplied.

The report treats indexed, selective filters using `=`, `IN`, and `BET` as recommended NFR-covered query shapes, and warns that unindexed, nonselective, or negative-operator predicates can be costly. This is a design heuristic, not a database-independent rule; index definitions and execution plans are required before adopting it as policy.