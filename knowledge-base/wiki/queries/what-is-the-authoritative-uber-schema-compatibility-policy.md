---
type: query
title: What Is the Authoritative Uber Schema Compatibility Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, schema-evolution, protobuf, json, tdsx]
related: [uber, tdsx, schema-evolution-for-cash-settlement, uber-restructured-workflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# What Is the Authoritative Uber Schema Compatibility Policy?

The source distinguishes two serialization paths:

- TDSX → Ratan: Proto Buffer → JSON.
- Ratan → Ratan: JSON → Proto Object → JSON.

It states that downstream upgrades are required when required fields change, but also describes potentially silent information loss, a default integer value of `0`, retention of only the last array element, and an array-size exception. These claims require executable compatibility tests and an approved policy.

## Policy decisions needed

- Define required-field ownership and enforcement.
- Define permitted type and cardinality changes.
- Reject or quarantine lossy conversions rather than silently accepting them where business-critical fields are affected.
- State compatibility requirements separately for TDSX ingress and Ratan internal traffic.
- Define mandatory upgrade rules for Group Management Service, lifecycle service, and dependent consumers.

See [[schema-evolution-for-cash-settlement]] for broader schema-evolution context.