---
type: comparison
title: Manual Hold Representation Options
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, manual-hold, architecture, status-model, exception-handling]
related: [manual-cashflow-holding, cashflow-status-restoration, holding-release-precheck, orchestration, what-is-the-authoritative-manual-hold-status-transition-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Manual Holding Process Tech Design.md"]
---
# Manual Hold Representation Options

The technical design considers three representations for manual cashflow holds. It records main-status holding as the selected option. The source provides an architecture comparison, not implementation or operational evidence.

## Dedicated `isHeld` attribute

This alternative would add a boolean `isHeld` field to the cashflow model. The Lifecycle service would switch the field on and off, Query service would expose it, and the UI would display it in the blotter and details page.

Its stated benefit is independence from exception handling. Its stated costs are a model change and changes across multiple services. The release-holding check would need to consider both queued-cutoff status and `isHeld`.

## Checker-only exception

This alternative would create a checker-only exception when a user manually holds a cashflow. It would require ad hoc exception creation in Camunda and UI exception highlighting.

The source rejects this design because it couples holding to exception handling. A user could not resolve all exceptions while retaining a hold. It also produces non-standard behavior: a hold on Waiting leaves the status unchanged while increasing the exception count; a hold on Ready increases the exception count and moves the cashflow back to Waiting or pending verification.

## Main-status representation

This is the selected option. Holding blocks Pending Exception, Pending Netting, Ready, Queued, and Projected processing. Unhold restores the original status to avoid duplicated work.

The selected model is incomplete: the source does not define the held status, pre-hold-state persistence, transition logic, or service ownership. [[cashflow-status-restoration]] and [[what-is-the-authoritative-manual-hold-status-transition-contract]] capture these gaps.