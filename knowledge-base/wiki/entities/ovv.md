---
type: entity
title: OVV
created: 2026-08-25
updated: 2026-08-25
tags: [ovv, markets-udp, ratan, readiness-notification]
related: [marketudp, ratan, solace, sabre, ratan-markets-udp-pv-integration]
sources: ["RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# OVV

## Role

OVV is described as a service within Markets UDP. It receives or exposes the upstream Sabre feed and notifies RATAN through Solace when PV data is ready.

## Integration Behavior

OVV’s notification triggers RATAN to fetch PV data separately through the Markets UDP API. The source does not specify the Solace subject, notification payload, batch identifier, correlation mechanism, or delivery guarantees.
