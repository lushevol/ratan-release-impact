---
type: query
title: What Exactly Separates EG, NP, and SA UBER Technical Live from Business Live?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, technical-live, business-live, eg, np, sa, operations]
related: [uber, technical-live-versus-business-live, uber-fxu-technical-live-and-business-go-live-2026, ratan-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
---
# What Exactly Separates EG, NP, and SA UBER Technical Live from Business Live?

## Question

What production capabilities may be enabled for EG, NP, and SA during UBER technical live without making the release business live?

## Evidence

The plan scopes UBER processing onboarding for EG, NP, and SA while stating that FXU will not be enabled. PSS records that opening EG, NP, and SA flow data would mean business live rather than technical live.

## Required resolution

Define, for each entity, whether the following are allowed during technical live:

- inbound flow ingestion;
- processing and persistence;
- cashflow-blotter and OpenSearch visibility;
- maker-checker actions;
- downstream accounting, netting, SWIFT, or settlement activity;
- operational ownership and customer/business impact.

The resolution should identify the approving authority, activation and rollback controls, monitoring responsibilities, and the evidence required to transition to business live.