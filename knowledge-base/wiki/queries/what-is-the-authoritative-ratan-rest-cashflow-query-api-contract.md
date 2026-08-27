---
type: query
title: What Is the Authoritative RATAN REST Cashflow Query API Contract?
tags: [ratan, rest-api, cashflow, api-contract, open-question]
related: [ratan, ratan-rest-cashflow-query-integration, consumer-initiated-cashflow-query, fmmis-51406, cis-31946, ssdr-51507, marketudp, pacman-51406, cnedmp-50584, ratan-interface-inventory, authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMMIS-51406  CIS-31946  SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584.md"]
---
# What Is the Authoritative RATAN REST Cashflow Query API Contract?

## Question

What are the authoritative REST API contracts used by FMMIS, CIS, PacMan, MarketUDP(SSDR), and CNEDMp to query cashflow data from [[ratan]]?

## Known Evidence

The source confirms five high-level consumer-to-RATAN REST query relationships. It does not identify whether the consumers use one API or multiple APIs.

## Information Needed

- Endpoint paths and API versions
- Request and response schemas
- Cashflow filters, states, and supported business scope
- Pagination, sorting, and volume limits
- Authentication and authorization requirements
- Data-entitlement rules and user or service identities
- Error, retry, timeout, and rate-limit behavior
- Data freshness and consistency guarantees
- Interface owners and support contacts
- Environment-specific connectivity and certificate requirements
- Applicable OLA commitments

Until these details are located, the source record remains an inventory entry rather than the authoritative interface specification.