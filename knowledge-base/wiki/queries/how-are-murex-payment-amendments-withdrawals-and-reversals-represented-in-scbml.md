---
type: query
title: How Are Murex Payment Amendments, Withdrawals, and Reversals Represented in SCBML?
created: 2026-08-24
updated: 2026-08-24
tags: [amendment, withdrawal, reversal, event, versioning, scbml, murex-211]
related: [murex-payment-mxml-to-scbml-transformation, murex-payment-pay-receive-derivation, cashflow-business-and-message-versioning, cashflow-version-concurrency-control, scbml-cashflow-payload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# How Are Murex Payment Amendments, Withdrawals, and Reversals Represented in SCBML?

## Question

What event, version, predecessor, and party-reference rules apply when a Murex payment is amended, withdrawn, or reversed?

## Current evidence

The mapping permits event values New, Withdrawal, and Amendment, but the CN Payments report proposal hard-codes `New`.

The mapping also hard-codes:

- `cashflowVersion = 0`.
- `businessVersion = 0`.

The source lists `TrnParentID`, `TrnOrginalID`, and nested flow information, while the report proposes `Comment` as the source of `Prev_Cashflow_Id`. No authoritative relationship is defined.

The non-reversed pay/receive rules are documented, but `Reverse=Y` behavior is missing.

## Required resolution

Confirm:

1. Event mapping for New, Withdrawal, Amendment, and reversal.
2. Version-increment rules.
3. Predecessor cashflow and parent-trade identifiers.
4. Whether reversal swaps payer and receiver.
5. Whether a reversal is a new cashflow, an amendment, or a withdrawal representation.