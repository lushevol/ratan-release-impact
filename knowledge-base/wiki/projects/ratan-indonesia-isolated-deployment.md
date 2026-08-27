---
type: project
title: Ratan Indonesia Isolated Deployment
status: on-hold
owner: ""
start_date: 2026-08-24
target_date: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, deployment, data-residency, iam]
related: [ratan, indonesia-ratan-data-residency-isolation, ratan-api-gateway-auth-server-consolidation, microsoft-entra-id, fmces]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# Ratan Indonesia Isolated Deployment

## Purpose

Establish an Indonesia-scoped Ratan deployment consistent with the source's stated in-country customer and transaction-data requirement.

## Documented scope

- Isolated PostgreSQL, Redis, and session-management infrastructure.
- IAM migration dependency from ForgeRock/OneMFA to [[microsoft-entra-id]].
- Functional-entitlement migration from [[ems2]] to [[fmces]].
- Evaluation of [[ratan-api-gateway-auth-server-consolidation]].

## Status

This project is marked on hold because the only supplied architecture proposal is explicitly deprecated. Scope, ownership, regulatory interpretation, target topology, and approved successor design require confirmation.

## Key open matters

- Data-residency controls for backups, DR, observability, keys, and operational access.
- Authoritative login, JWT, and session ownership.
- Entra service-to-service authentication model.
- Approved entitlement mapping and access-routing behavior.