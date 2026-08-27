---
type: concept
title: RATAN-TDSX Integration
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tdsx, integration, rest-api, solace, trade-validation, payment-schedule]
related: [tdsx, sabre, tds3, solace, ratan-trade-control, trade-validation, uber-validation, ratan-service-governance, what-is-the-authoritative-ratan-tdsx-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDSX)-29126.md"]
---
# RATAN-TDSX Integration

The RATAN-TDSX integration is a documented high-level relationship between RATAN and [[tdsx|TDSX]], which abstracts TDS2 and [[tds3|TDS3]] for consumer applications.

## Interaction patterns

### Payment Schedule retrieval

The RATAN [[ratan-trade-control|trade-control]] flow retrieves a Payment Schedule from TDSX for presentation in the Trade Blotter.

### REST trade validation

RATAN calls a TDSX REST API for trade validation. This statement applies to the documented RATAN-TDSX path only and does not establish TDSX as the dependency for every RATAN validation workflow.

### Uber-message delivery

TDSX publishes Uber messages that are delivered to RATAN through [[solace|Solace]]. The source does not name a Solace topic, queue, receiving component, message schema, acknowledgement policy, or delivery guarantee. It also does not confirm that [[ratanone-message-bridge|ratanone-message-bridge]] is the receiver.

## Operational ownership

The source assigns RATAN-side support to RATAN ONE PSS and identifies SABRE_TDSX_BA PSS and SABRE PSS as TDSX-side contacts. It references the BPMS OLA but does not reproduce its service targets, escalation paths, or incident procedures.

## Contract gap

The source contains no end-to-end sequence, connection parameters, REST specification, or troubleshooting procedure. The authoritative details remain tracked in [[what-is-the-authoritative-ratan-tdsx-interface-contract]].