---
type: project
title: Indonesia Cash Settlement Onshoring
status: active
owner: ""
start_date: 2026-08-22
target_date: ""
created: 2026-08-22
updated: 2026-08-22
tags: [indonesia, ratan, onshoring, data-residency, cash-settlement]
related: [ratan-id, ratan-indonesia-data-residency, entitlement-based-regional-routing, 002-select-scbml-message-bridge-routing-for-indonesia, does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements, what-is-the-approved-indonesia-gdc-cross-region-data-flow-matrix, what-jwt-claims-and-ces-controls-authorize-indonesia-ratan-access, what-is-the-approved-ratan-indonesia-time-zone-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Indonesia Cash Settlement Onshoring

## Objective

Deploy an Indonesia-local instance of [[ratan]] that stores Indonesia-related settlement data locally while retaining operational access through the shared Post Trade Portal and enforcing [[ces]] entitlements.

## Proposed scope

- Deploy [[ratan-id]] as a regional Ratan environment separate from Ratan GDC.
- Route Indonesian Murex-derived cashflows through the selected SCBML and [[message-bridge]] design.
- Provide region-aware portal, API, and notification routing.
- Establish local configuration and database repositories.
- Configure Indonesia-specific settlement, SWIFT, SSI, Nostro/Vostro, accounting, and netting static data.
- Prevent LMS feed generation for Indonesia.

## Design status

The technical design selects Diagram 3 for upstream data provisioning. Direct downstream access to Ratan ID is currently preferred. The UI routing model and the final data-isolation boundary are not selected or approved in the source.

## Dependencies and risks

- Diagram 3 identifies GDC database persistence during MxML-to-SCBML conversion, which may conflict with local-storage requirements.
- CES and JWT regional claims, API validation, and audit controls are unspecified.
- Cross-region data flows for RDM, legal-entity data, queues, UI proxying, logs, and failure persistence require approval.
- UTC+7 infrastructure may affect settlement-critical jobs and timestamp processing.
- The required “same benchmark as GDC” has no measurable service-level targets or test plan.
- The regional netting/splitting identifier format is inconsistent in the design examples.

## Key decision

- [[002-select-scbml-message-bridge-routing-for-indonesia]] — proposed recording of the selected Diagram 3 topology and its unresolved data-residency consequence.

## Open questions

- [[does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements]]
- [[what-is-the-approved-indonesia-gdc-cross-region-data-flow-matrix]]
- [[what-jwt-claims-and-ces-controls-authorize-indonesia-ratan-access]]
- [[what-is-the-approved-ratan-indonesia-time-zone-model]]