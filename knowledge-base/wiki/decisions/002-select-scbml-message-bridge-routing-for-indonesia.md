---
type: decision
title: Select SCBML Message Bridge Routing for Indonesia
status: proposed
deciders: []
date: 2026-08-22
supersedes: ""
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, indonesia, scbml, message-bridge, architecture]
related: [indonesia-cash-settlement-onshoring, message-bridge, ratan-id, mxml-to-scbml-conversion, ratan-indonesia-data-residency, does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Select SCBML Message Bridge Routing for Indonesia

## Context

Indonesia cashflows require a route into Ratan ID while real-time Murex MxML, cashflow batch files, and fixing-flag batch files follow different existing ingestion paths. Direct batch-service deployment in Indonesia is unsuitable because cross-country NAS mounting is not allowed and batch files can contain Indonesia and non-Indonesia payments together.

## Decision

Use the source document’s Diagram 3 design for upstream cashflow provisioning:

- Convert Murex inputs to SCBML in the existing GDC adaptor.
- Publish SCBML to GDC Message Bridge.
- Route Indonesian cashflows through FM Solace to Ratan ID.
- Send non-Indonesian cashflows through the existing standardization-service route.
- Keep batch-service for fixing-flag batch parsing and entity-based routing.
- Do not deploy mxg-adaptor or batch-service in Ratan ID for the described cashflow routes.

## Consequences

The design uses one new Solace SCBML topic and queue pair and combines real-time and batch routing after conversion. It reduces Indonesia deployment components.

However, the adaptor persists data in a GDC database during SCBML conversion. This creates an unresolved conflict with the requirement that Indonesia data be stored onshore and with the stated absolute GDC–Indonesia isolation objective. This decision remains proposed until data classification, permitted persistence, retention, and compliance approval are documented.