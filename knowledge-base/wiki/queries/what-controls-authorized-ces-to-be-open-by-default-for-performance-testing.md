---
type: query
title: What Controls Authorized CES to Be Open by Default for Performance Testing?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, entitlement, performance-testing, access-control, governance]
related: [uber-fxu-technical-live-and-business-go-live-2026, 002-place-ces-entitlement-mediation-in-auth-service, 003-adopt-two-layer-ces-emergency-disablement, fmaa]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
---
# What Controls Authorized CES to Be Open by Default for Performance Testing?

## Question

What access-control, approval, and rollback controls governed the plan to open CES by default for performance testing?

## Evidence

The release-page scope notes state: “CES go live plan, open CES (as default) for PT.” The source does not identify the environment, user population, time limit, approval authority, logging, rollback, or interaction with existing entitlement controls.

## Required resolution

Confirm:

- the CES environment and testing period;
- who received default access and why;
- the approval and change record;
- enforcement point and audit logging;
- emergency disablement and rollback procedure;
- alignment with [[002-place-ces-entitlement-mediation-in-auth-service]] and [[003-adopt-two-layer-ces-emergency-disablement]].

Until these controls are confirmed, the note should not be interpreted as authorization for broad or persistent CES access.