---
type: query
title: What Is the Authoritative RATAN-FMSGW Interface Contract?
tags: [ratan, fmsgw, interface-contract, solace, swift, settlement, open-question]
related: [ratan-fmsgw-settlement-messaging, fmsgw, ratan-interface-inventory, ratan-interface-architecture, swift, solace, operational-level-agreement]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMSGW 54949.md"]
---
# What Is the Authoritative RATAN-FMSGW Interface Contract?

## Question

What authoritative specification defines the technical, operational, ownership, and rollout contract for RATAN interface `54949` to FMSGW?

## Current Evidence

The source states that RATAN generates SWIFT MT and MX messages for settlement and publishes them to FMSGW through Solace:

```text
Ratan --(Solace)-->FMSGW
```

It records country coverage for both feeds, but does not provide implementation details or establish production status. The linked FM Settlement OLA is a reference only; its contents are not included in the source.

## Information Needed

The authoritative contract should be located or confirmed for:

- MT message types and MX business message definitions
- Payload schemas, validation, and versioning
- Solace topics, queues, endpoints, authentication, and authorization
- Delivery, acknowledgement, ordering, duplication, retry, replay, and dead-letter behavior
- Monitoring, alerting, operational ownership, and escalation paths
- Support procedures and troubleshooting documentation
- Country-level scope, rollout, and go-live status
- FMSGW’s formal name, ownership, and processing role
- The meaning of “real-time” for this interface
- The relationship between this interface and the FM Settlement OLA

## Interim Position

Treat [[concepts/ratan-fmsgw-settlement-messaging]] as a high-level inventory record rather than an authoritative technical contract. Do not infer FMSGW-specific details from other RATAN integrations such as eBBS, ENISIS, or CDUPS.