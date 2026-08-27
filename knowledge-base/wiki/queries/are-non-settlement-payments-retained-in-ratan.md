---
type: query
title: Are Non-Settlement Payments Retained in Ratan?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, scbml, xva, payment-selection, data-retention]
related: [intent-to-settle-payment-selection, scbml, ratan-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# Are Non-Settlement Payments Retained in Ratan?

The requirement describes `isIntentToSettle=false` payments as informational/XVA payments used for Blade query and display. However, when exactly one payment is marked `true`, the stated rule says to remove the `false` payments.

Clarification is required for each representation:

- raw inbound SCBML retention;
- Ratan persistence tables;
- cashflow-blotter display;
- Blade query/display use;
- settlement-processing projection; and
- audit and reconciliation data.

The final rule should establish whether false-intent payments are retained as child records, discarded after extraction, or available only in archived raw payloads.