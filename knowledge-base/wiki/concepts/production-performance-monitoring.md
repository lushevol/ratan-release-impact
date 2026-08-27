---
type: concept
title: Production Performance Monitoring
created: 2026-08-24
updated: 2026-08-24
tags: [production, monitoring, throughput, performance, cashflow-integration]
related: [pre-post-performance-regression-testing, fmrp-cashflow-publication-lifecycle, fmrp-murex-cashflow-status-synchronization, what-are-the-authoritative-production-performance-counters-for-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Production Performance Monitoring.md"]
---
# Production Performance Monitoring

Production performance monitoring records observed workload, routing outcomes, processing rates, errors, and backlog indicators after deployment. It should distinguish measured operational evidence from a conclusion that performance targets or SLAs have been met.

## Murex 2.11 cashflow integration evidence

The post-go-live source provides a point-in-time throughput baseline for the outbound FMRP path:

`docPayment → extSettleRouter → FmrpFilter → FmrpSettleEnrichment → FmrpSettleFilter → FmrpOutboundMQ`

For the recorded `20231113` snapshot, 4,057 records reached FMRP and were reported at every measured stage through [[fmrp-outbound-mq]]. The cited peak rate is 252 records per hour, or 4.20 records per minute.

The inbound snapshot reports 4,092 records at the source-labelled `FmrpInoundMQ`, split by `FmrpInboundRouter` into 4,057 acknowledged and 35 released records. These observations support monitoring of [[fmrp-murex-cashflow-status-synchronization]], but do not establish end-to-end latency or reliability.

## Minimum interpretation controls

Performance evidence should state:

- the measurement window and time zone;
- whether counters are interval, cumulative, or retry-inclusive;
- the population represented by each routing branch;
- latency, backlog, and resource measurements where an SLA conclusion is needed; and
- expected thresholds and the action to take when they are exceeded.

The cited record lacks these controls and contains unreconciled volumes. Its rates are useful as source-reported operational baselines only. See [[what-are-the-authoritative-production-performance-counters-for-murex-211-cashflow-integration]].