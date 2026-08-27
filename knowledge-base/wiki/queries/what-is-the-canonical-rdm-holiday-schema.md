---
type: query
title: What Is the Canonical RDM Holiday Schema?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, schema, holiday-calendar, data-contract]
related: [holiday-calendar-event-model, ratan-static-rdm-holiday-weekend-message, ratan-static-cashflow-currency-holiday, rdm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# What Is the Canonical RDM Holiday Schema?

The available sample establishes field names and example values but not the authoritative contract for either incoming messages or RATAN persistence tables.

## Evidence needed

- RDM message schema and service-specific contracts.
- Table DDL for raw and structured persistence.
- Date parsing rules for `eventDate`, `createdTime`, and `modifiedTime`.
- Timezone policy and permitted values for `dayType`, `fileType`, and `entityState`.