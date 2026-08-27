---
type: concept
title: Region-Aware UI Build Dependency Remapping
tags: [webpack, single-spa, build-system, microfrontend, indonesia, gdc]
related: [indonesia-ui-microfrontend-isolation, cash-settlement-platform, ratan-indonesia, ratan-gdc]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia/Indonesia.md"]
---
# Region-Aware UI Build Dependency Remapping

## Definition

Region-aware UI build dependency remapping selects a region-specific frontend package during a build while retaining a shared source repository. In the Indonesia design, `REGION=ID` selects `@fm/idns_ratan_container`; the default GDC build selects `@fm/ratan_container`.

## Proposed mechanism

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

The associated build command is:

```json
package.json build: "cross-env REGION=ID concurrently npm:build:*",
```

The remapping external is placed before the default `single-spa` externals. This ordering is required so the alias request can be rewritten before a default external rule handles it unchanged.

## Constraints

This approach selects dependencies at build time rather than switching dependencies at runtime. Consequently, GDC and Indonesia artifacts, promotion controls, configuration, and compatibility tests must be defined explicitly.

Required validation includes:

- Building with `REGION=ID` and verifying the resolved package.
- Building without `REGION` and verifying the GDC default.
- Confirming that no unintended `@fm/ratan_container` external remains in the ID artifact.
- Testing package-version compatibility and runtime loading.
- Verifying independent deployment and rollback behavior.
- Testing environment-variable handling in local, CI, and release builds.

The source presents this mechanism as an option, not an approved architecture decision.