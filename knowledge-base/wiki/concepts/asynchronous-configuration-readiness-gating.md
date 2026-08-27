---
type: concept
title: Asynchronous Configuration Readiness Gating
created: 2026-08-24
updated: 2026-08-24
tags: [asynchronous-loading, configuration, startup, readiness, error-handling]
related: [ratan-ui-configuration-bootstrap, window-ratan-config, form-rendering-action-gating, ratan-ui-form]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Optimize Cases.md"]
---

# Asynchronous Configuration Readiness Gating

Asynchronous configuration readiness gating is the rule that application initialization must wait until all mandatory configuration dependencies have loaded, parsed, and passed validation.

## Why it is needed

The documented RATAN UI implementation currently performs synchronous XHR before `main.js`. Replacing those calls with asynchronous requests removes the blocking XHR behavior but creates a race: `main.js` may execute before `window.ratanConfig` is complete.

The source explicitly calls for checking whether the configuration files have loaded before allowing the application entry point to proceed.

## Contract

A readiness mechanism should provide:

- A definitive ready state after all required resources succeed.
- A failure state when a resource is missing, malformed, unavailable, or invalid.
- A single atomic publication of the merged configuration.
- A way for `main.js` to await or subscribe to readiness.
- Explicit timeout and retry behavior.
- Diagnostics identifying the failed resource and failure reason.
- A policy for optional resources and partial configuration.

Consumers should never receive a partly merged `window.ratanConfig` unless partial configuration is an intentional, documented mode.

## Relationship to action gating

This concept is related to [[form-rendering-action-gating]] because both prevent dependent behavior from running too early. They operate at different lifecycle stages:

- Configuration readiness gates application initialization.
- Action gating controls user interactions after relevant UI state is available.

## Unresolved design questions

The source does not specify whether the six configuration files can be fetched in parallel, whether their merge order has semantic significance, or what user-visible experience should occur when configuration loading fails.