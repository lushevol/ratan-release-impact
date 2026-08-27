---
type: entity
title: Ratan ID
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, indonesia, regional-deployment, cash-settlement]
related: [ratan, indonesia-cash-settlement-onshoring, message-bridge, ratan-indonesia-data-residency, regional-cashflow-id-namespace]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Ratan ID

Ratan ID is the proposed Indonesia-local deployment of [[ratan]] for Indonesia settlement data and services.

The design intends Ratan ID to be independently deployed from Ratan GDC, with local data persistence and locally deployed services. It is expected to receive Indonesia cashflows through [[message-bridge]] and FM Solace after GDC-side message classification.

Ratan ID is a design target in the source, not evidence of an implemented or compliance-approved environment. Its final data boundary, shared-data dependencies, UI routing model, and downstream connectivity remain unresolved.