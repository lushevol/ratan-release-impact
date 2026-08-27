---
type: query
title: Does the RATAN FM Settlement OLA Cover RDM, FileIT, Solace, and KongGateway?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, rdm, ola, fileit, solace, konggateway, operations, open-question]
related: [ratan-rdm-reference-data-integration, rdm, operational-level-agreement, fmo]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# Does the RATAN FM Settlement OLA Cover RDM, FileIT, Solace, and KongGateway?

## Question

Does the referenced **RATAN - OLA - FM Settlement - IS - Confluence** document define operational responsibilities and service levels for the complete RDM integration?

## Current evidence

The source states:

> BPMS OLA location, no change required

It links to the RATAN OLA but supplies no service hours, recovery objectives, data-quality responsibilities, escalation path, or ownership information for RDM, FileIT, Enterprise Solace, or KongGateway.

## Required confirmation

The operating model should identify:

- End-to-end service owner.
- Owners for RDM, each transport channel, and receiving RATAN components.
- Availability and freshness targets for each feed.
- Incident, retry, replay, and recovery responsibilities.
- Monitoring and escalation procedures.
- Whether the existing OLA is approved for all seven feeds.