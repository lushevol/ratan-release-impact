---
type: query
title: What Is the Relationship Between SSDR, DQSL, and MarketUDP?
tags: [ssdr, dqsl, marketudp, ratan, interface-identity, open-question]
related: [ssdr-51507, marketudp, ratan, ratan-rest-cashflow-query-integration, dqsl]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMMIS-51406  CIS-31946  SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584.md"]
---
# What Is the Relationship Between SSDR, DQSL, and MarketUDP?

## Question

What are the canonical identities and runtime relationships among `SSDR-51507`, `DQSL`, and `MarketUDP(SSDR)` in the documented REST cashflow-query flow to [[ratan]]?

## Evidence

The source title contains `SSDR-51507 (DQSL)`, while the E2E flow identifies the caller as `MarketUDP(SSDR)`. It does not explain whether:

- `SSDR-51507` is an application, interface, change, or documentation identifier;
- `DQSL` owns, routes, hosts, or supports the integration;
- `MarketUDP` is the application represented by SSDR;
- DQSL participates in the runtime request path; or
- the parenthetical labels describe organizational or technical relationships.

A canonical interface specification, application inventory, or ownership record is needed before these names are merged.