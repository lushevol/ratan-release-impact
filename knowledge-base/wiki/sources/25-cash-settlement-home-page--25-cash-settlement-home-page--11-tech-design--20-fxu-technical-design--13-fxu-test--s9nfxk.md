---
type: source
title: FXU findCurrency2ByCurrency1 Performance Test Cases
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, performance-testing, apache-jmeter, rate-limiting, currency-lookup]
related: [fxu, find-currency2-by-currency1, fxu-operation-performance-testing, what-are-the-performance-results-for-find-currency2-by-currency1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/PT.md"]
authors: []
year: 2026
url: ""
venue: "FXU Technical Design"
---
# FXU findCurrency2ByCurrency1 Performance Test Cases

This test-case record documents four Apache JMeter performance-test configurations for the FXU operation [[find-currency2-by-currency1]]. It establishes the configured rate-limiter setting, JMeter throughput setting where provided, duration, and report location. It does not transcribe measured dashboard outcomes.

## Test configurations

| Test | Operation | Rate Limiter | JMeter throughput | Duration | Dashboard |
|---|---|---:|---:|---:|---|
| 1 | `findCurrency2ByCurrency1` | `10` | `10` | `360s` | [Apache JMeter Dashboard](https://uklvadrtn006a.pi.dev.net:8081/performance-test/1779353207713/report/index.html) |
| 2 | `findCurrency2ByCurrency1` | `20` | `10` | `360s` | [Apache JMeter Dashboard](https://uklvadrtn006a.pi.dev.net:8081/performance-test/1779351273062/report/index.html) |
| 3 | `findCurrency2ByCurrency1` | `ultimate` | Not set | `360s` | [Apache JMeter Dashboard](https://uklvadrtn006a.pi.dev.net:8081/performance-test/1779355474274/report/index.html) |
| 4 | `findCurrency2ByCurrency1` | `ultimate` | Not set | `3600s` | [Apache JMeter Dashboard](https://uklvadrtn006a.pi.dev.net:8081/performance-test/1779421344572/report/index.html) |

## Scope of evidence

The record supports that the operation was tested under two explicit limiter settings with the same nominal JMeter throughput and duration, plus two `ultimate` limiter configurations, including a one-hour sustained-load run.

It does not provide extractable values for achieved throughput, response-time percentiles, failures, timeouts, resource usage, acceptance criteria, or pass/fail status. The dashboard links must be inspected to establish those results.

`Rate Limiter ultimate` is not defined in the record. It must not be interpreted as unlimited capacity without confirming its configured numeric value and runtime semantics.

## Attached artifacts

The source references these image artifacts:

- `attachments/image-2026-5-22_13-52-26.png`
- `attachments/image-2026-5-22_13-53-2.png`
- `attachments/image-2026-5-22_13-56-58.png`

The first image is linked to the dashboard for Test 3. The source text does not provide reliable textual transcriptions of values displayed in these images.

## Related knowledge

This evidence is specific to [[find-currency2-by-currency1]] and should not be generalized to all of [[fxu]], other FXU APIs, or the Cash Settlement Platform. The test-design considerations are captured in [[fxu-operation-performance-testing]]. Outstanding result capture and interpretation are tracked in [[what-are-the-performance-results-for-find-currency2-by-currency1]].