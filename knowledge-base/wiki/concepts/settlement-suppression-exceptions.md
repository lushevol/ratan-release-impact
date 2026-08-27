---
type: concept
title: Settlement Suppression Exceptions
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-suppression, settlement, exceptions, ratan, swift]
related: [manual-entity-settlement-enablement, clearing-swift-suppression, clearing-resultant-swift-suppression, fmrp, ratan-cashflow-lifecycle-state-machine, manual-entity-lms-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md"]
---
# Settlement Suppression Exceptions

Settlement enablement does not remove cashflow-suppression controls. Suppression remains an explicit exception layer applied to particular entities, counterparties, currencies, products, and internal arrangements.

## SLATE_QFC

`SLATE_QFC` has FMID `401081696` and FMCODE `SLATE ONE LLC*DOH`.

Its treatment is intentionally different from DOHA:

- Settlement cashflows remain suppressed.
- Full Nostro, release-cutoff, and EBBS static data are not required.
- The entity is excluded from `STRATEGIC_FM_LIST`.
- The entity is still marked for LMS feed.

This is a downstream-specific exception, not a general rule that suppressed cashflows are excluded from all systems.

## Suppression categories

The source records rules for:

- Tranche 1 and Tranche 2 non-FMRP entities.
- Metals and PM currencies.
- Internal counterparties.
- PM trades.
- Vietnam `LN_BR` flows.
- Sri Lanka internal deals.
- Tanzania/XVA Omnibus flows.
- Selected country-specific and product-specific exceptions.

Representative conditions include:

```text
Entity__Booking_Entity_SCI_FMID in ("10036430", "300010782")
&& Cashflow__Payment_Currency in ("XAU", "XAG", "XPT", "XPD")
&& Entity__Counterparty_SCI_FMID == "10075222"
```

```text
Entity__Booking_Entity_SCI_FMID in
("10036430", "300084297", "300010782", "300011525",
 "10041903", "10037477", "10041902")
&& Cashflow__Payment_Currency in ("XAG", "XAU", "XPT", "XPD")
```

```text
Entity__Booking_Entity_SCI_FMID == "10040387"
&& Entity__Counterparty_SCI_FMID == "400795971"
```

The source contains longer counterparty lists and FMRP/FMRP2 rule identifiers in its Business Rule Setup and Cashflow Suppression sections. Those lists are controlled configuration and should be maintained in the rule repository rather than shortened during implementation.

## Receiver BIC decision

An early proposal would have hardcoded:

```text
receiverBIC = CHASGB2LXXXX
```

for selected entities and metal currencies. Later confirmation states that applicable PM cashflows remain suppressed and no hardcoded receiver BIC is required. The later decision is authoritative unless metal settlement scope changes.

## Suppression and downstream independence

Suppression can coexist with:

- LMS feed eligibility.
- Existing lifecycle processing.
- Rule evaluation and operational exceptions.
- Accounting exclusions for specified PM currencies and entities.

Each downstream outcome must therefore be validated separately.