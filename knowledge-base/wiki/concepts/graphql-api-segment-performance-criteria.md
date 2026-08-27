---
type: concept
title: GraphQL API Segment Performance Criteria
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, performance, latency, cash-settlement, api]
related: [graphql-frontend-aggregation, cashflow-data-provider-query-performance, cash-settlement-capacity-planning-baseline, is-graphql-candidate-query-performance-within-sla]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# GraphQL API Segment Performance Criteria

The GraphQL proposal recommends evaluating each API segment independently so that aggregation does not become constrained by a slow resolver or backend dependency.

## Recorded Thresholds

| API Segment Size | Recommended Response Time | Minor Response Time |
| --- | --- | --- |
| <= 500B | <= 200ms | <= 300ms |
| <= 1KB | <= 200ms | <= 300ms |
| <= 50KB | <= 500ms | <= 1000ms |
| <= 100kb | <= 1000ms | <= 1500ms |

The source cites an external Hobo web-performance article for this guidance. It does not define payload compression, timing boundaries, percentile targets, concurrency, or whether the thresholds are formal internal SLAs.

## RATAN Observations

The source reports an average full GraphQL request time of 393ms and partial requests generally between 220ms and 320ms. It also reports maximum times of 4.6 seconds for the full request and 9.6 seconds for candidate queries.

The candidate-query maximum is materially above the recorded minor target and requires separate investigation. See [[queries/is-graphql-candidate-query-performance-within-sla]].