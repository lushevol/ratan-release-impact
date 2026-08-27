---
type: query
title: Which LIEN Amount Is Authoritative During Resultant Generation?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lien, netting, resultant-generation, data-consistency]
related: [lien, lien-stamping-and-re-stamping, netting-service, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# Which LIEN Amount Is Authoritative During Resultant Generation?

## Question

During resultant generation, should the authoritative LIEN value come from component 2, each component's latest trade data, cashflow SCBML, or another source?

## Evidence

The source requires `ratan-cash-settlement-netting-service` to query LIEN amounts for each component before generating the resultant and to select the LIEN amount field from component 2.

## Required resolution

The implementation contract should clarify:

- Why component 2 is authoritative for the resultant.
- Whether all component queries are mandatory when only component 2 supplies the resultant value.
- How conflicting component values are handled.
- What happens when a component query fails or returns no LIEN amount.
- Whether the resultant stores a snapshot or maintains a reference to source data.