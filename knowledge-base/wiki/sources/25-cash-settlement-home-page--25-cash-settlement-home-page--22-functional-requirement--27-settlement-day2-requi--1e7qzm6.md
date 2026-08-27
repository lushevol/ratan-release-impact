---
type: source
title: Self-Service New Entity and Branch Onboarding
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11351733"
venue: Functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, entity-onboarding, branch-onboarding, static-data, functional-requirement]
related: [entities/cash-settlement-home-page, concepts/self-service-entity-onboarding, comparisons/entity-onboarding-options, concepts/nostro-csv-bulk-maintenance, entities/settlement-accounting, entities/ratanone-swift-service, entities/azure-devops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Self‑service new entity & branch onboarding.md"]
---

# Self-Service New Entity and Branch Onboarding

## Source context

This functional requirement proposes a self-service workflow for onboarding new entities and branches through the [[entities/cash-settlement-home-page]]. The associated ADO work item is [11351733](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11351733). A related design is available in [Self Service new branch/entity onboarding Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3556617786).

The source does not state a confirmed requirement date. Attachment filenames include `2026-7-*`, but those filenames are not treated as authoritative source dates.

## Problem statement

Current new-entity onboarding requires multiple backend configuration changes and static-data imports deployed during scheduled release windows. The stated effects are long lead times, reduced responsiveness to business needs, and dependency on scheduled releases.

The proposed objective is to streamline onboarding, improve turnaround time, and reduce dependence on scheduled deployments through user-managed static-data configuration.

## Proposed implementation

The document presents two options:

1. An Excel template for importing all static data into backend tables. This option is struck through in the source.
2. A new onboarding blotter in which required static-data areas are exposed as sub-tiles. This is the emphasized direction and appears to be the preferred proposal, although the source does not record a formal decision.

The proposed workflow is described in [[concepts/self-service-entity-onboarding]].

## Access model

Static Ops users are intended to have edit access. Other user profiles are intended to have read-only access, following the existing permission model of the Nostro Static blotter.

The source does not specify maker-checker approval, audit-history requirements, rollback behavior, or permissions that vary by static-data category.

## Onboarding dashboard

The dashboard is a drilldown from the `New Entity Onboarding` tile on the Cash Settlement Home Page. Its proposed fields are:

| FMID | FMCODE | Status | Missing Static |
|---|---|---|---|
|  |  |  | Format to be confirmed |

The status values, missing-static calculation, and definition of complete onboarding remain unspecified.

## Required static-data areas

The proposed onboarding experience contains the following areas:

- Currency Mapping, including rounding static and ISO currency mapping
- Branch Code
- Nostro Static, using the existing blotter and adding bulk upload
- Swift Generation
- Release Time
- Accounting Static

The source provides the following field structures.

### Currency Mapping

| Non-ISO CCY | Precision | Type | ISO CCY |
|---|---:|---|---|
|  | 0 | ROUNDING_OFF |  |

### Branch Code

| FMID | FMCODE | Branch Code |
|---|---|---|
|  |  |  |

### Swift Generation

| FMID | Sender BIC | Field 53 BIC | Field 53 CCY | Field 58 BIC |
|---|---|---|---|---|
|  |  |  |  |  |

### Release Time

| Booking Entity FMID | Booking Entity FMCODE | Currency | cutoff time (GMT) | cutoff shifter | cutoff shifter unit |
|---|---|---|---|---|---|
|  |  |  |  | -2/-1/0 | BUSINESS DAY |

### Accounting Static

| Booking Entity FMID | Booking Entity FMCODE | EBBS Bridge Account | Country Full Name | Country Code | ZoneId () | Posting Branch | Txn Type Code | Dr Txn Code | Cr Txn Code |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  | BAHRAIN | BH | Asia/Bahrain | 055 | RTN | 478 | 378 |

The example values appear illustrative. The source does not establish reference-data validation, uniqueness constraints, or whether all accounting records must exist before an entity can be marked onboarded.

## Deferred static data

The following items are explicitly described as non-mandatory for initial new-entity onboarding and are to remain in the backend:

- PM CCY
- PM CCY Receiver BIC
- UDF_Strategy
- UDF_SWF_LS
- CFI Code Mapping

The source preserves these deferred structures:

```text
UDF_Strategy
- k_strategy
- v_allocation
- v_available_location

Example:
- COM_BOE_DELIV | ALLOC | BOE
- COM_CHAS_LDN  |      | LONDON
```

```text
UDF_SWF_LS
- k_currency
- v_allocation
- v_available_location
- v_quality
- v_type
- v_unit

Examples:
- XAG | UNALL | LONDON | 9990 | SILV  | GOZ
- XAQ | UNALL | LONDON |      | GOLD  | FOZ
```

The struck-through presentation indicates removal from the initial UI scope; it does not establish permanent removal from the overall system.

## Implementation limitations and open questions

This requirement is a functional proposal rather than a complete backend contract. It does not define:

- Whether static domains are saved independently or committed atomically
- The owning backend service for each write
- Whether existing APIs are reused, extended, or replaced
- Validation rules for FMID, FMCODE, branch codes, BICs, currencies, time zones, and transaction codes
- Duplicate, retry, partial-save, and failed-upload behavior
- The precise onboarding status model and completion rule
- The holiday-calendar behavior for business-day cutoff shifting
- Whether bulk upload is limited to Nostro Static
- Whether newly created static records require downstream notification or cache refresh

Existing Nostro upload and validation pages provide related context, but their contracts should not be assumed to apply to this workflow without confirmation.