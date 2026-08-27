---
type: query
title: What Was the Final Authorized Deployment Manifest for the 2026-03-28 UBER Technical Release?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, uber, release-management, deployment, audit]
related: [uber-fxu-technical-live-and-business-go-live-2026, release-branch-synchronization-and-deployment-gating, technical-live-versus-business-live]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
---
# What Was the Final Authorized Deployment Manifest for the 2026-03-28 UBER Technical Release?

## Question

Which exact artifacts were authorized and deployed for the planned 2026-03-28 UBER technical release, and what evidence confirms their production validation?

## Why this is open

The source gives a target date and a component matrix, but it also contains pipeline activity after the target date. Several components are explicitly marked `DO NOT DEPLOY!!` despite passing pipelines. The source does not provide an approved change record, production timestamps, a signed deployment manifest, or post-deployment validation results.

## Evidence needed

- approved change record and final deployment manifest;
- exact service, frontend, database, and configuration versions;
- environment-specific deployment timestamps;
- list of excluded components and their rationale;
- rollback versions and rollback readiness;
- regression, performance, and PSS readiness sign-off;
- production validation results and the actual feature-activation state.

This query should distinguish planned, built, pipeline-passing, deployed, enabled, and business-live states.