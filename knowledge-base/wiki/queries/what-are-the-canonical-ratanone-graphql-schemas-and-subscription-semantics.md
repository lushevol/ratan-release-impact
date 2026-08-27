---
type: query
title: What Are the Canonical RATANONE GraphQL Schemas and Subscription Semantics?
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, schema, subscriptions, notifications, ratanone, cashflow]
related: [ratanone-graphql-front-end-api-standard, cash-settlement-query-service-graphql-read-model, cashflow-notification-and-auto-refresh, entitlement-aware-ui-notifications, cashflow-version-tuple-comparison]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN.md"]
---
# What Are the Canonical RATANONE GraphQL Schemas and Subscription Semantics?

The source requires a clear schema for each use case and names trade, cashflow, counterparty, and exception queries and notifications. However, the available text supplies only empty schema-diagram headings and no executable or descriptive contract.

## Required Evidence

Obtain the authoritative schemas and supporting contracts for:

- trade list, detail, search, and notifications;
- cashflow list, detail, audit, detail extensions, search, and notifications for BCS and Settlement CN;
- counterparty information;
- exception list and notifications.

## Semantic Questions

- What types, fields, arguments, filter operators, pagination rules, null semantics, and error conventions apply?
- What is the resolver ownership and source-of-truth mapping for each field?
- How are `RATAN_DATA` fields registered, reviewed, versioned, and authorized?
- Which subscription transport is used?
- How are subscription authentication and entitlements enforced?
- What payload identity, ordering, deduplication, reconnect, replay, and version semantics apply?
- How do proposed GraphQL cashflow subscriptions preserve or integrate with [[cashflow-notification-and-auto-refresh]], [[entitlement-aware-ui-notifications]], and [[cashflow-version-tuple-comparison]]?

## Current Status

The source establishes planned coverage and a schema-first expectation, but it does not establish any canonical GraphQL schema or delivery behavior.