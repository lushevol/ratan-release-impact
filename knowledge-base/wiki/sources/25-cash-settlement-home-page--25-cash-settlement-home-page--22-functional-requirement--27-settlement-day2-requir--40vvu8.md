---
type: source
title: Capture LEI
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7412111"
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, LEI, India, SWIFT, RATAN, regulatory]
related: [ratan, ssi, sci, india-payment-lei-swift-enrichment, sci-lei-regulatory-data-lookup, ssi-swift-field-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md"]
---
# Capture LEI

## Purpose

This requirement defines an India regulatory enhancement for automatically adding Legal Entity Identifiers (LEIs) to generated SWIFT messages for qualifying SCB payments. The objective is to reduce manual effort and prevent operational errors.

The primary processing platform is [[ratan]]. LEI data is sourced from [[sci]], while existing settlement-instruction content may affect SWIFT field layout.

## Eligibility

LEI enrichment applies only when all applicable conditions are satisfied:

- The cashflow is an SCB payment. Receipts are excluded.
- The cashflow currency is in the stated `(INR, INO, INY)` scope, with INR represented in SWIFT.
- The payment amount is equal to or greater than INR 500,000,000.
- The India booking entity is `FMID = 4` and `FMCODE = SCB BOMBAY*MMB`.
- The settlement means is `NOS`.
- The generated message is MT103 or MT202.

The requirement does not apply to Over-Account or other settlement means, MT202 Flip, MT103+202COV, or MT210.

## SCI LEI Retrieval

Both the booking entity and counterparty LEIs are retrieved from SCI:

- Booking-entity LEI input: `Entity.Booking_Entity_SCI_FMID`
- Counterparty LEI input: `Entity.Counterparty_SCI_FMID`

The retrieval selects:

```text
legalEntity.regulatoryInfo.regulatoryFieldText
where regulatoryTypeValue = 'MIFID'
and regulatoryFields = 'LEI'
```

For the current India scope, the stated SCB LEI is:

```text
RILFO74KP1CM8P6PCT96
```

## SWIFT Placement

Both LEIs occupy the first two applicable lines of the relevant SWIFT field:

| Message type | Field | Placement |
|---|---:|---|
| MT103 | 70 | SCB LEI on line 1; counterparty LEI on line 2 |
| MT202 | 72 | SCB LEI on line 1; counterparty LEI on line 2 |

The source provides this sample representation:

```text
72:/SL/RILFO74KP1CM8P6PCT96
//BL/5493001JZ37UBBZF6L49
```

LEIs are added to the generated SWIFT message and do not need to be captured on the settlement-instruction screen.

If SSI content already occupies line 1 of field 70 or 72, it is moved to line 3 onwards. The stated exception rule is that values beyond line 2 for field 70 or beyond line 4 for field 72 are ignored.

## Related Message Types

No new LEI logic is required for MT192 or MT292. LEI values appearing in the corresponding MT103 or MT202 are expected to be reflected automatically in those messages.

## Business Acceptance Scenarios

| Function | Scenario | Expected result | UAT sample |
|---|---|---|---|
| MT103 with LEI | Qualifying SCB payment, amount at least INR 500,000,000, booking entity `FMID = 4`, and maker/checker release | SWIFT is generated with LEI added to field 70 | `M02756535371` |
| MT202 with LEI | Qualifying SCB payment, amount at least INR 500,000,000, booking entity `FMID = 4`, and maker/checker release | SWIFT is generated with LEI added to field 72 | `M01756535168` |
| Other SWIFT type without LEI | MT202 Flip, MT103/202COV, or MT210 | SWIFT is generated without LEI enrichment | Not provided |
| MT103/MT202 outside scope | Any required eligibility condition is not met | SWIFT is generated without LEI enrichment | Not provided |

## Implementation Reference

The requirement links to [FMRP Swift Generation](https://confluence.global.standardchartered.com/display/DSP/FMRP+Swift+Generation) and requests review of the tag 70 and tag 72 logic for MT103 and MT202.

## Open Points

The source does not define behavior for unavailable or missing SCI data, duplicate or malformed LEIs, conflicting SCI values, the exact meaning of `INO` and `INY`, or whether ignored field content must be audited or surfaced as an exception. It also does not clarify whether `/SL/` and `//BL/` are mandatory qualifiers for both fields.