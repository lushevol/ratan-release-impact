---
type: query
title: Is 6 GB JVM Heap Sufficient for RATAN Auto Materialize at UK Volume?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, auto-materialize, jvm, performance, uk]
related: [ratan, cash-settlement-batch-job-performance, paginated-cashflow-batch-processing, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--21--1yk3s57]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
---
# Is 6 GB JVM Heap Sufficient for RATAN Auto Materialize at UK Volume?

Auto Materialize V2 failed on page 48 of 50 at 100k with `java.lang.OutOfMemoryError: Java heap space` under:

```text
-Xms1024m -Xmx2048m -XX:MaxMetaspaceSize=1024m
```

The source proposes, but does not validate, this configuration:

```text
-Xms3072m -Xmx6144m -XX:MaxMetaspaceSize=3072m
```

## Evidence needed

- Successful repeatable V2 completion at 40k, 50k, and 100k.
- Heap, Metaspace, and retained-object trends by page.
- An explanation for memory growth despite 2,000-record pagination.
- Production-like database size, indexing, dependency latency, and concurrent load.
- A defined job completion-time SLO and peak eligible-record volume per invocation.

A 6 GB configuration should not be considered sufficient until these tests establish completion and stable memory behavior.