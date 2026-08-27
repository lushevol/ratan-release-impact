---
type: source
title: HKCS Initiative
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14724643"
venue: "Cash Settlement Home Page functional requirements"
created: 2026-08-23
updated: 2026-08-23
tags: [HKCS, cash-settlement, SCB-HK, HAU, XAU, RATAN, SWIFT]
related: [hkcs, scb-hk, hau, xau, ratan, cis, ebbs, lms, hau-gold-settlement-configuration, mt604-mt605-hau-message-customization, hkcs-ratan-cis-api-integration, hau-cashflow-routing-to-lms, canonical-hau-hkcs-bic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# HKCS Initiative

## Summary

This functional-requirements record describes the proposed enablement of SCB HK as a Gold Clearing Agent under HKCS (HK Commodity Settlement). Deals will be booked in SCB HK books, with gold represented by `HAU` rather than `XAU`.

The document records intended requirements and several confirmations, but it does not provide implementation evidence, a completed technical design, or UAT and production-readiness sign-off.

## ADO Work Item

[ADO 14724643](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14724643)

## Functional Requirements

1. Deals will be booked in SCB HK books.
2. Gold will be booked as `HAU` instead of `XAU`.
3. RATAN must customize the SWIFT message handling for MT604 / MT605:
   - The receiver of SWIFT should be `BKCHHKHHGSI` according to Requirement Detail 3.1.
   - RATAN must update the mapping to capture Field 26C for the HAU equivalent.
   - Field 23 must be set to `TRANSFER`.
   - Field 72 must begin with `/ACC/SCRTRF`; additional SSI+ values from line 2 onward are appended using `//`.
4. RATAN will not send accounting. CIS will query the relevant data from the RATAN API.
5. A separate `HAU MAIN` Nostro must be configured.
6. Vostros are expected to be configured as `HAU MAIN`.
7. HAU approval limits should use the same limits as XAU.
8. Upstream and downstream impact assessment must cover:
   - Conversion rate in MDS.
   - HAU holiday data and RDM.
   - HAU data sent through the RATAN-to-CIS flow, with CIS querying the RATAN API instead of RATAN sending data.

## SWIFT Message Requirements

The source includes the following MT604 sample:

| :[26C:/HONGKONG/UNALLGOLD995+](http://26C/HONGKONG/UNALLGOLD995+) |
| --- |
| :30:260520 |
| :20:SCBHKSCTS20MAY |
| :21:SCBHKSCTS20MAY |
| :23:TRANSFER |
| :32F:FOZ100,00 |
| :87A:UBSWHKH0XXX |
| :88A:UBSWHKH0XXX |
| :[72:/ACC/SCRTRF](http://72/ACC/SCRTRF) |

The Field 72 rule is recorded verbatim below:

```text
[72:/ACC/SCRTRF]
append other values from SSI+ from line 2 with //
```

Vivek Aggarwal confirmed that Field 23 may be set to `TRANSFER` when Field 26 is `UNALL`.

## Settlement Accounting and Downstream Interfaces

The document states that accounting for HAU is not required in RATAN and that RATAN will not send accounting. CIS is expected to query RATAN API instead. The exact API payload, endpoint, timing, error handling, and reconciliation contract are not defined.

The open-question record also states that LMS confirmed on 2026-07-29 that HAU cashflows must be sent to LMS. The attached message contents and the LMS interface contract are not included in this source.

## Configuration and Open Questions

- HAU holiday static data ownership, including whether RDM is authoritative, remains open.
- HAU release-cutoff data may be copied from existing XAU data, but Carrie was to extract the XAU values for confirmation.
- HAU-to-XAU ISO currency mapping is stated to be unnecessary because HAU accounting is not required and the currency field is not used in precious-metal-related SWIFT.
- HAU rounding is stated as three decimals, rounding off, but formal approval and downstream validation are not supplied.
- Nostro static-data completion remains unresolved.
- The receiver BIC is inconsistent within the source. Requirement Detail 3.1 specifies `BKCHHKHHGSI`, while Requirement Detail 5 specifies `BKCHCHKHHGSI` as the Nostro Agent.

## Evidence Boundaries

This source does not include:

- RATAN configuration evidence.
- A CIS API specification.
- An LMS interface contract or test result.
- SWIFT validation results.
- MDS conversion-rate assessment.
- RDM holiday-data confirmation.
- Nostro or Vostro deployment evidence.
- UAT or production-readiness sign-off.

The MT692 reference is an assessment request only. No approved MT692 field changes or applicability rules are specified.

## Open Questions

1. Which BIC is authoritative for HKCS HAU SWIFT and Nostro configuration?
2. Is RDM the authoritative source for HAU holiday static data?
3. Are HAU release cutoffs formally copied from XAU, and what values, time zone, and effective date apply?
4. What is the formal RATAN API contract consumed by CIS?
5. What records constitute `HAU MAIN` for Nostro and Vostro setup?
6. What is the complete LMS interface contract for HAU cashflows?
7. Does MT692 require changes?
8. Is the three-decimal, rounding-off rule formally approved across downstream systems?