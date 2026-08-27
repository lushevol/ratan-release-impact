---
type: query
title: "What Are the Korea 2026 NDS Auto Netting and Pending Fixing Blacklists?"
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, NDS-auto-netting, pending-fixing, blacklist, RATAN]
related: ["2026-korea-cash-settlement-onboarding", "nds-auto-netting", "pending-fixing", "pending-another-leg"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/New Entity onboarding checking list - Korea 2026.md"]
---
# What Are the Korea 2026 NDS Auto Netting and Pending Fixing Blacklists?

## Question

Which Korea 2026 entities, products, or flows must be excluded from NDS Auto Netting and Pending Fixing STP/NSTP processing?

## Evidence

The onboarding checklist lists both blacklists as `TBD`. NDS Auto Netting applies where Murex creates a child FXD trade to convert ND currency into delivery currency. Pending Fixing applies where products with fixing events require a cashflow to remain in `WAITING` with `Pending Another Leg`.

## Required resolution

Confirm the final blacklist values with Murex, Settlement Ops, and the RATAN business-rule owners before configuration, UAT, and regression testing.