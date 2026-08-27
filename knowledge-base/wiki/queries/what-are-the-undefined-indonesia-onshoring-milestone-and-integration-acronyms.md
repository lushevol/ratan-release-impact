---
type: query
title: What Are the Undefined Indonesia Onshoring Milestone and Integration Acronyms?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, onshoring, integration, delivery-planning, terminology]
related: [ratan-indonesia-onshoring-2026, surrounding-system-integration, ratan, solace]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia.md"]
---
# What Are the Undefined Indonesia Onshoring Milestone and Integration Acronyms?

The Indonesia onshoring plan uses terms without expansion or contract detail. Their meanings must be confirmed before they are used as implementation requirements or delivery acceptance gates.

## Terms requiring confirmation

- **MB:** Required integration between Global and ID; the participating systems, direction, protocol, ownership, and acceptance criteria are absent.
- **PT:** Listed in the September NFR row; it may refer to performance testing, but the source does not confirm this.
- **CPT:** Scheduled for November; the source does not define the activity or entry/exit criteria.
- **GDCW/GDCE:** Named in August connectivity requirements, without expansion or network-boundary definition.
- **FM Solace and Enterprise Solace:** Both are named as September message-channel dependencies. The source does not establish whether they are separate brokers, environments, services, or logical channels.

## Required resolution

Confirm the formal expansion, accountable team, scope, technical contract, prerequisites, and completion evidence for each term. Record whether May SIT and November CPT use non-production or production-connected environments.

This investigation supports [[ratan-indonesia-onshoring-2026]] and should not be used to infer topology or message behavior for [[solace]] without authoritative interface documentation.