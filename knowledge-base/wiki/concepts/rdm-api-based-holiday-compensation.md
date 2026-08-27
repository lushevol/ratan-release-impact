---
type: concept
title: RDM API-Based Holiday Compensation
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, indonesia, holiday-calendar, static-data, scheduled-sync, nas]
related: [rdm, 51358-ratanone-static-data-service, static-data-synchronization, indonesia-environment-readiness-dependencies, indonesia-ratan-data-residency-isolation, rdm-api-pagination-and-reconciliation, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# RDM API-Based Holiday Compensation

RDM API-Based Holiday Compensation is the proposed Indonesia pattern for maintaining currency holidays, special holidays, and country-code mappings when NAS-mounted RDM files cannot be consumed locally.

The pattern replaces the relevant parts of legacy RDM-FILEIT file ingestion with scheduled API calls from [[51358-ratanone-static-data-service]] to [[rdm]]. It is intended to preserve downstream business-day and settlement cutoff-date calculation while keeping GDC and Indonesia deployments separate.

## Required Data Scope

The immediate implementation scope includes:

- Currency holidays and special holidays used for cash-settlement cutoff calculations.
- Country-code mappings used by SSI stamping.

The reviewed RDM common files and bank-code/LEI data are excluded only under current Indonesia usage assumptions. Their exclusion must be revisited if Indonesia trade rule checking or relevant payment flows are introduced.

## Design Requirements

A production implementation should provide:

- Validated per-environment RDM API routes, versions, and response schemas.
- Authenticated access through [[kong]] where applicable.
- Complete pagination, including the documented page-number difference between holiday and country APIs.
- Idempotent insertion, update, and deletion behavior.
- Normalization of RDM date formats before persistence.
- Run-level observability: source window, pages fetched, records received, changes applied, failures, retry status, and reconciliation outcomes.
- Threshold and approval behavior for unusually large deltas.
- A schedule that runs after RDM data becomes available and before settlement operations require the calendar.

## Constraints and Risks

The design does not establish that all changes with an unchanged holiday natural key are irrelevant to cutoff logic. It must not implement insert/delete-only behavior until [[what-are-the-authoritative-ratan-holiday-update-and-deletion-semantics]] is resolved.

The selected approach also depends on unresolved API, credential, and operational scheduling decisions. See [[what-is-the-approved-rdm-api-contract-for-indonesia-holiday-compensation]], [[what-is-the-approved-indonesia-rdm-api-schedule-and-data-freshness-sla]], and [[how-should-ratan-manage-kong-authentication-for-scheduled-rdm-api-calls]].