---
type: concept
title: RATAN REST Cashflow Query Integration
tags: [ratan, rest-api, cashflow, integration, interface-inventory]
related: [ratan, fmmis-51406, cis-31946, ssdr-51507, marketudp, pacman-51406, cnedmp-50584, consumer-initiated-cashflow-query, ratan-interface-inventory, what-is-the-authoritative-ratan-rest-cashflow-query-api-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMMIS-51406  CIS-31946  SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584.md"]
---
# RATAN REST Cashflow Query Integration

This concept describes the high-level integration pattern in which downstream or peer applications query cashflow data from [[ratan]] through REST APIs.

## Documented Consumers

The source records five query paths:

- FMMIS to RATAN
- CIS to RATAN
- PacMan to RATAN
- MarketUDP(SSDR) to RATAN
- CNEDMp to RATAN

The source does not establish that these consumers share a common endpoint, schema, authorization scope, or service-level agreement.

## Evidence Boundary

This is an interface-inventory-level concept. It confirms protocol family, direction, and broad data domain only. It does not establish RATAN's authority over the underlying cashflow lifecycle, data freshness, query semantics, or operational ownership.

The missing contract details are tracked in [[what-is-the-authoritative-ratan-rest-cashflow-query-api-contract]].