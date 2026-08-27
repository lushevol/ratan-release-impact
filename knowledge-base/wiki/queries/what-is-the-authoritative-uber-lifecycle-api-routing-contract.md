---
type: query
title: What Is the Authoritative Uber Lifecycle API Routing Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, lifecycle, api-routing, workflow-migration]
related: [uber-restructured-workflow-integration, uber-restructured-flow-vs-scbml-legacy-flow, cashflow-lifecycle-state-machine-restructuring, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# What Is the Authoritative Uber Lifecycle API Routing Contract?

The source proposes `/v2/ratan/camunda/lifecycle/status/move` as the consolidated Camunda lifecycle endpoint, while retaining some “Keep Same” endpoints and identifying several legacy calls as not Uber-supported.

A confirmed routing decision is needed for lifecycle status changes, user-status actions, holding, pre-check, stamping, Swift interactions, and UI callers.

## Evidence

- Swift service calls a legacy lifecycle API that is not Uber-supported in the documented maker-checker scenario.
- MFE Cashflow Blotter is mapped from `/v1/ratan/cashflow/user/status/update` to `/v2/ratan/cashflow/move/status/user`.
- The lifecycle API inventory labels publication responsibilities and several pre-check/stamping behaviours as “Need confirm.”
- The source asks whether a new flow can route SCBML traffic to the old flow while retaining transactional operations.

## Resolution criteria

Publish an approved routing matrix that identifies, for each action, its caller, canonical endpoint, flow-selection rule, compatibility behaviour, transaction boundary, and event/publication responsibility.