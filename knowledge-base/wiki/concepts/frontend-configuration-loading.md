---
type: concept
title: Frontend Configuration Loading
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, configuration, startup-performance, configmap, caching]
related: [ratanone, ratanone-ui-performance, static-configuration-management, config-server]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# Frontend Configuration Loading

## Problem

RatanOne blotter applications synchronously load separate configuration JSON files before application JavaScript can execute. This serializes I/O and delays mounting and first meaningful paint, even when local browser cache is available.

## Measured behavior

The unzipped configuration benchmarks reached `set-config-done` at approximately 1.68–1.75 seconds. The reported cashflow-grid FMP occurred at 2.89–4.46 seconds.

A consolidated zipped configuration reached:

- `load-zippedConfig-done`: 257.60 ms
- `set-config-done`: 257.80 ms
- `mount-app`: 601.70 ms
- Cashflow-grid FMP: 1,026.00 ms

The comparison is promising but does not isolate network latency, cache state, browser CPU, or parallel-request behavior.

## Proposed Config Map solution

The source proposes a single configuration API response with:

- One request for configuration.
- HTTP and server-side caching.
- Configuration synchronization and versioning.
- Auditability.
- DEVOPS integration hooks.
- Policy-based access control.
- Easier settings management.

This extends the concerns documented in [[static-configuration-management]] and may relate to [[config-server]], but the source does not establish the authoritative service or ownership model.

## Design questions

The source leaves unresolved whether the preferred implementation is:

- Parallel retrieval of individual files.
- A zipped configuration response.
- A centralized ConfigMap API.
- Another configuration-delivery mechanism.

Any production decision should compare cold-cache and warm-cache behavior under controlled network and browser conditions.