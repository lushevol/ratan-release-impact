---
type: concept
title: Application Documentation Set
tags: [application-documentation, documentation-governance, service-management, ratan]
related: [ratan, ratan-service-governance, ratan-user-guide-segmentation, ratan-operational-resilience-plans, ratan-test-environment-specification]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -App Docs/RATAN -App Docs.md"]
---
# Application Documentation Set

An application documentation set is a coordinated collection of documents covering the technical, functional, service-management, operational, resilience, capacity, and testing aspects of a production application.

The RATAN register demonstrates this pattern through the linked [[ratan-service-governance]] artifacts, user guides, recovery and restoration plans, capacity-management documentation, and test-environment specification.

## RATAN coverage

The documented categories are:

1. Architecture or service-management reference material (`ASRM`)
2. User guidance
3. Service-level agreement
4. Operational-level agreement
5. Disaster-recovery plan
6. Service-restore plan
7. Capacity-management plan
8. Test-environment specification

## Significance

A register of this kind provides a navigation and governance baseline. It indicates which classes of documentation are expected to exist, but does not by itself verify that the linked documents are current, complete, approved, or operationally effective.

For RATAN, the set also separates user-facing guidance by [[ratan-user-guide-segmentation]] and distinguishes resilience planning from ordinary service restoration through [[ratan-operational-resilience-plans]].