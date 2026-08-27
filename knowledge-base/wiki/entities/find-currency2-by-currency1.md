---
type: entity
title: findCurrency2ByCurrency1
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, currency-lookup, operation, performance-testing]
related: [fxu, fx-utilization, fxu-operation-performance-testing, what-are-the-performance-results-for-find-currency2-by-currency1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/PT.md"]
---
# findCurrency2ByCurrency1

`findCurrency2ByCurrency1` is an FXU operation tested in the cited performance-test record. Its name indicates a lookup of currency-2 information using currency-1 as input, but the source does not define its API protocol, request and response contract, owning service, or downstream dependencies.

## Performance-test evidence

Four Apache JMeter runs are recorded:

- Rate Limiter `10`, JMeter throughput `10`, duration `360s`.
- Rate Limiter `20`, JMeter throughput `10`, duration `360s`.
- Rate Limiter `ultimate`, JMeter throughput not set, duration `360s`.
- Rate Limiter `ultimate`, JMeter throughput not set, duration `3600s`.

The evidence confirms configurations rather than outcomes. No achieved request rate, latency, error count, resource-utilization result, or completion status is captured in source text.

## Scope

The performance evidence applies only to this operation. It does not demonstrate performance characteristics for [[fxu]] generally or for [[fx-utilization]] workflows.

See [[fxu-operation-performance-testing]] for the configuration and evidence-capture model, and [[what-are-the-performance-results-for-find-currency2-by-currency1]] for missing performance results.