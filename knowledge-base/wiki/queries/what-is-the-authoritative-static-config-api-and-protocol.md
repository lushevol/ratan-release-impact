---
type: query
title: What Is the Authoritative Static Configuration API and Protocol?
created: 2026-08-24
updated: 2026-08-24
tags: [static-configuration, api, graphql, rest, authorization]
related: [static-data-service, cache-first-static-configuration-retrieval, static-config-service-draft-vs-static-configuration-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# What Is the Authoritative Static Configuration API and Protocol?

The draft assumes that [[static-data-service]] can provide GraphQL APIs, but its only concrete access example is a REST-style POST request to `/api/ratan/staticconfig`.

The authoritative contract should resolve:

- whether GraphQL, REST, or both are supported;
- query, mutation, and subscription operations;
- lookup semantics by configuration name and domain;
- response shape, filtering, pagination, and error behavior;
- authentication and authorization for reads and administrative changes;
- cache validation and configuration-version exposure; and
- which contexts, if any, require real-time push notifications.

The draft should not be treated as defining an API contract.