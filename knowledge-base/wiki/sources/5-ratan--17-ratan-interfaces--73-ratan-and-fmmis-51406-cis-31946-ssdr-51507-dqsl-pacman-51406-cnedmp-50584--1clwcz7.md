---
type: source
title: Ratan and FMMIS-51406, CIS-31946, SSDR-51507, PacMan-51406, and CNEDMp-50584
authors: [Yunzhe Ta, Zhenzhen Liu, Junying Jiang, Terris Li]
year: 2026
url: "https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA"
venue: Confluence
tags: [ratan, interfaces, rest-api, cashflow, interface-inventory, documentation-governance]
related: [ratan, fmmis-51406, cis-31946, ssdr-51507, marketudp, pacman-51406, cnedmp-50584, ratan-rest-cashflow-query-integration, consumer-initiated-cashflow-query, ratan-interface-inventory, operational-level-agreement, what-is-the-authoritative-ratan-rest-cashflow-query-api-contract, what-is-the-relationship-between-ssdr-dqsl-and-marketudp]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMMIS-51406  CIS-31946  SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584.md"]
---
# Ratan and FMMIS-51406, CIS-31946, SSDR-51507, PacMan-51406, and CNEDMp-50584

## Summary

This high-level interface inventory records five applications or application identifiers that query cashflow data from RATAN through REST APIs. The documented direction is consumer-initiated: FMMIS, CIS, PacMan, MarketUDP(SSDR), and CNEDMp call RATAN rather than RATAN publishing data to them.

The source does not provide an authoritative API contract. It contains no endpoint definitions, request or response schemas, authentication or authorization model, connectivity details, service ownership, interface-specific support terms, known issues, or troubleshooting procedures.

## E2E Data Flow

The source states:

```text
Sub application would trigger Rest API call to query cashflow data from Ratan

1. FMMIS–(REST API)-->RATAN
2. CIS–(REST API)-->RATAN
3. PacMan–(REST API)→RATAN
4. MarketUDP(SSDR)–(REST API)→RATAN
5. CNEDMp–(REST API)-->RATAN
```

These relationships establish only the high-level transport and direction. They do not establish that all five consumers use the same endpoint, schema, authorization scope, or operational configuration.

## Document Metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Zhenzhen Liu @Junying Jiang @Terris Li | 2026-02-04 | @Yunzhe Ta @Daiqi Wang | 2026-02-04 | |

The source guidance states that the status should be updated to `Published` after review, but the recorded Status cell is blank. Publication cannot therefore be confirmed.

## OLA Reference

The source states:

> BPMS OLA location, no change required

It links to [RATAN - OLA - FM Settlement - IS](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA). The source does not reproduce OLA commitments or demonstrate that the terms apply specifically to any of the five client integrations.

## Missing Interface Information

The following sections are empty or contain only documentation macros:

- Connection details
- Interface Specification
- Interface team contact
- Other Useful Docs
- Known Issues
- Troubleshooting Steps

Consequently, this record should be treated as an interface inventory entry, not as the authoritative contract for the integrations.

## Identity and Scope Cautions

The source uses shortened application names in the flow and numbered identifiers in the title. It does not explicitly define the relationships between `FMMIS` and `FMMIS-51406`, `CIS` and `CIS-31946`, `MarketUDP(SSDR)` and `SSDR-51507 (DQSL)`, or `PacMan` and `PacMan-51406`.

`DQSL` appears in the title but is not assigned a runtime role in the body. This source therefore does not establish that DQSL routes, owns, transforms, or otherwise intermediates the SSDR or MarketUDP request path.

## Evidence Boundaries

The source supports the following conclusions:

- RATAN is documented as a REST API provider for cashflow-data queries.
- Five named consumers or application identifiers are shown as calling RATAN.
- The interface direction is from each consumer toward RATAN.
- The documentation was reviewed on 2026-02-04 by named reviewers.
- The publication status remains undocumented in the source.

It does not support conclusions about data authority, data freshness, queryable cashflow scope, entitlements, API semantics, availability, or ownership.

## Related Pages

- [[ratan]]
- [[ratan-rest-cashflow-query-integration]]
- [[ratan-interface-inventory]]
- [[what-is-the-authoritative-ratan-rest-cashflow-query-api-contract]]
- [[what-is-the-relationship-between-ssdr-dqsl-and-marketudp]]