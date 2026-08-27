---
type: concept
title: Murex Payment and Trade Lineage Identifiers
created: 2026-08-22
updated: 2026-08-22
tags: [murex, mxpayml, payment-lineage, trade-identifiers, ratan]
related: [murex, ratan, mxpayml, murex-ratan-reversal-and-replacement-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# Murex Payment and Trade Lineage Identifiers

Murex-to-RATAN payment interpretation requires multiple identifiers and attributes rather than a single trade reference.

## Identifier semantics

- `flowID` identifies the Murex flow.
- `TrnRef` is the most recent trade number associated with a payment. It is mutable.
- `TrnID` identifies the trade from which a particular payment was originally created.
- `TrnParentID` identifies the immediate creator trade; it is `0` when no creator exists.
- `TrnOriginalID` identifies the original trade in an RPL chain; it is `0` where no RPL occurred.
- `tradeLastMKT` records the last qualifying Murex market operation.
- `Action` indicates payment context, including `MOD`, `INS`, and `FIX_DEF`.
- `comment` identifies reversal flows through the value `Reverse of flow`.
- `CpuDate` and `CpuTime` identify when the cashflow was persisted.

## Mutable `TrnRef`

`TrnRef` is not an immutable original-trade key. In an `A → RPL/RPL_M → B → CNCL` chain, Murex physically deletes trade `B` when the market operation is removed. Payments generated afterwards can carry `TrnRef=A`.

Likewise, a Cancel & Reissue can update `TrnRef` without changing the original flow identity. RATAN correlation must not use `TrnRef` as its sole business key.

## `tradeLastMKT` distinction

The source states that `MOD` and removal of market operations are not represented as Murex market operations for `tradeLastMKT` purposes. Thus, a payment-affecting Modify may not change this attribute even though it triggers a payment lifecycle event.

XPath spellings and field-population rules remain unvalidated; see [[are-murex-mxpayml-xpaths-and-field-spellings-validated-against-production-messages]].