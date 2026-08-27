---
type: concept
title: Consumer-Initiated Cashflow Query
tags: [cashflow, query-integration, rest-api, ratan, data-access]
related: [ratan, ratan-rest-cashflow-query-integration, ratan-interface-inventory, what-is-the-authoritative-ratan-rest-cashflow-query-api-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMMIS-51406  CIS-31946  SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584.md"]
---
# Consumer-Initiated Cashflow Query

A consumer-initiated cashflow query is a pull-based integration pattern in which an application requests cashflow data from a provider instead of receiving data through a provider-published feed.

In this source, FMMIS, CIS, PacMan, MarketUDP(SSDR), and CNEDMp initiate REST API calls toward [[ratan]]. The pattern identifies the direction of access, but it does not by itself establish data ownership, authority, freshness, entitlements, or response guarantees.

The source should therefore be used as evidence of connectivity intent and interface direction, not as evidence of a complete data lifecycle or API contract.