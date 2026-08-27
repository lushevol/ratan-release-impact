---
type: concept
title: Accounting Extended Narrative Format
created: 2026-08-22
updated: 2026-08-22
tags: [accounting, ebbs, reconciliation, cashflow, narrative]
related: [ebbs, ratan, swap-agent, rfr-payment-type-classification, reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# Accounting Extended Narrative Format

The accounting narrative requirement sends strategy, payment type, and netting ID from RATAN to eBBS so the clearing team can reconcile payments in TLM.

## Target field

```text
Path: data/attributes/request/transaction entry/extended-narratives
Field: EXTENDEDNARRATIVE1
Format: Instrument_Common.Murex_Product_Strategy#Cashflow.Payment_Type#Cashflow.Netting_Id
```

All three fields must be represented and separated by exactly two `#` delimiters. Unavailable values must be blank with no spaces.

```text
Swap_Agent#Bilateral netting#3297d3a6-b122-11ef-ac77-005056ac4ab7
#Bilateral Netting#3297d3a6-b122-11ef-ac77-005056ac4ab7
Swap_Agent#Interim MTM#
Swap_Agent##
#CouponFloat#
##
```

## Length rule

If the complete value exceeds 65 characters, truncate it from the trailing side to 65 characters.

Consequently, `EXTENDEDNARRATIVE1` is an accounting and reconciliation aid, not a lossless or authoritative representation of a full netting ID.