---
type: entity
title: 51358-ratan-cash-settlement-accounting-service
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, accounting, cash-settlement, tlm, oltp]
related: [ratan, chg1016055, ratan-settlement-korea, cash-settlement, reconciliation, what-were-the-tlm-performance-acceptance-criteria]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# 51358-ratan-cash-settlement-accounting-service

`51358-ratan-cash-settlement-accounting-service` is a RATAN backend service included in [[chg1016055]].

## Release Artifact

- Deployment step: `5`
- Branch: `release/v2.2.0`
- Package: `2.2.0-20260730.2`
- Pipeline run: `20260730.2`
- Owner: Chongxuan Li

## Scope

The release record assigns three changes to this service:

1. OLTP integration.
2. A tactical TLM reconciliation API.
3. API performance testing.

Production PIT also examines columns and indexes in the `ratan_cash_accounting_service` schema.

## Performance Evidence

The TLM reconciliation performance test records a response containing 20,286 items and links to Grafana and an Apache JMeter dashboard. No latency, throughput, concurrency, duration, error-rate, utilization, threshold, or explicit pass/fail values are transcribed.

The unresolved acceptance standard is tracked by [[what-were-the-tlm-performance-acceptance-criteria]].