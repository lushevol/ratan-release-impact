---
type: concept
title: Receive-to-Pay Cashflow Linkage
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, linkage, dvp, murex, stella]
related: [auto-dvp, murex, stella, rta-cashflow-validation, auto-dvp-cashflow-cardinality]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Receive-to-Pay Cashflow Linkage

Receive-to-pay cashflow linkage identifies the pay leg whose DVP exception may be closed after a receive leg is confirmed.

The stated rules are source-specific:

- Murex: trade ID plus payment date.
- Stella: trade ID, major version, and payment date.

The Stella major-version key addresses cases where multiple receive/pay pairs share a trade ID and payment date. The Murex rule is not settled for amendments that replace a pay cashflow with a changed trade ID. Auto DVP must not infer a new linkage key without an approved resolution.

A one-to-many result is safe for automation only when the pay legs are split children of one original pay cashflow. Independent multiple pay legs require manual handling.