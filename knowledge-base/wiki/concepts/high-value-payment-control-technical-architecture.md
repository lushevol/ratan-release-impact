---
type: concept
title: High Value Payment Control Technical Architecture
tags: [high-value-payment, technical-architecture, settlement-day-2, service-integration]
related: [ratan, settlement-day-2, high-value-payment-queue, high-value-payment-approval-queue, outbound-property-propagation-to-swift-mt-mx, parent-cashflow-resolution-by-splitting-id, what-is-the-authoritative-high-value-payment-decision-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# High Value Payment Control Technical Architecture

The HVP technical design distributes control-related responsibilities across five services rather than defining a single HVP engine.

## Design responsibilities

Orchestration extracts `cashflowId` and `businessVersion` from SCBML, retrieves STP/NSTP information and `lastUser` from Lifecycle service, then publishes outbound metadata. Swift service is expected to consume that metadata and enrich MT/MX output. Query service supports USD-equivalent query and persistence. Netting service resolves a parent cashflow from `splittingId`.

This architecture is a technical prerequisite or dependency map for HVP handling associated with [[ratan]]. It is related to, but does not define, the operational behavior of [[high-value-payment-queue]] or [[high-value-payment-approval-queue]].

## Boundaries

The source does not establish that lifecycle state, `lastUser`, USD equivalent, or parent-cashflow resolution are all inputs to one HVP decision. It also does not define thresholds, approval roles, queue outcomes, or release conditions.

See [[what-is-the-authoritative-high-value-payment-decision-rule]] for the unresolved policy and processing-order contract.