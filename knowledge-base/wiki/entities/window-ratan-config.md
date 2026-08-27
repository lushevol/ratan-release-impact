---
type: entity
title: window.ratanConfig
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, JavaScript, configuration, browser-global]
related: [ratan-ui-form, ratan-ui-configuration-bootstrap, asynchronous-configuration-readiness-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Optimize Cases.md"]
---

# window.ratanConfig

`window.ratanConfig` is the browser-global object used by RATAN UI startup code to expose merged application configuration.

## Construction

The source implementation loads and merges:

- `ratanConfig.json`
- `cashflowDetailsConfig.json`
- `tradeDetailsConfig.json`
- `tradesConfig.json`
- `exceptionConfig.json`
- `cashflowConfig.json`

The merge uses object spread syntax. `ratanConfig` is applied last and therefore takes precedence when keys overlap.

## Access protection

The implementation defines getter-only properties on `window.ratanConfig`. Reads return values from the merged configuration object. Writes invoke a setter that logs:

```text
Can not be modified!
```

This is a shallow top-level write guard, not proof of deep immutability. Nested objects may remain mutable unless an explicit deep-freezing strategy is implemented.

## Startup dependency

`main.js` must not consume `window.ratanConfig` until all mandatory configuration resources have loaded and been validated. This dependency is part of [[ratan-ui-configuration-bootstrap]] and requires [[asynchronous-configuration-readiness-gating]] if the requests are converted to asynchronous loading.