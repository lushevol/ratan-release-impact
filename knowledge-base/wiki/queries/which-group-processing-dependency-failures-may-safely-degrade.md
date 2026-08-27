---
type: query
title: Which Group Processing Dependency Failures May Safely Degrade?
created: 2026-08-24
updated: 2026-08-24
tags: [graceful-degradation, dependencies, cashflow, group-processing, data-quality]
related: [tdsx-uber-message-listener, kafka-persistent-retry-and-dlt-recovery, static-data-service, query-service, cashflow-precheck-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# Which Group Processing Dependency Failures May Safely Degrade?

The source reports different handling for dependency failures: some calls retry and return empty data, some return defaults or empty strings, some add an exception flag, and some propagate failure. It does not define a domain-approved classification for those choices.

## Areas Requiring Classification

- `isDedicatedChangeWithCatch` reportedly returns `true` when `ratanone-static-data-service` lookup fails.
- `CashflowGraphQLService` is intended to retry selected calls and eventually return empty results.
- Several commands degrade to defaults, empty strings, or incomplete fields.
- `DataAmbassadorClient` may return empty results after retry.
- The query-service path is reported to have no retry or degradation.
- Netting-client exceptions may propagate to an outer processing layer.

## Decision Criteria Needed

For each dependency and field, define:

1. whether failure may be retried synchronously;
2. whether an empty/default value is business-safe;
3. how a degraded result is marked for users and downstream services;
4. whether the event must enter retry topics or DLT instead;
5. the financial, operational, and audit consequences of incorrect enrichment.

Without this classification, graceful degradation can avoid a visible processing failure while creating incomplete or misclassified cashflow data.