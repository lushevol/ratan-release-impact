---
type: query
title: What Are the Authoritative OpenSearch Performance SLOs?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, performance, slo, testing, cashflow]
related: [search-query-performance-sla, opensearch-backed-cashflow-querying, graphql-query-performance-observability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
---
# What Are the Authoritative OpenSearch Performance SLOs?

The source lists workload-specific targets, including two seconds for 20,000-record filtered cashflow-blotter pages, but does not define percentile, concurrency, dataset size, timeout behavior, or the inclusion of network and rendering time.

A performance SLO contract should identify the exact workloads that will use OpenSearch, latency percentile, throughput, test environment, monitoring method, and acceptance thresholds. It should also define the unit for the stated CLS Netting target of “1 M per Month.”