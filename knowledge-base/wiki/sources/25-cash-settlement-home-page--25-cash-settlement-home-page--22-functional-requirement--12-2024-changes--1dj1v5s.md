---
type: source
title: Cash Settlement Home Page — Functional Requirement — 2024 Changes
tags: [cash-settlement, auto-netting, 2024, migration, delivery-plan]
related: [fmrp, fxu, stella, murex-2-11, ebbs, tds3, tdsx, razor, auto-netting, cash-settlement, ssi-stamping, cashflow-suppression-rules, utilization-pilot, cash-settlement-delivery-dependencies]
created: 2026-08-22
updated: 2026-08-22
authors: []
year: 2024
url: ""
venue: ""
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md"]
---
# Cash Settlement Home Page — Functional Requirement — 2024 Changes

## Summary

This functional-requirement and delivery-plan document defines 2024 cash-settlement scope across three workstreams:

- A Nepal/Saudi/Egypt utilization pilot using FMRP and FXU integration.
- SG/IN/MY/CN Day 2 exception handling dated 2024-01-04.
- UK/Germany cashflow consumption, netting, exception handling, SSI stamping, and Prime requirements.

The requirements span [[concepts/auto-netting]], cashflow splitting, settlement-method handling, DVP NSTP, STP/NSTP, SSI stamping and validation, accounting generation, SWIFT generation, EOD processing, and downstream exception handling.

## Regional and functional scope

### Nepal/Saudi/Egypt utilization pilot

The pilot covers FMRP utilization, FXU integration, Egypt product support, Swift Generation, Accounting Generation, and Drop2/Drop3 events. Its functional scope includes:

- Stella market-event support for Novation, Revive, Port Reassignment, and Close Out.
- Fixing/floating netting, dependent on Stella/TDSX payment-schedule data.
- CCIL Netting.
- Inter Entity Netting, listed but unchecked.
- Cashflow splitting.
- Settlement Method.
- DVP NSTP, dependent on Stella/TDSX payment-schedule data, with a source note asking whether this applies only for CN booking.
- Inherited on netting.
- A separate unchecked item for whether the behavior is seen as a financial attribute.
- LMS Feeding, described as rare for CN and absent for SG.
- Lien-driven NSTP, dependent on a Murex 2.11 indicator and potentially limited to SG/IN/MY cashflow migration.
- STP/NSTP and NSTP with a CDU unmatch event, dependent on Stella/TDS3 trade data for SCBML.
- SSI stamping, including unchecked CFI Code query enhancement and Omgeo Alert SSI work dependent on SSI+ input of Omgeo SSI setup details.

### SG/IN/MY/CN Day 2

The Day 2 scope includes:

- Consumption of COM status from TDS3.
- Maker/checker pending affirmation.
- Bulk approval.
- An unchecked settlement account/means issue fix.
- NACK handling from FMSRE/AMH, dependent on downstream integration.
- An unchecked withdrawal-after-released-netting capability.
- Reversal and rebook as maker/checker.
- Non-economic changes.
- SCPAY market SSI validation for Egypt and Malaysia, with a hard-coded booking-entity list.

### UK/Germany

The UK/Germany scope includes:

- File-based cashflow consumption.
- BIC netting.
- Auto-netting table enhancement.
- Netting with up to 500 cashflows.
- Murex fixing/floating netting, dependent on a Murex 2.11 indicator.
- Prime Data entitlement.
- A UK-specific SWIFT-generation requirement.
- Cashflow-blotter exception display and filtering by exception type.
- Lien-amount-driven cashflow NSTP.
- Clearing-status-driven cashflow suppression.
- Swap Agent support.
- Prime trade SSI stamping.
- Prime new-market-event support.

## Delivery dependencies and reported status

The source reports the following dependency information. `Closed`, `CLOSED`, `Not Required`, and blank statuses are reproduced as reported; they are not independently verified production outcomes.

