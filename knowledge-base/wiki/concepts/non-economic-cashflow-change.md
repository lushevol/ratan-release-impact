---
type: concept
title: Non-Economic Cashflow Change
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cashflow-events, amendments, non-economic-change, SCBML]
related: [ratanone, scbml, amendment-withdrawal-driven-stp, major-version-cashflow-grouping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md"]
---
# Non-Economic Cashflow Change

A non-economic cashflow change is a proposed amendment classification based on comparing selected economic and counterparty attributes between cashflow versions.

## Comparison fields

The design identifies these fields:

- `Entity.Booking_Entity_SCI_FMID`
- `Entity.Counterparty_SCI_FMID`
- `Cashflow.Payment_Currency`
- `Cashflow.Payment_Amount`
- `Cashflow.Payment_Date`
- `Cashflow.Pay_Receive_Indicator`

The physical sources are SCBML party identifiers, payment currency, payment amount, unadjusted payment date, and the payer-party reference. The pay/receive value is `Pay` when the payer reference points to `party1`; otherwise it is `Receive`.

## Incomplete specification

The source does not establish:

- Whether equality across all six fields is required.
- Normalization rules for identifiers, currencies, amounts, or dates.
- Tolerance for amount differences.
- Treatment of adjusted versus unadjusted payment dates.
- How missing or malformed fields are handled.
- Which workflow transition follows the classification.

The example amendment value `Amendment NonEcoAmend` indicates that non-economic classification may be encoded in the RATAN-generated SCBML event, but the allowed event vocabulary is not defined.