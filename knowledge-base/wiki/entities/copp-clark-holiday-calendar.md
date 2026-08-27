---
type: entity
title: Copp Clark Holiday Calendar
created: 2026-08-25
updated: 2026-08-25
tags: [copp-clark, holiday-calendar, reference-data, currencies, rdm, solace]
related: [rdm, ratan-rdm-reference-data-integration, solace, fileit]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# Copp Clark Holiday Calendar

## Role

The **Copp Clark Holiday Calendar** is listed as a global reference-data source received by RATANONE - 51358 from RDM. The inventory separates the data into two feeds:

1. Currency holiday and weekend data.
2. Special-holiday data.

## Stated delivery

- Currency holiday and weekend data: `Enterprise solace notification/FileIt`.
- Special-holiday data: `Enterprise solace`.

The source does not clarify whether Enterprise Solace carries the complete payload, a notification that triggers FileIT retrieval, or alternative delivery paths.

## Scope and unresolved details

Both feeds are labelled `Global`, but the document does not provide the included currencies, countries, calendars, effective-date rules, update schedule, schema, or ownership model. It also does not establish whether Copp Clark is an external provider, an RDM-maintained dataset, or a named reference-data product.