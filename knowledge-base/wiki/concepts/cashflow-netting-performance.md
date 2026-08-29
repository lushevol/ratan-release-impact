---
type: concept
title: Cashflow Netting Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, performance, throughput, resultant-cashflow]
related: [cash-settlement-performance-and-stress-testing, cash-settlement-batch-job-performance, netting-service, does-netting-meet-the-required-throughput-sla-at-production-volume]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result.md"]
---
# Cashflow Netting Performance

Cashflow netting performance measures the elapsed time and throughput required to process component cashflows and produce resultant cashflows and related events.

## Observed results

The source records the following single-run observations:

- 5,000 cashflows completed in 1.9 minutes, approximately 43.9 cashflows per second if 1.9 minutes is interpreted as 114 seconds.
- 1,994 cashflows completed in 47.3 seconds, approximately 42.2 cashflows per second.

The similar observed throughputs are consistent with approximately linear scaling between these two input sizes. This is not sufficient evidence for a scalability conclusion or service-level commitment because the source does not control or document execution environment, workload mix, concurrent load, configuration, repetitions, or error-rate treatment.

## Successful and failed processing

Input count must not be assumed to equal successful netting count. In the 5,000-cashflow observation, `cashflowN00000013565` moved to `TechFailed` because its booking entity or counterparty lacked an `fmcode`.

Performance reporting should distinguish:

- submitted component cashflows;
- successfully processed component cashflows;
- resultant cashflows and resultant events created;
- component events created;
- `TechFailed` and other exception outcomes;
- end-to-end elapsed time and any separately measured phases.

## Evidence boundaries

This concept concerns netting work performed by [[netting-service]]. It is distinct from cashflow-blotter query performance and from other cash settlement batch job performance workloads. The current evidence consists of two internally recorded test runs and does not define an approved performance target.

See does netting meet the required throughput sla at production volume for the required acceptance criteria and benchmark controls.