---
type: concept
title: Uber-SCBML Performance Regression Testing
created: 2026-08-24
updated: 2026-08-24
tags: [performance-testing, regression-testing, uber, scbml, settlement-stp]
related: [uber, scbml, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--19101up, does-uber-adoption-meet-the-scbml-no-regression-performance-requirement, does-message-bridge-change-uber-end-to-end-stp-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md"]
---
# Uber-SCBML Performance Regression Testing

Uber-SCBML performance regression testing evaluates whether introducing [[uber]] changes the performance of the established [[scbml]] settlement flow.

## Separate acceptance questions

Two claims require separate evidence:

- **No-regression requirement:** Uber adoption must not adversely affect the SCBML flow. This is the mandatory acceptance condition.
- **Relative-performance claim:** Uber messages perform better than SCBML messages. This is a separate, optional comparison and cannot be inferred from a mixed-flow aggregate.

## Minimum test design

A credible assessment should define and retain:

- A SCBML-only baseline and an Uber-enabled run under matched workload, environment, database state, and configuration.
- An explicit timing boundary for Settlement STP, including start and completion events.
- Workload composition, successful-ingestion counts, and reconciliation of messages, trades, and cashflows.
- Latency percentiles such as P50, P95, and P99, alongside average and maximum latency.
- Throughput, error and retry rates, and resource telemetry.
- Acceptance thresholds for regression and relative performance.
- Whether [[solace-to-kafka-fan-in]] or Message Bridge is included, excluded, or measured as a separate end-to-end path.

## Current evidence

The available Round 1 observation reports a 3.401777-second average STP time, 14.553234-second maximum, 1.474934-second minimum, and 13,737 total for a mixed workload without Message Bridge. It is useful as a preliminary observation but lacks the comparative controls needed for a non-regression conclusion or an Uber-versus-SCBML conclusion.