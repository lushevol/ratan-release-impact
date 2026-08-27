---
type: query
title: Why Does Auto Release Group-Lock Filtering Dominate Runtime?
created: 2026-08-24
updated: 2026-08-24
tags: [auto-release, group-locks, performance, cash-settlement]
related: [cash-settlement-batch-job-performance, cashflow-release-and-netting-race-condition, release-time-cashflow-status-gating, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--21--1yk3s57]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
---
# Why Does Auto Release Group-Lock Filtering Dominate Runtime?

At 50k cashflows, Auto Release V2 reports 5 minutes 37 seconds in group-lock filtering within a 6 minute 49 second total runtime. It filters 7,095 records through the group-lock check, while the 25 pages of query-by-ID and lifecycle processing take approximately 2.7 seconds each.

The source identifies 12.1 seconds for resultant filtering but does not name the operation consuming the remaining approximately 5 minutes 25 seconds. Investigation should isolate database query plans, indexes, lock-state retrieval, data cardinality, contention, network calls, and application-side processing. Any optimization must preserve the release/netting safety control described in [[cashflow-release-and-netting-race-condition]].