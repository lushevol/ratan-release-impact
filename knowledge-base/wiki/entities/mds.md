---
type: entity
title: MDS
created: 2026-08-23
updated: 2026-08-25
tags: [MDS, market-data, conversion-rate, HAU, reference-data, payment-holiday, API, golden-source]
related: [hau, hau-gold-settlement-configuration, tds3, sabre, control-m, ratan-payment-holiday-description-enrichment, authoritative-ratan-tds3-mds-29126-interface-contract, ratan-interface-architecture]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md", "RATAN/RATAN -Interfaces/Ratan and SABRE(TDS3_MDS)-29126.md"]
---
# MDS

## Role in the HKCS Requirement

MDS is identified in the upstream and downstream impact assessment as the system whose conversion-rate handling may require review for HAU.

No MDS impact-assessment result or configuration change is included in the HKCS requirement source.

## Role in the RATAN Integration

In the RATAN integration, MDS is identified as the golden source for the Payment Holiday description displayed on the RATAN Trade Detail page. RATAN retrieves this data from the MDS API because [[tds3]] provides only the Payment Holiday Source Name.

The source describes MDS as providing access to:

- `SD_TP_SYSTEM_MAP`
- `SD_CALENDAR_MAIN`

The exact API resource model is not specified.

MDS’s role in this integration is distinct from [[tds3]]:

- TDS3 supplies the Payment Holiday Source Name.
- MDS supplies the corresponding Payment Holiday description.

## Data-Quality Ownership

The upstream MDS API is assigned responsibility for data quality and validation of the cobdate. The source does not define RATAN’s behavior when cobdate validation fails, is missing, or conflicts with RATAN expectations.

## Operating Window

The documented MDS API Green Zone is:

| Time zone | From | To |
| --- | --- | --- |
| SGT | Sat 12:00 PM | Sun 6:00 PM |
| GMT | Sat 4:00 AM | Sun 10:00 AM |

The meaning of “Green Zone” is not defined. It should not yet be interpreted definitively as either an availability period or a maintenance period.

## Integration Constraints

The documented RATAN synchronization has a 60-second request timeout. Requests to `SD_TP_SYSTEM_MAP` are limited to 3,000 rows per request.

The source does not provide an endpoint, authentication mechanism, response schema, pagination protocol, retry policy, or service-level contact.