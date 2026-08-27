---
type: query
title: When Do Maker/Checker Approvals Trigger RATAN Global Rule Synchronization?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, maker-checker, approval, rule-sync, governance]
related: [central-global-and-local-indonesia-rule-governance, ratan-global-rule-synchronization, ratan-gdc, ratan-indonesia]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# When Do Maker/Checker Approvals Trigger RATAN Global Rule Synchronization?

The source requires maker/checker control for Global-rule changes in GDC and local rule input in Indonesia, but does not connect approval states to synchronization emission.

The required rule is unclear for maker submission, checker approval, rule activation to `LIVE`, rejection, withdrawal, expiry, rollback, and subsequent disablement. This timing must be defined to prevent unapproved or superseded rule content from being replicated.