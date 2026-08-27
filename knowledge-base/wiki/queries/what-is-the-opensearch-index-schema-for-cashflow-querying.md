---
type: query
title: What Is the OpenSearch Index Schema for Cashflow Querying?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, index-schema, cashflow, query-service]
related: [opensearch, opensearch-agent, opensearch-backed-cashflow-querying, ratan-opensearch-rollout]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
---
# What Is the OpenSearch Index Schema for Cashflow Querying?

The plan schedules an OpenSearch schema update based on the UBER Open search agent Query service but provides no index mappings, document identity rules, shard strategy, retention policy, query definitions, or handling for FMO Comment nanosecond timestamps.

The schema is required to assess whether filtered 20,000-record blotter pages and the other named workloads can meet their stated targets.