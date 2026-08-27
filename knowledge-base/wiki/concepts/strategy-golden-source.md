---
type: concept
title: Strategy Golden Source
created: 2026-08-22
updated: 2026-08-22
tags: [golden-source, strategy-data, static-data, settlement, governance]
related: [stella, fmrp, pct2, ssi-plus, booking-entity-counterparty-identifier, booking-currency-to-iso-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Strategy Golden Source

A strategy golden source is an authoritative system or repository for data used consistently across booking, settlement, and static-data processes.

The requirement invokes golden-source ownership for:

- Settlement methods and netting agreements
- Rounding rules
- Booking entity and counterparty identifiers
- Booking currencies and ISO currency mappings
- Product definitions
- Nostro static data

The source does not identify one universal golden source. It specifically notes that FMID mappings are in PCT2 and that SSI+ is the relevant Nostro static-data area. Ownership must therefore be defined by data domain rather than assumed to belong entirely to Blade or Stella.