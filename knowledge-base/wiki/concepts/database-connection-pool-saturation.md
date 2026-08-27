---
type: concept
title: Database Connection-Pool Saturation
created: 2026-08-24
updated: 2026-08-24
tags: [database, connection-pool, timeouts, kafka, retries, performance]
related: [fmrp2, staging, multi-topic-kafka-consumer-parallelism, kafka, cash-settlement-performance-and-stress-testing, what-partition-and-db-pool-configuration-sustains-uber-message-load]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
---
# Database Connection-Pool Saturation

Database connection-pool saturation occurs when concurrent application work needs more usable database connections than the application pool or database can provide within its timeout period. The result can be connection acquisition failures, delayed processing, retries, and reduced end-to-end throughput.

## Observed Cash Settlement Evidence

In [[fmrp2]], the Uber consumer test used a database pool with minimum two and maximum eight connections. The source reports database timeout and “connection limit reached” errors at higher send rates:

- 40 cashflows per trade at send TPS 4 and 5.
- 12 cashflows per trade at send TPS 6.
- 6 cashflows per trade at send TPS 14 and 16.

In the 100-message, 20-second test, the database exception reportedly routed messages to retry queues.

## Limits of the Evidence

The source does not provide pool active/idle counts, acquisition wait times, database session counts, PostgreSQL wait events, transaction durations, or leak diagnostics. It therefore supports an observed association with connection limits but does not identify the exact source of exhaustion.

Staging tests with pool maximum 24 and 56 show some shorter elapsed times at maximum 56, but they do not provide a complete controlled comparison. Retry-inclusive totals further limit direct comparison.

## Required Measurements

A capacity decision should capture:

- Pool active, idle, pending, and timeout counts.
- Connection-acquisition latency.
- Database-side connection counts and configured limits.
- Transaction duration and SQL latency by downstream component.
- Retry rate and retry-queue lag.
- Completed-message and completed-cashflow throughput.

See [[what-partition-and-db-pool-configuration-sustains-uber-message-load]].