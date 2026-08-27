---
type: query
title: What Are the Authoritative Production Performance Counters for Murex 2.11 Cashflow Integration?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, fmrp, production-monitoring, reconciliation, counters]
related: [production-performance-monitoring, fmrp-retry-and-purge-policy, fmrp-payment-insertion-eligibility, fmrp-murex-cashflow-status-synchronization, what-is-the-authoritative-fmrp-retry-limit-and-counter, what-is-the-final-fmrp-inbound-routing-design, what-is-the-authoritative-fmrp-mq-queue-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Production Performance Monitoring.md"]
---
# What Are the Authoritative Production Performance Counters for Murex 2.11 Cashflow Integration?

The production monitoring record reports useful volume evidence but does not define counter scope or measurement semantics.

## Evidence requiring resolution

- The inbound router reconciles: 4,092 inbound records equal 4,057 `acked` plus 35 `released`.
- The downstream `FlowEntrySpliter` reports 162 records from the release path, which does not reconcile with the router's 35 `released` records.
- `PayInsertionFilter` reports 2,240 input records but 2,297 total listed branch outcomes: 220 `discard`, 57 `retry`, and 2,020 `process`.
- `INIT2SNTR1` reports 2,020 input records, 2,018 `Triggered` records, and 439 `Error` records.
- The source reports a peak rate of 252 records/hour or 4.20 records/minute for core FMRP stages, but provides no interval definition or SLA threshold.

## Questions to resolve

1. Are all figures interval counters, cumulative counters, or a mixture?
2. Are retry and error outcomes counted in addition to their original processing outcomes?
3. Do `FlowEntrySpliter` and `FmrpInboundRouter` measure the same release population and time window?
4. What are the authoritative owners and meanings of nodes `82296`, `82205`, `82193`, `82224`, and `82208`?
5. Was 13 November 2023 the actual production go-live date, and how should 7–10 November activity be classified?
6. Which latency, queue-depth, utilization, and error thresholds constituted the production acceptance criteria?

Until these are answered, the observed figures should be used as routing and throughput evidence rather than as validated reliability or SLA metrics.