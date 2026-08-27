---
type: query
title: "What Is the Authoritative RATAN-TDS3-MDS 29126 Interface Contract?"
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, TDS3, MDS, SABRE, interface-contract, open-question, payment-holiday]
related: [5-ratan--17-ratan-interfaces--28-ratan-and-sabretds3mds-29126--1q6teeo, mds, tds3, sabre, ratan-payment-holiday-description-enrichment, ratan-interface-inventory, ratan-service-governance]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE(TDS3_MDS)-29126.md"]
---
# What Is the Authoritative RATAN-TDS3-MDS 29126 Interface Contract?

## Question

What is the authoritative system scope and production interface contract for interface `29126`, described in the source as “RATAN and SABRE(TDS3_MDS)”?

## Current evidence

The documented data flow is:

- TDS3 provides the Payment Holiday Source Name.
- MDS provides the Payment Holiday description as the golden source.
- RATAN performs the Trade Detail enrichment.
- Control-M triggers a once-per-working-day synchronization at 05:00 AM GMT.

The source also names `SD_TP_SYSTEM_MAP` and `SD_CALENDAR_MAIN`, specifies a 3,000-row request limit for `SD_TP_SYSTEM_MAP`, and gives a 60-second timeout.

## Open contract questions

1. Is the canonical scope RATAN–TDS3–MDS, RATAN–SABRE, or all four systems?
2. What are the MDS API endpoints and authentication requirements?
3. What fields and keys map Payment Holiday Source Name to Payment Holiday description?
4. What are the schemas, filters, effective-date rules, and pagination behavior for `SD_TP_SYSTEM_MAP` and `SD_CALENDAR_MAIN`?
5. What is RATAN’s failure, retry, alerting, and stale-data policy when MDS is unavailable?
6. Does the 3,000-row limit apply only to `SD_TP_SYSTEM_MAP`?
7. What does the MDS API Green Zone represent?
8. Has the document been formally published, given that its status field is blank despite the stated “Published after reviewed” convention?
9. What interface-team contact and troubleshooting route should be used for incidents?

## Working assessment

The source is sufficient to document the intended enrichment pattern but is not sufficient to establish a complete production-ready interface contract. Claims about SABRE ownership should remain qualified until an authoritative design or inventory record confirms them.