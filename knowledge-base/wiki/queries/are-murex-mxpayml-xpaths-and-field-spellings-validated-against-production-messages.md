---
type: query
title: Are Murex MxPayML XPaths and Field Spellings Validated Against Production Messages?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, mxpayml, interface-contract, xml, validation]
related: [murex, mxpayml, ratan, murex-payment-trade-lineage-identifiers]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# Are Murex MxPayML XPaths and Field Spellings Validated Against Production Messages?

## Question

Have the MxPayML field names, XPaths, and population rules used by the Murex-to-RATAN integration been verified against actual production payloads?

## Evidence requiring validation

The source records:

- `k/MxPayML/scbExtraInfoBlock/tradeLastMKT`, which contains a leading `k/`;
- `/MxPayML/scbExtraInfoBlock/TrnOrginalID`, whose spelling differs from `TrnOriginalID`;
- `SNTR` and `RLSR` as statuses in a payment snapshot;
- `Action` values including `INS`, `FIX_DEF`, and `MOD`; and
- `Reverse of flow` as the reversal comment.

## Required outcome

Validate representative original, reverse, replacement, fixing, Scan & Modify, and removed-market-operation messages. Confirm field spelling, XPath, null/default-value treatment, array semantics, and whether values match the stated lifecycle rules before relying on them for RATAN correlation.