---
type: concept
title: Confirmation Status Normalization
created: 2026-08-23
updated: 2026-08-23
tags: [confirmation, status-mapping, stp, ratan, deprecated-evidence]
related: [trade-confirmation-driven-cashflow-stp, cdu-lake, ratan, what-is-the-current-authoritative-confirmation-status-to-stp-mapping-for-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# Confirmation Status Normalization

Confirmation-status normalization maps source-system status values to a settlement eligibility state such as Confirmed for cashflow STP.

A deprecated requirement states that [[ratan]] historically treated these CDU Lake `Confirmation_Status` values as Confirmed:

`Matched`, `PairedDiscrepHost`, `PairedDiscrepCounterparty`, `PairedAutomatically`, `PairedManually`, `PairedPaper`, and `PairedPhone`.

The same source gives separate Stella-oriented values: `Affirm` and `Confirm`; it refers to `AFFIRMED`, `CONFIRMED`, and, for [[cfets]], `COMP` in direct Stella source-routing exceptions.

This is not an authoritative current enumeration. The source does not define negative cases, precedence, transition handling, terminality, or post-STP status reversals. See [[what-is-the-current-authoritative-confirmation-status-to-stp-mapping-for-ratan]].