---
type: entity
title: RATAN GDC
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, gdc, rule-governance, producer]
related: [ratan-indonesia, ratanone-rule-service, ratan-global-rule-synchronization, central-global-and-local-indonesia-rule-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# RATAN GDC

RATAN GDC is the proposed producer and governing location for Global rules replicated to [[ratan-indonesia]]. Under Proposal A, Global-rule replication is unidirectional from GDC to Indonesia through FM Solace.

Global rules are identified automatically from their expressions and must not contain Indonesia-specific `Entity__Booking_Entity_SCI_FMID` or `Entity__Booking_Entity_SCI_FMCODE` attributes. The source requires maker/checker control for Global-rule creation, amendment, and deletion in GDC.

The source does not establish that Proposal A is approved or implemented. See [[what-is-the-approved-ratan-gdc-to-indonesia-global-rule-sync-design]].