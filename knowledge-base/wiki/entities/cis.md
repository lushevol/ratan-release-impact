---
type: entity
title: CIS
tags: [downstream-system, cashflow, pm-ccy, integration, CIS, RATAN, API, settlement]
related: [irs-cashflow-aggregation, what-are-the-tlm-lms-and-cis-impacts-of-irs-cashflow-aggregation, ratan, ebbs, hkcs-ratan-cis-api-integration, hau]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# CIS

## IRS Cashflow Aggregation

The Cashflow Aggregation source identifies CIS as a downstream system potentially affected by IRS cashflow aggregation for PM currency processing.

That source provides:

- No definition of PM currency.
- No CIS message contract.
- No confirmed impact.

The required assessment is tracked in [[what-are-the-tlm-lms-and-cis-impacts-of-irs-cashflow-aggregation]].

## HKCS HAU Settlement Flow

Separately, the HKCS initiative source describes CIS as the downstream consumer in the HKCS HAU settlement flow. According to that source, CIS will query relevant data from the RATAN API rather than receiving accounting data pushed by RATAN.

The HKCS initiative source does not define:

- The API endpoint or version.
- The payload and data objects.
- Whether the data represents settlement, cashflow, status, position, or another non-accounting object.
- Timing, error handling, reconciliation, or retry behavior.

These items require an explicit interface contract before implementation sign-off.