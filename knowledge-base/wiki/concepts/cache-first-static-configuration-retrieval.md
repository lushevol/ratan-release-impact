---
type: concept
title: Cache-First Static Configuration Retrieval
created: 2026-08-24
updated: 2026-08-24
tags: [static-configuration, caching, web, client-integration]
related: [static-configuration-management, static-data-service, mfe-cashflow-blotter, what-is-the-authoritative-static-config-api-and-protocol]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# Cache-First Static Configuration Retrieval

Cache-first static-configuration retrieval is the draft's proposed web-consumer behavior: return a cached configuration immediately when present, query for a newer version in the background, and update the consumer after the query completes.

On a first request or after cache clearing, dependent components wait for the latest result and then populate the cache. A non-cache-first mode always depends on the latest configuration result.

## Intended use

The approach is presented for hook-based UI retrieval, including `useStatisConfigByNames`. It is relevant to consumers such as [[mfe-cashflow-blotter]] that need operator mappings or booking-entity options without embedding those values in a release artifact.

## Unspecified correctness semantics

The draft does not define cache keys, TTL, expiry, invalidation, stale-read tolerance, refresh concurrency, error fallback, or how a background refresh changes component state. It also mentions “Radis” for service caching without confirming [[redis]] or defining a service-side design.

Feature flags are identified as a possible real-time-subscription case, but the source does not prescribe subscriptions for ordinary static configuration.