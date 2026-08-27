---
type: concept
title: Uber-Legacy Workflow Isolation
created: 2026-08-22
updated: 2026-08-22
tags: [workflow, isolation, uber, scbml, json, migration, orchestration]
related: [uber, scbml, ratan, ratan-one, lifecycle-compatibility-api, ratan-strategic-json-data-model, ratan-uber-migration-options, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# Uber-Legacy Workflow Isolation

## Definition

Uber-legacy workflow isolation is the proposed migration pattern of operating a separate workflow for Uber/JSON cashflows while retaining the existing workflow for other or legacy SCBML cashflows.

## Rationale

The source gives four reasons for isolation:

1. Reduce the impact of orchestration changes.
2. Permit restructuring according to the RATAN 2.0 design.
3. Avoid requiring one service to support both SCBML and JSON.
4. Avoid making every domain API message-type agnostic, which would expand regression scope.

Isolation can reduce format complexity within an individual workflow, but it introduces parallel implementation, regression, and operational responsibilities.

## Routing implications

Every non-inbound operation must determine the correct workflow. Relevant boundaries include:

- UI requests to Lifecycle, Netting, and Orchestration.
- Rule-driven confirmation flows.
- Materialize, Release, and AutoNetting scheduled jobs.
- SSI refresh.
- Netting, un-netting, splitting, and component status operations.
- Single and bulk exception handling.

The design alternates between centralized routing in Lifecycle or Orchestration and caller-side checks based on booking entity or FMID. Distributed checks may make integration less transparent and spread Uber-specific logic into business clients.

## Limitations

Isolation does not by itself resolve historical Uber-scope cashflows carrying SCBML, mixed-format batch operations, lifecycle API differences, or ownership of `process_in` publishing. These issues are tracked in [[queries/who-owns-uber-versus-legacy-workflow-routing]], [[queries/how-are-historical-scbml-cashflows-handled-in-uber-scope]], and [[queries/who-publishes-process-in-for-netnew-and-revert-to-queued]].