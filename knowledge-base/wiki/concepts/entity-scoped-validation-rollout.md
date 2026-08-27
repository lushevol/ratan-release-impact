---
type: concept
title: Entity-Scoped Validation Rollout
tags: [release-rollout, entity-scope, fmid, uber, cashflow-validation, configuration]
related: [uber, ratanone, tdsx, uber-cashflow-validation-filtering, cashflow-validation-flag-contract, what-is-the-authoritative-uber-fmid-validation-scope, when-will-validation-be-enabled-for-all-uber-entities]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Upstream Integration.md"]
---
# Entity-Scoped Validation Rollout

## Definition

An entity-scoped validation rollout enables a new validation rule for selected entities while preserving legacy behavior for entities that are not yet configured.

For the March 28 `Uber` integration release, strict cashflow validation is limited to the scope associated with FMIDs:

```text
400007847
401036553
400991880
```

`TDSX` checks the actual `cashflowCheckResult.passed` value for that scope and hardcodes `true` for other entities.

## Benefits

The approach allows the release to proceed without unexpectedly rejecting messages from entities that have not completed configuration. It also provides a controlled path for introducing validation incrementally.

## Risks

The hardcoded default weakens validation coverage outside the configured scope. An incomplete cashflow for an unconfigured entity can appear valid to RATAN because the supplied flag is `true`.

The source states that additional configuration is required before go-live for all other entities, but does not specify the configuration owner, completion criteria, or target date. The expansion plan is tracked in [[when-will-validation-be-enabled-for-all-uber-entities]].

## Non-permanent status

The March 28 behavior should not be treated as the permanent production contract. The authoritative scope, FMID-to-entity mapping, and behavior for non-target FMIDs require confirmation.