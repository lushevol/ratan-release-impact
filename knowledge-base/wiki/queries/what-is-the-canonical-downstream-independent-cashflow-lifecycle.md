---
type: query
title: What Is the Canonical Downstream-Independent Cashflow Lifecycle?
tags: [cashflow-lifecycle, settlement-routing, fmsre, fmsgw, amh, scpay]
related: [ratan-cashflow-lifecycle-state-machine, ratan, fmsre, fm-swift-gateway, amh, scpay]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# What Is the Canonical Downstream-Independent Cashflow Lifecycle?

The RATAN ONE Processing Guide defines `RELEASED` as a cashflow acknowledged by FMSRE and `SETTLED` as acknowledged by AMH or SCPAY. Elsewhere, it describes selected entities for which RATAN directly generates SWIFT messages to [[fm-swift-gateway]].

This indicates that the documented lifecycle wording may represent a particular downstream route rather than a universal RATAN state definition.

## Required resolution

Define a route-independent lifecycle model that specifies:

1. The business meaning of each main state.
2. The downstream acknowledgement or event that transitions a cashflow on each route.
3. Whether `READY (Pending Ack)` and `RELEASED` have consistent meanings for RAZOR/FMSRE and direct FMSGW routes.
4. How accounting status relates to cashflow status for direct eBBS processing.
5. Whether `SETTLED` can be reached without a SWIFT message for receipt flows.

The resolved model should update [[ratan-cashflow-lifecycle-state-machine]] and clearly identify route-specific overlays.