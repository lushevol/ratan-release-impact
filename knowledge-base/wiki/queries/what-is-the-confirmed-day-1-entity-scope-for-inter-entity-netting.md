---
type: query
title: What Is the Confirmed Day 1 Entity Scope for Inter-Entity Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, settlement-day-2, entity-scope, open-question]
related: [inter-entity-netting, netting-eligibility-rules, settlement-day-2, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting - UAT.md"]
---

# What Is the Confirmed Day 1 Entity Scope for Inter-Entity Netting?

The source explicitly records the Day 1 entity scope as **to be confirmed**. One UAT case used a cashflow booked for SCB NY as an out-of-scope example, but that test does not establish the complete production scope.

Confirmation is needed for:

- The full Day 1 entity list.
- The owner of the scope configuration.
- Whether entity scope is evaluated before or after other netting conditions.
- The process for adding, removing, or temporarily excluding an entity.
- The rollback behavior for pending cashflows when an entity is removed from scope.

Until confirmed, the tested entity examples should not be generalized into the authoritative Day 1 policy.
