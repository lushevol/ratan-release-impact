---
type: source
title: New Currency Onboarding Checklist
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, static-data, currency-onboarding, settlement, swift]
related: [new-currency-onboarding-static-data-readiness, legal-entity-currency-cutoff-control, precious-metal-currency-classification, booking-currency-to-iso-code-mapping, currency-rounding-configuration-readiness, what-is-the-authoritative-change-control-for-pm-and-iso-currency-mappings, what-is-the-complete-new-currency-onboarding-acceptance-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
authors: []
year: 2024
url: ""
venue: ""
---
# New Currency Onboarding Checklist

This functional-requirement checklist identifies RATAN-local static data that must be reviewed when a TP system introduces a new currency during BAU. Supporting the currency upstream is not sufficient: RATAN settlement configuration must also be ready.

## Required Readiness Areas

The checklist requires review of:

- [[legal-entity-currency-cutoff-control]];
- settlement Nostro static data;
- [[precious-metal-currency-classification]];
- [[booking-currency-to-iso-code-mapping]];
- [[currency-rounding-configuration-readiness]].

## Currency Cutoff

Currency cutoff static data controls the cashflow release date and time. A cashflow posted after the cutoff begins SWIFT generation and can no longer be changed by Settlement Ops.

```text
Data lookup key: Legal Entity/Currency
```

![Currency cutoff static-data screenshot](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--33-new-c--15q2nmq/image2024-6-13_17-10-53.png)

The document does not define time-zone handling, default behavior for missing configuration, overrides, or late repair procedures.

## Nostro Static Data

A Nostro is mandatory static data for settlement. A Nostro record must be created for every newly onboarded currency.

This establishes a currency-onboarding prerequisite, but does not define the required account attributes, selection logic, approval workflow, or uniqueness scope. See [[nostro-records]] and [[nostro-static-data-migration]] for related static-data context.

## Precious-Metal Classification

A hardcoded PM currency list identifies precious-metal currencies. PM classification drives MT604, MT605, and MT692 generation. The list was provided by Murex 2.11 colleagues and is maintained in the external [FMRP Swift Generation](https://confluence.global.standardchartered.com/display/DSP/FMRP+Swift+Generation) Confluence document.

The source does not provide the list members or the separate emission conditions for each message type.

## Booking Currency to ISO Code Mapping

For both SWIFT and Accounting, the original booking currency must be converted to an ISO Code. RATAN contains a hardcoded booking-currency-to-ISO-code mapping provided by Murex 2.11 colleagues. Reference data is maintained in the external [Cash Settlement - Accounting](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+Accounting) Confluence document.

No mapping rows, ISO standard version, missing-value behavior, or synchronization process are included.

## Rounding Logic

The checklist requires confirmation that the new currency exists in the current RATAN rounding configuration. The cited tactical rounding logic was being built for the H1 cashflow-migration release covering SG/MY/IN.

Further details are referenced in [Rounding Rule - Tactical solution for H1 2024 Cashflow Migration](https://confluence.global.standardchartered.com/display/DSP/Rounding+Rule+-+Tactical+solution+for+H1+2024+Cashflow+Migration).

## Governance Gap

The PM list and booking-currency-to-ISO mapping are described as hardcoded in RATAN while reference information is maintained in external Confluence documents. The document does not identify the authoritative runtime owner, change approver, deployment process, or drift-detection control. This is tracked in [[what-is-the-authoritative-change-control-for-pm-and-iso-currency-mappings]].