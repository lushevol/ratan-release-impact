---
type: source
title: Rule Service Performance Testing
authors: [Jialin Wang]
year: 2024
url: ""
venue: Internal UAT/Pre-Prod performance-test record
created: 2026-08-24
updated: 2026-08-24
tags: [archived, performance-testing, rule-service, jmeter, drools, ratan-one]
related: [ratan-one-rule-service, rule-service-performance-testing, does-the-archived-rule-service-test-support-the-120-consumer-capacity-claim, what-caused-rule-service-throughput-to-plateau-below-31-percent-cpu, drools, stella, what-is-the-performance-and-concurrency-model-for-dynamic-drl-compilation, was-drools-selected-or-deployed-for-ratan-rule-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]
---
# Rule Service Performance Testing

This archived internal record describes UAT/Pre-Prod JMeter testing of the RATAN One rule-service trade-validation API. It was authored by Jialin Wang, initially drafted on 2024-01-15, and updated on 2024-01-16 to state that a JMeter report was attached and performance testing was complete.

It is historical test evidence, not an authoritative current production-capacity certification. The sign-off table contains no named signatory or date.

## Scope and stated objectives

The tested use case was trade validation: a consumer trade service calls the rule service to validate a trade against rules.

The document describes Drools as a mature open-source rule engine considered for RATAN One suppression, validation, and entitlement rules. However, it does not state the deployed rule-engine version, rule count, session lifecycle, compilation strategy, or rule-refresh model. The results therefore evaluate a rule-service scenario, not Drools in isolation or a comparative rule-engine benchmark.

Declared in-scope interfaces were TDS3+SSI+DQSL, STELLA, and BACKEND API. The reported results identify only the rule-validation endpoint and do not provide end-to-end evidence for every declared interface.

## Stated NFRs

| NFR | Target |
| --- | --- |
| Availability | 24x7 |
| API latency under normal load | Expected average response time: 15 seconds |
| Maximum concurrent users/applications | 60 |
| Maximum requests per hour | 9,344 |
| Endurance test | 1x load for 12 hours |
| Average CPU usage | <50% |
| Memory usage | <80% |

The source defines the peak hour as 9,344 API calls, approximately 2.60 requests per second when averaged over one hour. It does not explain how this workload maps to JMeter thread counts or the observed throughput.

## Tested API contract

| API | Name |
| --- | --- |
| `https://uklvadapp1346.uk.dev.net:8868/v1/rules/validate` | Rule Service Query |

The request body used `businessFlow` `FX_REPLICATE`, `ruleType` `FILTERING`, and a large SCBML/FpML-formatted FX Forward trade payload. The payload references STELLA as message sender, Blade as capture system, and SABRE as a transaction-processing source.

This single representative request does not establish production representativeness across payload sizes, trade products, business flows, rule types, rule counts, or dependency behaviour.

## Execution record

The documented JMeter invocation was:

```bash
/apps/ratanrt/goldenversions/apache-jmeter-5.5/bin/jmeter -n -t query_cashflows.jmx -l ./report/result.jtl -e -o ./report -JthreadNumber=25 -Jduration=900
```

The test strategy proposed 600-second runs at 1, 10, 30, 40, and 60 users. The results instead report 1, 10, 15, 20, and 30 users, each for 600 seconds. The command also refers to `query_cashflows.jmx` in a `query_cashflows_new_loop` directory rather than an explicitly named rule-validation test. These discrepancies need reconciliation against the referenced `ratanone-performancetest-api` repository and original JMeter artifacts.

## Reported results

| Concurrent users/applications | Duration (s) | Samples | 90% line (ms) | 99% line (ms) | Error rate | Throughput (requests/s) | Sent (KB/s) | Received (KB/s) | CPU usage | Memory usage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Check Trade Validation / 1 | 600 | 922 | 745.70 | 851.54 | 0.00% | 1.54 | 40.09 | 1.80 | <28% | <75% |
| 10 | 600 | 6,628 | 1,622.00 | 2,836.13 | 0.00% | 11.04 | 288.25 | 12.96 | <29% | <75.1% |
| 15 | 600 | 5,935 | 5,387.00 | 7,209.92 | 0.00% | 9.86 | 257.43 | 11.57 | <31% | <74.8% |
| 20 | 600 | 5,680 | 8,061.90 | 12,055.19 | 0.00% | 9.42 | 245.95 | 11.06 | <24% | <74.9% |
| 30 | 600 | 9,264 | 12,295.50 | 16,923.35 | 0.00% | 10.17 | 265.64 | 11.94 | <30% | <75% |

The source table appears malformed in its first row: an additional `922` value precedes values that appear to be the 90th and 99th percentile. The exact column mapping should be checked using the original `.jtl` or HTML reports before these metrics are reused.

## Findings bounded by the evidence

- All listed 600-second test rows report a `0.00%` error rate for the exercised validation scenario.
- Reported high-percentile latency rises materially as concurrent users increase, reaching 12,295.50 ms at the 90th percentile and 16,923.35 ms at the 99th percentile for 30 users.
- The stated latency NFR is an average-response-time target. Because mean latency is absent, compliance with that NFR cannot be established from this report. The 30-user 99th percentile exceeds 15 seconds.
- Reported CPU and memory stayed below the stated thresholds during listed runs. Throughput nevertheless plateaued around 9.42–11.04 requests per second, suggesting a possible bottleneck or variability not investigated in the report.
- The test evidence does not include the planned 40- or 60-user cases, a 12-hour soak test, a documented representative work mix, or demonstrated six-instance cluster load distribution.

## Capacity conclusion and limitation

The report concludes that six rule-service instances can support 6, 18, and 120 consumer applications, marking all scenarios as `PASS`.

This inference is not substantiated by the presented evidence. The report does not define a mapping from consumer applications to requests per second, concurrency, payloads, business flows, rule complexity, or instance allocation. It exercises one endpoint and one payload scenario with no more than 30 concurrent users.

See [[does-the-archived-rule-service-test-support-the-120-consumer-capacity-claim]] for the evidence required to validate or reject this conclusion.

## Environment-parity limitation

The source describes six UAT/Pre-Prod RHEL 7.7 application servers, each with 16 cores and 64 GB memory, and compares them with six production application servers plus two production database servers across ARK and WT. It asserts that comparable nominal server capacity should produce comparable performance.

Similar host specifications alone do not demonstrate equivalent production behaviour. The report does not establish parity for topology, load balancing, network paths, deployment settings, JVM configuration, data volume, rule sets, external dependencies, or database behaviour.

## Related pages

- [[ratan-one-rule-service]]
- [[rule-service-performance-testing]]
- [[drools]]
- [[stella]]
- [[what-is-the-performance-and-concurrency-model-for-dynamic-drl-compilation]]
- [[was-drools-selected-or-deployed-for-ratan-rule-processing]]
- [[what-caused-rule-service-throughput-to-plateau-below-31-percent-cpu]]