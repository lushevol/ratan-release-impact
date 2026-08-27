---
type: concept
title: Indonesia UI Microfrontend Isolation
created: 2026-08-24
updated: 2026-08-23
tags: [Indonesia, microfrontend, UI, regional-isolation, import-map, user-interface, deployment-isolation, css, browser-state]
related: [cash-settlement-platform, ratan-indonesia, fmo-post-trade-portal, indonesia-ratan-data-residency-isolation, region-entitled-drawer-filtering, regional-frontend-dual-build, gdc-to-id-ui-nginx-forwarding, ratan-indonesia-isolated-deployment, region-aware-ui-build-dependency-remapping, cashflow-blotter, grouping-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia/Indonesia.md"]
---
# Indonesia UI Microfrontend Isolation

## Definition

Indonesia UI Microfrontend Isolation is the design pattern for separating Indonesia-specific Cash Settlement Platform frontend assets, routes, runtime dependencies, client-side state, and release pipelines from their GDC counterparts within Post Trade Post. Its intended outcome is that Indonesia and GDC tiles can evolve and deploy independently without unintended interference.

The UI is hosted as a tenant on Post Trade Post. Runtime hosting and release governance are separate concerns: Indonesia releases are described as using independent CR processes and deployment pipelines.

## Indonesia modules and runtime loading

The primary UI architecture source describes Indonesia-specific modules exposed by `root-config` through `/static/idns/...` import-map entries:

- `idns_container.js`
- `idns_cashflow_blotter.js`
- `idns_rules.js`
- `idns_nostro_static.js`

Under that source's naming, the container, cashflow blotter, rules, and Nostro Static applications receive distinct Indonesia routes and labels.

The nested `Indonesia.md` source separately names `container.js`, `cashflow-blotter.js`, `mfe-rules`, and `nostro-static.js` as independently loaded Indonesia-specific packages that should be deployed to Indonesian servers. It does not establish whether these names correspond directly to the `idns_*` import-map assets described by the primary UI architecture source.

This approach is application and asset isolation rather than merely a visual filter applied to the GDC UI.

## Regional UI behavior

Indonesia-specific behavior includes:

- Indonesia-only booking-entity values in blotter dropdowns. The primary UI architecture source describes these generally; the nested `Indonesia.md` source identifies them as Indonesia-only `FMID` values.
- `Dashboard[ID]` navigation to Indonesia blotters.
- Booking-entity-based routing from trade details, including routing of Trade Blotter Cashflow Details according to booking entity.
- Indonesia timezone support.
- A separate `businessFieldsCashflowIndonesia` client-side storage identifier.

These behaviors are related to [[fmid-8-indonesia-entitlement]] and [[region-entitled-drawer-filtering]].

## Isolation dimensions

The nested `Indonesia.md` source states that deployment isolation alone is insufficient and identifies the following dimensions for a complete design:

- Separate asset origins, deployment environments, and release pipelines.
- Region-specific API base URLs or prefixes.
- CSS module boundaries and controlled global Ant Design selectors.
- Namespaces for `window` properties, DOM IDs, custom events, telemetry, and caches.
- Unique `localStorage`, `sessionStorage`, and IndexedDB keys or database names.
- Mount and unmount cleanup for DOM changes and event listeners.
- Service-worker and browser-cache scope.
- Destination-region authorization for cross-region navigation.

That source proposes CSS module migration and environment-variable-based isolation, but does not define the contracts needed for the other dimensions. Its proposed storage-key and browser-state isolation is consistent with, but should not be generalized beyond, the separately documented `businessFieldsCashflowIndonesia` identifier.

## Authorization and data boundary

Separate bundles, routes, client-side filters, and deployment pipelines do not prove backend authorization. Direct API access, entitlement enforcement, and data-residency compliance require independent server-side evidence.

Client-side filtering should not be treated as a substitute for backend authorization. Cross-region navigation must validate both the destination region and the user entitlement server-side. This distinction complements [[region-entitled-drawer-filtering]] and [[fmces-based-ratan-entitlement-authorization]].

## Relationship to build and deployment strategy

Independent CR processes and pipelines favor strong release boundaries. The nested `Indonesia.md` source states that shared source favors a single repository with region-aware builds, while also stating that repository choice is tracked separately from this isolation concept and should not be inferred from that source.

See [[gdc-to-id-ui-nginx-forwarding]] for the network path and [[regional-frontend-dual-build]] for the shared-source and build model.