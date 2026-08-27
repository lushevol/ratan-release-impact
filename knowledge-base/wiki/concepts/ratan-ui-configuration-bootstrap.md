---
type: concept
title: RATAN UI Configuration Bootstrap
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, frontend-performance, configuration, application-startup]
related: [ratan-ui-form, window-ratan-config, asynchronous-configuration-readiness-gating, form-rendering-action-gating, what-is-the-authoritative-ratan-ui-configuration-bootstrap-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Optimize Cases.md"]
---

# RATAN UI Configuration Bootstrap

RATAN UI configuration bootstrap is the startup lifecycle that retrieves application configuration, merges the configuration sources, publishes the result as [[window-ratan-config]], and makes it available to `main.js`.

## Existing lifecycle

The documented implementation runs an inline script in the HTML `<head>` before the deferred application bundle. It synchronously requests six JSON resources and parses each response before publishing the merged object.

This makes configuration retrieval part of the critical startup path. Requests are issued serially, so their durations accumulate.

## Required lifecycle properties

A robust bootstrap should define:

1. The mandatory and optional configuration resources for each application.
2. The merge order and duplicate-key precedence.
3. Schema validation and malformed-response handling.
4. A readiness signal consumed by `main.js`.
5. Atomic publication of the complete configuration.
6. Timeout, retry, fallback, and user-visible failure behavior.
7. Cache-control, versioning, and invalidation rules.
8. Whether configuration values are safe for browser exposure.

## Candidate delivery models

### Asynchronous browser-side loading

The browser can issue configuration requests asynchronously and publish the merged result after all required requests succeed. This can reduce serialized network blocking, but it requires an explicit readiness contract. Simply changing synchronous XHR to asynchronous XHR can cause `main.js` to observe missing or partial configuration.

### SSR-injected configuration

A server can serialize configuration into the generated HTML. This removes separate configuration requests from the client startup path, but introduces concerns about HTML size, safe serialization, caching, deployment capability, and disclosure of sensitive values.

## Evidence boundaries

The source clearly establishes the current synchronous loading pattern. It does not establish which delivery model should be adopted, provide performance measurements, or prove that the configuration files contain form-validation rules.

Startup readiness should remain distinct from [[form-rendering-action-gating]], which concerns whether user actions are enabled after UI state has been rendered.