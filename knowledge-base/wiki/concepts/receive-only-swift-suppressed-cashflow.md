---
type: concept
title: Receive-Only Swift Suppressed Cashflow
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, Swift, suppression, receipts, Ratan, LMS]
related: [cashflow-suppression-rule, swift-suppressed-lms-feed-contract, lms, ratan, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---
# Receive-Only Swift Suppressed Cashflow

A receive-only Swift Suppressed cashflow is a cashflow for which outbound Swift payment generation is suppressed, no corresponding nostro payment occurs in Ratan, and SCB nevertheless receives funds from the client.

## Downstream treatment

The requirement establishes that this cashflow must be sent to LMS. The absence of a Swift payment or a Ratan nostro payment does not, by itself, remove the cashflow from downstream processing.

This is a scoped exception to a broad interpretation of [[concepts/cashflow-suppression-rule]]. It concerns receipt-only cashflows and should not be generalized to outbound flows without a separate decision.

## Lifecycle

The initial transition is:

`New -> Swift Suppressed (Receive Only)`

The source also indicates that a subsequent Undo Swift Suppression and a withdrawal to `CANCELLED` each require another LMS message. The message event, payload, and ordering contract are not yet defined. Treatment of a transition to `FAILED` remains unresolved.

## Settlement data risk

Vostro/Nostro stamping may not be available when the cashflow reaches Swift Suppressed status. LMS must confirm whether it can process the message without these values and which SSI fields are mandatory.
