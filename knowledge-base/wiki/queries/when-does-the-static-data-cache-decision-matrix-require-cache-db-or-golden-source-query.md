---
type: query
title: When Does the Static Data Cache Decision Matrix Require Cache, Database, or Golden-Source Query?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, cache-policy, database, reference-data, NFRs]
related: [database-first-static-data-caching, static-reference-data-synchronization, redis, ssi-stamping-reference-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# When Does the Static Data Cache Decision Matrix Require Cache, Database, or Golden-Source Query?

## Question

What quantitative thresholds determine whether RatanOne should use database access, full cache, partial cache, or direct golden-source queries?

## Evidence

The matrix considers data origin, volume, access frequency, and change frequency. It recommends database persistence and conditional caching, but every row marks the business NFR condition as `not match`.

## Required resolution

Clarify whether `not match` means that database NFRs are not met. Define measurable thresholds for:

- Read latency and tail latency
- Throughput and concurrency
- Dataset size and cache memory
- Access frequency and cache-hit ratio
- Change frequency and acceptable staleness
- Database and golden-source availability
- Cache warm-up and rebuild time
- Reconciliation and correctness requirements

The thresholds should be applied separately to Vostro, Nostro, and Counterparty data.
