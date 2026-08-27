---
type: query
title: Who Owns Uber Versus Legacy Workflow Routing?
created: 2026-08-22
updated: 2026-08-22
tags: [query, routing, workflow, uber, lifecycle, orchestration]
related: [uber, scbml, uber-legacy-workflow-isolation, lifecycle-compatibility-api, ratan-uber-migration-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# Who Owns Uber Versus Legacy Workflow Routing?

## Question

Which component is authoritative for selecting the Uber/JSON workflow versus the legacy SCBML workflow for single-cashflow, batch, scheduled-job, netting, exception, confirmation, and SSI-refresh operations?

## Evidence

The proposal assigns transparent routing to Lifecycle for several UI and scheduled-job operations. Other proposals require UI or Rule to inspect booking-entity scope, FMID, or a message-type response. SSI cannot directly determine message type and may require Orchestration to choose the next flow.

## Why it matters

Distributed routing can spread tactical Uber-specific logic across clients and domain services. Centralized routing reduces duplication but requires Lifecycle or Orchestration to have sufficient data and clear ownership.

## Resolution needed

Define the authoritative routing component, the source of truth for entity scope and message type, behavior for mixed-format batches, and fallback handling when routing metadata is unavailable.