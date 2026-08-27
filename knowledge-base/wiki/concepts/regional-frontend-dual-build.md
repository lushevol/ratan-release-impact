---
type: concept
title: Regional Frontend Dual Build
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, build, Indonesia, GDC, CI/CD, shared-repository]
related: [indonesia-ui-microfrontend-isolation, ratan-indonesia-isolated-deployment, indonesia-environment-readiness-dependencies, deployment-profile]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# Regional Frontend Dual Build

Regional Frontend Dual Build produces GDC and Indonesia frontend artifacts from shared repositories using environment-dependent imports, bundle names, and API prefixes.

## Build selection

The documented build command is:

```json
"build": "cross-env REGION=idns concurrently npm:build:*"
```

The application selects regional dependencies and bundle names with:

```text
isIdns ? "@fm/idns_container" : "@fm/ratan_container";
isIdns ? "idns_container.js" : "ratan_container.js";
```

API configuration is selected with:

```text
isIdns ? "./.env.idns" : "./.env.global"
API_URL_PREFIX=/api/idns/ratan
API_URL_PREFIX=/api/ratan
process.env.API_URL_PREFIX
```

## Artifact mapping

| Repository | GDC artifact | Indonesia artifact |
| --- | --- | --- |
| `51358-mfe-ratan-container` | `ratan_container.js` | `idns_container.js` |
| `51358-mfe-cashflow-blotter` | `ratan_cashflow_blotter.js` | `idns_cashflow_blotter.js` |
| `51358-mfe-rules` | `ratan_rules.js` | `idns_rules.js` |
| `51358-mfe-nostro-static` | `ratan_nostro_static.js` | `idns_nostro_static.js` |

## Deployment separation

The source describes independent CR processes and deployment pipelines for Indonesia go-live. The pipeline parameter is:

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

Some shared dependencies remain GDC-hosted, including records for `51358-mfe-admin-module`, `51358-mfe-base`, `51358-mfe-trades`, and `51358-mfe-root-config`. The document does not fully explain whether this is intentional architecture or incomplete deployment reporting.

## Trade-off

The model avoids a permanently forked Indonesia codebase, but shared logic creates a risk of configuration drift and inconsistent behavior. Both regional outputs require coordinated testing and release controls.