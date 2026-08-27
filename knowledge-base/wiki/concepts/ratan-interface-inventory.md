---
type: concept
title: RATAN Interface Inventory
tags: [ratan, interfaces, integration, go-live, architecture]
related: [ratan, fmmis-41190, filenet-28852, ratanone-message-bridge, fileit-file-arrival-notification, operational-level-agreement, what-is-the-authoritative-ratan-interface-and-go-live-inventory]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN -Interfaces.md"]
---
# RATAN Interface Inventory

## Definition

A **RATAN interface inventory** is a register of systems, integration mechanisms, processing classifications, and business data exchanged through interfaces connected to RATAN. It provides scope-level integration visibility rather than a complete technical or operational contract.

## Inventory Recorded by the Source

The source identifies two inbound flows under **Pending go-live flow**:

1. **FMMIS - 41190 → Ratan - 51358** through **FileIT**, classified as **online**, exchanging **exception data**.
2. **FileNet - 28852 → Ratan - 51358** through an **API**, classified as **online**, exchanging **term sheet data**.

No outbound RATAN interface is identified in this source.

## Status Semantics

“Pending go-live” indicates go-live-related scope, but does not establish that the interfaces are implemented, tested, approved, or live in production. A production configuration reference is evidence of a configuration location only; it is not evidence of operational status.

The term **online** is not defined. For the FileIT flow, it could refer to event-triggered or near-real-time processing, or simply distinguish the flow from a scheduled batch. The source does not resolve this ambiguity.

## Configuration and Governance

Interface behavior may depend on both:

- `/apps/ratanrt/services/ratan-service-properties/config-repo/application-prod.yml`; and
- the resources in [[ratanone-message-bridge]].

The source also references the [[operational-level-agreement]] for RATAN and FM Settlement. It does not reproduce OLA commitments or identify interface owners.

## Required Evidence for a Complete Inventory

A complete authoritative inventory should record, for each interface:

- canonical sender and receiver identities;
- interface status and effective date;
- file or API contract;
- endpoint, authentication, and authorization details;
- field mappings and validation rules;
- retry, failure, reconciliation, and monitoring behavior;
- service ownership and support contacts; and
- availability and processing commitments.

The authoritative status and contract remain open questions in [[what-is-the-authoritative-ratan-interface-and-go-live-inventory]].