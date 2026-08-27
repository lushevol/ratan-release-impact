---
type: concept
title: SCBML Cashflow Payload
created: 2026-08-24
updated: 2026-08-24
tags: [scbml, xml, cashflow, lms, integration-contract]
related: [lms, ratan, cash-settlement-home-page, lms-cashflow-feed-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# SCBML Cashflow Payload

The LMS integration uses an XML `SCBML` message for cashflow delivery.

## Envelope

The documented envelope has:

```text
scbmlVersion = 4-0
messageVersion = 1.0
messageType = CashflowData
payloadFormat = XML
payloadType = cashflowPayload
payloadVersion = 4-0
eventType = Insert
```

## Payload areas

The message contains:

- Business event and cashflow identifier.
- Netting link when applicable.
- Payment party references, currency, amount, and unadjusted payment date.
- Trade identifier, booking timestamp, source-system name, product type, allotment, portfolio, and workflow status.
- Party 1 and party 2 identifiers.
- Cashflow SSI data, including SSI ID, intermediary, beneficiary bank, beneficiary, ordering customer, settlement account, correspondent, and party references.

## Contract boundary

Ratan sends source-system and cashflow data. LMS consumes the SCBML payload and generates or supports downstream field 20 prefix handling. The message template is explicitly unchanged by the entity-filter removal requirement.

The published XPath mapping remains subject to reconciliation because of malformed path literals and inconsistent field semantics.