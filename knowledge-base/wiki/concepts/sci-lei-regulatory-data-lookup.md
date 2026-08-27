---
type: concept
title: SCI LEI Regulatory Data Lookup
created: 2026-08-23
updated: 2026-08-23
tags: [SCI, LEI, regulatory-data, lookup, MIFID]
related: [sci, india-payment-lei-swift-enrichment, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md"]
---
# SCI LEI Regulatory Data Lookup

SCI LEI Regulatory Data Lookup is the retrieval of Legal Entity Identifier data from [[sci]] for SWIFT enrichment.

## Retrieval Contract

The required value is retrieved from:

```text
legalEntity.regulatoryInfo.regulatoryFieldText
```

The lookup filters regulatory data using:

```text
regulatoryTypeValue = 'MIFID'
regulatoryFields = 'LEI'
```

## Party-Specific Inputs

The lookup uses separate SCI FMID inputs:

- Booking entity: `Entity.Booking_Entity_SCI_FMID`
- Counterparty: `Entity.Counterparty_SCI_FMID`

The booking-entity result supplies the SCB LEI for line 1, while the counterparty result supplies the counterparty LEI for line 2.

The current requirement identifies the SCB LEI as:

```text
RILFO74KP1CM8P6PCT96
```

## Unspecified Controls

The source does not define the response when SCI is unavailable, no matching record exists, multiple records qualify, or the returned value is malformed, expired, or different from the stated SCB value. These cases require an authoritative operational and compliance decision.