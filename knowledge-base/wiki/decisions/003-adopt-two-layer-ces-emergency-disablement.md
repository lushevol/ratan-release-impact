---
type: decision
title: Adopt Two-Layer CES Emergency Disablement
created: 2026-08-24
updated: 2026-08-24
tags: [ces, data-entitlement, emergency-access, resilience, security]
related: [ces, auth-service, query-service, cash-settlement-data-entitlement, what-controls-govern-ces-entitlement-emergency-bypass]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
status: proposed
deciders: []
date: 2026-08-24
supersedes: ""
---
# Adopt Two-Layer CES Emergency Disablement

## Context

CES failures or erroneous CES policy data can prevent users from accessing Cash Settlement data because normal CES enforcement is fail-closed. The design rejected a URL-based bypass because it could not cover SSDR and notification paths and introduced additional security risk.

## Decision

Use two configuration layers for emergency CES downgrade:

1. Query Service has a CES enable/disable control that falls back to existing behavior when disabled.
2. auth-service has a global CES toggle and a per-user disabled list. When disabled, auth-service does not fetch CES and reports that entitlement enforcement is disabled.

```yml
scb:
  ems3:
    enabled: true
    disabled-users:
      - 2022123
```

## Consequences

- Operators can restore service availability during a prolonged CES outage or incorrect CES configuration.
- The fallback removes CES data-entitlement enforcement and can provide privileged access; it is therefore a material security exception.
- The configuration must not be treated as a normal resilience mechanism or an automatic circuit breaker.
- Required controls include restricted approvers, auditable changes, monitoring, reason capture, expiry or review deadlines, rollback, and notification of affected stakeholders.
- The document does not define these controls or identify the authorized operators. They remain tracked in [[what-controls-govern-ces-entitlement-emergency-bypass]].

## Status note

The source calls this the chosen configuration, but the current production implementation and its control governance are not confirmed. This page remains proposed pending confirmation.