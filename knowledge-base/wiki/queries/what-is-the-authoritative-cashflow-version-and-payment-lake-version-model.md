---
type: query
title: What Is the Authoritative Cashflow Version and Payment Lake Version Model?
tags: [cashflow, versioning, payment-lake, event-processing]
related: [cashflow-event-versioning, cashflow-partial-update, cash-settlement-platform, stella]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/SFMRP - Cash Settlement Platform Integration（Deprecated）.md"]
---
# What Is the Authoritative Cashflow Version and Payment Lake Version Model?

The deprecated source presents three version values: Business Version, Cashflow Version, and Payment Lake Version. Its examples suggest that Stella increments Business Version for business amendments, while the platform increments Cashflow Version and Payment Lake Version for lifecycle updates.

The source does not define ownership, increment rules, event correlation keys, idempotency behavior, ordering guarantees, or reconciliation rules. Define the authoritative model before relying on version values for event processing or user-visible history.
---