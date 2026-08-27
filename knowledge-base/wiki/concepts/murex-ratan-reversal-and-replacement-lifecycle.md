---
type: concept
title: Murex–RATAN Reversal and Replacement Lifecycle
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, payment-lifecycle, reversals, replacements, migration]
related: [murex, ratan, murex-payment-trade-lineage-identifiers, irs-resultant-cashflow-netting, cashflow-netting-renetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# Murex–RATAN Reversal and Replacement Lifecycle

Murex payment-affecting operations can cancel, reverse, replace, or add cashflows that are sent to [[ratan]]. The lifecycle response depends materially on the Murex payment status and value-date horizon.

## Status-dependent behaviour

The source describes the following expected pattern:

- `INIT` payments are generally cancelled and replaced after `RPL_M`, `RPL`, or payment-affecting `MOD`.
- `SNTR` payments, expected for RATAN-eligible payments within seven business days, generally produce a reversal and a new payment.
- `SENT` payments also produce reverse/new behaviour for relevant operations.
- `RLSR` denotes a cashflow expected to be sent to RATAN; Scan & Modify may affect an already released payment.

Payments beyond the seven-business-day horizon remain `INIT`; cancellation without an emitted reversal can therefore still occur after migration.

## Correlation requirements

A reversal and replacement cannot be assumed to be adjacent, simultaneous, equal in count, or equal in amount. Re-fixing can defer the replacement by hours or days. Cashflow customisation can produce multiple replacements from fewer reversals, and IRS fixed/floating-leg re-netting can create intermediate flows.

RATAN processing should therefore retain durable lineage information, tolerate delayed and out-of-order events, and process reverse and new flows independently until a validated correlation policy exists.

## IRS sequencing

Murex can net IRS fixed and floating legs into one settlement payment. After an amendment, it can reverse the netted payment and either:

- emit a newly netted fixed-plus-floating payment when fixing already occurred; or
- emit a fixed-leg payment that is later re-netted when the floating leg is fixed.

This is an upstream Murex event pattern and must not be conflated with the lifecycle-service ownership described in [[lifecycle-netting-responsibility-separation]].

See [[what-is-the-approved-ratan-correlation-key-for-murex-reversal-and-new-payments]] and [[how-should-ratan-recover-missing-or-out-of-order-murex-payment-events]].