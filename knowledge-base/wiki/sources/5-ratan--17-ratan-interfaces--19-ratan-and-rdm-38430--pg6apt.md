---
type: source
title: Ratan and RDM 38430
authors: [Junying Jiang, Yunzhe Ta, Daiqi Wang]
year: 2026
url: "https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA"
venue: Confluence
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, rdm, interface, reference-data, fileit, solace, konggateway]
related: [rdm, ratan-rdm-reference-data-integration, fileit, solace, konggateway, rat-pct2-refresh, ratan-interface-inventory, relationship-between-ratan-and-ratanone]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---

# Ratan and RDM 38430

## Summary

This document is a high-level inventory of data received or extracted by **RATANONE - 51358** from **RDM**. It identifies seven global data feeds and three stated delivery patterns: FileIT transfer, Enterprise Solace messaging or notification, and an API accessed through KongGateway.

The document does not provide a complete technical or operational interface contract. Connection details, interface specifications, team contacts, known issues, and troubleshooting procedures are blank or remain as placeholders.

## Review and publication metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Junying Jiang @Yunzhe Ta | 2026-01-21 | @Yunzhe Ta @Daiqi Wang | 2026-01-21 | |

The page states that reviewed articles should have their status updated to `Published`, but the status field is blank. Its authority and publication state therefore remain uncertain.

## Interface inventory

| **Data Feed** | **Countries in scope** | **Delivery mechanism** |
| --- | --- | --- |
| Copp Clark Holiday Calendar - Currencies Holiday & Weekend | Global | Enterprise solace notification/FileIt |
| Copp Clark Holiday Calendar - Special Holiday | Global | Enterprise solace |
| Country-S3 | Global | FileIt |
| Murex Structures And Strategies | Global | FileIt |
| Rules Engine Configuration Table | Global | FileIt |
| 15a6 Registered Staff | Global | FileIt |
| PCT2 portfolio data by job **`RAT_PCT2_REFRESH`** | Global | API via KongGateway |

All seven feeds are labelled `Global`, but the document does not define a country roster, legal-entity scope, regional exclusions, or data-residency constraints.

## Stated end-to-end flow

The source records the following flow:

```text
RDM->FileIT->RATAN
```

This flow is not sufficient as a universal architecture for the inventory because the table also identifies Enterprise Solace and KongGateway API delivery. Separate flow descriptions are required for the messaging and API paths.

## Referenced systems and channels

- **RDM** is presented as the upstream source.
- **RATANONE - 51358** is described as the receiving or extracting application.
- **FileIT** is listed for at least five feeds.
- **Enterprise Solace** is listed for the two Copp Clark Holiday Calendar feeds, although the phrase `notification/FileIt` is ambiguous.
- **KongGateway** is listed for the scheduled `RAT_PCT2_REFRESH` portfolio-data refresh.

The relationship between **RATAN**, **RATANONE - 51358**, and interface identifier `38430` is not resolved. See [[queries/are-ratan-ratanone-51358-and-ratan-38430-the-same-interface-scope]].

## Operational governance

The OLA section states:

> BPMS OLA location, no change required

It links to [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA). The source does not establish whether that OLA covers RDM, FileIT, Enterprise Solace, KongGateway, data quality, recovery, or end-to-end incident ownership. This question is tracked in [[queries/does-the-ratan-fm-settlement-ola-cover-rdm-fileit-solace-and-konggateway]].

## Missing contract information

The document does not specify:

- File names, locations, formats, schemas, encryption, acknowledgements, retention, or replay procedures.
- Solace topics, payload ownership, notification semantics, delivery guarantees, or retry behaviour.
- The `RAT_PCT2_REFRESH` schedule, endpoint, authentication, response schema, retry policy, or failure handling.
- Feed owners, technical contacts, support hours, escalation paths, monitoring, or data-quality controls.
- The consuming RATAN component for each feed, particularly the Rules Engine Configuration Table.
- Confirmed publication status or authoritative-document designation.

Accordingly, this page should be treated as high-level source evidence rather than an authoritative technical interface specification. The open contract questions are collected in [[queries/what-is-the-authoritative-ratan-rdm-38430-interface-contract]] and [[queries/what-are-the-rdm-feed-schedules-schemas-and-failure-handling]].

## Related documentation

The source references the RATAN OLA and is relevant to [[concepts/ratan-interface-inventory]]. It also provides additional evidence for the unresolved relationship between [[entities/ratan]] and RATANONE, and extends the known uses of [[entities/fileit]] and [[entities/solace]].