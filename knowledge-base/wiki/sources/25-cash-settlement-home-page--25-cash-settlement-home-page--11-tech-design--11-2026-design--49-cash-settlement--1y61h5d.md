---
type: source
title: Cash Settlement Platform Architecture — Indonesia UI
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, Indonesia, UI, microfrontend, Nginx, deployment]
related: [cash-settlement-platform, ratan-indonesia, ratan-gdc, indonesia-ui-microfrontend-isolation, gdc-to-id-ui-nginx-forwarding, regional-frontend-dual-build, ratan-indonesia-network-segmentation, indonesia-ratan-data-residency-isolation, fmo-post-trade-portal, ratan-indonesia-isolated-deployment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# Cash Settlement Platform Architecture — Indonesia UI

## Summary

This technical design describes the Indonesia-specific user interface deployment for the Cash Settlement Platform. Indonesia UI packages are hosted as tenants on Post Trade Post and are served from Indonesian infrastructure. The global shell accesses Indonesia APIs and static assets through GDC-to-ID Nginx forwarding.

The design combines regional runtime separation with shared source repositories. Shared frontend repositories produce separate GDC and Indonesia bundles, while Indonesia releases use independent change-management and deployment pipelines.

## Deployment model

Opening an Indonesia tile loads regional bundles including:

- `container.js`
- `cashflow-blotter.js`
- `mfe-rules`
- `nostro-static.js`

The design distinguishes tenant hosting, regional bundle delivery, shared source repositories, and independent deployment operations. These characteristics do not, by themselves, prove complete runtime independence or backend authorization isolation.

## GDC-to-ID Nginx mapping

The documented environment mapping is:

| GDC Nginx environment | ID Nginx environment |
| --- | --- |
| Dev | STG |
| FMRP1 | STG |

The Dev-to-STG mapping has two documented upstream alternatives.

```nginx
# Indonisia location /api/idns/ {
rewrite ^/api/idns/(.*)$ /api/$1 break;
proxy_redirect off;
proxy_set_header Host fmo-mfe-preprod.id.standardchartered.com;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-Proto https;
proxy_set_header X-Forwarded-For $remote_addr;
proxy_set_header X-Forwarded-Host $remote_addr;
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "Upgrade";
proxy_ssl_server_name on;
proxy_ssl_name fmo-mfe-preprod.id.standardchartered.com;
proxy_ssl_verify off;
proxy_pass https://indonisia;
}
location /static/idns/ {
rewrite ^/static/idns/(.*)$ /$1 break;
proxy_redirect off;
proxy_set_header Host fmo-mfe-preprod.id.standardchartered.com;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-Proto https;
proxy_set_header X-Forwarded-For $remote_addr;
proxy_set_header X-Forwarded-Host $remote_addr;
proxy_ssl_server_name on;
proxy_ssl_name fmo-mfe-preprod.id.standardchartered.com;
proxy_ssl_verify off;
proxy_pass https://indonisia;
}
upstream indonisia {
least_conn;
server fmo-mfe-preprod.id.standardchartered.com:8453;
}
```

```nginx
# Indonisia location /api/idns/ {
rewrite ^/api/idns/(.*)$ /api/$1 break;
proxy_redirect off;
proxy_set_header Host uklvadrat0014a.pi.dev.net;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-Proto https;
proxy_set_header X-Forwarded-For $remote_addr;
proxy_set_header X-Forwarded-Host $remote_addr;
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "Upgrade";
proxy_ssl_server_name on;
proxy_ssl_name uklvadrat0014a.pi.dev.net;
proxy_ssl_verify off;
proxy_pass https://indonisia;
}
location /static/idns/ {
rewrite ^/static/idns/(.*)$ /$1 break;
proxy_redirect off;
proxy_set_header Host uklvadrat0014a.pi.dev.net;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-Proto https;
proxy_set_header X-Forwarded-For $remote_addr;
proxy_set_header X-Forwarded-Host $remote_addr;
proxy_ssl_server_name on;
proxy_ssl_name uklvadrat0014a.pi.dev.net;
proxy_ssl_verify off;
proxy_pass https://indonisia;
}
upstream indonisia {
least_conn;
server 10.198.75.20:8453;
}
```

The configuration explicitly disables upstream TLS verification with `proxy_ssl_verify off`. The source does not state whether this is limited to development or staging, so production acceptability remains unresolved.

## URL and asset prefixes

| Type | GDC | Indonesia |
| --- | --- | --- |
| API request | `/api/ratan/...`, `/api/log/` | `/api/idns/ratan/...`, `/api/idns/log/` |
| Static JavaScript module | `/ratan_container/ratan_container.js`; `/ratan_cashflow_blotter/ratan_cashflow_blotter.js`; `/ratan_rules/ratan_rules.js`; `/ratan_nostro_static/ratan_nostro_static.js` | `/static/idns/idns_container/idns_container.js`; `/static/idns/idns_cashflow_blotter/idns_cashflow_blotter.js`; `/static/idns/idns_rules/idns_rules.js`; `/static/idns/idns_nostro_static/idns_nostro_static.js` |

The API locations rewrite `/api/idns/...` to `/api/...` before forwarding. Static locations rewrite `/static/idns/...` to the corresponding upstream path.

## WebSocket forwarding

The source identifies Nginx's default HTTP/1.0 proxy behavior as incompatible with WebSocket upgrade. The required settings are:

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "Upgrade";
```

The document establishes a configuration requirement, but does not establish end-to-end WebSocket testing across every intermediary.

## Indonesia routes and import maps

The `root-config` import-map entries are:

```text
@fm/idns_container: "/static/idns/idns_container/idns_container.js"
@fm/idns_cashflow_blotter: "/static/idns/idns_cashflow_blotter/idns_cashflow_blotter.js"
@fm/idns_ratan_nostro_static: "/static/idns/idns_nostro_static/idns_nostro_static.js"
@fm/idns_ratan_rules: "/static/idns/idns_rules/idns_rules.js"
```

The route model is:

| Repository | Indonesia routes or screens |
| --- | --- |
| `ratan-container` | `/indonesia_cashflow_blotter_cn/*`; `/indonesia_rules_blotter/*`; `/indonesia_nostro_static_container/*` |
| `cashflow-blotter` | `Cashflow Blotter[ID]`: `indonesia_cashflow`; `Grouping Blotter[ID]`: `indonesia_cashflow_group_management`; `Cashflow Dashboard[ID]`: `indonesia_cashflow_dashboard`; `Authorization Limits[ID]`: `indonesia_cashflow_authorization_limits`; `BIC Netting Static[ID]`: `indonesia_cashflow_bic_netting_static_table`; `Nostro Threshold Static[ID]`: `indonesia_cashflow_splitting_static`; `Utilization Static[ID]`: `indonesia_cashflow_utilization_static_table` |
| `mfe-rules` | `Settlement NSTP Rules New[ID]`: `indonesia_new_nstp_rules`; `Suppression Rules [Swift][ID]`: `indonesia_swift_suppression_rules`; `Suppression Rules [Cashflow][ID]`: `indonesia_cashflow_suppression_rules`; `Netting [ID]`: `indonesia_new_netting_rules` |
| `nostro-static` | `Nostro Static[ID]`: `indonesia_nostro_static` |

## Shared repository and dual-build model

The build is controlled with a regional environment variable:

```json
"build": "cross-env REGION=idns concurrently npm:build:*"
```

Conditional imports and bundle names are documented as:

```text
isIdns ? "@fm/idns_container" : "@fm/ratan_container";
isIdns ? "idns_container.js" : "ratan_container.js";
```

API configuration is selected through environment files:

```text
isIdns ? "./.env.idns" : "./.env.global"
API_URL_PREFIX=/api/idns/ratan
API_URL_PREFIX=/api/ratan
process.env.API_URL_PREFIX
```

The bundle mapping is:

| UI repository | GDC bundle | Indonesia bundle |
| --- | --- | --- |
| `51358-mfe-ratan-container` | `ratan_container.js` | `idns_container.js` |
| `51358-mfe-cashflow-blotter` | `ratan_cashflow_blotter.js` | `idns_cashflow_blotter.js` |
| `51358-mfe-rules` | `ratan_rules.js` | `idns_rules.js` |
| `51358-mfe-nostro-static` | `ratan_nostro_static.js` | `idns_nostro_static.js` |

The shared-repository approach reduces duplication but requires controls against configuration and behavior drift between GDC and Indonesia outputs.

## Regional client-side behavior

The design adds Indonesia-specific client-side storage:

```text
businessFieldsCashflowIndonesia
```

It also retains the existing `holidayDB` IndexedDB handling. Regional styling changes include adjustments for `ag-grid` components and shared frontend styles.

## Functional requirements

The source lists these Indonesia UI requirements:

1. Indonesia blotter booking-entity dropdowns include only Indonesia.
2. Indonesia dashboard status cards open the Indonesia Cashflow Blotter or Grouping Blotter.
3. Trade blotter cashflow-details navigation redirects to GDC or Indonesia according to trade booking entity.
4. Global rules synchronize from GDC to Indonesia.
5. Indonesia timezone is supported.
6. Post Trade Portal tiles support the Indonesia UI.

Regional routes and UI filters are not evidence of backend authorization enforcement.

## Deployment services and pipeline parameter

The documented service matrix includes:

| Service | Indonesia change or deployment role | Environment | Deployed |
| --- | --- | --- | --- |
| `51358-ratanone-ansible` | GDC Nginx and Indonesia Nginx deployment | GDC, ID | Y |
| `51358-mfe-admin-module` | Import map and Indonesia tiles | GDC | Y |
| `51358-mfe-base` | Indonesia API handling | GDC | Y |
| `51358-mfe-container` | Indonesia URL prefix and routes | ID | Y |
| `51358-mfe-cashflow-blotter` | Indonesia URL prefix and routes | ID | Y |
| `51358-mfe-rules` | Indonesia URL prefix and routes | ID | Y |
| `51358-mfe-nostro-static` | Indonesia URL prefix, route, and version guard | ID | Y |
| `51358-mfe-trades` | Redirect to the Indonesia cashflow blotter | GDC | Not recorded |
| `51358-mfe-root-config` | Import map calls `/api/auth/v1/fmo/admin/importmap/active` | GDC | Not recorded |

The pipeline exposes a deployment location parameter:

```yaml
azure-pipelines-npm.yml
- name: deploymentLocation
  type: string
  displayName: deployment area "indonesia" or "global"
  default: global
  values:
  - global
  - indonesia
deploymentLocation: ${{ parameters.deploymentLocation }}
```

## Evidence boundaries and open issues

The document provides strong implementation evidence for routes, prefixes, bundle names, Nginx directives, and pipeline parameters. It does not establish:

- the authoritative GDC-to-ID environment mapping;
- whether `proxy_ssl_verify off` is allowed outside development or staging;
- which components are intentionally GDC-hosted;
- how direct API access is prevented across regions;
- how shared-repository changes are validated against both builds;
- complete production approval or operational ownership.

These issues should be tracked alongside [[queries/what-is-the-authoritative-indonesia-ui-deployment-and-hosting-model]], [[queries/is-proxy-ssl-verify-off-permitted-in-indonesia-production-nginx]], and [[queries/does-indonesia-ui-route-filtering-enforce-backend-authorization]].