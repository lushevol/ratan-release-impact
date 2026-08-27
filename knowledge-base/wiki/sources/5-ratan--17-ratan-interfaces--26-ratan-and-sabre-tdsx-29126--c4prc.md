---
type: source
title: RATAN and SABRE (TDSX)-29126
authors: [Yunzhe-Ta, Zhenzhen-Liu]
year: 2026
url: ""
venue: Internal Confluence documentation
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tdsx, sabre, interface, trade-data, solace]
related: [tdsx, ratan-tdsx-integration, what-is-the-authoritative-ratan-tdsx-interface-contract, sabre, tds3, solace, ratan-trade-control, trade-validation]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDSX)-29126.md"]
---
# RATAN and SABRE (TDSX)-29126

This source is a high-level overview of the RATAN integration with TDSX, titled “SABRE (TDSX)” but primarily describing RATAN and TDSX. It documents intended interaction patterns but does not provide a complete technical or operational interface contract.

## Document review metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Zhenzhen Liu | 2026-02-04 | @Yunzhe Ta @Pengpeng Li | 2026-02-04 | |

The document states that the status should be updated to Published after review, but its Status field is blank.

## Documented architecture

[[tdsx|TDSX]] is described as Trade Data Store X: a unified API layer above TDS2 and [[tds3|TDS3]]. It is part of the Trade Store Convergence Program and is intended to hide the two physical stores from consumers.

The documented RATAN interaction patterns are:

- The RATAN trade-control flow retrieves a Payment Schedule from TDSX for display on the Trade Blotter.
- RATAN calls a TDSX REST API for trade validation.
- TDSX publishes Uber messages, delivered to RATAN through [[solace|Solace]].

These patterns are captured in [[ratan-tdsx-integration]]. The document does not establish that every RATAN validation or every Uber message uses TDSX and Solace respectively.

## Interface team contacts

| service | Contact Name | Email Address | Phone Number |
| --- | --- | --- | --- |
| RATAN (RATAN ONE) | RATAN ONE PSS | FM_BPMS.SUPPORT@sc.com | +862259806892 |
| SABRE TDSX | SABRE_TDSX_BA PSS, SABRE PSS | Source markup is malformed; verification required |  |

The source rendering suggests `SABRE_TDSX_BA@exchange.standardchartered.com` and `ABRE.PSS@sc.com`; neither should be treated as authoritative without verification because the markup is malformed and the latter appears to be missing an initial `S`.

## Operational reference

The source references the BPMS OLA without reproducing its terms:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

## Limitations

Sections intended for E2E data flow, connection details, interface specification, known issues, and troubleshooting are unpopulated. The source therefore does not specify REST endpoints, schemas, authentication, TDS2/TDS3 routing, Solace destinations, message contracts, delivery semantics, failure handling, reconciliation, or service-level targets.

See [[what-is-the-authoritative-ratan-tdsx-interface-contract]] for the missing authoritative contract details.