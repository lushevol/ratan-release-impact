---
type: source
title: Cash Settlement Platform Architecture — Indonesia UI
authors: []
year: 2026
url: ""
venue: ""
tags: [cash-settlement, indonesia, user-interface, microfrontend, deployment-isolation]
related: [cash-settlement-platform, ratan-indonesia, ratan-gdc, ratan-indonesia-isolated-deployment, indonesia-ratan-data-residency-isolation, ratan-global-rule-synchronization, indonesia-ui-microfrontend-isolation, region-aware-ui-build-dependency-remapping]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia/Indonesia.md"]
---
# Cash Settlement Platform Architecture — Indonesia UI

## Summary

This design note proposes ways to isolate Indonesia-specific Cash Settlement UI packages from GDC while retaining selected code-sharing mechanisms. The intended deployment model gives Indonesia its own versions of `container.js`, `cashflow-blotter.js`, `mfe-rules`, and `nostro-static.js`, deployed to Indonesian servers.

Indonesia is expected to use independent CR processes and deployment pipelines. Indonesian features may therefore diverge from GDC. The source does not select an approved repository or release strategy and does not provide sufficient implementation detail to prove that GDC and Indonesia tiles cannot affect one another.

## Architecture options

### Duplicate repository

The Indonesia repository synchronizes code from GDC through a Git remote and merge. This approach provides stronger code-line independence but leaves the long-term maintenance model unresolved.

```bash
git remote add source-repo <repo url>
git fetch source-repo
git checkout feature/xxxx
git merge --no-ff --allow-unrelated-histories source-repo/main
```

### Git cherry-pick

Selected GDC commits are copied into the Indonesia code line. This allows granular reuse but requires policies for dependency ordering, conflict resolution, missed commits, and auditability.

```bash
git remote add source-repo <repo URL>
git fetch source-repo
git log source-repo/branch-name
git cherry-pick <commit-hash>
```

### Single repository with build-time dependency remapping

A shared repository can select the container package during the webpack build. The proposed build command sets `REGION=ID`:

```json
package.json build: "cross-env REGION=ID concurrently npm:build:*",
```

The proposed webpack configuration maps `@fm/ratan_container` to the Indonesia package for an ID build:

```js
const region = (process.env.REGION || "GDC").toUpperCase();
const containerPackage = region === "ID" ? "@fm/idns_ratan_container" : "@fm/ratan_container";
// single-spa default externals may externalize @fm/* first.
// Put remap external in front so @fm/ratan_container can be rewritten by REGION.
const defaultExternals = Array.isArray(defaultConfig.externals) ? defaultConfig.externals : [defaultConfig.externals].filter(Boolean);
const remapContainerExternal = ({ request }, callback) => {
  if (request === "@fm/ratan_container") {
    return callback(null, containerPackage);
  }
  return callback();
};
defaultConfig.externals = [remapContainerExternal, ...defaultExternals];
```

The remapping external must precede the default `single-spa` externals so that the request is rewritten before it is externalized unchanged. This is a build-time mechanism, not evidence of runtime switching within a single artifact.

## UI isolation requirements

The source identifies several possible leakage paths between GDC and Indonesia:

- Global LESS styles.
- `window` properties.
- `document.body` mutations.
- Storage, session storage, and IndexedDB.
- API prefixes and regional service endpoints.

The proposed style migration is:

- Normal LESS to `module.less`.
- Ant Design LESS to a module with selectors such as `:global(.ant-xxx)`.
- AG Grid LESS to be deleted, although the replacement styling approach is not specified.

The source mentions environment variables for API prefixes and browser storage isolation but does not define variable names, build-time versus runtime semantics, key-prefix conventions, database naming, or enforcement.

## Indonesia business behavior

The source specifies the following functional expectations:

1. Trade Blotter Cashflow Details supports redirection to GDC or Indonesia according to the trade booking entity.
2. Indonesia blotter booking-entity dropdowns contain Indonesia `FMID` values only.
3. Global rules synchronize in real time from GDC to Indonesia.
4. `Dashboard[ID]` status cards open `Cashflow Blotter[ID]` or `Grouping Blotter[ID]`.

These requirements relate to [[fmid-8-indonesia-entitlement]], [[region-entitled-drawer-filtering]], and [[ratan-global-rule-synchronization]]. They do not define an authoritative booking-entity-to-region mapping, destination authorization check, route contract, synchronization guarantees, or acceptance tests.

## Assessment

The strongest contribution of this source is its explicit intent for independent Indonesia/GDC UI deployment and its concrete webpack remapping option. The repository strategy remains unresolved between duplicate repositories, cherry-picking, and a single repository.

The design should be followed by an architecture decision covering repository ownership, release governance, artifact versioning, rollback, and synchronization. A separate isolation specification is also needed for CSS, browser globals, DOM mutations, storage, IndexedDB, custom events, cache, service workers, telemetry, and cross-region navigation authorization.

## Source material

The source is a short design note titled `Indonesia.md` under the Cash Settlement Platform Architecture — Indonesia UI design area. It includes references to architecture diagrams stored as source attachments; those diagrams are not reproduced here because their content is not available in the supplied text.