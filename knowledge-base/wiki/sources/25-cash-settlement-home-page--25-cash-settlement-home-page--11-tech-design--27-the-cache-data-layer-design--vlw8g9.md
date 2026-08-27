---
type: source
title: The Cache Data Layer Design
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page Tech Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, static-data, caching, Redis, Hazelcast, SSI-stamping, reference-data]
related: [redis, hazelcast-imdg, static-reference-data-synchronization, database-first-static-data-caching, ssi-stamping-reference-data, api-gateway, cashflow-lifecycle-stamping, cashflow-precheck-validation, database-opensearch-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# The Cache Data Layer Design

## Summary

This design proposes how RatanOne should store, synchronize, and cache static data required for STP cashflow processing. It distinguishes externally mastered reference data, such as Vostro and Counterparty data, from RatanOne-owned static data, such as Nostro data.

The design proposes local persistence to improve STP stability and reduce dependency and access pressure on surrounding systems. External reference data is initialized from a golden-source database dump, updated through EDMI notifications, supplemented by daily change files received through FileIT or another transfer channel, and reconciled against the golden source by end of day.

The design principle is database first: cached static data should also be persisted in the database, and cache middleware should be used when database access does not meet business NFRs. Redis version 6+ is proposed for the Day 1 release because Redis is already used by RatanOne and is considered lower risk and lower cost. Hazelcast IMDG is deferred as a possible post-Day 1 NFR improvement.

## Static-data ownership model

| Data category | Examples | External or local ownership | Proposed initialization and synchronization |
| --- | --- | --- | --- |
| Reference data | Vostro, Counterparty information | Mastered by SSI+ or SCI; copied locally by RatanOne | Golden-source dump, event notifications, daily files, and EOD reconciliation |
| RatanOne-owned data | Nostro | Maintained by RatanOne | Manual initialization and subsequent data dumps |

The design does not define authoritative database tables, freshness targets, event ordering, replay behavior, discrepancy thresholds, or ownership and governance controls for each data domain.

## Reference-data synchronization strategy

1. Initialize data with a database dump provided by the golden-source system.
2. Receive update notifications from the golden source through EDMI, including FM-EDMI or Enterprise-EDMI, with data payloads.
3. Consume a daily golden-source change file through FileIT or another suitable data channel.
4. Reconcile RatanOne data with the golden-source data. If the datasets differ, parse the golden-source file and refresh RatanOne data by the end of the day.

The source does not specify whether events or files take precedence, how duplicate or late events are handled, how updates are versioned, or what constitutes successful reconciliation.

## Cache decision principle

The source states that if an application can meet business NFRs with database access, it should not use in-memory cache middleware. It also states that reference data should be stored in the database first and kept updated even when the data is cached.

### Source decision matrix

| DATA Type | ** Store strategy for RatanOne** | Business NFRs match | **Data volume** | **Use frequency** | Change frequency | Note |
| --- | --- | --- | --- | --- | --- | --- |
| Refence data | cache in memory （all data in DB） | not match | small | common case need （often） | more than one hour | |
| Refence data | cache in memory （all data in DB） | not match | small | common case need （often） | Less than one hour | |
| Refence data | DB | not match | small | special case need （not often） | more than one hour | |
| Refence data | Query Golden Source | not match | small | special case need （not often） | Less than one hour | |
| Refence data | parts of data cache in memory and all data in DB | not match | big | common case need （often） | more than one hour | |
| Refence data | parts of data cache in memory and all data in DB | not match | big | common case need （often） | Less than one hour | |
| Refence data | DB | not match | big | special case need （not often） | more than one hour | |
| Refence data | Query Golden Source | not match | big | special case need （not often） | Less than one hour | |
| Ratan data | cache in memory （all data in DB） | not match | small | common case need （often） | more than one hour | |
| Ratan data | cache in memory （all data in DB） | not match | small | common case need （often） | Less than one hour | |
| Ratan data | DB | not match | small | special case need （not often） | more than one hour | |
| Ratan data | DB | not match | small | special case need （not often） | Less than one hour | |
| Ratan data | parts of data cache in memory and all data in DB | not match | big | common case need （often） | more than one hour | |
| Ratan data | parts of data cache in memory and all data in DB | not match | big | common case need （often） | Less than one hour | |
| Ratan data | DB | not match | big | special case need （not often） | more than one hour | |
| Ratan data | DB | not match | big | special case need （not often） | Less than one hour | |
| | | | | | | |

The repeated `not match` value appears inconsistent with the surrounding principle and requires clarification.

## Dataset-specific use cases

### Vostro data for SSI Stamping

- Source and owner: SSI+
- Approximate 2022 size: about one million records
- Initialization: SSI+-provided database dump
- Key: `SSI-ID`
- Updates: SSI+ notifications update RatanOne; reconciliation and refresh occur by EOD

The example payload is a nested entity and settlement-instruction document containing counterparty identity, account, BIC, settlement, currency, SSI status, and source-system fields. It includes sensitive-looking account and counterparty information, but the source does not define masking, encryption, access control, retention, or cache-memory security requirements.

### Nostro data for SSI Stamping

- Source and owner: RatanOne
- Approximate 2022 size: 100,000 records
- Initialization: manual
- Updates: new-data dumps
- Key: `legalEntityFmId+Currency+settlementMeans+settlementAccount`

The example record contains legal entity, FMID, settlement means, settlement account, settlement currency, Nostro account, Swift, correspondent, address, and message-type fields.

### Counterparty information for SSI Stamping

- Source and owner: SCI
- Approximate 2022 size: 400 records
- Initialization: API query provided by SCI
- Key: `FMID`
- Updates: SCI notifications and a scheduled daily synchronization job

The example payload is a small FMID-to-profile mapping:

```json
{
  "fm_profile_sys_gen_id": "10075222",
  "fpi_fm_code": "SCB LONDON*LDN"
}
```

## RatanOne cache middleware use cases

| **Use cases** | **Middleware ** | Note |
| --- | --- | --- |
| Distributed locks | Redis | |
| Duplicate check | Redis | |
| User Session （X-Token） | Redis | |
| URL whitelist in API Gateway | Redis | |
| cache data | Redis | |

For UI queries, the source allows either local caching or Redis according to the static-data cache rule.

## Hazelcast design proposal

The source describes Hazelcast IMDG as a distributed in-memory object store that supports maps, multimaps, atomic longs, queues, lists, and sets. Hazelcast Management Center is proposed for cluster monitoring, statistics, SQL queries, and REST access.

The proposed deployment is a Hazelcast cluster with an instance on each of six production nodes in both ARK and Watford. ARK and Watford are described as active-active, with RatanOne service traffic routed to live service nodes. The DR strategy is stated to be the same as the HA strategy.

The source does not define partition backups, WAN replication, split-brain prevention, cross-site consistency, failover behavior, RPO, or RTO.

## Day 1 middleware direction

Because RatanOne already uses Redis, the source proposes upgrading Redis to version 6+ for the Day 1 release, citing cost and risk reduction. Hazelcast is described as an improvement for system NFRs after Day 1 rather than the initial implementation.

## Indicative CN Cashflow volume

| Year | Daily volume | 8 hours to handle | each instance handle (based on six instances) | Daily Max records | Daily Max 8 hours to handle | each instance handle (based on six instances) |
| --- | --- | --- | --- | --- | --- | --- |
| 2023 | 400 records | 0.83 records/min | 0.14 records/min | 900 | 1.875 records/min | 0.3 records/min |
| 2024 | 18000 records | 37.5 records/min | 6.25 records/min | 40500 | 84.3 records/min | 14 records/min |

| Year | Daily volume | 24 hours to handle | each instance handle (based on six instances) | Daily Max records | Daily Max 24 hours to handle | each instance handle (based on six instances) |
| --- | --- | --- | --- | --- | --- | --- |
| 2023 | 400 records | 0.28 records/min | 0.05 records/min | 900 | 0.625 records/min | 0.1 records/min |
| 2024 | 18000 records | 12.5 records/min | 2.1 records/min | 40500 | 28.1 records/min | 4.6 records/min |

These figures are not connected to cache object size, read rate, cache-hit rate, replication overhead, or memory sizing.

## Unofficial Redis and PostgreSQL benchmark

The source reports an unofficial development-environment comparison for the Nostro fuzzy-query endpoint:

```text
Test API: http://domain/v1/static/nostros/fuzzy?legalEntityFmid=401021850&currency=EUR
Environment: Development server
Client: CPU i5 / Memory 8G / Storage 500G
```

| storage | average | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cache ( Redis 5) | 285.7ms | 265ms | 280ms | 269ms | 290ms | 282ms | 324ms | 292ms | 326ms | 251ms | 278ms |
| DB (PostgreSQL 12） | 814 ms | 730ms | 736ms | 846ms | 867ms | 759ms | 784ms | 855ms | 868ms | 888ms | 807ms |

The reported average indicates approximately 65% lower response time for Redis in this test. The result does not establish production performance because concurrency, workload, cache-hit rate, data volume, tail latency, warm-up, correctness, and failure behavior were not specified.

## Assessment

The document establishes a clear architectural direction but leaves the operational contract incomplete. In particular, it does not define measurable freshness, performance, capacity, availability, recovery, security, or reconciliation requirements. The distinction between external golden-source data and RatanOne-owned data should be retained in subsequent designs.

This design is related to [[concepts/database-opensearch-reconciliation]] because both use persistent storage and synchronization/reconciliation, but it should not be treated as an OpenSearch design. It also complements [[concepts/cached-rule-loading]] while addressing a different data domain. The Redis use for the [[entities/api-gateway]] URL whitelist is an implementation detail and does not make Redis authoritative for gateway configuration.
