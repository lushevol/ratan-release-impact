---
type: concept
title: Indonesia Ratan Data Residency Isolation
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, data-residency, isolation, redis, postgresql]
related: [ratan, ratan-indonesia-isolated-deployment, murex-ratan-cashflow-ringfencing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# Indonesia Ratan Data Residency Isolation

The source treats Indonesia as a country-isolated Ratan deployment requiring separate in-country PostgreSQL, Redis, and session-management instances.

This is a data-residency control, distinct from [[murex-ratan-cashflow-ringfencing]]. The proposal does not define data classification, backup and DR location, cross-border replication, logs and telemetry, encryption-key custody, or privileged support access.