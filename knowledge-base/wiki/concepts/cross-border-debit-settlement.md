---
type: concept
title: Cross-Border Debit Settlement
created: 2026-08-23
updated: 2026-08-23
tags: [cross-border-debit, settlement, ssi, cashflow, uat]
related: [cross-border-debit-message-mapping, vostro-field-57-routing-derivation, cross-border-debit-withdrawal-cancellation, ssi-stamping, vostro-nostro-ssi-matching, ratan, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# Cross-Border Debit Settlement

Cross-border debit settlement is the processing of a cashflow using a designated `CROSSDEBIT` settlement account and direction-specific downstream payment messaging in [[ratan]].

## UAT-Evidenced Behavior

The UAT source demonstrates two SSI-selection paths for receive-side cashflows:

- automatic `CROSSDEBIT` stamping for USD under booking entity `10075222`;
- ad hoc SSI selection and maker/checker release for USD under `10075222` and EUR and GBP under booking entity `2`.

Receive-side cases produced cross-debit MT202 output. Pay-side cases also used `CROSSDEBIT` accounts, but retained normal payment mapping. This distinction is documented in [[cross-border-debit-message-mapping]].

## SSI Dependencies

UAT setup copied and amended Vostro and Nostro instructions to establish USD, GBP, and EUR `CROSSDEBIT` accounts. The source associates receive-message routing/header behavior with Vostro SI field 57, as described in [[vostro-field-57-routing-derivation]].

The source does not establish whether automatic stamping is supported beyond the tested USD case or explain the mapping between its Trading Account ID values and booking-entity identifiers.

## Boundary

This page describes UAT-observed behavior only. It does not establish production eligibility, a canonical SSI matching algorithm, or a complete payment-format rule.