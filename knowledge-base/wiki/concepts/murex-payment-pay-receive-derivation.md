---
type: concept
title: Murex Payment Pay/Receive Derivation
created: 2026-08-24
updated: 2026-08-24
tags: [pay-receive, payer, receiver, reverse, murex-211, ratan-mls]
related: [murex-payment-mxml-to-scbml-transformation, ratan, scbml-cashflow-payload, cashflow-lifecycle-state-model, how-are-murex-payment-amendments-withdrawals-and-reversals-represented-in-scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# Murex Payment Pay/Receive Derivation

## Purpose

This concept defines the draft logic for deriving the cashflow pay/receive indicator and SCBML payer and receiver party references from Murex credit and reverse indicators.

## Proposed non-reversed logic

The source provides these new rules for `Reverse=N`:

| Credit | Reverse | Pay/Receive |
|---|---|---|
| Y | N | Receive |
| N | N | Pay |

The primary mapping indicates that `isCredit=N` can populate the payer reference and `isCredit=Y` can populate the receiver reference. RATAN MLS is named as the transformation location.

## Reversal gap

The earlier rows for `Reverse=Y` are struck out:

- `Credit=Y`, `Reverse=Y` → Pay
- `Credit=N`, `Reverse=Y` → Receive

No replacement behavior is supplied. The specification therefore does not establish whether a reversal swaps payer and receiver, creates a new cashflow with a predecessor reference, or follows another rule.

The resulting gap affects:

- `Cashflow.Pay_Receive_Indicator`;
- `Payment_Payer_Party_Reference`;
- `Payment_Receiver_Party_Reference`;
- `Cashflow.Prev_Cashflow_Id`;
- amendment, withdrawal, and reversal event handling.

Implementation should not infer reversal behavior from the deprecated rows without confirmation.