```text
- **Stella** | Delivery Plan | Function | RATAN Prioritize | Desc | Status | | --- | --- | --- | --- | --- | | Drop2/Drop3 | **Market Event Support** | | Revive/Port Reassignment/Novation/Close Out | Closed | | | **Fixing Cashflow** | | | Closed | | | | **FMRP & Non FMRP Indicator** | | | Closed | | 2024 H1 | **DVP Indicator** | Q1 | | | | | Settlement Method | | | | | 2024 H2 | New market events support | | | | | | | | | |
- **EBBS** | Delivery Plan | Function | Sub Task | Desc | Status | | --- | --- | --- | --- | --- | | 2024 H1 | Accounting feeding | ISD Review & Approval | | Closed | | | | VD EOD Schedule | | Closed | | | | Solace & Connection | | Closed | | | | UAT( by 26th Mar) | | Closed | | | | EOD Running | | Closed |
- **FM Swift Gateway** | Delivery Plan | Function | Desc | Status | | --- | --- | --- | --- | --- | 2024 H1 | NACK status | | Closed |
- EMDI | Delivery Plan | Function | Desc | Status | | --- | --- | --- | --- | --- | 2024 H1 | Solace Connection with EBBS/FM Swift Gateway | | Closed | | | Solace Connection to consume Murex 2.11 trades | | Closed |
- TDS2: | Delivery Plan | Function | Desc | Status | | --- | --- | --- | --- | --- | Drop2/Drop3 | TDSX API | | Closed |
- Murex 2.11 | Delivery Plan | Function | Ratan Prioritize | Desc | Status | | --- | --- | --- | --- | --- | | 2024 H1 | | | | | | | CCIL indicator | H1 | | Closed | | | Suppression Rule | H1 | | Closed | | 2024 H2 | | | | | | IRS Fix/Floating indicator | H2 | | | | | Lien Indicator | H2 | | | | | Clearing Indicator | H2 | |
- Razor/FMSGW | Delivery Plan | Function | Sub Task | Desc | Status | | --- | --- | --- | --- | --- | | Nepal/Saudi/Egypt | FX Utilization ( FXU integration) | | Not required | Closed | | 2024 H1 | Swift Generation | Solace setup & Connection | | Closed | | | NACK(Swift Gateway/AMH) | | Closed | | | UAT & Release timeline | | Closed |
- SCI | Delivery Plan | Function | Desc | Status | | --- | --- | --- | --- | --- | 2024 H1 | | | | | | Inter Entity indicator | Not Required | CLOSED | | | Counterparty Murex Code field | Not Required | CLOSED | | | CCIL indicator | Not Required | CLOSED | | 2024 H2 | | | | | | Ben BIC Netting | | | | | Domicile Client | | |
- ~~iCDMS~~ | Delivery Plan | Function | Desc | Status | | --- | --- | --- | --- | --- | 2024 H2 | Netting agreement on product level | | |
```

## Interpretation of status evidence

The document is evidence of intended scope and reported delivery dependencies rather than independent operational validation. It contains no test results, production deployment dates, incident history, performance measurements, or acceptance criteria demonstrating that a `Closed` item was operationally successful.

The source also contains unresolved or ambiguous items:

- Inter-entity netting is unchecked.
- CFI Code query enhancement is unchecked.
- Omgeo Alert SSI is unchecked.
- Settlement account/means issue fix is unchecked.
- Withdrawal after released netting is unchecked.
- Several 2024 H2 Murex 2.11 indicators have blank statuses.
- SCI BIC netting and Domicile Client have no stated status.
- The iCDMS product-level netting-agreement entry is struck through without an explanation.
- The DVP payment-schedule dependency may apply only to CN booking, but this is explicitly uncertain.
- The relationship between FM Swift Gateway and Razor/FMSGW is not defined.
- TDS2, TDS3, and TDSX are named separately, but their ownership boundaries are not specified.

## Existing wiki connections

The source extends existing pages for [[entities/fmrp]], [[entities/stella]], [[entities/murex-2-11]], [[entities/ebbs]], [[entities/tds3]], [[entities/ccil]], [[entities/lms]], and [[entities/razor]]. It also provides implementation evidence for [[concepts/auto-netting]], [[concepts/cash-settlement]], [[concepts/delivery-versus-payment]], [[concepts/straight-through-processing]], [[concepts/ssi-stamping]], [[concepts/cashflow-suppression-rules]], [[concepts/settlement-suppression]], and [[concepts/financial-field-classification]].