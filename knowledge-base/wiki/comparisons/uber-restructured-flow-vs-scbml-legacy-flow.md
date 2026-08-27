---
type: comparison
title: Uber Restructured Flow vs SCBML Legacy Flow
created: 2026-08-24
updated: 2026-08-24
tags: [uber, scbml, api-migration, workflow-routing, cash-settlement]
related: [uber, scbml, uber-restructured-workflow-integration, cashflow-lifecycle-state-machine-restructuring, netting-service, what-is-the-authoritative-uber-lifecycle-api-routing-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# Uber Restructured Flow vs SCBML Legacy Flow

| Dimension | Uber restructured flow | SCBML legacy flow |
| --- | --- | --- |
| Intended API direction | Uses consolidated or version-2 lifecycle APIs and new UI routing. | Retains legacy endpoints, some of which are explicitly described as SCBML-only. |
| Lifecycle status movement | Candidate consolidation on `/v2/ratan/camunda/lifecycle/status/move`. | Existing version-1 lifecycle endpoints remain present or are being removed. |
| User-status update | MFE Cashflow Blotter target is `/v2/ratan/cashflow/move/status/user`. | Existing caller uses `/v1/ratan/cashflow/user/status/update`. |
| UI netting and unnetting | Requires an Uber-capable Netting/UnNetting API. | The documented old UI netting API supports only SCBML. |
| Event publication | Proposed to persist state and publish only a domain event for selected user actions; `process_in` responsibility is unresolved. | Not established by this source. |
| Transactional operations | The source raises manual netting and transactional operation preservation as an open integration issue. | Existing transactional behaviour may be embedded in legacy routing, but the source provides no final contract. |
| Schema path | Includes TDSX → Ratan protobuf-to-JSON and Ratan → Ratan JSON-to-protobuf-to-JSON compatibility assumptions. | Not separately specified. |

## Observed migration gaps

The source records that the Swift service calls a legacy lifecycle API not supported for Uber and that the UI uses SCBML-only APIs for netting and manual unnetting. It also records a `NetNew` publication gap in an Uber netting scenario.

These observations do not establish a final coexistence strategy. “Keep Same” entries in the API inventory may mean temporary compatibility, no migration, or an unchanged endpoint; the source does not consistently distinguish these meanings.

## Decision needed

The authoritative routing contract must specify:

1. Which actions are accepted by Uber/restructured APIs.
2. Whether and how SCBML requests are routed to a legacy path.
3. How transactional netting and unnetting are preserved across the boundary.
4. Which component publishes domain events and processing messages.

See [[what-is-the-authoritative-uber-lifecycle-api-routing-contract]].