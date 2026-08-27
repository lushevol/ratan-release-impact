---
type: source
title: RATAN Interfaces
authors: []
year: 2026
url: ""
venue: ""
tags: [ratan, interfaces, integration, go-live, fileit, api]
related: [ratan, ratan-interface-inventory, fmmis-41190, filenet-28852, ratanone-message-bridge, operational-level-agreement, what-is-the-authoritative-ratan-interface-and-go-live-inventory]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN -Interfaces.md"]
---
# RATAN Interfaces

## Summary

This document records two inbound interfaces associated with the **pending go-live flow** for RATAN:

- **FMMIS - 41190** sends exception data to **Ratan - 51358** through **FileIT**.
- **FileNet - 28852** sends term sheet data to **Ratan - 51358** through an **API**.

Both interfaces are classified as **online** in the source. The document does not establish whether either interface is implemented, tested, approved, or operational in production.

## Referenced Configuration and Operational Sources

- Common configuration file: `/apps/ratanrt/services/ratan-service-properties/config-repo/application-prod.yml`
- Message bridge resources repository: [51358-ratanone-message-bridge resources](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-message-bridge?path=/src/main/resources&_a=contents&version=GBmain)
- OLA portal: [RATAN-OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN-OLA)

The source does not identify the specific configuration properties, routes, credentials, mappings, schemas, retry settings, or monitoring controls held in these locations.

## Verbatim Interface Inventory

```markdown
Pending go-live flow:

| Sender Business Application | Recevier Business Application | Interface Mechanism | online or batch | Data Entiy exchanged |
| --- | --- | --- | --- | --- |
| FMMIS - 41190 | Ratan - 51358 | FileIT | online | exception data |
| FileNet - 28852 | Ratan - 51358 | API | online | term sheet data |
```

The column-label spellings **“Recevier”** and **“Data Entiy”** are preserved from the source.

## Interpretation and Boundaries

The inventory provides an interface-level view of sender, receiver, mechanism, processing classification, and exchanged data. It does not provide:

- file or API schemas;
- endpoint, authentication, or response details;
- ownership or support assignments;
- availability or processing-time commitments;
- retry, reconciliation, or error-handling behavior; or
- evidence of go-live approval or production operation.

The presence of a production configuration path does not by itself prove that the listed interfaces are live. Likewise, the use of `51358-ratanone-message-bridge` does not establish the canonical relationship between RATAN and RatanOne.

## Related Wiki Context

The FileIT flow should be considered alongside [[fileit-file-arrival-notification]] and [[fileit-return-code-taxonomy]], without assuming that FileIT is identical to [[cft]]. The referenced OLA relates to [[operational-level-agreement]] and the existing RATAN OLA inventory. The receiver naming should be investigated with [[what-is-the-relationship-between-ratan-and-ratanone]].

## Evidence Gaps

The authoritative status of these interfaces, the precise meaning of **online**, and the operational contracts for both flows require confirmation. See [[what-is-the-authoritative-ratan-interface-and-go-live-inventory]].