---
type: query
title: What Is the Approved RATAN Correlation Key for Murex Reversal and New Payments?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, murex, payment-correlation, reversals, mxpayml]
related: [murex, ratan, mxpayml, murex-ratan-reversal-and-replacement-lifecycle, murex-payment-trade-lineage-identifiers]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Surrounding System Integration -- Settlement - Murex 2.11 Cashflow Integration -- CN Settlement - Murex 2.11 Cashflow Integration -- CN Settlement - Analyse murex event impacting payment to Ratan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# What Is the Approved RATAN Correlation Key for Murex Reversal and New Payments?

## Question

What identifier combination and processing rules does RATAN use to correlate original, reversal, and replacement Murex payments?

## Evidence

The source demonstrates that:

- `TrnRef` is mutable and can revert when a market operation is removed.
- Reversal and new events can be separated by hours or days.
- Cashflow customisation can create non-1:1 reverse/new cardinality.
- IRS re-fixing and subsequent netting can create intermediate or delayed payment outcomes.
- `flowID`, trade-lineage identifiers, `Action`, `comment`, and persistence timestamps are available in MxPayML.

## Needed decision evidence

An approved interface contract should define:

1. the immutable business identity retained by RATAN;
2. the relationship model for originals, reversals, and replacements;
3. idempotency keys and duplicate-event handling;
4. handling for unmatched reversals, delayed replacements, and many-to-many outcomes; and
5. the reconciliation and exception-ownership process.

See [[murex-payment-trade-lineage-identifiers]].