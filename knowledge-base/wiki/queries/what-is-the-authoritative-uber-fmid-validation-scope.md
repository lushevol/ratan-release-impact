---
type: query
title: What Is the Authoritative Uber FMID Validation Scope?
tags: [query, uber, fmid, validation, routing, ratan]
related: [uber, ratanone, tdsx, message-bridge, uber-cashflow-validation-filtering, entity-scoped-validation-rollout, sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--1isntku]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Upstream Integration.md"]
---
# What Is the Authoritative Uber FMID Validation Scope?

## Question

For the March 28 and subsequent releases, does the target list

```text
400007847
401036553
400991880
```

define:

1. The only FMIDs that RATAN processes;
2. The FMIDs for which strict `cashflowCheckResult.passed` validation applies; or
3. The FMIDs enabled for an initial rollout while all other entities retain legacy behavior?

The source also requires confirmation of the exact mapping between `EG`, `NP`, `SA`, and these FMIDs. The mapping must not be inferred from the current document.

## Evidence

Cases 2 and 3 demonstrate validation behavior for FMID `400007847`. Case 1 used FMID `400899993`, but the open test environment did not apply the Message Bridge filter, so it cannot establish non-target routing behavior.

## Resolution needed

Confirm the authoritative FMID scope, the country/entity mapping, and whether filtering is performed by Message Bridge, TDSX, or RATAN.