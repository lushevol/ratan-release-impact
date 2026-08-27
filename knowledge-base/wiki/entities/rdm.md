---
type: entity
title: RDM
created: 2026-08-22
updated: 2026-08-25
tags: [reference-data, holidays, cash-settlement, business-calendar, currency-rounding, data-governance, RDM, holiday-calendar, HAU, currency-calendar, static-data, country-code, api, fileit, ratan, indonesia, country-data, dataset, upstream-system]
related: ["ratan", "cashflow-multi-exception-generation", "nstp-exception-handling", "bad-business-day", "mx211-cash-settlement-decommission", "hau", "hau-gold-settlement-configuration", "cashflow-cutoff-static-data", "cash-settlement-home-page", "51358-ratanone-static-data-service", "rdm-api-based-holiday-compensation", "rdm-api-pagination-and-reconciliation", "kong", "indonesia-environment-readiness-dependencies", "rdm-reference-data-integration-via-kong", "what-is-the-production-readiness-plan-for-ratan-rdm-kong-integration", "how-should-ratan-handle-rdm-amber-data-quality-and-pagination", "static-data-service", "country-reference-data-reload", "what-is-the-canonical-country-dataset-schema-and-rdm-transformation", "rdm-holiday-and-weekend-ingestion", "ordinary-versus-special-holiday-feeds", "holiday-calendar-event-model", "ratanone", "fileit", "ratan-rdm-reference-data-integration", "solace", "konggateway"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Settlement Touchpoints.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation/RDM Integration via Kong Gateway.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md", "RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---

# RDM

## Role and scope

RDM is referenced across Cash Settlement requirements and designs as a provider or upstream location for reference data, including currency-calendar, holiday, country-code, and country-dataset data. The Indonesia technical-design sources additionally consider RDM for special-holiday and bank-code data.

The *Ratan holiday data process from RDM introduction* version identifies RDM as the upstream source of currency-holiday, special-holiday, and weekend data used by [[ratanone]] cash-settlement processing. This source documents message-level holiday data and a full BCDF file delivered through [[fileit]].

The *RDM Integration via Kong Gateway* version describes RDM as the reference-data API provider consumed by Ratanone through [[kong]] for the Indonesia Cash Settlement Platform Architecture.

Separately, the *Ratan and RDM 38430* inventory identifies **RDM** as the upstream system from which **RATANONE - 51358** receives or extracts global reference and portfolio-related data. It lists these seven feeds:

- Copp Clark Holiday Calendar currency-holiday and weekend data.
- Copp Clark Holiday Calendar special-holiday data.
- Country-S3.
- Murex Structures And Strategies.
- Rules Engine Configuration Table.
- 15a6 Registered Staff.
- PCT2 portfolio data retrieved by `RAT_PCT2_REFRESH`.

The seven-feed inventory is broader than the Cash Settlement-specific sources. It does not establish that all of these feeds are used by the cash-settlement functions described below.

## Integration routes

The *Ratan and RDM 38430* inventory describes RDM data as arriving through multiple routes:

- [[fileit]] for at least five feeds.
- [[solace]] for Copp Clark Holiday Calendar messaging or notification.
- [[konggateway]] for the `RAT_PCT2_REFRESH` API path.

The Cash Settlement and Indonesia design sources describe additional or more specific delivery mechanisms, including [[fileit]] BCDF files, real-time holiday events, REST APIs, and [[kong]] gateway access. These references come from different source documents and should not be assumed to define one unified integration contract.

## Evidence limitations and boundaries

The *Ratan and RDM 38430* document is an inventory rather than a technical contract. It does not supply schemas, schedules, endpoints, credentials, data-quality controls, or support responsibilities. It also uses both **RATAN** and **RATANONE - 51358**, leaving the application boundary unresolved. The document does not define RDM’s functional expansion, ownership, authoritative-data responsibilities, or the exact relationship between RDM and the receiving RATAN components.

The Cash Settlement sources likewise leave several operational details unresolved. In particular, the *Static Data* version does not specify the interface, synchronization schedule, calendar semantics, ownership of corrections, or fallback behavior.

## Holiday, weekend, and currency-calendar reference data

The *Static Data* functional-requirement version identifies RDM as the source system for Currency Calendar data used by Cash Settlement Home Page static-data requirements. It states that Currency Calendar data is sourced from RDM and that RDM should be treated as the authoritative upstream dependency for that data, pending confirmation of the integration contract.

The *Ratan holiday data process from RDM introduction* version states that RDM supplies currency-holiday, special-holiday, and weekend data for [[ratanone]]. It also states that RDM exposes holiday information through service identifiers and a production GUI portal using SSO.

### Ratan cashflow processing

In the *Multi Exceptions* functional-requirement version, RDM is the referenced source of currency-holiday static data for [[ratan]] cashflow processing.

[[ratan]] uses `Cashflow.Payment_Currency` to select an underlying currency calendar from RDM and compares `Cashflow.Payment_Date` against holiday data to identify the Bad Business Day exception.

That source does not define calendar publication timing, regional-calendar handling, stale-data behavior, or the response to unavailable RDM data.

### NSTP workflow

In the *NSTP Workflow* version, RDM is the reference-data source for bad-business-day information.

A Bad Business Day exception is identified from an RDM feed. The exception can be removed when the holiday is removed, after which a Checker releases the cashflow within applicable authority limits.

### HAU holiday data

In the *HKCS initiative* version, RDM is identified as a possible source or owner of [[hau]] holiday static data.

That source does not confirm whether RDM is authoritative, which holiday calendar applies, or how HAU holiday data is to be delivered and maintained.

## Ratanone holiday-data delivery

The *Ratan holiday data process from RDM introduction* version documents two RDM holiday-data forms for [[ratanone]]:

- Message-level holiday data.
- A full BCDF file delivered through [[fileit]].

It also states that RDM holiday information is available through service identifiers and a production GUI portal using SSO.

This source names the following contacts but does not assign formal operational ownership:

| Role described by source | Contact |
|---|---|
| RDM development SPOC | `Indrani.Kandasamy@sc.com` |
| RDM BA | `GokulPrasath.J1@sc.com` |

## Currency rounding governance

In the *Settlement Touchpoints* version, RDM is proposed as the golden source for currency rounding rules, with [[ratan]] subscribing to those rules for net cashflows.

That source does not confirm approval of this governance model, the currencies in scope, or how RDM values reconcile with [[stella]] behavior.

## Country reference data

RDM is named as the upstream location from which operators download the country dataset used to reload [[static-data-service]] country mappings.

The documented country-dataset import procedure requires operators to:

1. Download the country dataset from RDM.
2. Remove lines 1–11 from the downloaded file.
3. Save the remaining content as CSV.
4. Upload the resulting CSV to Static Data Service.

The country-dataset import source does not establish that RDM is the authoritative owner of this dataset, identify a dataset version, or define the meaning of the removed rows.

See [[what-is-the-canonical-country-dataset-schema-and-rdm-transformation]] for unresolved dataset and transformation requirements.

This manual country-dataset procedure is separate from the Indonesia design's documented RDM country-code API integration. The two sources should not be treated as defining the same delivery mechanism.

## Indonesia design

The Indonesia technical-design version describes RDM as the reference-data provider for currency holidays, special holidays, country codes, and bank-code data considered by the Cash Settlement Indonesia design.

For Indonesia, RDM data is needed for:

- Maintaining business-day calendars used in settlement cutoff-date calculations.
- Maintaining country mappings used by SSI stamping.

### Integration mechanisms

The Indonesia technical-design version documents the following RDM integration mechanisms:

- Real-time holiday events through `Rdm_Currency_Holiday_Weekend_In`.
- File-notification ingestion through `Rdm_FileIT_Notification_In`. This depends on accessible file paths and is unsuitable for the stated Indonesia NAS constraint.
- Scheduled REST APIs for currency holidays, special holidays, and country codes through direct development access or [[kong]] gateway URLs.

The *RDM Integration via Kong Gateway* version specifically documents RDM API consumption through [[kong]] for Ratanone.

The *Ratan holiday data process from RDM introduction* version separately documents full BCDF-file delivery through [[fileit]] and a production GUI portal using SSO. It should not be assumed that this file-delivery and GUI model is the same mechanism as the Indonesia design's API integration.

### Documented Kong API functions

The *RDM Integration via Kong Gateway* version documents these RDM functions through Kong:

- Currency holiday and weekend calendar: `v2/holidayCalendarCurrencyHldyWkend`
- Special holiday calendar: `v2/holidayCalendarSpecial`
- Country code reference data: `v1/countries`

Access requires the `RDMApiService_GET` OAuth scope and producer-side authorization for consumer ID `EDMILDAP/RATAN_EDMI_PROD`.

### Data scope

The currently required RDM datasets for the Indonesia technical-design version are:

- Currency holidays and special holidays for cutoff-date calculation.
- Country-code mappings for SSI stamping.

The reviewed common configuration files and bank-code/LEI feed are out of scope only under the current Indonesia design assumptions. Bank-code/LEI usage was described as UK CHAPS-specific and should not be generalized to all RDM consumers or regions.

### Data quality, pagination, and reconciliation

The *RDM Integration via Kong Gateway* version reports that the demonstrated currency-holiday response has:

- `dataQuality: "Amber"`
- `totalRecords: "541550"`
- `pageSize: "2000"`

That source does not define whether Amber data is usable for compensation processing or the supported pagination and reconciliation approach. These uncertainties are tracked in [[how-should-ratan-handle-rdm-amber-data-quality-and-pagination]].

### Operational dependencies and production readiness

The Indonesia technical-design version states that RDM availability follows third-party CoppClark processing after 09:00 HK. Indonesia's synchronization schedule must therefore account for source availability, Indonesia time zones, API pagination, authentication, and retry behavior.

Production onboarding for the Ratanone integration remains unresolved according to the *RDM Integration via Kong Gateway* version; see [[what-is-the-production-readiness-plan-for-ratan-rdm-kong-integration]].

See also [[rdm-api-based-holiday-compensation]] and [[what-is-the-approved-rdm-api-contract-for-indonesia-holiday-compensation]].

## Open questions

Across the source versions, the following matters remain unresolved or source-specific:

- The authoritative ownership and operational responsibility for each RDM dataset.
- The relationship between the inventory feeds in *Ratan and RDM 38430* and the Cash Settlement-specific feeds.
- The exact boundary between RATAN, RATANONE, and RATANONE - 51358.
- The schemas, schedules, endpoints, credentials, and support model for the broader RDM feed inventory.
- Whether the manual country-dataset download and the Indonesia country-code API represent separate datasets or merely separate delivery mechanisms.
- Whether RDM is authoritative for HAU holiday data.
- Whether the proposed currency-rounding governance model has been approved.
- The handling of Amber data quality, pagination, reconciliation, stale data, unavailable RDM data, and fallback behavior.
- The production-readiness status of the Ratanone integration through [[kong]].
