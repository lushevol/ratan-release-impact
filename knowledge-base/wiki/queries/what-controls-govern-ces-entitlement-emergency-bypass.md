---
type: query
title: What Controls Govern CES Entitlement Emergency Bypass?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, emergency-access, security, audit, authorization]
related: [ces, auth-service, query-service, cash-settlement-data-entitlement, adopt-two-layer-ces-emergency-disablement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
---
# What Controls Govern CES Entitlement Emergency Bypass?

The documented two-layer configuration can disable CES entitlement enforcement globally or for named users. In this state, users revert to behavior without CES data filtering. This is an emergency privileged-access mechanism.

## Questions

- Which roles may enable global or per-user bypass, and who approves activation?
- Are changes maker-checker controlled, audited, and correlated with an incident record?
- What maximum duration, expiry, renewal, and rollback process applies?
- How are affected users, data access, and configuration state monitored?
- Is the cache-reset endpoint separately protected against unauthorized wildcard invalidation?
- How are secrets for the documented `ratanone-rundeck` Basic-authentication path stored, rotated, and audited?