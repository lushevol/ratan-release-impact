---
type: concept
title: Indonesia Pending-Fixing-Flag Relay
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, pending-fixing-flag, murex, kafka, solace, batch-to-realtime, draft]
related: [batch-service, mxg-adaptor, message-bridge, nas, kafka, solace, indonesia-ratan-data-residency-isolation, murex-ratan-hybrid-batch-and-realtime-processing, fixing-flag-entity-based-routing, what-is-the-authoritative-indonesia-fixing-flag-event-contract, what-is-the-approved-gdc-indonesia-kafka-solace-topology-for-fixing-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# Indonesia Pending-Fixing-Flag Relay

Indonesia Pending-Fixing-Flag Relay is a proposed architecture for delivering Murex pending-fixing-flag information to Ratan Indonesia without direct cross-country NAS access.

## Proposed mechanism

GDC processes the NAS-hosted batch file, selects Indonesia cashflows, and publishes events to Kafka. [[message-bridge]] forwards the messages through FM Solace; an Indonesia bridge consumes from an FM Solace queue and writes to Indonesia Kafka. The Indonesia [[batch-service]] then applies unspecified existing revert logic.

## Scope boundary

This is a draft design for pending-fixing flags only. It should not be generalized as the standard contract for Murex cashflow processing or as a replacement for all batch integrations.

## Preconditions still requiring definition

A production-ready relay requires an approved event envelope, correlation and idempotency keys, source-file lineage, ordering and duplicate rules, retries and replay, reconciliation, observability, and data-residency/security controls. See [[what-is-the-authoritative-indonesia-fixing-flag-event-contract]] and [[what-is-the-approved-gdc-indonesia-kafka-solace-topology-for-fixing-flags]].