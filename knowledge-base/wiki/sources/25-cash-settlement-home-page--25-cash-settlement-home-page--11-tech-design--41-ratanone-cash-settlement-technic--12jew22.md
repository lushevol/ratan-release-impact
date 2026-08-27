---
type: source
title: OpenSearch Business Live Plan
authors: []
year: 2026
url: ""
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratanone, opensearch, migration, business-go-live]
related: [opensearch, ratanone-opensearch-agent, ratanone, opensearch-business-live, three-way-data-reconciliation, idempotent-historical-data-migration, double-writing, kafka-persistent-retry-and-dlt-recovery, cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# OpenSearch Business Live Plan

## Summary

This technical design proposes moving OpenSearch from technical go-live to business go-live for the RatanOne Cash Settlement platform in 2026. OpenSearch already persists cashflow and cashflow-history data. The proposed next stage makes OpenSearch the default query source while retaining PostgreSQL (PG) persistence and immediate PG fallback during the initial rollout.

The plan is directional rather than execution-ready. It does not define final schemas, API contracts, ownership boundaries, performance targets, cutover gates, or the target date for stopping PG writes.

## Proposed rollout

### Day 1: Internal flow switch

The internal rollout should:

1. Add persistence for other required domains, including Trade and NSTP Exception data.
2. Adapt queries to OpenSearch using the Ultra query model.
3. Make OpenSearch the default source for cashflow blotter, cashflow detail, and cashflow dashboard queries.
4. Continue PG persistence during the transition.
5. Switch affected queries back to PG immediately if production issues occur.
6. Perform a one-time historical migration with a cutoff time.
7. Ensure that migration is idempotent and does not create dirty or duplicate data.
8. Establish real-time reconciliation across the lifecycle service, Query service PG, and OpenSearch.

### Day 2: External flow switch

The external rollout should:

1. Update external queries if the OpenSearch data model changes.
2. Open the required firewall path.
3. Provide a v2 query API.

Day 2 depends on decisions made during Day 1 about the canonical data model, query behavior, security, and API compatibility.

## Data model adaptation

The following representations must be aligned without conflating persistence and query concerns:

- `RatanCashSettlementData.proto`
- `ResultNew` GraphQL schema
- OpenSearch schema definition

The current GraphQL query surface includes:

```text
Cashflow Data Query
Cashflow Data History Query
Exception Query
SSI Stashing Query
SSI Candidates Query
Affirmation Details
Netting Component Query
```

Each query domain requires an explicit decision about whether data is sourced from OpenSearch, a domain service, or a combination of both.

## Data flow and double writing

Cash Settlement currently uses a double-writing model after technical go-live. Other domain data is expected to follow the same strategy. The transition therefore requires clear write ordering, retry behavior, document identity, version handling, and reconciliation rules.

See [[double-writing]] and [[ratanone-opensearch-agent]].

## Real-time reconciliation

The proposed reconciliation compares three data sources:

```text
1. Lifecycle service - SCBML history
2. Query service PG - cashflow data & cashflow data history
3. OpenSearch - cashflow index & cashflow history index
```

The existing production Grafana reconciliation section is described as inaccurate and requires enhancement. The design does not yet specify reconciliation keys, frequency, freshness windows, completeness rules, tolerances, mismatch ownership, or remediation workflow.

Grafana dashboard:

https://uklvapapp591.gdc.standardchartered.com:3000/d/fxz10qqf6kvswa/middleware-opensearch?from=now-5m&to=now&timezone=browser&var-application=ratanone-opensearch-agent&var-instance=uklvadrtn002a.pi.dev.net:ratanone-opensearch-agent:0&var-datasource=de6jyvajhwbnkd&var-Month=2025-08&var-monthPattern=2025-08.%2A&var-Day=$__all&refresh=5m

See [[three-way-data-reconciliation]].

## Exception management

The OpenSearch agent currently uses Kafka non-blocking retry but has no further operational process for messages that reach the DLT. The proposed improvement is to:

- Create an index recording DLT messages.
- Provide manual replay.
- Consider automatic replay.

Replay must be safe under duplicate delivery, stale updates, out-of-order events, poison messages, and repeated failure. These controls should extend the existing [[kafka-persistent-retry-and-dlt-recovery]] approach.

## Historical data migration

Historical migration is required before business go-live so that users receive complete historical data and complete real-time data after the cutover. The migration requires a cutoff time, restartability, idempotency, validation, and duplicate prevention.

The initial tool inventory is:

| Industry ETL Tool | Language | Pros | Cons | Official Website | |
| --- | --- | --- | --- | --- | --- |
| pgsync | Python | lightweight | only support PG as data source | [AtomGit \| GitCode - 全球开发者的开源社区,开源代码托管平台}](https://gitcode.com/gh_mirrors/pgs/pgsync) | |
| Apache NIFI | java | support customized requirement UI management | Complicate Learning curve not easy to maintain | [Apache NiFi](https://nifi.apache.org/) | |
| Logstash | Ruby | existing tech stack | Need development | [Logstash: Collect, Parse, Transform Logs \| Elastic](https://www.elastic.co/logstash) | |
| Self Development | Java/python | easy to customized | dev effort | | |

This comparison is only an initial inventory and is insufficient for tool selection. Throughput, restartability, schema transformation, security, operational ownership, validation, and rollback need to be assessed.

See [[idempotent-historical-data-migration]].

## CCR enhancement

The plan records that CCR enhancement requires Zeyu's input. The meaning, scope, acceptance criteria, and critical-path impact of CCR are not defined.

## Data visibility

OpenSearch Dashboards is identified as an operational visibility tool.

Development environment:

http://10.198.199.160:5602/app/home

## Relevant repositories

- [51358-ratan-cashflow-lifecycle-service](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-cashflow-lifecycle-service)
- [51358-ratan-cash-settlement-query-service](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratan-cash-settlement-query-service)
- [51358-ratanone-data-provider-internal-client](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-data-provider-internal-client)
- [51358-ratanone-internal-component-simulator](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-internal-component-simulator)
- [51358-ratanone-data-provider-external-client](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-data-provider-external-client)
- [51358-ratanone-external-component-simulator](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-external-component-simulator)
- [51358-ratanone-opensearch-agent](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-opensearch-agent)
- [51358-ratanone-grpc-api](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-grpc-api)

## Referenced material

- [OpenSearch Technical Go Live Introduction - 2025](https://confluence.global.standardchartered.com/display/DSP/OpenSearch+Technical+Go+Live+Introduction+-+2025)
- [OpenSearch Inbound/Outbound Performance Testing](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3212175335)

## Open design questions

- Which domains and fields must be persisted in OpenSearch?
- Which source is authoritative for each query field?
- What is the canonical OpenSearch schema and versioning contract?
- What constitutes behavioral equivalence between OpenSearch and PG queries?
- What are the reconciliation keys, freshness targets, and mismatch-resolution procedures?
- How are OpenSearch documents versioned and deduplicated?
- What are the cutover and rollback gates?
- When can PG writes be stopped?
- What is the scope of the CCR enhancement?
