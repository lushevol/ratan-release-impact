---
type: concept
title: Cashflow Hold and Unhold
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, hold, maker-checker, settlement-operations]
related: [maker-checker-settlement-control, ratan-cashflow-blotter, what-are-the-authoritative-fmrp-hold-eligibility-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# Cashflow Hold and Unhold

Hold temporarily pauses cashflow processing pending review or information completion. The historical FMRP description says Hold can be applied after any status except `RELEASED`, `NET`, or `SPLIT`, changes the main status to `ON HOLD`, and sets `Pending Verification`.

Unhold is described as a checker action that cannot be performed by the user who placed the hold; it returns processing to the preceding state. The matrix instead limits Hold to `READY` after struck-through `QUEUED` and `WAITING` values, and identifies `HOLD` for Unhold and Send To WAITING.

These conflicting requirements must not be implemented as a single authoritative rule without resolution.