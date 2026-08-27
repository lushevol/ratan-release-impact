---
type: comparison
title: Static Config Service Draft versus Static Configuration Design
created: 2026-08-24
updated: 2026-08-24
tags: [static-configuration, architecture, governance, reconciliation]
related: [static-configuration-management, static-data-service, ratan-static-data-service, config-server, shared-static-configuration-maker-checker-engine, kafka-based-configuration-propagation, what-is-the-authoritative-static-config-api-and-protocol]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# Static Config Service Draft versus Static Configuration Design

This comparison records the need to reconcile *Ratan Static Config Service Design (Draft)* with the existing [[static-configuration-design]] source and [[self-service-entity-branch-onboarding]] design before implementation.

## What this draft proposes

The draft proposes a generic database-backed configuration model, per-context JSON Schema validation, versions, audit records, name/domain lookup, web cache-first access, and a possible extension of [[static-data-service]].

It also introduces pending content states compatible in principle with [[shared-static-configuration-maker-checker-engine]], but it does not specify maker/checker roles, approvals, or transition rules.

## Reconciliation points

A review of the related designs should establish the authoritative answer for:

- service ownership among [[static-data-service]], [[ratan-static-data-service]], and [[config-server]];
- canonical persistence and identity model for configuration definitions and content;
- maker/checker governance and pending-change isolation;
- API protocol and consumer integration;
- configuration propagation, including whether [[kafka-based-configuration-propagation]] applies;
- cache invalidation and real-time change delivery; and
- the canonical model for entity and branch onboarding versus `settlement_booking_entities`.

This page does not assert that the designs conflict. The available draft alone does not provide enough evidence to compare the other designs' detailed contracts.