---
type: concept
title: GDC-to-ID UI Nginx Forwarding
created: 2026-08-24
updated: 2026-08-24
tags: [Nginx, Indonesia, GDC, reverse-proxy, WebSocket, routing]
related: [ratan-gdc, ratan-indonesia, indonesia-ui-microfrontend-isolation, ratan-indonesia-network-segmentation, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# GDC-to-ID UI Nginx Forwarding

GDC-to-ID UI Nginx forwarding routes Indonesia API and static-asset requests from the GDC-facing shell to Indonesia infrastructure.

## Prefixes

Indonesia requests use:

```text
/api/idns/ratan/...
/api/idns/log/...
/static/idns/idns_container/idns_container.js
/static/idns/idns_cashflow_blotter/idns_cashflow_blotter.js
/static/idns/idns_rules/idns_rules.js
/static/idns/idns_nostro_static/idns_nostro_static.js
```

The API prefix is rewritten from `/api/idns/...` to `/api/...` at the forwarding layer. Static requests are similarly rewritten from `/static/idns/...` to the upstream asset path.

## WebSocket support

The proxy must use HTTP/1.1 and preserve upgrade headers:

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "Upgrade";
```

The source attributes the requirement to Nginx's default HTTP/1.0 forwarding behavior.

## Documented targets

The Dev-to-STG configuration includes either:

- `fmo-mfe-preprod.id.standardchartered.com:8453`; or
- `10.198.75.20:8453`, with host `uklvadrat0014a.pi.dev.net`.

Both examples use `least_conn` and contain `proxy_ssl_verify off`.

## Risks and unknowns

The source does not identify which target is authoritative, whether the same configuration applies to production, or whether disabling upstream certificate verification is permitted outside development or staging. The FMRP1-to-STG mapping is also incomplete.

This forwarding layer should not be treated as proof of backend authorization or complete data-residency compliance.