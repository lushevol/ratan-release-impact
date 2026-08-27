---
type: query
title: Which Cash Settlement Indexes Were Deployed on February 16 and What Was the Effect of Each?
tags: [cash-settlement, postgresql, indexing, deployment, performance-measurement]
related: [postgresql-sequential-scan-triage, cash-settlement-batch-job-performance, group-service, adaptor, cashflow-lifecycle-service, postgresql, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--56--11z02tq]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/DB High CPU Usage Investigation - Since Feb.16th Midnight.md"]
---
# Which Cash Settlement Indexes Were Deployed on February 16 and What Was the Effect of Each?

The source reports that a 16 February index release substantially reduced high CPU samples, but it does not state which of the seven appendix indexes were deployed, in what sequence, or which workload each change affected.

## Why this remains open

The report names only two main contributors—holiday-currency and lifecycle message-event-source tables—while its appendix contains indexes for [[group-service]], static-service processing, [[adaptor]], and [[cashflow-lifecycle-service]]. Early isolation testing also suspected adaptor and group processing, while later tests focus on Lifecycle Service precheck activity.

Without a deployment record and per-index measurements, it is not possible to distinguish:

- indexes deployed on 16 February from recommendations or later test changes;
- root-cause remediation from secondary optimisation;
- the effect of each index from workload variation or other concurrent changes.

## Required evidence

- Change records, migration logs, and target environments for every index.
- Deployment order, build method, rollback readiness, and any failures.
- Before-and-after workload volume, concurrency, duration, and CPU sampling method.
- Query-level latency, plan, I/O, and index-usage metrics for each affected service.
- Side-effect measurements for writes, storage, autovacuum, replication, and operational maintenance.

The reported reduction from 124–297 samples above 90% CPU on 4–6 February to 27 on 17 February is promising but does not, by itself, attribute improvement to individual indexes.