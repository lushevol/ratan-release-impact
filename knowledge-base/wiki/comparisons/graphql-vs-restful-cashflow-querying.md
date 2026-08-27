---
type: comparison
title: GraphQL versus RESTful Cashflow Querying
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, restful-api, cashflow, performance, cn-cash-settlement]
related: [graphql, cashflow-blotter, ratanone-ui-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# GraphQL versus RESTful Cashflow Querying

## Scope

This comparison covers the tested CN Cash Settlement query-service implementations and request shapes. It does not establish that GraphQL universally outperforms RESTful APIs.

Both endpoints used `/v1/query/cashflows`, requested equivalent logical data, supported paging and JWT, and were tested against a database prepared with 10,000,000 records.

## Local single-request test

| Measure | GraphQL | RESTful |
| --- | ---: | ---: |
| Before query data | 77 ms | 119 ms |
| Fetch data | 3819 ms | 3619 ms |
| Response | 3860 ms | 3720 ms |
| Response size | 9.93 KB | 60.66 KB |

GraphQL reduced response size substantially, but its data-fetch duration and total response time were similar to RESTful in this test.

## Local concurrency test

| Requests | Workers | GraphQL | RESTful |
| ---: | ---: | ---: | ---: |
| 10 | 10 | 5.05 sec | 5.06 sec |
| 50 | 10 | 18.19 sec | 18.14 sec |
| 100 | 20 | 41.34 sec | 44.4 sec |
| 300 | 20 | 130.08 sec | 143.22 sec |

The local results show broadly similar concurrency behavior.

## Staging single-request test

| Measure | Index GraphQL | Index RESTful | Cashflow ID GraphQL | Cashflow ID RESTful |
| --- | ---: | ---: | ---: | ---: |
| Parse params duration | 176 ms | 190 ms | 180 ms | 183 ms |
| Response size | 89.27 KB | 658.77 KB | 2.08 KB | 13.43 KB |
| Total duration | 1883 ms | 3580 ms | 271.45 ms | 500.62 ms |

## Staging concurrency test

| Requests | Workers | Index GraphQL | Index RESTful | Cashflow ID GraphQL | Cashflow ID RESTful |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 10 | 6.09 sec | 9.06 sec | 1.04 sec | 2.04 sec |
| 50 | 10 | 26.23 sec | 49.52 sec | 2.07 sec | 3.09 sec |
| 100 | 20 | 56.42 sec | 77.85 sec | 2.04 sec | 3.04 sec |
| 300 | 20 | 174.59 sec | 217 sec | 3.05 sec | 5.06 sec |
| 300 | 150 | — | — | 2.11 sec | 2.23 sec |
| 300 | 300 | — | — | 2.10 sec | 2.49 sec |
| 500 | 100 | — | — | 3.14 sec | 4.21 sec |

## Interpretation

GraphQL’s clearest measured advantage is response-size reduction through field selection. The staging tests also show lower total duration and better reported concurrency for the tested query shapes.

GraphQL does not automatically reduce underlying database or microservice work. Its end-to-end performance remains bounded by the slowest resolver or downstream service. The local and staging differences also demonstrate environment sensitivity.

Further validation should use repeated runs, controlled cache and network conditions, identical datasets, resolver instrumentation, and statistical summaries.