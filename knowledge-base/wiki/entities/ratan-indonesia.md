---
type: entity
title: RATAN Indonesia
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, rule-governance, consumer]
related: [ratan-gdc, ratanone-rule-service, ratan-global-rule-synchronization, central-global-and-local-indonesia-rule-governance, indonesia-ratan-data-residency-isolation, ratan-indonesia-onshoring-2026, ratan-indonesia-isolated-deployment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# RATAN Indonesia

RATAN Indonesia, also called RATAN ID, is the proposed consumer of replicated Global rules from [[ratan-gdc]].

The source distinguishes two rule populations:

- Replicated Global rules are centrally governed in GDC and read-only in Indonesia.
- Indonesia-specific rules are entered locally and contain Indonesia's `Entity__Booking_Entity_SCI_FMID` and `Entity__Booking_Entity_SCI_FMCODE` attributes by default; these fields are locked against editing.

Direct local static-data and rule input is required to use maker/checker control. The source does not define the Indonesia-side behavior for a source-rule deletion, revocation, or amendment. See [[what-are-the-authoritative-global-rule-deletion-and-revocation-semantics-in-ratan-id]].