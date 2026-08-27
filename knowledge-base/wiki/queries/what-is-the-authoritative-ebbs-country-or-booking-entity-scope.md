---
type: query
title: What Is the Authoritative eBBS Country or Booking-Entity Scope?
tags: [ebbs, scope, country-codes, booking-entities, ratan]
related: [ebbs, ratan-ebbs-accounting-feed, what-is-the-canonical-ratan-to-ebbs-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Authoritative eBBS Country or Booking-Entity Scope?

The source calls its listed values “eBBS countries,” but the mapping combines country codes, country names, city names, and a possible business entity.

## Why this needs validation

Examples of ambiguity include:

- `AE` mapped to `DUBAI`
- `ID` mapped to `JAKARTA`
- `PH` mapped to `MANILA`
- `PHILIP FCU`, which may be an entity rather than a location
- inconsistent capitalization and naming conventions

The list should be validated against an authoritative eBBS deployment, booking-entity, or supported-jurisdiction inventory before it is used in interface configuration, operational reporting, or scope control.

## Resolution needed

Identify:

1. Whether the values represent countries, cities, branches, booking entities, or eBBS instances.
2. The canonical identifier and display name for each supported scope item.
3. Which entries are in scope for the RATAN accounting feed in each environment.
4. The owner and change process for this inventory.