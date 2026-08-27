---
type: query
title: "What Is the Authoritative Korea 2026 Routing and Entity Scope?"
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, routing, entity-scope, cash-settlement, RATAN]
related: ["2026-korea-cash-settlement-onboarding", "korea", "legacy-versus-strategic-cash-settlement-routing"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/New Entity onboarding checking list - Korea 2026.md"]
---
# What Is the Authoritative Korea 2026 Routing and Entity Scope?

## Question

Which booking entities and branches are in scope for the Korea 2026 cash-settlement onboarding, and should Korea follow the legacy LOANIQ/BCS flow, the strategic flow, or another routing model?

## Evidence

The checklist is explicitly associated with Korea 2026, but its strategic-flow whitelist is:

`CN/SG/MY/IN/UK/DE/EG/NP/SAUDI`

Korea does not appear in that list. The source also distinguishes routing to RAZOR from processing in RATAN, where RATAN generates SWIFT and accounting.

## Why this matters

The routing decision determines:

- The responsible settlement platform.
- SWIFT-generation ownership.
- Accounting-generation ownership.
- Cashflow suppression and workflow whitelist configuration.
- SSI hierarchy and Tag 20 logic.
- Required downstream changes and test coverage.

## Required resolution

Obtain an authoritative entity-and-branch list and routing decision from the project owner, Settlement Ops, Product Owners, and relevant platform teams. Do not infer Korea's routing from its presence in the migration title alone.