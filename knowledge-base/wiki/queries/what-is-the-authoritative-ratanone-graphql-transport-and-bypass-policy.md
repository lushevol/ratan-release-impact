---
type: query
title: What Is the Authoritative RATANONE GraphQL Transport and Bypass Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, transport, rest, frontend, architecture, ratanone]
related: [ratanone-graphql-front-end-api-standard, graphql-query-performance-observability, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN.md"]
---
# What Is the Authoritative RATANONE GraphQL Transport and Bypass Policy?

The source says RATANONE frontend queries should use GraphQL, but labels listed read cases as `HTTPS GET`. It also permits a “single API call” where aggregation creates a performance issue.

## Questions to Resolve

- Is GraphQL mandatory for every RATANONE frontend read?
- Does the single-call performance exception mean one GraphQL operation, a REST endpoint, or another gateway pattern?
- May a frontend call a backend service directly, and who approves such an exception?
- Are GraphQL queries transported over GET, POST, or both?
- What authentication, caching, logging, and query-safety rules apply to each supported transport?
- Does the policy differ across trade, cashflow, counterparty, and exception domains?

## Why It Matters

Without a defined boundary, teams cannot determine whether a performance-driven implementation remains compliant with the GraphQL-first standard or creates an unmanaged alternate frontend API path.