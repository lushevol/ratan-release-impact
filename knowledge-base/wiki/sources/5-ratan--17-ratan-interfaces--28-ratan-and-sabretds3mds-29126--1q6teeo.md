---
type: source
title: "RATAN and SABRE (TDS3_MDS) Interface 29126"
authors: [Yunzhe Ta, Zhenzhen Liu, Junying Jiang, LiPing Gao]
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/TD-006%3A+Design+of+MDS+Payment+Holiday+Description+Data+Integration"
venue: Confluence
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, SABRE, TDS3, MDS, payment-holiday, interface, reference-data]
related: [mds, tds3, sabre, control-m, ratan-payment-holiday-description-enrichment, authoritative-ratan-tds3-mds-29126-interface-contract, ratan-interface-architecture, ratan-interface-inventory, ratan-service-governance]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE(TDS3_MDS)-29126.md"]
---
# RATAN and SABRE (TDS3_MDS) Interface 29126

## Summary

This document describes a RATAN integration that enriches Trade Detail data with the Payment Holiday description. TDS3 provides the Payment Holiday Source Name, but not the user-facing description. MDS is identified as the golden source for the description, and RATAN retrieves the relevant data from MDS and enriches the corresponding Trade Detail field.

The documented flow should be treated as a high-level design description rather than a complete production interface contract. Connection details, interface-team contact information, field-level schemas, error handling, and troubleshooting procedures are not provided.

## Document metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Zhenzhen Liu @Junying Jiang | 2026-01-22 | @Yunzhe Ta @LiPing Gao | 2026-03-26 | |

The source states that the status should be updated to Published after review, but the status field is blank.

## Data flow

1. TDS3 supplies the Payment Holiday Source Name.
2. RATAN periodically queries MDS through its API.
3. MDS provides the Payment Holiday description and related reference or calendar data.
4. RATAN enriches the corresponding field on the Trade Detail page.

The source names the following MDS datasets or tables:

```text
SD_TP_SYSTEM_MAP
SD_CALENDAR_MAIN
```

The document does not establish whether these are physical database tables exposed through an API, logical API resources, or table-shaped API responses.

## Synchronization details

| Synchronization Attribute | Value |
| --- | --- |
| Frequency | Once per working day |
| Execution Time | 05:00 AM GMT |
| Maximum Records per Request (`SD_TP_SYSTEM_MAP`) | 3,000 rows |
| Request Timeout | 60 seconds |

The synchronization job is scheduled and triggered by [[control-m]]. The source also states that the upstream MDS API owns cobdate validation and data-quality validation for cobdate.

## MDS Green Zone

| MDS api Green Zone | From | To |
| --- | --- | --- |
| SGT | Sat 12:00 PM | Sun 6:00 PM |
| GMT | Sat 4:00 AM | Sun 10:00 AM |

The document does not clarify whether this interval is an availability window, maintenance window, or preferred operating period.

## Referenced documentation

- [TD-006: Design of MDS Payment Holiday Description Data Integration - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/TD-006%3A+Design+of+MDS+Payment+Holiday+Description+Data+Integration)
- [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

The OLA section states: “BPMS OLA location, no change required.”

## Incomplete contract areas

The source contains no textual details for:

- MDS connection or endpoint configuration
- Authentication
- Interface-team contact
- Request and response schemas
- Field-level mapping or keys
- RATAN persistence or caching
- Cobdate filtering rules
- Retry and failure handling
- Partial synchronization behavior
- Duplicate or stale-record handling
- Alerting and escalation
- Troubleshooting procedures
- Known issues

The interface specification is represented by an embedded image and does not provide extractable schema details in the source text.

## Wiki implications

This source adds a reference-data enrichment flow to the broader [[ratan-interface-architecture]] and may belong in the [[ratan-interface-inventory]]. The filename places the integration in a SABRE, TDS3, and MDS context, but the described ownership boundary is more precise: TDS3 supplies the source name, MDS supplies the description, and RATAN performs the enrichment. The role of SABRE requires confirmation before it is treated as the owner of the flow.

See [[authoritative-ratan-tds3-mds-29126-interface-contract]] for unresolved contract questions.