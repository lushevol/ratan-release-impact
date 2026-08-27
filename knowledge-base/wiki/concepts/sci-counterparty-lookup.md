---
type: concept
title: SCI Counterparty Lookup
created: 2026-08-23
updated: 2026-08-23
tags: [SCI, counterparty, BIC, reference-data, settlement-instructions]
related: [sci, ratan, ordering-customer-info-auto-population, ssi-swift-field-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto Populate Ordering Info for Notice to Receive Cashflow.md"]
---
# SCI Counterparty Lookup

SCI counterparty lookup is the branching retrieval strategy used to obtain ordering-customer data for RATAN cashflows that lack a stamped vostro.

## Bank Classification

The requirement treats the following values as bank client types:

```text
BANK
MULTDEV
INTEBCH
FININST
HDGEFND
INTLACC
INTECOM
INTDESK
FUNDMGR
CENTBK
OSEASBK
```

The source writes the field name as `Cient_Type`, while the acceptance cases use `Client Type`. The canonical field identifier remains unresolved.

## Lookup Branches

### Bank with a BIC

SCI is queried for:

```text
fmSysContact.addrLine
```

The selected contact must have:

```text
fmSystemContact.mediumCode="SWIFT"
fmSystemContact.mediumUsage="MAIN"
```

The result populates `Settlement_Instruction.Account.Ordering_Customer_BIC_Code`. `Entity.Counterparty_SCI_FMID` populates the ordering-customer account number.

### Bank without a BIC

When the bank has no qualifying BIC, SCI supplies:

- `fmAccount.fmLongName` for ordering-customer name.
- `fmAddress.addressLine1 + " " + fmAddress.city` for ordering-customer address.
- `Convert(fmAddress.country)` for the country value.
- `Entity.Counterparty_SCI_FMID` for the ordering-customer account number.

### Non-bank Counterparty

Non-bank counterparties bypass the BIC-first path and use the name, address, country, and account-number lookup.

## Failure and Data-Quality Boundaries

No fallback values are auto-populated when SCI returns no value or an exception occurs. The requirement does not state how partially populated responses should be handled, whether SCI failures are retried, or whether they create an SSI exception.

The target field `Ordering_Customer_City` is specified for converted country data, which may indicate a naming issue or an incorrect mapping.