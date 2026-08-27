---
type: concept
title: RATAN-RDM Reference-Data Integration
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, rdm, reference-data, integration, fileit, solace, api]
related: [rdm, ratan, fileit, solace, konggateway, rat-pct2-refresh, ratan-interface-inventory]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# RATAN-RDM Reference-Data Integration

## Definition

The **RATAN-RDM reference-data integration** is the high-level interface through which RDM supplies global reference, configuration, staff, calendar, and portfolio data to RATANONE - 51358.

The source describes a multi-channel integration rather than a single file-transfer route.

## Feed and transport inventory

| Data feed | Scope | Stated transport |
| --- | --- | --- |
| Copp Clark Holiday Calendar - Currencies Holiday & Weekend | Global | Enterprise Solace notification/FileIT |
| Copp Clark Holiday Calendar - Special Holiday | Global | Enterprise Solace |
| Country-S3 | Global | FileIT |
| Murex Structures And Strategies | Global | FileIT |
| Rules Engine Configuration Table | Global | FileIT |
| 15a6 Registered Staff | Global | FileIT |
| PCT2 portfolio data by job `RAT_PCT2_REFRESH` | Global | API via KongGateway |

## Integration patterns

### File-based integration

FileIT is the stated route for Country-S3, Murex Structures And Strategies, Rules Engine Configuration Table, and 15a6 Registered Staff. It is also listed for the currency holiday and weekend feed, although its relationship to the Enterprise Solace notification is unclear.

### Event-driven messaging or notification

Enterprise Solace is listed for both Copp Clark Holiday Calendar feeds. The source does not identify topics, message formats, event triggers, whether messages contain full payloads, or whether Solace only signals the availability of files.

### API-based scheduled refresh

PCT2 portfolio data is associated with `RAT_PCT2_REFRESH` and an API accessed through KongGateway. No endpoint, schedule, authentication method, schema, or failure policy is provided.

## End-to-end flow caveat

The source gives the simplified flow:

```text
RDM->FileIT->RATAN
```

This should not be applied to all seven feeds. It omits the Enterprise Solace and KongGateway paths, and it also leaves unresolved whether the receiving application is RATAN or RATANONE - 51358. See [[queries/are-ratan-ratanone-51358-and-ratan-38430-the-same-interface-scope]].

## Scope and authority

All feeds are labelled `Global`, but the geographical and legal-entity boundaries are not defined. The source is useful as an interface inventory, but it lacks the details required for an authoritative contract. Its review metadata is populated while its publication status is blank.