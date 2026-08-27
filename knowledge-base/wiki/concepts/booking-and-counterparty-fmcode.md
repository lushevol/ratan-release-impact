---
type: concept
title: Booking and Counterparty FMCODE
created: 2026-08-23
updated: 2026-08-23
tags: [fmcode, booking-entity, counterparty, cashflow, settlement]
related: [cashflow-auto-netting, cashflow-identifier, uat-test-case]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# Booking and Counterparty FMCODE

FMCODE values identify the booking entity and external counterparty associated with a cashflow in the UAT sample. The visible format combines a name-like value with a location or market suffix separated by `*`, `/`, or other source-specific punctuation.

Examples include:

- `SCB LONDON*LDN` as a booking entity.
- `SCB HONGKON*HKG` as a booking entity.
- `SCB TAIPEI*TPE` as a booking entity.
- `SCB CN CHO*CHO` as a booking entity.
- `LCH*LDN`, `SCBOTCCCP*HKG`, and `TAIFEX/TWN*TPE` as counterparties.

The sample uses these values to segment test coverage. It does not establish that an FMCODE alone determines Cashflow Auto Netting eligibility or the netting group.

## Coverage relationship

Most cohorts use one fixed booking-entity and counterparty pairing. SAL is different: it uses `INDO*PAR`, `PARIBAS*PAR`, `BARCLAYS FX*LDN`, `BOA (NABK)*CLT`, and `DEUTSCHE*LDN` under `SCB LONDON*LDN`.

The exact FMCODE grammar, validation rules, ownership, and authoritative reference data are not defined by this source.