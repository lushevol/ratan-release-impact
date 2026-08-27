---
type: source
title: CN Settlement Ops Weekly Session — 16 November 2022
created: 2026-08-23
updated: 2026-08-23
tags: [cn-settlement, murex-2-11, derivative-settlement, swift, field-20, agency-payments]
related: [murex-2-11, fmrp, razor, opics, cn-settlement-ops, murex-2-11-cn-derivative-settlement, murex-2-11-field-20-format, agency-payment-identification, pre-trade-settlement-accounting-exceptions, what-is-the-authoritative-murex-2-11-cn-field-20-contract, what-is-the-authoritative-agency-payment-booking-and-swift-generation-model, is-auto-split-in-scope-for-fmrp-cn-settlement, what-are-the-p2p-portfolio-accounting-exceptions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
authors: [CN Settlement Ops]
year: 2022
url: ""
venue: CN Settlement Ops weekly session
---
# CN Settlement Ops Weekly Session — 16 November 2022

Operational discussion of Murex 2.11 derivative settlement in China, covering Field 20 population, SWIFT block 1 generation, agency bookings, payment splitting, settlement exceptions, and reported NSTP volume.

## Recorded Field 20 Format

The meeting recorded the following Murex 2.11 derivative-product format:

```text
MX+00+BRANCH+10 DIGIT+A OR B
```

The historical rationale for the format was not known to CN Settlement Ops. The `MX` prefix was proposed for configuration in [[fmrp]], analogous to the `FX` prefix used in [[razor]]. CMO confirmation was requested to determine whether the prefix has routing significance.

The notes are internally inconsistent about valid suffixes: the meeting notes state `A OR B`, while the action register requests confirmation of `A`/`B`/`C`. The format and its semantics are therefore provisional. See [[murex-2-11-field-20-format]].

## Agency Booking and SWIFT Generation

The meeting identified an agency-booking scenario in which trades are booked with an agency profile and portfolio, but no payment is generated in the China agent queue and no SWIFT message is generated on the agency profile.

Current payment identification was described as portfolio-based. Field 72 reportedly includes an indicator that identifies an agency payment. The affected portfolios also do not generate settlement accounting. No production test case was available, but equivalent handling was considered necessary for a future requirement.

Front Office booking-model confirmation was to be sought from Yuanyuan Cang. See [[agency-payment-identification]].

## Payment Splitting

[[razor]] BAU was described as automatically splitting payments above predefined thresholds for selected countries and currencies. Thresholds are maintained as currency-level static data, and post-split payments carry a parent-payment linkage in SWIFT Field 72.

This behavior was explicitly distinguished from Murex 2.11 derivative settlement:

- No auto-split requirement was identified for Murex 2.11 derivatives.
- Splitting is product-related.
- Client-requested manual splits are performed in [[opics]].
- Manually split payments have no recorded linkage to their original payments.

Razor behavior is reference information, not evidence that auto split is required in FMRP CN Settlement.

## Settlement Exceptions

The main identified business exception was missing Vostro or Nostro SSI. A separate upstream issue affects some portfolios described as `P2P`: no trade or settlement accounting is generated, and the exception occurs during pre-trade processing rather than appearing in a payment queue.

These are distinct failure classes. Payment-queue monitoring may identify payment-stage SSI exceptions but cannot by itself identify failures that prevent payment creation. See [[pre-trade-settlement-accounting-exceptions]].

## Reported Volume

The notes state:

```text
CN 150 as NSTP daily
```

This is an initial operational indicator only. The notes do not establish whether 150 represents trades, payments, settlement instructions, or completed settlement cases.

## Follow-up Actions

| Action | Owner | Due date |
|---|---|---|
| Confirm Field 20 prefix, suffix values, and routing significance with CMO. | Not recorded | Not recorded |
| Confirm the agency-booking model with Yuanyuan Cang. | Arockia Dinesh | Not recorded |
| Confirm whether agency-booking Field 20 logic should be implemented. | Arockia Dinesh, Srinivas, Asther | Not recorded |
| Confirm whether auto split is out of scope for FMRP CN Settlement. | Arockia Dinesh, Srinivas, Asther | Not recorded |
| Investigate the `Reasons` field in Murex 2.11 payment queues. | Yi Li | Not recorded |
| Investigate the P2P portfolio exceptions discussed by Divya. | Divya / to be confirmed | Not recorded |
| Validate agency-payment behavior in a test or production-like case. | To be assigned | Not recorded |