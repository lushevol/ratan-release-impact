---
type: concept
title: RATAN Counterparty Data Integration
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, counterparty-data, integration, cache, graphql, trade-blotter]
related: [ratan, dqsl, bpsi, sci, graphql, operational-level-agreement, what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract, what-is-the-ratan-counterparty-cache-freshness-and-failure-policy, what-is-the-authoritative-ratan-operational-monitoring-and-alerting-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
---
# RATAN Counterparty Data Integration

RATAN retrieves counterparty information for trade details through an integration path involving [[dqsl]], [[bpsi]], and [[sci]].

```text
RATAN → GraphQL request → DQSL → BPSI authentication → SCI → SCI data → RATAN
```

## Responsibilities

- [[ratan]] initiates the request from the trade-details experience and caches retrieved SCI data.
- [[dqsl]] receives RATAN's GraphQL request and participates in the authenticated downstream access path.
- [[bpsi]] provides an authentication token only.
- [[sci]] is the stated source of counterparty business data.

The source does not demonstrate that the trade blotter is the same interface as [[cashflow-blotter]].

## Cache and Freshness Behaviour

RATAN refreshes the counterparty-data cache daily at `03:00 SGT`. If requested information is absent, RATAN makes a real-time call to downstream systems.

This means normal reads can use data from the last successful scheduled refresh, while cache misses depend on the availability and latency of DQSL, BPSI, and SCI. The source does not define refresh-failure handling, stale-data display, cache expiry, invalidation, or whether cache-miss responses are persisted.

## Contract Boundary

This is an interface-flow description, not a complete API contract. The GraphQL operation, endpoints, schemas, token mechanics, field mappings, timeouts, retries, and error semantics are unavailable because the source's interface specification is image-only.

The operational reference points to an OLA, but no commitments are stated in this source. Monitoring requirements remain unresolved in [[what-is-the-authoritative-ratan-operational-monitoring-and-alerting-contract]].
---
