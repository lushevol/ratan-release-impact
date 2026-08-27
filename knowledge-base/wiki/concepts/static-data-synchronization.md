---
type: concept
title: Static Data Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-data, rules, cross-data-centre, synchronization]
related: [ratan, data-synchronizer-manager, ratan-data-synchronizer, request-id-based-sync-correlation, per-destination-sync-status-tracking, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# Static Data Synchronization

Static data synchronization is the proposed transfer of static/reference data and rules from Ratan GDC to downstream XDC deployments. The source illustrates the pattern with synchronization from GDC to IDDC for Indonesia.

## Proposed architecture

The design positions synchronization as a reusable capability that is independent of domain business logic. It is embedded as a common module in a domain service, with domain-specific producers and consumers responsible for the business payload.

[[data-synchronizer-manager]] manages event tracking and delivery state, while [[ratan-data-synchronizer]] retains the newest synchronization event for each data object.

An independent synchronization service is named as an alternative deployment approach but is not specified or evaluated.

## Operational model

The model separates:

- Data Producer publication and retry responsibility.
- Data Consumer consumption acknowledgement and periodic reconciliation responsibility.
- Common-module responsibility for correlation and destination-specific synchronization state.

The source does not specify the static-data object lifecycle for deletes, rule removal, schema evolution, version compatibility, or manual refresh operations.

## Scope

This pattern applies to static data and rules. It is not evidence of a generic replacement for existing Ratan cashflow or settlement integration controls.