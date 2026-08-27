---
type: query
title: Does Manual-Entity Onboarding Require NDS Auto Netting Configuration?
created: 2026-08-22
updated: 2026-08-22
tags: [nds, auto-netting, manual-entities, configuration]
related: [nds-auto-netting, pending-nds-netting, nds-duplicate-payment-prevention, manual-entity-settlement-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/00 Manual Entities Onboarding Checklist.md"]
---
# Does Manual-Entity Onboarding Require NDS Auto Netting Configuration?

The displayed Pending NDS Netting condition has product-typology, parent-typology, event-reason, netting-ID, and duplicate-payment predicates but no entity predicate. The checklist therefore asks whether entity setup is unnecessary.

This is unresolved. The absence of an entity condition in the displayed rule does not establish that upstream, downstream, static-data, or workflow controls are entity-agnostic.

Required evidence includes the authoritative rule set, rule execution order, and confirmation of any entity-scoped NDS configuration.